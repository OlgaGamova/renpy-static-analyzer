from lark import Transformer
from core.ir.model import Script, Label, Jump, Call, Return, Say, Menu, MenuOption, Assignment, Condition, ElifBranch, UnknownStatement, Statement
from lark import Transformer, Token

class RenPyTransformer(Transformer):

    def start(self, items):
        script = Script()
        for item in items:
            if isinstance(item, Label):
                script.add_label(item)
                # Также извлечь вложенные метки из тела этой метки
                self._extract_nested_labels(item, script)
        return script
    
    def _extract_nested_labels(self, label, script):
        """Рекурсивно извлечь вложенные метки из тела метки и добавить их в скрипт."""
        nested_labels = []
        new_body = []
        for stmt in label.body:
            if isinstance(stmt, Label):
                nested_labels.append(stmt)
                script.add_label(stmt)
                self._extract_nested_labels(stmt, script)
                new_body.append(stmt)  # Оставить ссылку на метку в теле для анализа потока выполнения
            elif isinstance(stmt, list):
                # Обработка списков операторов (например, из блоков unknown_statement)
                for sub_stmt in stmt:
                    if isinstance(sub_stmt, Label):
                        nested_labels.append(sub_stmt)
                        script.add_label(sub_stmt)
                        self._extract_nested_labels(sub_stmt, script)
                # Оставить список в теле (содержит UnknownStatement + возможные метки)
                new_body.append(stmt)
            else:
                new_body.append(stmt)
        label.body = new_body

    def label(self, items):
        # Обработка локальных меток с точкой (dot-labels)
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
        # items может быть: [target] или [target, 'from', return_label]
        target = str(items[0])
        line = getattr(items[0], 'line', None)
        column = getattr(items[0], 'column', None)
        # Примечание: предложение 'from' пока игнорируется, так как наш анализатор
        # состояний автоматически отслеживает адреса возврата. Метка 'from' не нужна.
        return Call(target=target, line=line, column=column)

    def return_stmt(self, items):
        # Получить строку/столбец из токена 'return', если доступен
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
        # Новый формат: DOLLAR_ASSIGN _NEWLINE?
        # DOLLAR_ASSIGN включает "$", поэтому нужно его убрать
        # items[0] — всё выражение включая $
        line = None
        column = None
        
        if items and len(items) > 0:
            token = items[0]
            line = getattr(token, 'line', None)
            column = getattr(token, 'column', None)
            source = str(token).strip()
            
            # Убрать ведущий $, если есть
            if source.startswith('$'):
                source = source[1:].strip()
        else:
            source = ""
        
        # Попытаться разобрать простые присваивания вида "var = value" или "var=True"
        # Для сложных выражений вроде "renpy.notify(...)" просто сохраняем исходный код
        import re
        match = re.match(r'(\w+)\s*([+]?=)\s*(.+)', source)
        if match:
            var = match.group(1)
            op = match.group(2)
            val_str = match.group(3).strip()
            
            # Преобразовать True/False в 1/0
            if val_str == 'True':
                value = 1
            elif val_str == 'False':
                value = 0
            else:
                try:
                    value = int(val_str)
                except ValueError:
                    # Для сложных значений используем 0
                    value = 0
            
            return Assignment(var=var, op=op, value=value, line=line, column=column)
        else:
            # Сложное выражение — создать фиктивное присваивание
            return Assignment(var=source, op="=", value=0, line=line, column=column)

    def condition(self, items):
        # Грамматика: "if" NAME [OP NUMBER] ":" _NEWLINE INDENT statement+ DEDENT elif_branch* else_branch?
        # Структура items: [NAME, (OP|None), (NUMBER|None), *statements, *ElifBranch, *(else_statements)]
        
        # Найти, где заканчивается тело if и начинается elif/else
        var_token = items[0]
        var = str(var_token)
        line = getattr(var_token, 'line', None)
        column = getattr(var_token, 'column', None)
        
        if items[1] is not None and not isinstance(items[1], (Statement, ElifBranch, list)):
            op = str(items[1])
            value = int(items[2])
            body_start = 3
        else:
            op = "!="
            value = 0  # if var: означает var != 0
            body_start = 1

        # Разделить операторы тела, ветки elif и тело else
        body = []
        elif_branches = []
        else_body = []
        
        for item in items[body_start:]:
            if isinstance(item, ElifBranch):
                elif_branches.append(item)
            elif isinstance(item, list) and len(item) == 1 and isinstance(item[0], Statement) and not isinstance(item[0], ElifBranch):
                # else_body возвращается как список из метода else_branch
                else_body = item
            elif isinstance(item, Statement) and not isinstance(item, ElifBranch):
                body.append(item)
            elif isinstance(item, Token):
                # Пропустить токены (переносы строк, маркеры indent/dedent)
                continue
            elif isinstance(item, list):
                # Может быть else_body, обёрнутый в список
                for sub in item:
                    if isinstance(sub, Statement):
                        body.append(sub)

        return Condition(var=var, op=op, value=value, body=body, 
                         elif_branches=elif_branches, else_body=else_body,
                         line=line, column=column)

    def elif_branch(self, items):
        var_token = items[0]
        var = str(var_token)
        line = getattr(var_token, 'line', None)
        column = getattr(var_token, 'column', None)
        
        if items[1] is not None and not isinstance(items[1], (Statement, list)):
            op = str(items[1])
            value = int(items[2])
            body_start = 3
        else:
            op = "!="
            value = 0
            body_start = 1

        body = [
            item for item in items[body_start:]
            if isinstance(item, Statement) and not isinstance(item, Token)
        ]

        return ElifBranch(var=var, op=op, value=value, body=body, line=line, column=column)

    def else_branch(self, items):
        # items: [токены/операторы из блока else]
        body = [
            item for item in items
            if isinstance(item, Statement) and not isinstance(item, Token)
        ]
        return body

    def unknown_statement(self, items):
        # items: [UNKNOWN_TOKEN, ...операторы_опционального_блока...]
        # Грамматика: UNKNOWN_TOKEN _NEWLINE? (INDENT statement+ DEDENT)?
        # Операторы блока включены в items, если они есть
        line = None
        column = None
        body = []
        
        for item in items:
            if isinstance(item, Token):
                if item.type == 'UNKNOWN_TOKEN':
                    line = getattr(item, 'line', None)
                    column = getattr(item, 'column', None)
            elif item is not None:
                # Это оператор из опционального блока
                body.append(item)
        
        # Если в теле есть вложенные метки, их нужно вернуть,
        # чтобы родительская метка могла извлечь их через _extract_nested_labels
        if body:
            # Вернуть список: [UnknownStatement, Label1, Label2, ...]
            # Метод _extract_nested_labels найдёт и извлечёт метки
            result = [UnknownStatement(source="__UNKNOWN__", line=line, column=column)]
            result.extend(body)
            return result
        
        return UnknownStatement(source="__UNKNOWN__", line=line, column=column)
    
    def UNKNOWN_TOKEN(self, token):
        return token

    def UNKNOWN_LINE(self, token):
        return token
