#!/usr/bin/env python
"""
Pytest тесты для проверки производительности системы.

Тесты проверяют:
1. Время выполнения анализа для разных размеров сценариев
2. Отсутствие ошибок при обработке больших сценариев
3. Линейность масштабирования (или близкую к ней)
"""

import pytest
import time
import os
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.graph.builder import GraphBuilder
from core.analysis.reachability import ReachabilityAnalyzer
from core.analysis.dead_ends import DeadEndAnalyzer
from core.analysis.infinite_loops import InfiniteLoopAnalyzer
from core.analysis.state import StateAnalyzer


@pytest.fixture
def parser():
    """Фикстура для создания парсера."""
    return RenPyParser()


@pytest.fixture
def transformer():
    """Фикстура для создания трансформера."""
    return RenPyTransformer()


@pytest.fixture
def graph_builder():
    """Фикстура для создания построителя графа."""
    return GraphBuilder()


def create_test_scenario(num_labels, branching=2, include_conditions=True):
    """
    Создание тестового сценария с заданным количеством label'ов.
    
    Args:
        num_labels: количество label'ов
        branching: количество ветвей в menu
        include_conditions: включать ли условия if
        
    Returns:
        str: сценарий RenPy
    """
    lines = []
    lines.append("label start:")
    lines.append("    $ stat = 0")
    lines.append("")
    
    for i in range(1, num_labels):
        label_name = f"label_{i}"
        lines.append(f"label {label_name}:")
        lines.append(f'    "Сцена {i}"')
        lines.append(f"    $ stat += 1")
        
        # Добавляем переходы
        if i < num_labels - 1:
            if include_conditions and i % 3 == 0:
                # Условный переход
                next_label = f"label_{i+1}"
                lines.append(f"    if stat >= {i}:")
                lines.append(f"        jump {next_label}")
            else:
                # Menu с ветвлениями
                lines.append("    menu:")
                for j in range(min(branching, num_labels - i - 1)):
                    target = f"label_{i+j+1}"
                    lines.append(f'        "Вариант {j+1}":')
                    lines.append(f"            jump {target}")
        else:
            lines.append('    "Конец"')
        
        lines.append("")
    
    return "\n".join(lines)


class TestPerformanceSmall:
    """Тесты производительности для маленьких сценариев (до 100 узлов)."""
    
    def test_50_nodes_parsing(self, parser):
        """Парсинг сценария с 50 узлами должен занимать < 1 секунды."""
        script = create_test_scenario(50)
        
        start = time.perf_counter()
        tree = parser.parse_text(script)
        elapsed = time.perf_counter() - start
        
        assert elapsed < 1.0, f"Парсинг 50 узлов занял {elapsed:.3f}с (ожидалось < 1с)"
    
    def test_50_nodes_full_analysis(self, parser, transformer, graph_builder):
        """Полный анализ сценария с 50 узлами должен занимать < 2 секунд."""
        script = create_test_scenario(50)
        
        start = time.perf_counter()
        
        tree = parser.parse_text(script)
        ir = transformer.transform(tree)
        graph = graph_builder.build(ir)
        
        reach = ReachabilityAnalyzer()
        reach.find_unreachable(graph)
        
        dead = DeadEndAnalyzer()
        dead.find_dead_ends(graph)
        
        loop = InfiniteLoopAnalyzer()
        loop.find_infinite_loops(graph)
        
        state = StateAnalyzer()
        state.analyze(ir)
        
        elapsed = time.perf_counter() - start
        
        assert elapsed < 2.0, f"Полный анализ 50 узлов занял {elapsed:.3f}с (ожидалось < 2с)"
    
    def test_100_nodes_full_analysis(self, parser, transformer, graph_builder):
        """Полный анализ сценария с 100 узлами должен занимать < 3 секунд."""
        script = create_test_scenario(100)
        
        start = time.perf_counter()
        
        tree = parser.parse_text(script)
        ir = transformer.transform(tree)
        graph = graph_builder.build(ir)
        
        reach = ReachabilityAnalyzer()
        reach.find_unreachable(graph)
        
        dead = DeadEndAnalyzer()
        dead.find_dead_ends(graph)
        
        loop = InfiniteLoopAnalyzer()
        loop.find_infinite_loops(graph)
        
        state = StateAnalyzer()
        state.analyze(ir)
        
        elapsed = time.perf_counter() - start
        
        assert elapsed < 3.0, f"Полный анализ 100 узлов занял {elapsed:.3f}с (ожидалось < 3с)"


class TestPerformanceMedium:
    """Тесты производительности для средних сценариев (100-500 узлов)."""
    
    def test_250_nodes_full_analysis(self, parser, transformer, graph_builder):
        """Полный анализ сценария с 250 узлами должен занимать < 10 секунд."""
        script = create_test_scenario(250, branching=3)
        
        start = time.perf_counter()
        
        tree = parser.parse_text(script)
        ir = transformer.transform(tree)
        graph = graph_builder.build(ir)
        
        reach = ReachabilityAnalyzer()
        reach.find_unreachable(graph)
        
        dead = DeadEndAnalyzer()
        dead.find_dead_ends(graph)
        
        loop = InfiniteLoopAnalyzer()
        loop.find_infinite_loops(graph)
        
        state = StateAnalyzer()
        state.analyze(ir)
        
        elapsed = time.perf_counter() - start
        
        assert elapsed < 10.0, f"Полный анализ 250 узлов занял {elapsed:.3f}с (ожидалось < 10с)"
    
    def test_500_nodes_full_analysis(self, parser, transformer, graph_builder):
        """Полный анализ сценария с 500 узлами должен занимать < 30 секунд."""
        script = create_test_scenario(500, branching=3)
        
        start = time.perf_counter()
        
        tree = parser.parse_text(script)
        ir = transformer.transform(tree)
        graph = graph_builder.build(ir)
        
        reach = ReachabilityAnalyzer()
        reach.find_unreachable(graph)
        
        dead = DeadEndAnalyzer()
        dead.find_dead_ends(graph)
        
        loop = InfiniteLoopAnalyzer()
        loop.find_infinite_loops(graph)
        
        state = StateAnalyzer()
        state.analyze(ir)
        
        elapsed = time.perf_counter() - start
        
        assert elapsed < 30.0, f"Полный анализ 500 узлов занял {elapsed:.3f}с (ожидалось < 30с)"


class TestPerformanceLarge:
    """Тесты производительности для больших сценариев (500+ узлов)."""
    
    @pytest.mark.slow
    def test_1000_nodes_full_analysis(self, parser, transformer, graph_builder):
        """Полный анализ сценария с 1000 узлами должен занимать < 60 секунд."""
        script = create_test_scenario(1000, branching=3)
        
        start = time.perf_counter()
        
        tree = parser.parse_text(script)
        ir = transformer.transform(tree)
        graph = graph_builder.build(ir)
        
        reach = ReachabilityAnalyzer()
        reach.find_unreachable(graph)
        
        dead = DeadEndAnalyzer()
        dead.find_dead_ends(graph)
        
        loop = InfiniteLoopAnalyzer()
        loop.find_infinite_loops(graph)
        
        state = StateAnalyzer()
        state.analyze(ir)
        
        elapsed = time.perf_counter() - start
        
        assert elapsed < 60.0, f"Полный анализ 1000 узлов занял {elapsed:.3f}с (ожидалось < 60с)"


class TestPerformanceScenarios:
    """Тесты на реальных сгенерированных сценариях."""
    
    @pytest.fixture
    def performance_dir(self):
        """Директория с производительными сценариями."""
        return Path(__file__).parent.parent / "samples" / "performance"
    
    def test_small_scenario_exists(self, performance_dir):
        """Проверка существования маленького сценария."""
        scenario_path = performance_dir / "perf_small_50.rpy"
        assert scenario_path.exists(), "Сценарий perf_small_50.rpy не найден. Запустите generate_performance_scenarios.py"
    
    def test_medium_scenario_exists(self, performance_dir):
        """Проверка существования среднего сценария."""
        scenario_path = performance_dir / "perf_medium_500.rpy"
        assert scenario_path.exists(), "Сценарий perf_medium_500.rpy не найден. Запустите generate_performance_scenarios.py"
    
    def test_large_scenario_exists(self, performance_dir):
        """Проверка существования большого сценария."""
        scenario_path = performance_dir / "perf_large_1000.rpy"
        assert scenario_path.exists(), "Сценарий perf_large_1000.rpy не найден. Запустите generate_performance_scenarios.py"
    
    def test_xlarge_scenario_exists(self, performance_dir):
        """Проверка существования очень большого сценария (5000 узлов)."""
        scenario_path = performance_dir / "perf_xlarge_5000.rpy"
        assert scenario_path.exists(), "Сценарий perf_xlarge_5000.rpy не найден. Запустите generate_performance_scenarios.py"
    
    def test_existing_small_scenario(self, parser, transformer, graph_builder, performance_dir):
        """Тест на существующем маленьком сценарии."""
        scenario_path = performance_dir / "perf_small_50.rpy"
        
        if not scenario_path.exists():
            pytest.skip("Сценарий не сгенерирован")
        
        with open(scenario_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        start = time.perf_counter()
        
        tree = parser.parse_text(code)
        ir = transformer.transform(tree)
        graph = graph_builder.build(ir)
        
        reach = ReachabilityAnalyzer()
        reach.find_unreachable(graph)
        
        dead = DeadEndAnalyzer()
        dead.find_dead_ends(graph)
        
        loop = InfiniteLoopAnalyzer()
        loop.find_infinite_loops(graph)
        
        state = StateAnalyzer()
        state.analyze(ir)
        
        elapsed = time.perf_counter() - start
        
        assert elapsed < 5.0, f"Анализ малого сценария занял {elapsed:.3f}с"
    
    def test_existing_medium_scenario(self, parser, transformer, graph_builder, performance_dir):
        """Тест на существующем среднем сценарии."""
        scenario_path = performance_dir / "perf_medium_500.rpy"
        
        if not scenario_path.exists():
            pytest.skip("Сценарий не сгенерирован")
        
        with open(scenario_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        start = time.perf_counter()
        
        tree = parser.parse_text(code)
        ir = transformer.transform(tree)
        graph = graph_builder.build(ir)
        
        reach = ReachabilityAnalyzer()
        reach.find_unreachable(graph)
        
        dead = DeadEndAnalyzer()
        dead.find_dead_ends(graph)
        
        loop = InfiniteLoopAnalyzer()
        loop.find_infinite_loops(graph)
        
        state = StateAnalyzer()
        state.analyze(ir)
        
        elapsed = time.perf_counter() - start
        
        assert elapsed < 30.0, f"Анализ среднего сценария занял {elapsed:.3f}с"
    
    def test_existing_xlarge_scenario(self, parser, transformer, graph_builder, performance_dir):
        """Тест на существующем очень большом сценарии (5000 узлов)."""
        scenario_path = performance_dir / "perf_xlarge_5000.rpy"
        
        if not scenario_path.exists():
            pytest.skip("Сценарий не сгенерирован")
        
        with open(scenario_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        start = time.perf_counter()
        
        tree = parser.parse_text(code)
        ir = transformer.transform(tree)
        graph = graph_builder.build(ir)
        
        reach = ReachabilityAnalyzer()
        reach.find_unreachable(graph)
        
        dead = DeadEndAnalyzer()
        dead.find_dead_ends(graph)
        
        loop = InfiniteLoopAnalyzer()
        loop.find_infinite_loops(graph)
        
        state = StateAnalyzer()
        state.analyze(ir)
        
        elapsed = time.perf_counter() - start
        
        # 5000 узлов может занять больше времени
        assert elapsed < 300.0, f"Анализ очень большого сценария занял {elapsed:.3f}с (ожидалось < 5 минут)"


class TestPerformanceScaling:
    """Тесты масштабирования производительности."""
    
    def test_scaling_50_to_100(self, parser, transformer, graph_builder):
        """Проверка, что увеличение в 2 раза не приводит к экспоненциальному замедлению."""
        # 50 узлов
        script_50 = create_test_scenario(50)
        
        start = time.perf_counter()
        tree_50 = parser.parse_text(script_50)
        ir_50 = transformer.transform(tree_50)
        graph_50 = graph_builder.build(ir_50)
        state_50 = StateAnalyzer()
        state_50.analyze(ir_50)
        time_50 = time.perf_counter() - start
        
        # 100 узлов
        script_100 = create_test_scenario(100)
        
        start = time.perf_counter()
        tree_100 = parser.parse_text(script_100)
        ir_100 = transformer.transform(tree_100)
        graph_100 = graph_builder.build(ir_100)
        state_100 = StateAnalyzer()
        state_100.analyze(ir_100)
        time_100 = time.perf_counter() - start
        
        # Время не должно увеличиться более чем в 10 раз (с запасом на нелинейность)
        if time_50 > 0:
            ratio = time_100 / time_50
            assert ratio < 10, f"Время увеличилось в {ratio:.1f} раз при удвоении размера (ожидалось < 10x)"
    
    def test_no_errors_on_large_scenario(self, parser, transformer, graph_builder):
        """Проверка отсутствия ошибок на большом сценарии."""
        script = create_test_scenario(500, branching=3, include_conditions=True)
        
        # Не должно быть исключений
        tree = parser.parse_text(script)
        ir = transformer.transform(tree)
        graph = graph_builder.build(ir)
        
        reach = ReachabilityAnalyzer()
        unreachable = reach.find_unreachable(graph)
        
        dead = DeadEndAnalyzer()
        dead_ends = dead.find_dead_ends(graph)
        
        loop = InfiniteLoopAnalyzer()
        loops = loop.find_infinite_loops(graph)
        
        state = StateAnalyzer()
        state_result = state.analyze(ir)
        
        # Результаты должны быть корректными
        assert isinstance(unreachable, set)
        assert isinstance(dead_ends, set)
        assert isinstance(loops, list)
        assert isinstance(state_result, dict)


class TestMemoryLeaks:
    """Тесты на утечки памяти (базовые)."""
    
    def test_multiple_runs_same_scenario(self, parser, transformer, graph_builder):
        """Многократный запуск одного сценария не должен приводить к проблемам."""
        script = create_test_scenario(100)
        
        for i in range(5):
            tree = parser.parse_text(script)
            ir = transformer.transform(tree)
            graph = graph_builder.build(ir)
            
            reach = ReachabilityAnalyzer()
            reach.find_unreachable(graph)
            
            dead = DeadEndAnalyzer()
            dead.find_dead_ends(graph)
            
            loop = InfiniteLoopAnalyzer()
            loop.find_infinite_loops(graph)
            
            state = StateAnalyzer()
            state.analyze(ir)
        
        # Если дошли сюда без ошибок - тест пройден
        assert True
