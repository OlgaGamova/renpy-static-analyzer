from core.ir.model import Assignment, Condition, ElifBranch, Menu, Call, Return
from collections import deque

INF = float("inf")
MAX_CALL_STACK_DEPTH = 10  # Максимальная глубина стека вызовов для предотвращения бесконечных циклов

class StateAnalyzer:
    """
    Анализатор состояния сценария Ren'Py.
    - Проверяет impossible conditions (противоречия во флагах/статах)
    - Поддерживает несколько переменных
    - Хранит путь до ошибки для UI
    - Итеративный обход вместо рекурсии
    """

    def analyze(self, script):
        results = {
            "impossible_conditions": [],
            "always_true_conditions": [],
            "flag_contradictions": [],
            "undefined_labels": [],
            "stack_overflow_warnings": []  # Предупреждения о глубоком стеке вызовов
        }

        # очередь для обхода: каждый элемент = (label, state, path, call_stack, operator_index)
        # call_stack — список кортежей (return_label, next_index)
        # operator_index — текущая позиция в теле метки
        queue = deque()
        queue.append(("start", {}, ["start"], [], 0))

        visited = set()
        undefined_labels_checked = set()
        # Для простого определения противоречий флагов: записываем наблюдаемые значения флагов по меткам
        seen_flags = {}
        reported_flag_contradictions = set()

        while queue:
            label, state, path, call_stack, op_index = queue.popleft()
            
            # Пропустить, если метки нет в скрипте
            if label not in script.labels:
                # Сообщить о неопределённой метке, если ещё не сообщалось
                if label not in undefined_labels_checked:
                    undefined_labels_checked.add(label)
                    results["undefined_labels"].append({
                        "label": label,
                        "path": path.copy()
                    })
                continue
            
            key = (label, self._key(state), tuple(call_stack))
            if key in visited:
                continue
            visited.add(key)

            # собрать флаги, замеченные на этой метке, для обнаружения простых противоречий между путями
            for var, val in state.items():
                if isinstance(val, tuple) and len(val) == 2 and val[0] == 'flag':
                    lf = seen_flags.setdefault(label, {}).setdefault(var, set())
                    lf.add(val[1])
                    if True in lf and False in lf:
                        rep_key = (label, var)
                        if rep_key not in reported_flag_contradictions:
                            reported_flag_contradictions.add(rep_key)
                            # добавить в результаты
                            line_num = getattr(script.labels.get(label, None), 'line', None)
                            results["flag_contradictions"].append({
                                "label": label,
                                "path": path.copy(),
                                "var": var,
                                "values": list(lf),
                                "line": line_num
                            })

            body = script.labels[label].body
            
            # Обработать операторы начиная с op_index
            for idx in range(op_index, len(body)):
                node = body[idx]

                # --- ПРИСВАИВАНИЕ ---
                if isinstance(node, Assignment):
                    state = self._apply(state, node)

                # --- ВЫЗОВ ---
                elif isinstance(node, Call):
                    # Сохранить адрес возврата: (текущая_метка, следующий_индекс)
                    next_index = idx + 1
                    new_stack = call_stack + [(label, next_index)]
                    
                    # Проверить лимит глубины стека
                    if len(new_stack) > MAX_CALL_STACK_DEPTH:
                        line_num = getattr(node, 'line', None)
                        results["stack_overflow_warnings"].append({
                            "label": label,
                            "path": path.copy(),
                            "target": node.target,
                            "stack_depth": len(new_stack),
                            "max_depth": MAX_CALL_STACK_DEPTH,
                            "line": line_num
                        })
                        # Не добавлять в очередь, чтобы предотвратить бесконечные циклы
                        continue
                    
                    # Перейти к вызываемой метке
                    queue.append((node.target, state.copy(), path + [node.target], new_stack, 0))

                # --- ВОЗВРАТ ---
                elif isinstance(node, Return):
                    if call_stack:
                        # Извлечь адрес возврата
                        return_label, return_index = call_stack[-1]
                        new_stack = call_stack[:-1]
                        
                        # Продолжить с адреса возврата
                        queue.append((return_label, state.copy(), path + [return_label], new_stack, return_index))
                    # Если стек пуст — это конец сценария, ничего не делаем

                # --- УСЛОВИЕ ---
                elif isinstance(node, Condition):
                    # Определить, является ли условие флаговым (if flag / сравнение с 0/1)
                    entry = state.get(node.var, None)
                    is_flag = False
                    flag_val = None
                    min_v, max_v = (0, 0)

                    if isinstance(entry, tuple) and len(entry) == 2 and entry[0] == 'flag':
                        is_flag = True
                        flag_val = entry[1]
                    elif isinstance(entry, tuple) and len(entry) == 2:
                        min_v, max_v = entry
                    else:
                        # числовой интервал по умолчанию
                        min_v, max_v = (0, 0)

                    # Эвристика: если у условия нет оператора (пустой) или сравнение с 0/1, считать флагом
                    if (not node.op) or (node.op in ("==", "!=") and node.value in (0, 1)):
                        is_flag = True

                    # --- Обработка флагового условия ---
                    if is_flag:
                        # ожидаемое булево значение для условия: если node.value в (0,1) — использовать его, иначе без op -> True
                        if node.op in ("==", "!=") and node.value in (0, 1):
                            expected = bool(node.value)
                            if node.op == "!=":
                                expected = not expected
                        else:
                            # простой `if var` означает ожидание True
                            expected = True

                        # Если значение флага известно
                        if flag_val is not None:
                            line_num = getattr(node, 'line', None)
                            if flag_val is not expected:
                                # невозможное флаговое условие
                                results["impossible_conditions"].append({
                                    "label": label,
                                    "path": path.copy(),
                                    "var": node.var,
                                    "required": expected,
                                    "range": (None, None),
                                    "line": line_num,
                                    "type": "flag"
                                })
                            else:
                                # условие всегда истинно для флага
                                line_num = getattr(node, 'line', None)
                                results["always_true_conditions"].append({
                                    "label": label,
                                    "path": path.copy(),
                                    "var": node.var,
                                    "op": node.op,
                                    "value": node.value,
                                    "range": (flag_val, flag_val),
                                    "line": line_num
                                })
                        else:
                            # неизвестный флаг (None) — нечего утверждать, продолжаем
                            pass

                    else:
                        # Обработка числового условия
                        # Всегда проверять, невозможно ли условие
                        if not self._check(min_v, max_v, node.op, node.value):
                            # Получить номер строки из узла условия, если доступен
                            line_num = getattr(node, 'line', None)
                            
                            results["impossible_conditions"].append({
                                "label": label,
                                "path": path.copy(),
                                "var": node.var,
                                "required": node.value,
                                "range": (min_v, max_v),
                                "line": line_num
                            })

                        # Также обнаружить всегда истинные: инвертировать невозможность
                        inv_op = self._invert_op(node.op)
                        if inv_op and not self._check(min_v, max_v, inv_op, node.value):
                            # обратное невозможно => условие всегда истинно
                            line_num = getattr(node, 'line', None)
                            results["always_true_conditions"].append({
                                "label": label,
                                "path": path.copy(),
                                "var": node.var,
                                "op": node.op,
                                "value": node.value,
                                "range": (min_v, max_v),
                                "line": line_num
                            })
                        # НЕ продолжать — всё ещё нужно обработать другие операторы в теле
                        # В теле условия могут быть переходы, которые нужно исследовать
                    
                    # Обработать тело условия (ветка true) — ВСЕГДА исследовать
                    if node.body:
                        # Обработать каждый оператор в теле
                        for stmt in node.body:
                            if hasattr(stmt, 'target'):
                                # Обработать операторы перехода в теле условия
                                queue.append((stmt.target, state.copy(), path + [stmt.target], call_stack.copy(), 0))
                            elif isinstance(stmt, Assignment):
                                state = self._apply(state, stmt)
                            elif isinstance(stmt, Condition):
                                # Обработать вложенные условия
                                queue.append((label, state.copy(), path.copy(), call_stack.copy(), idx + 1))
                            else:
                                # Добавить в очередь для обработки этого оператора
                                queue.append((label, state.copy(), path.copy(), call_stack.copy(), idx + 1))

                    # Обработать ветки elif (каждая представляет взаимоисключающий путь)
                    for elif_br in node.elif_branches:
                        elif_state = state.copy()
                        for stmt in elif_br.body:
                            if hasattr(stmt, 'target'):
                                queue.append((stmt.target, elif_state.copy(), path + [stmt.target], call_stack.copy(), 0))
                            elif isinstance(stmt, Assignment):
                                elif_state = self._apply(elif_state, stmt)

                    # Обработать ветку else, если она есть
                    if node.else_body:
                        else_state = state.copy()
                        for stmt in node.else_body:
                            if hasattr(stmt, 'target'):
                                queue.append((stmt.target, else_state.copy(), path + [stmt.target], call_stack.copy(), 0))
                            elif isinstance(stmt, Assignment):
                                else_state = self._apply(else_state, stmt)

                # --- МЕНЮ ---
                elif isinstance(node, Menu):
                    # Обработать опции меню — каждая опция ведёт к разным путям
                    for option in node.options:
                        # Обработать тело каждой опции
                        option_state = state.copy()
                        for stmt in option.body:
                            if isinstance(stmt, Assignment):
                                option_state = self._apply(option_state, stmt)
                            elif hasattr(stmt, 'target'):
                                # Добавить целевую метку с обновлённым состоянием
                                queue.append((stmt.target, option_state.copy(), path + [stmt.target], call_stack.copy(), 0))

                # --- ПЕРЕХОД ---
                elif hasattr(node, "target"):
                    # Обработать операторы перехода, чтобы обеспечить обход всех путей
                    queue.append((node.target, state.copy(), path + [node.target], call_stack.copy(), 0))
                    # После перехода не продолжаем обработку тела текущей метки
                    break

        return results

    def _apply(self, state, node: Assignment):
        state = state.copy()
        # Если присваивание похоже на булево (0/1), считать флагом
        if node.op == "=" and node.value in (0, 1):
            state[node.var] = ('flag', bool(node.value))
            return state

        # Числовая обработка
        existing = state.get(node.var, (0, 0))
        # Если ранее было записано как флаг, повысить до числового для арифметических операций
        if isinstance(existing, tuple) and len(existing) == 2 and existing[0] == 'flag':
            fv = existing[1]
            if fv is None:
                min_v, max_v = (0, 0)
            else:
                min_v = 1 if fv else 0
                max_v = min_v
        else:
            min_v, max_v = existing

        if node.op == "+=":
            min_v += node.value
            max_v += node.value if max_v != INF else INF
        elif node.op == "-=":
            min_v -= node.value
            max_v -= node.value
        elif node.op == "=":
            min_v = node.value
            max_v = node.value

        state[node.var] = (min_v, max_v)
        return state

    def _check(self, min_v, max_v, op, value):
        if op == ">=":
            return max_v >= value
        if op == ">":
            return max_v > value
        if op == "<=":
            return min_v <= value
        if op == "<":
            return min_v < value
        if op == "==":
            return min_v <= value <= max_v
        return True

    def _invert_op(self, op):
        if op == ">=":
            return "<"
        if op == ">":
            return "<="
        if op == "<=":
            return ">"
        if op == "<":
            return ">="
        if op == "==":
            return "!="
        if op == "!=":
            return "=="
        return None

    def _key(self, state):
        # используется для visited, чтобы избежать бесконечных циклов
        items = []
        for k, v in state.items():
            if isinstance(v, tuple) and len(v) == 2 and v[0] == 'flag':
                items.append((k, 'flag', v[1]))
            elif isinstance(v, tuple) and len(v) == 2:
                items.append((k, 'num', v[0], v[1]))
            else:
                items.append((k, str(v)))
        return tuple(sorted(items))
