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
        line = getattr(items[0], 'line', None)
        column = getattr(items[0], 'column', None)

        body = [
            item for item in items[1:]
            if not isinstance(item, Token)
        ]

        return Label(name=name, body=body, line=line, column=column)

    def jump(self, items):
        target = str(items[0])
        line = getattr(items[0], 'line', None)
        column = getattr(items[0], 'column', None)
        return Jump(target=target, line=line, column=column)

    def say(self, items):
        text = items[0][1:-1]
        line = getattr(items[0], 'line', None)
        column = getattr(items[0], 'column', None)
        return Say(text=text, line=line, column=column)

    def menu(self, items):
        options = [
            item for item in items
            if not isinstance(item, Token)
        ]
        line = getattr(items[0], 'line', None) if items else None
        column = getattr(items[0], 'column', None) if items else None
        return Menu(options=options, line=line, column=column)

    def menu_option(self, items):
        text = items[0][1:-1]
        line = getattr(items[0], 'line', None)
        column = getattr(items[0], 'column', None)

        body = [
            item for item in items[1:]
            if not isinstance(item, Token)
        ]

        return MenuOption(text=text, body=body, line=line, column=column)

    def statement(self, items):
        return items[0]

    def assignment(self, items):
        var = str(items[0])
        op = str(items[1])
        val = items[2]
        line = getattr(items[0], 'line', None)
        column = getattr(items[0], 'column', None)
        if str(val) == 'True':
            value = 1
        elif str(val) == 'False':
            value = 0
        else:
            value = int(val)
        return Assignment(var=var, op=op, value=value, line=line, column=column)

    def condition(self, items):
        var = str(items[0])
        line = getattr(items[0], 'line', None)
        column = getattr(items[0], 'column', None)
        if items[1] is not None:
            op = str(items[1])
            value = int(items[2])
            body_start = 3
        else:
            op = "!="
            value = 0  # if var: means var != 0
            body_start = 1

        body = [
            item for item in items[body_start:]
            if not isinstance(item, Token)
        ]

        return Condition(var=var, op=op, value=value, body=body, line=line, column=column)
