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


# --- форматирование узла ---
def format_label(label):
    lines = []

    for stmt in label.body:
        name = stmt.__class__.__name__

        if name == "Say":
            lines.append("Диалог")

        elif name == "Assignment":
            lines.append(f"{stmt.var} {stmt.op} {stmt.value}")

        elif name == "Condition":
            lines.append(f"if {stmt.var} {stmt.op} {stmt.value}")

        elif name == "Jump":
            lines.append(f"→ {stmt.target}")

    return "\n".join(lines[:5])


def full_code(label):
    return "\n".join(str(stmt) for stmt in label.body)


def build_recommendations(analysis):
    recs = []

    for node in analysis["unreachable"]:
        recs.append(f"Узел '{node}' недостижим — добавьте переход")

    for node in analysis["terminal_nodes"]:
        recs.append(f"Узел '{node}' завершает сценарий — проверьте корректность")

    for loop in analysis["infinite_loops"]:
        recs.append(f"Бесконечный цикл: {' → '.join(loop)}")

    for err in analysis["state"]["impossible_conditions"]:
        recs.append(
            f"{err['label']}: {err['var']} ≥ {err['required']} недостижимо (макс {err['range'][1]})"
        )

    return recs


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

    nodes = []
    for k in all_nodes:
        if k in script.labels:
            label = script.labels[k]
            nodes.append({
                "data": {
                    "id": k,
                    "label": k,
                    "summary": format_label(label),
                    "code": full_code(label)
                }
            })
        else:
            nodes.append({
                "data": {
                    "id": k,
                    "label": k,
                    "summary": "Несуществующий label",
                    "code": ""
                }
            })

    edges = [
        {"data": {"source": s, "target": t}}
        for s, targets in graph.items()
        for t in targets
    ]

    reach = ReachabilityAnalyzer()
    dead = DeadEndAnalyzer()
    loop = InfiniteLoopAnalyzer()
    state = StateAnalyzer()

    analysis = {
        "unreachable": list(reach.find_unreachable(graph)),
        "terminal_nodes": list(dead.find_dead_ends(graph)),
        "missing": [n for n in all_nodes if n not in graph],
        "infinite_loops": loop.find_infinite_loops(graph),
        "state": state.analyze(script)
    }

    return {
        "nodes": nodes,
        "edges": edges,
        "analysis": analysis,
        "recommendations": build_recommendations(analysis)
    }