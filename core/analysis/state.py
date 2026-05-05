from core.ir.model import Assignment, Condition
from collections import deque

INF = float("inf")

class StateAnalyzer:
    """
    Анализатор состояния сценария Ren'Py.
    - Проверяет impossible conditions (противоречия во флагах/статах)
    - Поддерживает несколько переменных
    - Хранит путь до ошибки для UI
    - Итеративный обход вместо рекурсии
    """

    def analyze(self, script):
        results = {
            "impossible_conditions": []
        }

        # очередь для обхода: каждый элемент = (label, state, path)
        queue = deque()
        queue.append(("start", {}, ["start"]))

        visited = set()

        while queue:
            label, state, path = queue.popleft()
            key = (label, self._key(state))
            if key in visited:
                continue
            visited.add(key)

            body = script.labels[label].body

            for node in body:

                # --- ASSIGNMENT ---
                if isinstance(node, Assignment):
                    state = self._apply(state, node)

                # --- CONDITION ---
                elif isinstance(node, Condition):
                    min_v, max_v = state.get(node.var, (0, 0))
                    if not self._check(min_v, max_v, node.op, node.value):
                        # Get line number from condition node if available
                        line_num = getattr(node, 'line', None)
                        
                        results["impossible_conditions"].append({
                            "label": label,
                            "path": path.copy(),
                            "var": node.var,
                            "required": node.value,
                            "range": (min_v, max_v),
                            "line": line_num
                        })
                        continue

                    # добавляем ветку тела условия в очередь
                    queue.append((label, state.copy(), path.copy()))

                    # также проверяем else_body
                    if node.else_body:
                        queue.append((label, state.copy(), path.copy()))

                # --- JUMP ---
                elif hasattr(node, "target"):
                    queue.append((node.target, state.copy(), path + [node.target]))

        return results

    def _apply(self, state, node: Assignment):
        state = state.copy()
        min_v, max_v = state.get(node.var, (0, 0))

        if node.op == "+=":
            min_v += node.value
            max_v += node.value if max_v != INF else INF
        elif node.op == "-=":
            min_v -= node.value
            max_v -= node.value
        elif node.op == "=":
            min_v = node.value
            max_v = node.value

        state[node.var] = (min_v, max_v)
        return state

    def _check(self, min_v, max_v, op, value):
        if op == ">=":
            return max_v >= value
        if op == ">":
            return max_v > value
        if op == "<=":
            return min_v <= value
        if op == "<":
            return min_v < value
        if op == "==":
            return min_v <= value <= max_v
        return True

    def _key(self, state):
        # используется для visited, чтобы избежать бесконечных циклов
        return tuple(sorted((k, v[0], v[1]) for k, v in state.items()))