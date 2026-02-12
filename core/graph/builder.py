from collections import defaultdict
from core.ir.model import Script, Jump, Menu


class GraphBuilder:
    """
    Строит ориентированный граф переходов между label'ами.
    """

    def build(self, script: Script) -> dict[str, set[str]]:
        graph = defaultdict(set)

        for label_name, label in script.labels.items():
            graph[label_name]
            self._walk_body(label_name, label.body, graph)

        return dict(graph)

    def _walk_body(self, current_label: str, body, graph):
        for node in body:

            if isinstance(node, Jump):
                graph[current_label].add(node.target)

            elif isinstance(node, Menu):
                for option in node.options:
                    self._walk_body(current_label, option.body, graph)

            elif hasattr(node, "body"):
                self._walk_body(current_label, node.body, graph)

