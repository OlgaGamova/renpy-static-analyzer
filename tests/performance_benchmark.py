#!/usr/bin/env python
"""
Бенчмарк производительности системы статического анализа RenPy.

Замеряет время выполнения каждого этапа анализа:
1. Парсинг
2. Трансформация
3. Построение графа
4. Анализ достижимости
5. Анализ мертвых концов
6. Анализ бесконечных циклов
7. Анализ состояния

Результаты сохраняются в JSON для последующего анализа.
"""

import time
import json
import os
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.graph.builder import GraphBuilder
from core.analysis.reachability import ReachabilityAnalyzer
from core.analysis.dead_ends import DeadEndAnalyzer
from core.analysis.infinite_loops import InfiniteLoopAnalyzer
from core.analysis.state import StateAnalyzer


class PerformanceBenchmark:
    """Класс для запуска бенчмарков производительности."""
    
    def __init__(self, output_dir="tests/results/performance"):
        """
        Инициализация бенчмарка.
        
        Args:
            output_dir: директория для сохранения результатов
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.results = []
        
    def run_benchmark(self, script_path, script_name=None):
        """
        Запуск бенчмарка на одном файле.
        
        Args:
            script_path: путь к файлу сценария
            script_name: имя сценария для отчета (None для использования имени файла)
            
        Returns:
            dict: результаты бенчмарка
        """
        if script_name is None:
            script_name = os.path.basename(script_path)
        
        print(f"\n{'='*70}")
        print(f"БЕНЧМАРК: {script_name}")
        print(f"{'='*70}")
        
        # Читаем файл
        with open(script_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        file_size = len(code)
        line_count = code.count('\n') + 1
        
        print(f"Размер файла: {file_size:,} байт")
        print(f"Количество строк: {line_count:,}")
        
        timings = {}
        errors = []
        
        # 1. Парсинг
        print("\n[1/7] Парсинг...", end=' ', flush=True)
        try:
            start = time.perf_counter()
            parser = RenPyParser()
            tree = parser.parse_text(code)
            parse_time = time.perf_counter() - start
            timings['parsing'] = parse_time
            print(f"✓ {parse_time:.3f}с")
        except Exception as e:
            error_msg = f"Ошибка парсинга: {str(e)}"
            print(f"✗ {error_msg}")
            errors.append(error_msg)
            return self._create_error_result(script_name, file_size, line_count, timings, errors)
        
        # 2. Трансформация
        print("[2/7] Трансформация...", end=' ', flush=True)
        try:
            start = time.perf_counter()
            transformer = RenPyTransformer()
            script = transformer.transform(tree)
            transform_time = time.perf_counter() - start
            timings['transformation'] = transform_time
            
            label_count = len(script.labels)
            print(f"✓ {transform_time:.3f}с ({label_count} label'ов)")
        except Exception as e:
            error_msg = f"Ошибка трансформации: {str(e)}"
            print(f"✗ {error_msg}")
            errors.append(error_msg)
            return self._create_error_result(script_name, file_size, line_count, timings, errors)
        
        # 3. Построение графа
        print("[3/7] Построение графа...", end=' ', flush=True)
        try:
            start = time.perf_counter()
            builder = GraphBuilder()
            graph = builder.build(script)
            build_time = time.perf_counter() - start
            timings['graph_building'] = build_time
            
            node_count = len(graph)
            edge_count = sum(len(targets) for targets in graph.values())
            print(f"✓ {build_time:.3f}с ({node_count} узлов, {edge_count} рёбер)")
        except Exception as e:
            error_msg = f"Ошибка построения графа: {str(e)}"
            print(f"✗ {error_msg}")
            errors.append(error_msg)
            return self._create_error_result(script_name, file_size, line_count, timings, errors)
        
        # 4. Анализ достижимости
        print("[4/7] Анализ достижимости...", end=' ', flush=True)
        try:
            start = time.perf_counter()
            reach = ReachabilityAnalyzer()
            unreachable = reach.find_unreachable(graph)
            reach_time = time.perf_counter() - start
            timings['reachability'] = reach_time
            print(f"✓ {reach_time:.3f}с ({len(unreachable)} недостижимых)")
        except Exception as e:
            error_msg = f"Ошибка анализа достижимости: {str(e)}"
            print(f"✗ {error_msg}")
            errors.append(error_msg)
        
        # 5. Анализ мертвых концов
        print("[5/7] Анализ мертвых концов...", end=' ', flush=True)
        try:
            start = time.perf_counter()
            dead = DeadEndAnalyzer()
            dead_ends = dead.find_dead_ends(graph)
            dead_time = time.perf_counter() - start
            timings['dead_ends'] = dead_time
            print(f"✓ {dead_time:.3f}с ({len(dead_ends)} мертвых концов)")
        except Exception as e:
            error_msg = f"Ошибка анализа мертвых концов: {str(e)}"
            print(f"✗ {error_msg}")
            errors.append(error_msg)
        
        # 6. Анализ бесконечных циклов
        print("[6/7] Анализ бесконечных циклов...", end=' ', flush=True)
        try:
            start = time.perf_counter()
            loop = InfiniteLoopAnalyzer()
            infinite_loops = loop.find_infinite_loops(graph)
            loop_time = time.perf_counter() - start
            timings['infinite_loops'] = loop_time
            print(f"✓ {loop_time:.3f}с ({len(infinite_loops)} циклов)")
        except Exception as e:
            error_msg = f"Ошибка анализа циклов: {str(e)}"
            print(f"✗ {error_msg}")
            errors.append(error_msg)
        
        # 7. Анализ состояния
        print("[7/7] Анализ состояния...", end=' ', flush=True)
        try:
            start = time.perf_counter()
            state = StateAnalyzer()
            state_result = state.analyze(script)
            state_time = time.perf_counter() - start
            timings['state_analysis'] = state_time
            
            impossible = len(state_result.get('impossible_conditions', []))
            undefined = len(state_result.get('undefined_labels', []))
            print(f"✓ {state_time:.3f}с ({impossible} невозможных условий, {undefined} undefined)")
        except Exception as e:
            error_msg = f"Ошибка анализа состояния: {str(e)}"
            print(f"✗ {error_msg}")
            errors.append(error_msg)
        
        # Общее время
        total_time = sum(timings.values())
        timings['total'] = total_time
        
        print(f"\n{'='*70}")
        print(f"ОБЩЕЕ ВРЕМЯ: {total_time:.3f}с")
        print(f"{'='*70}")
        
        # Создаем результат
        result = {
            'script_name': script_name,
            'file_size': file_size,
            'line_count': line_count,
            'label_count': len(script.labels) if 'script' in locals() else 0,
            'node_count': len(graph) if 'graph' in locals() else 0,
            'edge_count': sum(len(targets) for targets in graph.values()) if 'graph' in locals() else 0,
            'timings': timings,
            'errors': errors,
            'timestamp': time.time()
        }
        
        self.results.append(result)
        
        return result
    
    def run_benchmarks(self, script_paths):
        """
        Запуск бенчмарков на нескольких файлах.
        
        Args:
            script_paths: список путей к файлам сценариев
            
        Returns:
            list: результаты всех бенчмарков
        """
        all_results = []
        
        for script_path in script_paths:
            if os.path.exists(script_path):
                result = self.run_benchmark(script_path)
                all_results.append(result)
            else:
                print(f"\n⚠ Файл не найден: {script_path}")
        
        return all_results
    
    def save_results(self, filename=None):
        """
        Сохранение результатов в JSON.
        
        Args:
            filename: имя файла (None для автоматического)
        """
        if filename is None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"benchmark_{timestamp}.json"
        
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"\nРезультаты сохранены: {filepath}")
        return filepath
    
    def print_summary(self):
        """Вывод сводки по всем результатам."""
        if not self.results:
            print("\nНет результатов для вывода.")
            return
        
        print(f"\n{'='*70}")
        print("СВОДКА ПО ВСЕМ БЕНЧМАРКАМ")
        print(f"{'='*70}")
        print(f"{'Сценарий':<30} {'Узлы':>6} {'Рёбра':>7} {'Время':>8}")
        print(f"{'-'*70}")
        
        for result in self.results:
            name = result['script_name'][:28]
            nodes = result['node_count']
            edges = result['edge_count']
            total = result['timings'].get('total', 0)
            
            print(f"{name:<30} {nodes:>6} {edges:>7} {total:>7.3f}с")
        
        print(f"{'='*70}")
        
        # Статистика
        if self.results:
            total_times = [r['timings'].get('total', 0) for r in self.results]
            print(f"Всего сценариев: {len(self.results)}")
            print(f"Мин. время: {min(total_times):.3f}с")
            print(f"Макс. время: {max(total_times):.3f}с")
            print(f"Среднее время: {sum(total_times)/len(total_times):.3f}с")
            print(f"{'='*70}")
    
    def _create_error_result(self, script_name, file_size, line_count, timings, errors):
        """Создание результата с ошибкой."""
        result = {
            'script_name': script_name,
            'file_size': file_size,
            'line_count': line_count,
            'label_count': 0,
            'node_count': 0,
            'edge_count': 0,
            'timings': timings,
            'errors': errors,
            'timestamp': time.time()
        }
        self.results.append(result)
        return result


def main():
    """Главная функция запуска бенчмарков."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Бенчмарк производительности RenPy анализатора')
    parser.add_argument('--scenarios', nargs='+', help='Пути к файлам сценариев')
    parser.add_argument('--scenario-dir', help='Директория со сценариями')
    parser.add_argument('--output-dir', default='tests/results/performance',
                       help='Директория для результатов')
    parser.add_argument('--generate', action='store_true',
                       help='Сгенерировать тестовые сценарии перед тестом')
    parser.add_argument('--save', action='store_true',
                       help='Сохранить результаты в JSON')
    
    args = parser.parse_args()
    
    # Генерация сценариев если нужно
    if args.generate:
        print("="*70)
        print("ГЕНЕРАЦИЯ ТЕСТОВЫХ СЦЕНАРИЕВ")
        print("="*70)
        
        from tests.generate_performance_scenarios import generate_test_suite
        
        scenario_dir = args.scenario_dir or 'tests/samples/performance'
        generate_test_suite(scenario_dir)
    
    # Определяем сценарии для тестирования
    scenario_dir = args.scenario_dir or 'tests/samples/performance'
    
    if args.scenarios:
        script_paths = args.scenarios
    else:
        # Ищем все .rpy файлы в директории
        if os.path.exists(scenario_dir):
            script_paths = [
                os.path.join(scenario_dir, f)
                for f in os.listdir(scenario_dir)
                if f.endswith('.rpy')
            ]
            script_paths.sort()
        else:
            print(f"Директория не найдена: {scenario_dir}")
            print("Используйте --generate для создания тестовых сценариев")
            return
    
    if not script_paths:
        print("Не найдено сценариев для тестирования")
        return
    
    print(f"\nНайдено {len(script_paths)} сценариев для тестирования")
    
    # Запуск бенчмарков
    benchmark = PerformanceBenchmark(output_dir=args.output_dir)
    benchmark.run_benchmarks(script_paths)
    
    # Вывод результатов
    benchmark.print_summary()
    
    # Сохранение
    if args.save:
        benchmark.save_results()


if __name__ == "__main__":
    main()
