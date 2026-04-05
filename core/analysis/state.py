from core.ir.model import Assignment, Condition

INF = float("inf")


class StateAnalyzer:

    def analyze(self, script):
        visited = set()

        results = {
            "impossible_conditions": []
        }

        self._dfs(script, "start", {}, visited, results, [])
        return results

    def _dfs(self, script, label, state, visited, results, path):
        path = path + [label]

        key = (label, self._key(state))

        if key in visited:
            return

        visited.add(key)

        body = script.labels[label].body

        for node in body:

            if isinstance(node, Assignment):
                state = self._apply(state, node)

            elif isinstance(node, Condition):
                min_v, max_v = state.get(node.var, (0, 0))

                if not self._check(min_v, max_v, node.op, node.value):
                    results["impossible_conditions"].append({
                        "label": label,
                        "path": path,
                        "var": node.var,
                        "required": node.value,
                        "range": (min_v, max_v)
                    })
                    continue

                self._walk(script, node.body, state.copy(), visited, results, path)

            elif hasattr(node, "target"):
                self._dfs(script, node.target, state.copy(), visited, results, path)

    def _apply(self, state, node):
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

    def _walk(self, script, body, state, visited, results, path):
        for node in body:
            if hasattr(node, "target"):
                self._dfs(script, node.target, state.copy(), visited, results, path)

    def _key(self, state):
        return tuple(sorted((k, v[0], v[1]) for k, v in state.items()))