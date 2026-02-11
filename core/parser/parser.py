from lark import Lark
from lark.indenter import Indenter
from core.parser.grammar import RENPY_GRAMMAR


class RenPyIndenter(Indenter):
    NL_type = "_NEWLINE"
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = "INDENT"
    DEDENT_type = "DEDENT"
    tab_len = 4


class RenPyParser:
    def __init__(self):
        self._parser = Lark(
            RENPY_GRAMMAR,
            parser="lalr",
            postlex=RenPyIndenter(),
            propagate_positions=True,
        )

    def parse_text(self, text: str):
        return self._parser.parse(text)

    def parse_file(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            return self.parse_text(f.read())
