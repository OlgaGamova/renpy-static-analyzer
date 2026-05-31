from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import Tuple, List, Dict

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.graph.builder import GraphBuilder

from core.analysis.reachability import ReachabilityAnalyzer
from core.analysis.dead_ends import DeadEndAnalyzer
from core.analysis.infinite_loops import InfiniteLoopAnalyzer
from core.analysis.state import StateAnalyzer
from core.ir.model import UnknownStatement

app = FastAPI()

# Обратная совместимость: внешние тестовые скрипты импортируют preprocess_code из core.api
preprocess_code = RenPyParser.preprocess_code

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
            for elif_br in getattr(stmt, 'elif_branches', []):
                lines.append(f"elif {elif_br.var} {elif_br.op} {elif_br.value}")
            if getattr(stmt, 'else_body', None):
                lines.append("else")

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

    for err in analysis.get("state_impossible_aggregated", []):
        line = err.get("line", None)
        if line is not None:
            recs.append(
                f"{err['label']}: {err['var']} ≥ {err['required']} недостижимо (строка {line}) — снизьте порог или добавьте больше выборов, дающих очки опыта"
            )
        else:
            recs.append(
                f"{err['label']}: {err['var']} ≥ {err['required']} недостижимо — снизьте порог или добавьте больше выборов, дающих очки опыта"
            )

    # Всегда истинные условия — использовать агрегированные данные
    for at in analysis.get("state_always_true_aggregated", []):
        line = at.get("line", None)
        lbl = at.get("label")
        var = at.get("var")
        op = at.get("op")
        val = at.get("value")
        occ = at.get("occurrences", 1)
        if line is not None:
            recs.append(f"{lbl}: Условие '{var} {op} {val}' всегда истинно — ветка else никогда не выполнится (строка {line}). Проверьте логику условия — возможно, вы перепутали знак сравнения или переменная не может принять нужное значение.")
        else:
            recs.append(f"{lbl}: Условие '{var} {op} {val}' всегда истинно — ветка else никогда не выполнится. Проверьте логику условия — возможно, вы перепутали знак сравнения или переменная не может принять нужное значение.")

    # Противоречия флагов — использовать агрегированные данные
    for fc in analysis.get("state_flag_contradictions_aggregated", []):
        line = fc.get("line", None)
        lbl = fc.get("label")
        var = fc.get("var")
        vals = fc.get("values", [])
        if line is not None:
            recs.append(f"{lbl}: Флаг '{var}' имеет несовместимые значения на разных путях ({', '.join(map(str, vals))}) (строка {line}). Проверьте все места установки флага, особенно при переходе между сезонами или при загрузке сохранений. Убедитесь, что флаг инициализирован (default) и правильно изменяется во всех ветках.")
        else:
            recs.append(f"{lbl}: Флаг '{var}' имеет несовместимые значения на разных путях ({', '.join(map(str, vals))}). Проверьте все места установки флага, особенно при переходе между сезонами или при загрузке сохранений. Убедитесь, что флаг инициализирован (default) и правильно изменяется во всех ветках.")

    return recs


@app.post("/analyze")
def analyze_script(req: ScriptRequest):
    try:
        # Шаг 1: Создать парсер и препроцессировать код для обработки неизвестных операторов
        parser = RenPyParser()
        processed_code, replaced_lines_info = parser.preprocess_code(req.code)

        # Построить словарь для быстрого доступа: номер_строки -> исходный_текст
        original_texts = {info['line']: info['text'] for info in replaced_lines_info}

        # Шаг 2: Распарсить обработанный код
        tree = parser.parse_text(processed_code)

        transformer = RenPyTransformer()
        script = transformer.transform(tree)

        # Шаг 3: Собрать предупреждения из UnknownStatement
        warnings = []
        critical_keywords = ['call', 'return', 'while', 'repeat', 'python:']
        
        for label_name, label_obj in script.labels.items():
            for stmt in label_obj.body:
                if isinstance(stmt, UnknownStatement):
                    # Получить номер строки из оператора
                    line_num = stmt.line
                    
                    # Найти исходный текст
                    original_text = original_texts.get(line_num, stmt.source)
                    
                    # Проверить наличие критических ключевых слов в исходном тексте
                    source_lower = original_text.lower()
                    is_critical = any(keyword in source_lower for keyword in critical_keywords)
                    
                    if is_critical:
                        warnings.append({
                            "label": label_name,
                            "line": line_num,
                            "column": stmt.column,
                            "source": original_text[:200],
                            "message": f"Пропущена конструкция, влияющая на логику переходов: {original_text[:100]}"
                        })

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
        loop_analyzer = InfiniteLoopAnalyzer()
        state = StateAnalyzer()

        # Получить номера строк для недостижимых узлов
        unreachable_nodes = set()
        unreachable_with_lines = []
        unreachable_simple = []
        for node in reach.find_unreachable(graph):
            unreachable_nodes.add(node)
            unreachable_simple.append(node)
            if node in script.labels:
                label = script.labels[node]
                if hasattr(label, 'line') and label.line is not None:
                    unreachable_with_lines.append({"node": node, "line": label.line})
                else:
                    unreachable_with_lines.append({"node": node, "line": None})
            else:
                unreachable_with_lines.append({"node": node, "line": None})

        # Получить номера строк для терминальных узлов
        terminal_nodes_set = set()
        terminal_with_lines = []
        terminal_simple = []
        for node in dead.find_dead_ends(graph):
            terminal_nodes_set.add(node)
            terminal_simple.append(node)
            if node in script.labels:
                label = script.labels[node]
                if hasattr(label, 'line') and label.line is not None:
                    terminal_with_lines.append({"node": node, "line": label.line})
                else:
                    terminal_with_lines.append({"node": node, "line": None})
            else:
                terminal_with_lines.append({"node": node, "line": None})

        # Получить номера строк для бесконечных циклов
        infinite_loop_nodes = set()
        infinite_loops_with_lines = []
        infinite_loops_simple = []
        for loop in loop_analyzer.find_infinite_loops(graph):
            loop_with_lines = []
            loop_simple = []
            for node in loop:
                infinite_loop_nodes.add(node)
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

        # Получить узлы с ошибками состояний и их номера строк
        state_error_nodes = set()
        state_errors_with_lines = []
        state_analysis = state.analyze(script)
        # Построить агрегированное представление ошибок состояний, чтобы избежать
        # повторения одинаковых предупреждений для одного label+переменной
        # на разных путях. Это делает отчёт фронтенда более лаконичным.
        agg_impossible = {}
        for err in state_analysis.get("impossible_conditions", []):
            key = (err.get("label"), err.get("var"), err.get("type"))
            item = agg_impossible.setdefault(key, {
                "label": err.get("label"),
                "var": err.get("var"),
                "type": err.get("type", None),
                "required": err.get("required"),
                "ranges": set(),
                "paths": set(),
                "lines": set()
            })
            rng = err.get("range")
            if isinstance(rng, (list, tuple)):
                item["ranges"].add((rng[0], rng[1]))
            if err.get("path"):
                item["paths"].add(tuple(err.get("path")))
            if err.get("line") is not None:
                item["lines"].add(err.get("line"))

        impossible_aggregated = []
        for key, v in agg_impossible.items():
            impossible_aggregated.append({
                "label": v["label"],
                "var": v["var"],
                "type": v["type"],
                "required": v.get("required"),
                "ranges": list(v["ranges"]),
                "paths": [list(p) for p in v["paths"]],
                "line": (min(v["lines"]) if v["lines"] else None),
                "occurrences": len(v["paths"]) or 1
            })

        # Агрегировать противоречия флагов (дедупликация по label+var)
        agg_fc = {}
        for fc in state_analysis.get("flag_contradictions", []):
            key = (fc.get("label"), fc.get("var"))
            item = agg_fc.setdefault(key, {"label": fc.get("label"), "var": fc.get("var"), "values": set(), "paths": set(), "lines": set()})
            for val in fc.get("values", []):
                item["values"].add(val)
            if fc.get("path"):
                item["paths"].add(tuple(fc.get("path")))
            if fc.get("line") is not None:
                item["lines"].add(fc.get("line"))

        # Агрегировать всегда истинные условия (дедупликация по label+var+op+value)
        agg_at = {}
        for at in state_analysis.get("always_true_conditions", []):
            key = (at.get("label"), at.get("var"), at.get("op"), at.get("value"))
            item = agg_at.setdefault(key, {
                "label": at.get("label"),
                "var": at.get("var"),
                "op": at.get("op"),
                "value": at.get("value"),
                "ranges": set(),
                "paths": set(),
                "lines": set()
            })
            rng = at.get("range")
            if isinstance(rng, (list, tuple)):
                item["ranges"].add((rng[0], rng[1]))
            if at.get("path"):
                item["paths"].add(tuple(at.get("path")))
            if at.get("line") is not None:
                item["lines"].add(at.get("line"))

        always_true_aggregated = []
        for k, v in agg_at.items():
            always_true_aggregated.append({
                "label": v["label"],
                "var": v["var"],
                "op": v["op"],
                "value": v["value"],
                "ranges": list(v["ranges"]),
                "paths": [list(p) for p in v["paths"]],
                "line": (min(v["lines"]) if v["lines"] else None),
                "occurrences": len(v["paths"]) or 1
            })

        flag_contradictions_aggregated = []
        for k, v in agg_fc.items():
            flag_contradictions_aggregated.append({
                "label": v["label"],
                "var": v["var"],
                "values": list(v["values"]),
                "paths": [list(p) for p in v["paths"]],
                "line": (min(v["lines"]) if v["lines"] else None),
                "occurrences": len(v["paths"]) or 1
            })
        if state_analysis.get("impossible_conditions"):
            for err in state_analysis["impossible_conditions"]:
                label_name = err.get("label")
                state_error_nodes.add(label_name)
                if label_name in script.labels:
                    label_obj = script.labels[label_name]
                    line_num = getattr(label_obj, 'line', None)
                    err_with_line = err.copy()
                    err_with_line['line'] = line_num
                    state_errors_with_lines.append(err_with_line)
                else:
                    err_with_line = err.copy()
                    err_with_line['line'] = None
                    state_errors_with_lines.append(err_with_line)

        # Построить узлы с предвычисленными классами
        missing_nodes = set(n for n in all_nodes if n not in graph)
        nodes = []
        for k in all_nodes:
            # Построить классы узла и предупреждения
            node_classes = []
            node_warnings = []
            
            if k in unreachable_nodes:
                node_classes.append("unreachable")
                node_warnings.append({
                    "type": "unreachable",
                    "icon": "🚫",
                    "title": "Недостижимый узел",
                    "details": "Этот узел недостижим из начальной точки. Добавьте переход к нему или удалите, если он не нужен."
                })
            
            if k in missing_nodes:
                node_classes.append("missing")
                node_warnings.append({
                    "type": "missing",
                    "icon": "❌",
                    "title": "Ошибка перехода",
                    "details": "Ссылка на этот узел существует, но сам узел не найден в графе. Проверьте правильность jump/call."
                })
            
            if k in infinite_loop_nodes:
                node_classes.append("infinite")
                node_warnings.append({
                    "type": "infinite",
                    "icon": "🔄",
                    "title": "Бесконечный цикл",
                    "details": "Этот узел участвует в бесконечном цикле. Добавьте условие выхода из цикла (например, проверку переменной или menu)."
                })
            
            if k in state_error_nodes:
                node_classes.append("bad-state")
                # Использовать агрегированные невозможные условия, чтобы избежать дубликатов
                aggs = impossible_aggregated
                seen_vars = set()
                for a in aggs:
                    if a.get('label') != k:
                        continue
                    var = a.get('var')
                    if var in seen_vars:
                        continue
                    seen_vars.add(var)
                    typ = a.get('type')
                    line = a.get('line')
                    paths = a.get('paths', [])
                    occ = a.get('occurrences', 1)
                    path_info = ' → '.join(paths[0]) if paths and paths[0] else ''
                    
                    # Специфика флагов
                    if typ == 'flag':
                        node_warnings.append({
                            "type": "bad-state",
                            "icon": "⚠️",
                            "title": "Ошибка состояния (флаг)",
                            "details": f"Флаг {var} не может принять требуемое значение ({a.get('required')}). Путь: {path_info}. Проверьте инициализацию и присваивания ({var} = True/False)."
                        })
                    else:
                        # Численный или неизвестный диапазон
                        ranges = a.get('ranges', [])
                        has_unknown = any(r is None or (isinstance(r, (list,tuple)) and (r[0] is None or r[1] is None)) for r in ranges)
                        if has_unknown:
                            node_warnings.append({
                                "type": "bad-state",
                                "icon": "⚠️",
                                "title": "Ошибка состояния",
                                "details": f"Требуется {var} ≥ {a.get('required')}, но состояние переменной неопределено. Проверьте инициализацию и места присваиваний переменной; возможно, это булевый флаг или значение устанавливается не во всех ветках."
                            })
                        else:
                            # показать числовую сводку (использовать первый диапазон)
                            rng0, rng1 = (ranges[0] if ranges else (None, None))
                            node_warnings.append({
                                "type": "bad-state",
                                "icon": "⚠️",
                                "title": "Ошибка состояния",
                                "details": f"Требуется {var} ≥ {a.get('required')}, но максимум: {rng1}. Путь: {path_info}."
                            })
            
            if k in terminal_nodes_set:
                node_classes.append("dead-end")
                node_warnings.append({
                    "type": "dead-end",
                    "icon": "🏁",
                    "title": "Конечный узел",
                    "details": "Этот узел завершает ветвь сценария (нет исходящих переходов). Убедитесь, что это намеренно."
                })
            
            if k in script.labels:
                label = script.labels[k]
                line_num = getattr(label, 'line', None)
                nodes.append({
                    "data": {
                        "id": k,
                        "label": k,
                        "summary": format_label(label),
                        "code": full_code(label),
                        "line": line_num,
                        "warnings": node_warnings
                    },
                    "classes": " ".join(node_classes)
                })
            else:
                nodes.append({
                    "data": {
                        "id": k,
                        "label": k,
                        "summary": "Несуществующий label",
                        "code": "",
                        "line": None,
                        "warnings": node_warnings
                    },
                    "classes": " ".join(node_classes)
                })

        analysis = {
            "unreachable": unreachable_simple,
            "unreachable_with_lines": unreachable_with_lines,
            "terminal_nodes": terminal_simple,
            "terminal_nodes_with_lines": terminal_with_lines,
            "missing": list(missing_nodes),
            "infinite_loops": infinite_loops_simple,
            "infinite_loops_with_lines": infinite_loops_with_lines,
            "state": state_analysis,
            "state_errors_with_lines": state_errors_with_lines,
            # Агрегированные сводки, чтобы помочь фронтенду избежать дубликатов
            "state_impossible_aggregated": impossible_aggregated,
            "state_flag_contradictions_aggregated": flag_contradictions_aggregated,
            "state_always_true_aggregated": always_true_aggregated,
            "warnings": warnings
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
