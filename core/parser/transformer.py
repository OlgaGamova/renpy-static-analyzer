from lark import Transformer
from core.ir.model import Script, Label, Jump, Say, Menu, MenuOption


class RenPyTransformer(Transformer):

    def start(self, items):
        script = Script()
        for item in items:
            if isinstance(item, Label):
                script.add_label(item)
        return script

    def label(self, items):
        name = str(items[0])
        body = items[1:]
        return Label(name=name, body=body)

    def jump(self, items):
        target = str(items[0])
        return Jump(target=target)

    def say(self, items):
        if len(items) == 1:
            text = items[0][1:-1]
            return Say(text=text)
        else:
            character = str(items[0])
            text = items[1][1:-1]
            return Say(text=text, character=character)

    def menu(self, items):
        return Menu(options=items)

    def menu_option(self, items):
        text = items[0][1:-1]
        body = items[1:]
        return MenuOption(text=text, body=body)

    def statement(self, items):
        return items[0]
