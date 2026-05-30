from collections import defaultdict
from core.ir.model import Script, Jump, Call, Return, Menu, Label


class GraphBuilder:
    """
    Строит ориентированный граф переходов между label'ами.
    """

    def build(self, script: Script) -> dict[str, set[str]]:
        graph = defaultdict(set)

        for label_name, label in script.labels.items():
            graph[label_name]
            self._walk_body(label_name, label.body, graph)

        # Add fall-through edges: if a label doesn't end with an unconditional
        # jump/return, execution continues to the next label in source order.
        labels_by_line = [
            (name, lbl)
            for name, lbl in script.labels.items()
            if lbl.line is not None
        ]
        labels_by_line.sort(key=lambda x: x[1].line)

        for i, (label_name, label) in enumerate(labels_by_line):
            if not self._is_terminal(label.body):
                # Find the next label in source order that is not nested inside this one
                if i + 1 < len(labels_by_line):
                    next_label_name = labels_by_line[i + 1][0]
                    graph[label_name].add(next_label_name)

        return dict(graph)

    def _is_terminal(self, body) -> bool:
        """Return True if the body ends with an unconditional jump or return
        (i.e. there is no fall-through to the next statement after this body)."""
        if not body:
            return False

        # Flatten any nested lists (from unknown_statement blocks)
        flat = []
        for item in body:
            if isinstance(item, list):
                flat.extend(item)
            else:
                flat.append(item)

        # Skip trailing nested Label definitions — they don't affect fall-through
        # of the *current* label's execution path.
        # We look at the last *non-Label* statement.
        last_non_label = None
        for item in reversed(flat):
            if not isinstance(item, Label):
                last_non_label = item
                break

        if last_non_label is None:
            return False

        if isinstance(last_non_label, (Jump, Return)):
            return True

        if isinstance(last_non_label, Menu):
            # Terminal if ALL options end with jump/return
            if not last_non_label.options:
                return False
            return all(
                self._is_terminal(opt.body) for opt in last_non_label.options
            )

        # Condition with elif/else: terminal if ALL branches end with jump/return
        if hasattr(last_non_label, 'elif_branches'):
            # All if/elif/else branches must be terminal for the condition to be terminal
            all_branches = [last_non_label.body]
            all_branches.extend(br.body for br in last_non_label.elif_branches)
            if last_non_label.else_body:
                all_branches.append(last_non_label.else_body)
            else:
                # No else branch means fall-through is possible
                return False
            # Must have else for terminal, and all branches must be terminal
            return all(self._is_terminal(b) for b in all_branches)

        return False

    def _walk_body(self, current_label: str, body, graph):
        for node in body:

            if isinstance(node, (Jump, Call)):
                graph[current_label].add(node.target)

            elif isinstance(node, Menu):
                for option in node.options:
                    self._walk_body(current_label, option.body, graph)

            elif hasattr(node, "body") and not isinstance(node, Label):
                self._walk_body(current_label, node.body, graph)
                # Walk elif branches
                if hasattr(node, 'elif_branches'):
                    for elif_br in node.elif_branches:
                        self._walk_body(current_label, elif_br.body, graph)
                # Walk else body
                if hasattr(node, 'else_body') and node.else_body:
                    self._walk_body(current_label, node.else_body, graph)

