from lark import Transformer
from core.ir.model import Script, Label, Jump, Call, Return, Say, Menu, MenuOption, Assignment, Condition, UnknownStatement
from lark import Transformer, Token

class RenPyTransformer(Transformer):

    def start(self, items):
        script = Script()
        for item in items:
            if isinstance(item, Label):
                script.add_label(item)
                # Also extract nested labels from this label's body
                self._extract_nested_labels(item, script)
        return script
    
    def _extract_nested_labels(self, label, script):
        """Recursively extract nested labels from a label's body and add them to the script."""
        nested_labels = []
        new_body = []
        for stmt in label.body:
            if isinstance(stmt, Label):
                nested_labels.append(stmt)
                script.add_label(stmt)
                self._extract_nested_labels(stmt, script)
                new_body.append(stmt)  # Keep label reference in body for flow analysis
            elif isinstance(stmt, list):
                # Handle lists of statements (e.g., from unknown_statement blocks)
                for sub_stmt in stmt:
                    if isinstance(sub_stmt, Label):
                        nested_labels.append(sub_stmt)
                        script.add_label(sub_stmt)
                        self._extract_nested_labels(sub_stmt, script)
                # Keep the list in body (contains UnknownStatement + any Labels)
                new_body.append(stmt)
            else:
                new_body.append(stmt)
        label.body = new_body

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
        # items: [UNKNOWN_TOKEN, ...optional_block_statements...]
        # With grammar: UNKNOWN_TOKEN _NEWLINE? (INDENT statement+ DEDENT)?
        # The block statements are included in items if present
        line = None
        column = None
        body = []
        
        for item in items:
            if isinstance(item, Token):
                if item.type == 'UNKNOWN_TOKEN':
                    line = getattr(item, 'line', None)
                    column = getattr(item, 'column', None)
            elif item is not None:
                # This is a statement from the optional block
                body.append(item)
        
        # If there are nested labels in the body, we need to return them
        # so that the parent label can extract them via _extract_nested_labels
        if body:
            # Return a list: [UnknownStatement, Label1, Label2, ...]
            # The _extract_nested_labels method will find and extract the Labels
            result = [UnknownStatement(source="__UNKNOWN__", line=line, column=column)]
            result.extend(body)
            return result
        
        return UnknownStatement(source="__UNKNOWN__", line=line, column=column)
    
    def UNKNOWN_TOKEN(self, token):
        return token

    def UNKNOWN_LINE(self, token):
        return token
