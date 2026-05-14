"""
Оптимизированные версии анализаторов с улучшенной производительностью.

Этот модуль содержит улучшенные версии:
1. Итеративный DFS вместо рекурсивного
2. Итеративный алгоритм Тарьяна
3. StateAnalyzer с ограничением глубины и merge состояний

Используйте эти версии вместо оригинальных для улучшения производительности.
"""

from collections import defaultdict, deque


class OptimizedReachabilityAnalyzer:
    """
    Оптимизированный анализатор достижимости.
    Использует итеративный DFS вместо рекурсивного.
    """
    
    def find_unreachable(self, graph: dict[str, set[str]], start="start"):
        """
        Находит недостижимые узлы используя итеративный DFS.
        
        Args:
            graph: граф переходов
            start: стартовый узел
            
        Returns:
            set: множество недостижимых узлов
        """
        visited = set()
        stack = [start]
        
        while stack:
            node = stack.pop()
            
            if node in visited:
                continue
            
            visited.add(node)
            
            # Добавляем соседей в стек
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)
        
        return set(graph.keys()) - visited


class OptimizedInfiniteLoopAnalyzer:
    """
    Оптимизированный анализатор бесконечных циклов.
    Использует итеративный алгоритм Тарьяна.
    """
    
    def find_infinite_loops(self, graph: dict[str, set[str]]) -> list[list[str]]:
        """
        Находит бесконечные циклы используя итеративный Tarjan's SCC.
        
        Args:
            graph: граф переходов
            
        Returns:
            list[list[str]]: список циклов (SCC без выхода)
        """
        sccs = self._tarjan_iterative(graph)
        infinite_loops = []
        
        for component in sccs:
            if len(component) == 1:
                node = component[0]
                # self-loop
                if node not in graph.get(node, set()):
                    continue
            
            # Проверяем: есть ли выход наружу
            has_exit = False
            
            for node in component:
                for neighbor in graph.get(node, []):
                    if neighbor not in component:
                        has_exit = True
                        break
                if has_exit:
                    break
            
            if not has_exit:
                infinite_loops.append(component)
        
        return infinite_loops
    
    def _tarjan_iterative(self, graph):
        """Итеративная версия алгоритма Тарьяна."""
        index_counter = [0]
        stack = []
        indices = {}
        lowlink = {}
        on_stack = set()
        result = []
        
        # Явный стек вызовов: (node, iterator, state)
        # state: 'enter' или 'exit'
        call_stack = []
        
        for start_node in graph:
            if start_node in indices:
                continue
            
            # Enter node
            call_stack.append({
                'action': 'process',
                'node': start_node,
                'neighbors': iter(graph.get(start_node, [])),
                'index_on_entry': index_counter[0]
            })
            
            while call_stack:
                frame = call_stack[-1]
                node = frame['node']
                
                if frame['action'] == 'process':
                    # Первый визит
                    indices[node] = index_counter[0]
                    lowlink[node] = index_counter[0]
                    index_counter[0] += 1
                    stack.append(node)
                    on_stack.add(node)
                    
                    frame['action'] = 'iterate'
                
                # Обработка соседей
                found_unvisited = False
                
                for neighbor in frame['neighbors']:
                    if neighbor not in indices:
                        # Рекурсивный вызов - push новый frame
                        call_stack.append({
                            'action': 'process',
                            'node': neighbor,
                            'neighbors': iter(graph.get(neighbor, [])),
                            'index_on_entry': index_counter[0],
                            'parent': node
                        })
                        found_unvisited = True
                        break
                    elif neighbor in on_stack:
                        lowlink[node] = min(lowlink[node], indices[neighbor])
                
                if found_unvisited:
                    continue
                
                # Все соседи обработаны - check SCC
                if lowlink[node] == indices[node]:
                    scc = []
                    while True:
                        w = stack.pop()
                        on_stack.remove(w)
                        scc.append(w)
                        if w == node:
                            break
                    result.append(scc)
                
                # Pop и update parent
                call_stack.pop()
                
                if call_stack:
                    parent_frame = call_stack[-1]
                    if 'parent' in frame:
                        parent = frame['parent']
                        if parent in lowlink:
                            lowlink[parent] = min(lowlink[parent], lowlink[node])
        
        return result


class OptimizedStateAnalyzer:
    """
    Оптимизированный анализатор состояний.
    
    Улучшения:
    1. Ограничение глубины обхода
    2. Merge состояний для одного label
    3. Ограничение длины пути
    4. Более эффективные структуры данных
    """
    
    def __init__(self, max_depth=100, max_path_length=50, merge_states=True):
        """
        Инициализация.
        
        Args:
            max_depth: максимальная глубина обхода (None для безлимита)
            max_path_length: максимальная длина сохраняемого пути
            merge_states: объединять ли состояния для одного label
        """
        self.max_depth = max_depth
        self.max_path_length = max_path_length
        self.merge_states = merge_states
    
    def analyze(self, script):
        """
        Анализ состояния сценария.
        
        Args:
            script: IR сценарий
            
        Returns:
            dict: результаты анализа
        """
        from core.ir.model import Assignment, Condition, Menu
        
        results = {
            "impossible_conditions": [],
            "undefined_labels": []
        }
        
        # Очередь: (label, state, path, depth)
        queue = deque()
        queue.append(("start", {}, ["start"], 0))
        
        visited = {}  # label -> state (для merge)
        undefined_labels_checked = set()
        
        while queue:
            label, state, path, depth = queue.popleft()
            
            # Проверка глубины
            if self.max_depth is not None and depth > self.max_depth:
                continue
            
            # Skip if label doesn't exist
            if label not in script.labels:
                if label not in undefined_labels_checked:
                    undefined_labels_checked.add(label)
                    results["undefined_labels"].append({
                        "label": label,
                        "path": path.copy()
                    })
                continue
            
            # Merge states если включено
            if self.merge_states:
                key = label
                if key in visited:
                    # Merge с существующим состоянием
                    merged = self._merge_states(visited[key], state)
                    if merged == visited[key]:
                        # Состояние не изменилось - skip
                        continue
                    visited[key] = merged
                    state = merged
                else:
                    visited[key] = state.copy()
            else:
                key = (label, self._key(state))
                if key in visited:
                    continue
                visited[key] = True
            
            body = script.labels[label].body
            
            for node in body:
                # ASSIGNMENT
                if isinstance(node, Assignment):
                    state = self._apply(state, node)
                
                # CONDITION
                elif isinstance(node, Condition):
                    min_v, max_v = state.get(node.var, (0, 0))
                    
                    if not self._check(min_v, max_v, node.op, node.value):
                        line_num = getattr(node, 'line', None)
                        results["impossible_conditions"].append({
                            "label": label,
                            "path": path.copy(),
                            "var": node.var,
                            "required": node.value,
                            "range": (min_v, max_v),
                            "line": line_num
                        })
                        continue
                    
                    # Process condition body
                    if node.body:
                        for stmt in node.body:
                            if hasattr(stmt, 'target'):
                                new_path = self._extend_path(path, stmt.target)
                                queue.append((stmt.target, state.copy(), new_path, depth + 1))
                            elif isinstance(stmt, Condition):
                                queue.append((label, state.copy(), path, depth))
                            else:
                                queue.append((label, state.copy(), path, depth))
                
                # MENU
                elif isinstance(node, Menu):
                    for option in node.options:
                        option_state = state.copy()
                        for stmt in option.body:
                            if isinstance(stmt, Assignment):
                                option_state = self._apply(option_state, stmt)
                            elif hasattr(stmt, 'target'):
                                new_path = self._extend_path(path, stmt.target)
                                queue.append((stmt.target, option_state.copy(), new_path, depth + 1))
                
                # JUMP
                elif hasattr(node, "target"):
                    new_path = self._extend_path(path, node.target)
                    queue.append((node.target, state.copy(), new_path, depth + 1))
        
        return results
    
    def _extend_path(self, path, target):
        """Расширить путь с ограничением длины."""
        if len(path) >= self.max_path_length:
            # Сохранять только последние элементы
            return path[-self.max_path_length+1:] + [target]
        return path + [target]
    
    def _merge_states(self, old_state, new_state):
        """
        Объединить два состояния для одного label.
        Берет maximum range для каждой переменной.
        """
        merged = old_state.copy()
        
        for var, (new_min, new_max) in new_state.items():
            if var in merged:
                old_min, old_max = merged[var]
                # Расширить диапазон
                merged[var] = (min(old_min, new_min), max(old_max, new_max))
            else:
                merged[var] = (new_min, new_max)
        
        return merged
    
    def _apply(self, state, node):
        """Применить присваивание к состоянию."""
        from core.ir.model import Assignment
        
        state = state.copy()
        min_v, max_v = state.get(node.var, (0, 0))
        
        if node.op == "+=":
            min_v += node.value
            max_v += node.value if max_v != float("inf") else float("inf")
        elif node.op == "-=":
            min_v -= node.value
            max_v -= node.value
        elif node.op == "=":
            min_v = node.value
            max_v = node.value
        
        state[node.var] = (min_v, max_v)
        return state
    
    def _check(self, min_v, max_v, op, value):
        """Проверить условие."""
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
    
    def _key(self, state):
        """Создать ключ для visited."""
        return tuple(sorted((k, v[0], v[1]) for k, v in state.items()))


# Фабрика для создания оптимизированных анализаторов
def create_optimized_analyzers():
    """
    Создает набор оптимизированных анализаторов.
    
    Returns:
        dict: словарь с анализаторами
    """
    return {
        'reachability': OptimizedReachabilityAnalyzer(),
        'dead_ends': None,  # Не требует оптимизации
        'infinite_loops': OptimizedInfiniteLoopAnalyzer(),
        'state': OptimizedStateAnalyzer(
            max_depth=100,
            max_path_length=50,
            merge_states=True
        )
    }
