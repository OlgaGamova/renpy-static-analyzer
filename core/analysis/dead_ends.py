class DeadEndAnalyzer:
    """
    Находит мёртвые концы (узлы без исходящих рёбер).
    """

    def find_dead_ends(self, graph: dict[str, set[str]]):
        dead_ends = set()

        for node, neighbors in graph.items():
            if not neighbors:
                dead_ends.add(node)

        return dead_ends