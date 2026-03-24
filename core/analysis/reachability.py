class ReachabilityAnalyzer:
    """
    Находит недостижимые узлы графа.
    """

    def find_unreachable(self, graph: dict[str, set[str]], start="start"):
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neighbor in graph.get(node, []):
                dfs(neighbor)

        # стартуем обход
        if start in graph:
            dfs(start)

        # всё, что не посетили — недостижимо
        unreachable = set(graph.keys()) - visited
        return unreachable