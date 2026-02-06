from lark import Transformer, Tree, Token
from core.ir.model import Script, Label, Jump


class RenPyTransformer(Transformer):
    """
    Преобразует дерево разбора Lark в IR-модель.
    """

    def start(self, items):
        """
        start: statement+
        """
        script = Script()
        for item in items:
            if isinstance(item, Label):
                script.add_label(item)
        return script

    def label(self, items):
        """
        label: "label" NAME ":" NEWLINE INDENT label_body DEDENT
        """
        name_token = items[0]
        body = items[1:]

        return Label(
            name=str(name_token),
            body=body
        )

    def jump(self, items):
        """
        jump: "jump" NAME NEWLINE
        """
        target_token = items[0]
        return Jump(target=str(target_token))
