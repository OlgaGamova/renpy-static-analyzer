from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

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

app.mount("/static", StaticFiles(directory="web"), name="static")


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

    for item in analysis["unreachable_with_lines"]:
        node = item["node"]
        line = item["line"]
        if line is not None:
            recs.append(f"Узел '{node}' недостижим — добавьте переход (строка {line})")
        else:
            recs.append(f"Узел '{node}' недостижим — добавьте переход")

    for item in analysis["terminal_nodes_with_lines"]:
        node = item["node"]
        line = item["line"]
        if line is not None:
            recs.append(f"Узел '{node}' завершает сценарий — проверьте корректность (строка {line})")
        else:
            recs.append(f"Узел '{node}' завершает сценарий — проверьте корректность")

    for loop in analysis["infinite_loops_with_lines"]:
        loop_nodes = [item["node"] for item in loop]
        loop_lines = [str(item["line"]) for item in loop if item["line"] is not None]
        if loop_lines:
            recs.append(f"Бесконечный цикл: {' → '.join(loop_nodes)} (строки {', '.join(loop_lines)}) — добавьте условие выхода из цикла")
        else:
            recs.append(f"Бесконечный цикл: {' → '.join(loop_nodes)} — добавьте условие выхода из цикла")

    for err in analysis["state"]["impossible_conditions"]:
        line = err.get("line", None)
        if line is not None:
            recs.append(
                f"{err['label']}: {err['var']} ≥ {err['required']} недостижимо (макс {err['range'][1]}) (строка {line}) — снизьте порог или добавьте больше выборов, дающих очки опыта"
            )
        else:
            recs.append(
                f"{err['label']}: {err['var']} ≥ {err['required']} недостижимо (макс {err['range'][1]}) — снизьте порог или добавьте больше выборов, дающих очки опыта"
            )

    return recs


@app.post("/analyze")
def analyze_script(req: ScriptRequest):
    try:
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
                line_num = getattr(label, 'line', None)
                nodes.append({
                    "data": {
                        "id": k,
                        "label": k,
                        "summary": format_label(label),
                        "code": full_code(label),
                        "line": line_num
                    }
                })
            else:
                nodes.append({
                    "data": {
                        "id": k,
                        "label": k,
                        "summary": "Несуществующий label",
                        "code": "",
                        "line": None
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

        # Get line numbers for unreachable nodes
        unreachable_with_lines = []
        unreachable_simple = []
        for node in reach.find_unreachable(graph):
            unreachable_simple.append(node)
            if node in script.labels:
                label = script.labels[node]
                if hasattr(label, 'line') and label.line is not None:
                    unreachable_with_lines.append({"node": node, "line": label.line})
                else:
                    unreachable_with_lines.append({"node": node, "line": None})
            else:
                unreachable_with_lines.append({"node": node, "line": None})

        # Get line numbers for terminal nodes
        terminal_with_lines = []
        terminal_simple = []
        for node in dead.find_dead_ends(graph):
            terminal_simple.append(node)
            if node in script.labels:
                label = script.labels[node]
                if hasattr(label, 'line') and label.line is not None:
                    terminal_with_lines.append({"node": node, "line": label.line})
                else:
                    terminal_with_lines.append({"node": node, "line": None})
            else:
                terminal_with_lines.append({"node": node, "line": None})

        # Get line numbers for infinite loops
        infinite_loops_with_lines = []
        infinite_loops_simple = []
        for loop in loop.find_infinite_loops(graph):
            loop_with_lines = []
            loop_simple = []
            for node in loop:
                loop_simple.append(node)
                if node in script.labels:
                    label = script.labels[node]
                    if hasattr(label, 'line') and label.line is not None:
                        loop_with_lines.append({"node": node, "line": label.line})
                    else:
                        loop_with_lines.append({"node": node, "line": None})
                else:
                    loop_with_lines.append({"node": node, "line": None})
            infinite_loops_with_lines.append(loop_with_lines)
            infinite_loops_simple.append(loop_simple)

        analysis = {
            "unreachable": unreachable_simple,
            "unreachable_with_lines": unreachable_with_lines,
            "terminal_nodes": terminal_simple,
            "terminal_nodes_with_lines": terminal_with_lines,
            "missing": [n for n in all_nodes if n not in graph],
            "infinite_loops": infinite_loops_simple,
            "infinite_loops_with_lines": infinite_loops_with_lines,
            "state": state.analyze(script)
        }

        return {
            "nodes": nodes,
            "edges": edges,
            "analysis": analysis,
            "recommendations": build_recommendations(analysis)
        }
    except Exception as e:
        return {
            "error": str(e),
            "nodes": [],
            "edges": [],
            "analysis": {},
            "recommendations": []
        }
