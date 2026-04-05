class InfiniteLoopAnalyzer:
    """
    Находит бесконечные циклы (SCC без выхода наружу)
    """

    def find_infinite_loops(self, graph: dict[str, set[str]]) -> list[list[str]]:
        sccs = self._tarjan(graph)
        infinite_loops = []

        for component in sccs:
            if len(component) == 1:
                node = component[0]
                # self-loop
                if node not in graph.get(node, set()):
                    continue

            # проверяем: есть ли выход наружу
            has_exit = False

            for node in component:
                for neighbor in graph.get(node, []):
                    if neighbor not in component:
                        has_exit = True
                        break
                if has_exit:
                    break

            if not has_exit:
                infinite_loops.append(component)

        return infinite_loops

    def _tarjan(self, graph):
        index = 0
        stack = []
        indices = {}
        lowlink = {}
        on_stack = set()
        result = []

        def strongconnect(node):
            nonlocal index

            indices[node] = index
            lowlink[node] = index
            index += 1

            stack.append(node)
            on_stack.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in indices:
                    strongconnect(neighbor)
                    lowlink[node] = min(lowlink[node], lowlink[neighbor])
                elif neighbor in on_stack:
                    lowlink[node] = min(lowlink[node], indices[neighbor])

            if lowlink[node] == indices[node]:
                scc = []

                while True:
                    w = stack.pop()
                    on_stack.remove(w)
                    scc.append(w)
                    if w == node:
                        break

                result.append(scc)

        for node in graph:
            if node not in indices:
                strongconnect(node)

        return result