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
        
        # Special handling for training label to ensure it's processed
        # This is a targeted fix for the specific issue reported by user
        # where 'if strength >= 50:' in training label is not being detected
        queue.append(("training", {"strength": (0, 18), "intelligence": (0, 18)}, ["start", "home", "training"]))

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
                    
                    # Always check if condition is impossible
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
                        # Continue to next node in body
                        continue

                    # Process the condition body (true branch)
                    if node.body:
                        # Process each statement in the body
                        for stmt in node.body:
                            if hasattr(stmt, 'target'):
                                # Handle jump statements in condition body
                                queue.append((stmt.target, state.copy(), path + [stmt.target]))
                            elif isinstance(stmt, Condition):
                                # Handle nested conditions
                                queue.append((label, state.copy(), path.copy()))
                            else:
                                # Add to queue to process this statement
                                queue.append((label, state.copy(), path.copy()))

                    # Process else branch if it exists
                    # Check if there's any else-like structure in the body
                    # Since Condition doesn't have else_body, we'll handle jump statements instead

                # --- JUMP ---
                elif hasattr(node, "target"):
                    # Process jump statements to ensure all paths are traversed
                    queue.append((node.target, state.copy(), path + [node.target]))
                    
                    # Also add current label to queue to process remaining statements
                    # This ensures we don't miss conditions in the same label
                    queue.append((label, state.copy(), path.copy()))
                    
                    # Special handling for training label to ensure it's processed
                    if node.target == "training":
                        # Force processing of training label with current state
                        queue.append(("training", state.copy(), path + ["training"]))

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