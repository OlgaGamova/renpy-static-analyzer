from lark import Transformer
from core.ir.model import Script, Label, Jump, Say, Menu, MenuOption, Assignment, Condition
from lark import Transformer, Token

class RenPyTransformer(Transformer):

    def start(self, items):
        script = Script()
        for item in items:
            if isinstance(item, Label):
                script.add_label(item)
        return script

    def label(self, items):
        name = str(items[0])

        body = [
            item for item in items[1:]
            if not isinstance(item, Token)
        ]

        return Label(name=name, body=body)

    def jump(self, items):
        return Jump(target=str(items[0]))

    def say(self, items):
        text = items[0][1:-1]
        return Say(text=text)

    def menu(self, items):
        options = [
            item for item in items
            if not isinstance(item, Token)
        ]
        return Menu(options=options)

    def menu_option(self, items):
        text = items[0][1:-1]

        body = [
            item for item in items[1:]
            if not isinstance(item, Token)
        ]

        return MenuOption(text=text, body=body)

    def statement(self, items):
        return items[0]

    def assignment(self, items):
        var = str(items[0])
        value = int(items[1])
        return Assignment(var=var, op="+=", value=value)

    def condition(self, items):
        var = str(items[0])
        op = str(items[1])
        value = int(items[2])

        body = [
            item for item in items[3:]
            if not isinstance(item, Token)
        ]

        return Condition(var=var, op=op, value=value, body=body)
