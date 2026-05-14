#!/usr/bin/env python
"""
Генератор больших тестовых сценариев RenPy для тестирования производительности.
Создает сценарии с контролируемыми параметрами:
- Количество узлов (labels)
- Количество ветвлений (menus)
- Глубина вложенности
- Количество условий (if)
"""

import random
import os


class RenPyScenarioGenerator:
    """Генератор сценариев RenPy с настраиваемыми параметрами."""
    
    def __init__(self, seed=None):
        """
        Инициализация генератора.
        
        Args:
            seed: seed для воспроизводимости (None для случайной генерации)
        """
        if seed is not None:
            random.seed(seed)
        
        self.label_counter = 0
        self.created_labels = []
        self.end_labels = []
        
    def generate_scenario(self, 
                         num_nodes=500,
                         branching_factor=3,
                         max_depth=10,
                         condition_ratio=0.3,
                         output_path=None):
        """
        Генерация большого сценария RenPy.
        
        Args:
            num_nodes: целевое количество узлов (labels)
            branching_factor: среднее количество вариантов в menu
            max_depth: максимальная глубина дерева сценария
            condition_ratio: доля условий (if) среди узлов
            output_path: путь для сохранения файла (None для возврата строки)
            
        Returns:
            str: сгенерированный сценарий
        """
        self.label_counter = 0
        self.created_labels = []
        self.end_labels = []
        
        lines = []
        
        # Стартовый label с инициализацией переменных
        lines.append("label start:")
        lines.append("    $ strength = 0")
        lines.append("    $ intelligence = 0")
        lines.append("    $ luck = 0")
        lines.append("    $ charisma = 0")
        lines.append("")
        
        self.created_labels.append("start")
        
        # Генерируем дерево сценария
        nodes_created = 1  # start уже создан
        target_nodes = num_nodes
        
        # Рекурсивная генерация с ограничением глубины
        self._generate_branch(lines, "start", depth=0, max_depth=max_depth, 
                             nodes_info={'count': nodes_created, 'target': target_nodes},
                             branching_factor=branching_factor,
                             condition_ratio=condition_ratio)
        
        # Добавляем конечные label'ы
        lines.append("")
        for end_label in self.end_labels:
            lines.append(f"label {end_label}:")
            lines.append(f'    "Конец: {end_label}"')
            lines.append("")
        
        script = "\n".join(lines)
        
        if output_path:
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(script)
        
        return script
    
    def _generate_branch(self, lines, parent_label, depth, max_depth, 
                        nodes_info, branching_factor, condition_ratio):
        """Рекурсивная генерация ветвей сценария."""
        
        # Проверяем, не достигли ли лимита узлов
        if nodes_info['count'] >= nodes_info['target']:
            return
        
        # Ограничиваем глубину
        if depth >= max_depth:
            # Создаем терминальный узел
            end_label = f"end_{self.label_counter}"
            self.end_labels.append(end_label)
            lines.append(f"    jump {end_label}")
            lines.append("")
            self.created_labels.append(end_label)
            nodes_info['count'] += 1
            return
        
        # Решаем, что создать: menu или condition
        if random.random() < condition_ratio:
            # Создаем условие if
            self._create_condition(lines, parent_label, depth, max_depth, 
                                 nodes_info, branching_factor, condition_ratio)
        else:
            # Создаем menu с вариантами
            self._create_menu(lines, parent_label, depth, max_depth,
                            nodes_info, branching_factor, condition_ratio)
    
    def _create_condition(self, lines, parent_label, depth, max_depth,
                         nodes_info, branching_factor, condition_ratio):
        """Создание условного перехода if."""
        
        if nodes_info['count'] >= nodes_info['target']:
            return
        
        var = random.choice(['strength', 'intelligence', 'luck', 'charisma'])
        threshold = random.randint(5, 20)
        
        # True branch
        true_label = f"label_{self.label_counter}"
        self.label_counter += 1
        nodes_info['count'] += 1
        
        lines.append(f"    if {var} >= {threshold}:")
        lines.append(f"        jump {true_label}")
        lines.append("")
        
        self.created_labels.append(true_label)
        
        # Генерируем содержимое true branch
        lines.append(f"label {true_label}:")
        lines.append(f"    $ {var} += {random.randint(2, 5)}")
        
        self._generate_branch(lines, true_label, depth + 1, max_depth,
                            nodes_info, branching_factor, condition_ratio)
        
        # False branch (если еще есть место)
        if nodes_info['count'] < nodes_info['target']:
            false_label = f"label_{self.label_counter}"
            self.label_counter += 1
            nodes_info['count'] += 1
            
            lines.append(f"    jump {false_label}")
            lines.append("")
            
            self.created_labels.append(false_label)
            
            lines.append(f"label {false_label}:")
            lines.append(f'    "Ветка false для {true_label}"')
            
            self._generate_branch(lines, false_label, depth + 1, max_depth,
                                nodes_info, branching_factor, condition_ratio)
    
    def _create_menu(self, lines, parent_label, depth, max_depth,
                    nodes_info, branching_factor, condition_ratio):
        """Создание menu с вариантами выбора."""
        
        if nodes_info['count'] >= nodes_info['target']:
            return
        
        num_options = random.randint(2, branching_factor)
        
        lines.append("    menu:")
        
        # First: create all menu options with jumps
        option_labels = []
        for i in range(num_options):
            if nodes_info['count'] >= nodes_info['target']:
                break
            
            option_label = f"label_{self.label_counter}"
            self.label_counter += 1
            nodes_info['count'] += 1
            option_labels.append(option_label)
            
            option_text = random.choice([
                "Go forward",
                "Look around",
                "Talk",
                "Use item",
                "Go back",
                "Explore",
                "Open door",
                "Pick up item"
            ])
            
            # Menu option with 8 spaces, body with 12 spaces
            lines.append(f'        "{option_text}":')
            
            # Add assignment if we want (50% chance)
            if random.random() < 0.5:
                var = random.choice(['strength', 'intelligence', 'luck', 'charisma'])
                lines.append(f"            $ {var} += {random.randint(1, 3)}")
            
            lines.append(f"            jump {option_label}")
            
            self.created_labels.append(option_label)
        
        # Close the menu block
        lines.append("")
        
        # Second: generate content for each option label (after menu closes)
        for option_label in option_labels:
            lines.append(f"label {option_label}:")
            lines.append(f'    "Scene {option_label}"')
            
            self._generate_branch(lines, option_label, depth + 1, max_depth,
                                nodes_info, branching_factor, condition_ratio)
    
    def generate_linear_scenario(self, num_nodes=500, output_path=None):
        """
        Генерация линейного сценария (без ветвлений).
        
        Args:
            num_nodes: количество узлов
            output_path: путь для сохранения
            
        Returns:
            str: сгенерированный сценарий
        """
        lines = []
        lines.append("label start:")
        lines.append('    "Начало истории"')
        lines.append("")
        
        for i in range(1, num_nodes):
            label_name = f"scene_{i}"
            lines.append(f"label {label_name}:")
            lines.append(f'    "Сцена {i}"')
            
            if i < num_nodes - 1:
                next_label = f"scene_{i+1}"
                lines.append(f"    jump {next_label}")
            
            lines.append("")
        
        script = "\n".join(lines)
        
        if output_path:
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(script)
        
        return script
    
    def generate_deep_tree_scenario(self, depth=20, branching=2, output_path=None):
        """
        Генерация глубокого дерева с фиксированной глубиной.
        
        Args:
            depth: глубина дерева
            branching: количество ветвей на каждом уровне
            output_path: путь для сохранения
            
        Returns:
            str: сгенерированный сценарий
        """
        self.label_counter = 0
        self.created_labels = []
        self.end_labels = []
        
        lines = []
        lines.append("label start:")
        lines.append("    $ depth_counter = 0")
        lines.append("")
        self.created_labels.append("start")
        
        self._generate_deep_tree(lines, depth=0, max_depth=depth, 
                                branching=branching)
        
        # Добавляем терминальные label'ы
        lines.append("")
        for end_label in set(self.end_labels):
            lines.append(f"label {end_label}:")
            lines.append(f'    "Конец: {end_label}"')
            lines.append("")
        
        script = "\n".join(lines)
        
        if output_path:
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(script)
        
        return script
    
    def _generate_deep_tree(self, lines, depth, max_depth, branching):
        """Рекурсивная генерация глубокого дерева."""
        
        if depth >= max_depth:
            end_label = f"end_depth_{depth}_{self.label_counter}"
            self.end_labels.append(end_label)
            lines.append(f"    jump {end_label}")
            lines.append("")
            self.label_counter += 1
            return
        
        current_label = f"level_{depth}_{self.label_counter}"
        self.label_counter += 1
        self.created_labels.append(current_label)
        
        lines.append(f"label {current_label}:")
        lines.append(f"    $ depth_counter += 1")
        lines.append("")
        lines.append(f"    menu:")
        
        # First: create all menu options
        next_labels = []
        for i in range(branching):
            next_label = f"level_{depth+1}_{self.label_counter}"
            self.label_counter += 1
            next_labels.append(next_label)
            
            # Menu option with 8 spaces, jump with 12 spaces
            lines.append(f'        "Option {i+1}":')
            lines.append(f"            jump {next_label}")
        
        # Close the menu block
        lines.append("")
        
        # Second: generate content for each next level
        for i, next_label in enumerate(next_labels):
            self.created_labels.append(next_label)
            lines.append(f"label {next_label}:")
            lines.append(f'    "Level {depth+1}, branch {i+1}"')
            lines.append("")
            
            self._generate_deep_tree(lines, depth + 1, max_depth, branching)


def generate_test_suite(output_dir="tests/samples/performance"):
    """
    Генерация набора тестовых сценариев разной сложности.
    
    Args:
        output_dir: директория для сохранения
    """
    generator = RenPyScenarioGenerator(seed=42)
    
    scenarios = [
        # Маленькие сценарии
        ("perf_small_50.rpy", {'num_nodes': 50, 'branching_factor': 2, 'max_depth': 5}),
        ("perf_small_100.rpy", {'num_nodes': 100, 'branching_factor': 2, 'max_depth': 6}),
        
        # Средние сценарии
        ("perf_medium_250.rpy", {'num_nodes': 250, 'branching_factor': 3, 'max_depth': 8}),
        ("perf_medium_500.rpy", {'num_nodes': 500, 'branching_factor': 3, 'max_depth': 10}),
        
        # Большие сценарии
        ("perf_large_1000.rpy", {'num_nodes': 1000, 'branching_factor': 3, 'max_depth': 12}),
        ("perf_large_2000.rpy", {'num_nodes': 2000, 'branching_factor': 4, 'max_depth': 15}),
        
        # Очень большие сценарии
        ("perf_xlarge_5000.rpy", {'num_nodes': 5000, 'branching_factor': 4, 'max_depth': 18}),
        
        # Специальные сценарии
        ("perf_linear_500.rpy", {'type': 'linear', 'num_nodes': 500}),
        # NOTE: Deep tree scenarios removed - they generate too large files (20M+ lines)
        # ("perf_deep_tree.rpy", {'type': 'deep_tree', 'depth': 20, 'branching': 2}),
        # ("perf_wide_tree.rpy", {'type': 'deep_tree', 'depth': 5, 'branching': 5}),
    ]
    
    os.makedirs(output_dir, exist_ok=True)
    
    generated_files = []
    
    for filename, params in scenarios:
        filepath = os.path.join(output_dir, filename)
        
        print(f"Генерация {filename}...")
        
        if params.get('type') == 'linear':
            generator.generate_linear_scenario(
                num_nodes=params['num_nodes'],
                output_path=filepath
            )
        elif params.get('type') == 'deep_tree':
            generator.generate_deep_tree_scenario(
                depth=params['depth'],
                branching=params['branching'],
                output_path=filepath
            )
        else:
            generator.generate_scenario(
                num_nodes=params['num_nodes'],
                branching_factor=params['branching_factor'],
                max_depth=params['max_depth'],
                output_path=filepath
            )
        
        generated_files.append(filepath)
        print(f"  ✓ Создан: {filepath}")
    
    return generated_files


if __name__ == "__main__":
    print("="*70)
    print("ГЕНЕРАТОР ТЕСТОВЫХ СЦЕНАРИЕВ RENPY")
    print("="*70)
    print()
    
    files = generate_test_suite()
    
    print()
    print("="*70)
    print(f"СГЕНЕРИРОВАНО {len(files)} ФАЙЛОВ")
    print("="*70)
