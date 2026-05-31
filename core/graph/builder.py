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

        # Добавление рёбер неявного перехода (fall-through):
        # если метка не заканчивается безусловным переходом (jump/return),
        # выполнение продолжается на следующей метке в порядке исходного кода.
        labels_by_line = [
            (name, lbl)
            for name, lbl in script.labels.items()
            if lbl.line is not None
        ]
        labels_by_line.sort(key=lambda x: x[1].line)

        for i, (label_name, label) in enumerate(labels_by_line):
            if not self._is_terminal(label.body):
                # Найти следующую метку в порядке исходного кода, которая не вложена в данную.
                if i + 1 < len(labels_by_line):
                    next_label_name = labels_by_line[i + 1][0]
                    graph[label_name].add(next_label_name)

        return dict(graph)

    def _is_terminal(self, body) -> bool:
        """Возвращает True, если тело заканчивается безусловным переходом (jump) или возвратом (return)
        (т.е. после этого тела нет неявного перехода к следующему оператору)."""
        if not body:
            return False

        # Развернуть любые вложенные списки (из блоков unknown_statement)
        flat = []
        for item in body:
            if isinstance(item, list):
                flat.extend(item)
            else:
                flat.append(item)

        # Пропустить завершающие вложенные определения меток — они не влияют на неявный переход
        # (fall-through) пути выполнения текущей метки. Мы смотрим на последний оператор,
        # не являющийся меткой.
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
            # Терминальный (завершающий), если ВСЕ варианты заканчиваются на jump/return.
            if not last_non_label.options:
                return False
            return all(
                self._is_terminal(opt.body) for opt in last_non_label.options
            )

        # Условный оператор с elif/else: терминальный, если ВСЕ ветки заканчиваются на jump/return.
        if hasattr(last_non_label, 'elif_branches'):
            # Все ветки if/elif/else должны быть терминальными
            all_branches = [last_non_label.body]
            all_branches.extend(br.body for br in last_non_label.elif_branches)
            if last_non_label.else_body:
                all_branches.append(last_non_label.else_body)
            else:
                # Без ветки else возможен неявный переход (fall-through)
                return False
            # Для терминальности нужна ветка else, и все ветки должны быть терминальными
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
                # Обойти ветки elif
                if hasattr(node, 'elif_branches'):
                    for elif_br in node.elif_branches:
                        self._walk_body(current_label, elif_br.body, graph)
                # Обойти тело else
                if hasattr(node, 'else_body') and node.else_body:
                    self._walk_body(current_label, node.else_body, graph)

