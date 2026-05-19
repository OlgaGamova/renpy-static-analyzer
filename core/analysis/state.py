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
            "always_true_conditions": [],
            "flag_contradictions": [],
            "undefined_labels": []
        }

        # очередь для обхода: каждый элемент = (label, state, path)
        queue = deque()
        queue.append(("start", {}, ["start"]))

        visited = set()
        undefined_labels_checked = set()
        # For simple detection of flag contradictions: record observed flag values per label
        seen_flags = {}
        reported_flag_contradictions = set()

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

            # collect flags seen at this label to detect simple contradictions across paths
            for var, val in state.items():
                if isinstance(val, tuple) and len(val) == 2 and val[0] == 'flag':
                    lf = seen_flags.setdefault(label, {}).setdefault(var, set())
                    lf.add(val[1])
                    if True in lf and False in lf:
                        rep_key = (label, var)
                        if rep_key not in reported_flag_contradictions:
                            reported_flag_contradictions.add(rep_key)
                            # add to results
                            line_num = getattr(script.labels.get(label, None), 'line', None)
                            results["flag_contradictions"].append({
                                "label": label,
                                "path": path.copy(),
                                "var": var,
                                "values": list(lf),
                                "line": line_num
                            })

            body = script.labels[label].body

            for node in body:

                # --- ASSIGNMENT ---
                if isinstance(node, Assignment):
                    state = self._apply(state, node)

                # --- CONDITION ---
                elif isinstance(node, Condition):
                    # Detect whether this is a flag-style condition (if flag / compare to 0/1)
                    entry = state.get(node.var, None)
                    is_flag = False
                    flag_val = None
                    min_v, max_v = (0, 0)

                    if isinstance(entry, tuple) and len(entry) == 2 and entry[0] == 'flag':
                        is_flag = True
                        flag_val = entry[1]
                    elif isinstance(entry, tuple) and len(entry) == 2:
                        min_v, max_v = entry
                    else:
                        # default numeric interval
                        min_v, max_v = (0, 0)

                    # Heuristic: if condition has no operator (empty) or compares to 0/1, treat as flag
                    if (not node.op) or (node.op in ("==", "!=") and node.value in (0, 1)):
                        is_flag = True

                    # --- FLAG condition handling ---
                    if is_flag:
                        # expected boolean for condition: if node.value in (0,1) use that, else if no op -> True
                        if node.op in ("==", "!=") and node.value in (0, 1):
                            expected = bool(node.value)
                            if node.op == "!=":
                                expected = not expected
                        else:
                            # plain `if var` means expect True
                            expected = True

                        # If we have known flag value
                        if flag_val is not None:
                            line_num = getattr(node, 'line', None)
                            if flag_val is not expected:
                                # impossible flag condition
                                results["impossible_conditions"].append({
                                    "label": label,
                                    "path": path.copy(),
                                    "var": node.var,
                                    "required": expected,
                                    "range": (None, None),
                                    "line": line_num,
                                    "type": "flag"
                                })
                            else:
                                # condition always true for flag
                                line_num = getattr(node, 'line', None)
                                results["always_true_conditions"].append({
                                    "label": label,
                                    "path": path.copy(),
                                    "var": node.var,
                                    "op": node.op,
                                    "value": node.value,
                                    "range": (flag_val, flag_val),
                                    "line": line_num
                                })
                        else:
                            # unknown flag (None) - nothing to assert, continue
                            pass

                    else:
                        # Numeric condition handling
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

                        # Additionally detect always-true: inverse impossible
                        inv_op = self._invert_op(node.op)
                        if inv_op and not self._check(min_v, max_v, inv_op, node.value):
                            # inverse impossible => condition always true
                            line_num = getattr(node, 'line', None)
                            results["always_true_conditions"].append({
                                "label": label,
                                "path": path.copy(),
                                "var": node.var,
                                "op": node.op,
                                "value": node.value,
                                "range": (min_v, max_v),
                                "line": line_num
                            })
                        # DON'T continue - still need to process other statements in body
                        # The condition might have a body with jumps that we need to explore
                    
                    # Process the condition body (true branch) - ALWAYS explore
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
        # If assignment looks like a boolean assignment (0/1), treat as flag
        if node.op == "=" and node.value in (0, 1):
            state[node.var] = ('flag', bool(node.value))
            return state

        # Numeric handling
        existing = state.get(node.var, (0, 0))
        # If previously recorded as a flag, promote to numeric for arithmetic ops
        if isinstance(existing, tuple) and len(existing) == 2 and existing[0] == 'flag':
            fv = existing[1]
            if fv is None:
                min_v, max_v = (0, 0)
            else:
                min_v = 1 if fv else 0
                max_v = min_v
        else:
            min_v, max_v = existing

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

    def _invert_op(self, op):
        if op == ">=":
            return "<"
        if op == ">":
            return "<="
        if op == "<=":
            return ">"
        if op == "<":
            return ">="
        if op == "==":
            return "!="
        if op == "!=":
            return "=="
        return None

    def _key(self, state):
        # используется для visited, чтобы избежать бесконечных циклов
        items = []
        for k, v in state.items():
            if isinstance(v, tuple) and len(v) == 2 and v[0] == 'flag':
                items.append((k, 'flag', v[1]))
            elif isinstance(v, tuple) and len(v) == 2:
                items.append((k, 'num', v[0], v[1]))
            else:
                items.append((k, str(v)))
        return tuple(sorted(items))
