from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.graph.builder import GraphBuilder
from core.analysis.reachability import ReachabilityAnalyzer
from core.analysis.dead_ends import DeadEndAnalyzer

app = FastAPI()

# --- CORS (чтобы frontend работал) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ScriptRequest(BaseModel):
    code: str


@app.post("/analyze")
def analyze_script(req: ScriptRequest):
    # --- parse ---
    parser = RenPyParser()
    tree = parser.parse_text(req.code)

    transformer = RenPyTransformer()
    script = transformer.transform(tree)

    # --- graph ---
    builder = GraphBuilder()
    graph = builder.build(script)

    # --- СОБИРАЕМ ВСЕ УЗЛЫ (включая несуществующие target) ---
    all_nodes = set(graph.keys())
    for targets in graph.values():
        all_nodes.update(targets)

    # --- Cytoscape формат ---
    nodes = [{"data": {"id": k}} for k in all_nodes]

    edges = [
        {"data": {"source": s, "target": t}}
        for s, targets in graph.items()
        for t in targets
    ]

    # --- анализ ---
    reach = ReachabilityAnalyzer()
    dead = DeadEndAnalyzer()

    unreachable = list(reach.find_unreachable(graph))
    dead_ends = list(dead.find_dead_ends(graph))

    # --- несуществующие label ---
    missing = [n for n in all_nodes if n not in graph]

    return {
        "nodes": nodes,
        "edges": edges,
        "analysis": {
            "unreachable": unreachable,
            "dead_ends": dead_ends,
            "missing": missing
        }
    }