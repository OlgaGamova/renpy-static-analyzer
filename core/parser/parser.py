from lark import Lark
from lark.indenter import Indenter
from lark.exceptions import UnexpectedToken
from core.parser.grammar import RENPY_GRAMMAR
from typing import Tuple, List, Dict


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
            lexer="basic",
            postlex=RenPyIndenter(),
            propagate_positions=True,
        )

    @staticmethod
    def preprocess_code(code: str) -> Tuple[str, List[Dict]]:
        """
        Preprocess Ren'Py code to replace unknown statements with __UNKNOWN__ markers.
        Each line is processed independently - no child skipping.
        The grammar supports __UNKNOWN__ with optional blocks (INDENT/DEDENT).

        Returns:
            Tuple of (processed_code, replaced_lines_info)
            where replaced_lines_info is a list of dicts: {line: int, text: str}
        """
        lines = code.split('\n')
        processed_lines = []
        replaced_lines_info = []

        for i, line in enumerate(lines):
            line_num = i + 1
            stripped = line.strip()

            # Handle comments: remove indented comments to avoid indenter issues
            if stripped.startswith('#'):
                if line != line.lstrip() and len(line) - len(line.lstrip()) > 0:
                    processed_lines.append('')
                else:
                    processed_lines.append(stripped)
            elif stripped == '':
                processed_lines.append(line)
            # Supported constructs
            elif (stripped.startswith('$') or
                  stripped.startswith('label ') or
                  stripped.startswith('label.') or
                  stripped.startswith('jump ') or
                  (stripped.startswith('call ') and not stripped.startswith('call screen')) or
                  stripped.startswith('return') or
                  stripped.startswith('menu:') or
                  stripped.startswith('menu ') or
                  stripped.startswith('if ') or
                  stripped.startswith('elif ') or
                  stripped.startswith('else:') or
                  stripped.startswith('"') or
                  stripped.startswith("'")):
                processed_lines.append(line)
            else:
                indent = len(line) - len(line.lstrip())
                replaced_lines_info.append({
                    'line': line_num,
                    'text': stripped
                })
                processed_lines.append(' ' * indent + '__UNKNOWN__')

        processed_code = '\n'.join(processed_lines)
        return processed_code, replaced_lines_info

    def parse_text(self, text: str):
        return self._parser.parse(text)

    def parse_file(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            return self.parse_text(f.read())

    def preprocess_and_parse(self, code: str) -> Tuple[object, List[Dict]]:
        """Preprocess Ren'Py code and parse it in one step.

        Returns:
            Tuple of (parse_tree, replaced_lines_info)
        """
        processed_code, replaced_lines_info = self.preprocess_code(code)
        tree = self.parse_text(processed_code)
        return tree, replaced_lines_info
