from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.graph.builder import GraphBuilder

from core.analysis.reachability import ReachabilityAnalyzer
from core.analysis.dead_ends import DeadEndAnalyzer
from core.analysis.infinite_loops import InfiniteLoopAnalyzer
from core.analysis.state import StateAnalyzer

app = FastAPI()

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
    parser = RenPyParser()
    tree = parser.parse_text(req.code)

    transformer = RenPyTransformer()
    script = transformer.transform(tree)

    builder = GraphBuilder()
    graph = builder.build(script)

    all_nodes = set(graph.keys())
    for targets in graph.values():
        all_nodes.update(targets)

    nodes = [{"data": {"id": k}} for k in all_nodes]

    edges = [
        {"data": {"source": s, "target": t}}
        for s, targets in graph.items()
        for t in targets
    ]

    reach = ReachabilityAnalyzer()
    dead = DeadEndAnalyzer()
    loop = InfiniteLoopAnalyzer()
    state = StateAnalyzer()

    return {
        "nodes": nodes,
        "edges": edges,
        "analysis": {
            "unreachable": list(reach.find_unreachable(graph)),
            "dead_ends": list(dead.find_dead_ends(graph)),
            "missing": [n for n in all_nodes if n not in graph],
            "infinite_loops": loop.find_infinite_loops(graph),
            "state": state.analyze(script)
        }
    }