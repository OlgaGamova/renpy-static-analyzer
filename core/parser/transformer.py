from lark import Transformer
from core.ir.model import Script, Label, Jump, Call, Return, Say, Menu, MenuOption, Assignment, Condition, UnknownStatement
from lark import Transformer, Token

class RenPyTransformer(Transformer):

    def start(self, items):
        script = Script()
        for item in items:
            if isinstance(item, Label):
                script.add_label(item)
        return script

    def label(self, items):
        # Handle dot-labels (local labels)
        if items[0] == '.':
            name = "." + str(items[1])
            line = getattr(items[1], 'line', None)
            column = getattr(items[1], 'column', None)
            body_start = 2
        else:
            name = str(items[0])
            line = getattr(items[0], 'line', None)
            column = getattr(items[0], 'column', None)
            body_start = 1

        body = [
            item for item in items[body_start:]
            if not isinstance(item, Token)
        ]

        return Label(name=name, body=body, line=line, column=column)

    def jump(self, items):
        target = str(items[0])
        line = getattr(items[0], 'line', None)
        column = getattr(items[0], 'column', None)
        return Jump(target=target, line=line, column=column)

    def call(self, items):
        # items can be: [target] or [target, 'from', return_label]
        target = str(items[0])
        line = getattr(items[0], 'line', None)
        column = getattr(items[0], 'column', None)
        # Note: We ignore the 'from' clause for now since our state analyzer
        # automatically tracks return addresses. The 'from' label is not needed.
        return Call(target=target, line=line, column=column)

    def return_stmt(self, items):
        # Get line/column from the 'return' token if available
        line = None
        column = None
        if items and len(items) > 0:
            token = items[0]
            line = getattr(token, 'line', None)
            column = getattr(token, 'column', None)
        return Return(line=line, column=column)

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
        # New format: DOLLAR_ASSIGN _NEWLINE?
        # DOLLAR_ASSIGN includes the "$", so we need to strip it
        # items[0] is the entire expression including $
        line = None
        column = None
        
        if items and len(items) > 0:
            token = items[0]
            line = getattr(token, 'line', None)
            column = getattr(token, 'column', None)
            source = str(token).strip()
            
            # Strip leading $ if present
            if source.startswith('$'):
                source = source[1:].strip()
        else:
            source = ""
        
        # Try to parse simple assignments like "var = value" or "var=True"
        # For complex expressions like "renpy.notify(...)", we just store the source
        import re
        match = re.match(r'(\w+)\s*([+]?=)\s*(.+)', source)
        if match:
            var = match.group(1)
            op = match.group(2)
            val_str = match.group(3).strip()
            
            # Convert True/False to 1/0
            if val_str == 'True':
                value = 1
            elif val_str == 'False':
                value = 0
            else:
                try:
                    value = int(val_str)
                except ValueError:
                    # For complex values, just use 0
                    value = 0
            
            return Assignment(var=var, op=op, value=value, line=line, column=column)
        else:
            # Complex expression - create a dummy Assignment
            return Assignment(var=source, op="=", value=0, line=line, column=column)

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

    def unknown_statement(self, items):
        # items[0] is the UNKNOWN_TOKEN
        line = None
        column = None
        
        if items and len(items) > 0:
            token = items[0]
            line = getattr(token, 'line', None)
            column = getattr(token, 'column', None)
        
        # The source will be looked up from original_texts in API
        # but we store a placeholder here
        return UnknownStatement(source="__UNKNOWN__", line=line, column=column)
    
    def UNKNOWN_TOKEN(self, token):
        return token

    def UNKNOWN_LINE(self, token):
        return token
