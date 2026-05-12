from core.ir.model import Assignment, Condition, Menu
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
            "impossible_conditions": [],
            "undefined_labels": []
        }

        # очередь для обхода: каждый элемент = (label, state, path)
        queue = deque()
        queue.append(("start", {}, ["start"]))

        visited = set()
        undefined_labels_checked = set()

        while queue:
            label, state, path = queue.popleft()
            
            # Skip if label doesn't exist in the script
            if label not in script.labels:
                # Report undefined label if not already reported
                if label not in undefined_labels_checked:
                    undefined_labels_checked.add(label)
                    results["undefined_labels"].append({
                        "label": label,
                        "path": path.copy()
                    })
                continue
            
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

                # --- MENU ---
                elif isinstance(node, Menu):
                    # Handle menu options - each option leads to different paths
                    for option in node.options:
                        # Process each option's body
                        option_state = state.copy()
                        for stmt in option.body:
                            if isinstance(stmt, Assignment):
                                option_state = self._apply(option_state, stmt)
                            elif hasattr(stmt, 'target'):
                                # Add the target label with updated state
                                queue.append((stmt.target, option_state.copy(), path + [stmt.target]))

                # --- JUMP ---
                elif hasattr(node, "target"):
                    # Process jump statements to ensure all paths are traversed
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