from core.ir.model import Assignment, Condition

INF = float("inf")


class StateAnalyzer:

    def analyze(self, script):
        visited = set()

        results = {
            "impossible_conditions": []
        }

        self._dfs(script, "start", {}, visited, results)
        return results

    def _dfs(self, script, label, state, visited, results):
        key = (label, self._key(state))

        if key in visited:
            return

        visited.add(key)

        body = script.labels[label].body

        for node in body:

            # ✅ ТОЛЬКО Assignment
            if isinstance(node, Assignment):
                state = self._apply(state, node)

            # ✅ ТОЛЬКО Condition
            elif isinstance(node, Condition):
                min_v, max_v = state.get(node.var, (0, 0))

                print("CHECK:", node.var, node.value, (min_v, max_v))  # DEBUG

                if max_v < node.value:
                    results["impossible_conditions"].append({
                        "label": label,
                        "var": node.var,
                        "required": node.value,
                        "range": (min_v, max_v)
                    })
                    continue

                self._walk(script, node.body, state.copy(), visited, results)

            # jump
            elif hasattr(node, "target"):
                self._dfs(script, node.target, state.copy(), visited, results)

    def _apply(self, state, node):
        state = state.copy()

        min_v, max_v = state.get(node.var, (0, 0))

        min_v += node.value
        max_v = INF if max_v == INF else max_v + node.value

        state[node.var] = (min_v, max_v)

        return state

    def _walk(self, script, body, state, visited, results):
        for node in body:
            if hasattr(node, "target"):
                self._dfs(script, node.target, state.copy(), visited, results)

    def _key(self, state):
        return tuple(sorted((k, v[0], v[1]) for k, v in state.items()))