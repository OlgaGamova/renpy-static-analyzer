# core/parser/parser.py

from lark import Lark
from core.parser.grammar import RENPLY_GRAMMAR


class RenPyParser:
    """
    Парсер сценариев Ren'Py.
    Преобразует текст в синтаксическое дерево.
    """

    def __init__(self):
        self._parser = Lark(
            RENPLY_GRAMMAR,
            parser="lalr",
            propagate_positions=True,
            maybe_placeholders=False,
        )

    def parse_text(self, text: str):
        """
        Разобрать текст сценария.
        """
        return self._parser.parse(text)

    def parse_file(self, path: str):
        """
        Прочитать файл .rpy и разобрать его.
        """
        with open(path, "r", encoding="utf-8") as f:
            return self.parse_text(f.read())