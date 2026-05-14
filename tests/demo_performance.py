#!/usr/bin/env python
"""
Демонстрация системы тестирования производительности.

Этот скрипт показывает:
1. Генерацию сценария
2. Запуск бенчмарка
3. Применение оптимизаций
4. Сравнение результатов
"""

import sys
import time
from pathlib import Path

# Добавляем корень проекта
sys.path.insert(0, str(Path(__file__).parent.parent))

from tests.generate_performance_scenarios import RenPyScenarioGenerator
from tests.performance_benchmark import PerformanceBenchmark


def print_header(text):
    """Вывод заголовка."""
    print("\n" + "="*70)
    print(text)
    print("="*70)


def print_subheader(text):
    """Вывод подзаголовка."""
    print("\n" + "-"*70)
    print(text)
    print("-"*70)


def demo():
    """Главная демонстрация."""
    
    print_header("ДЕМОНСТРАЦИЯ СИСТЕМЫ ТЕСТИРОВАНИЯ ПРОИЗВОДИТЕЛЬНОСТИ")
    
    # Шаг 1: Генерация сценария
    print_subheader("ШАГ 1: Генерация тестового сценария (500 узлов)")
    
    generator = RenPyScenarioGenerator(seed=42)
    
    print("Генерация сценария с параметрами:")
    print("  - Узлов: 500")
    print("  - Branching factor: 3")
    print("  - Max depth: 10")
    print("  - Condition ratio: 0.3")
    
    start = time.perf_counter()
    script = generator.generate_scenario(
        num_nodes=500,
        branching_factor=3,
        max_depth=10,
        condition_ratio=0.3,
        output_path="demo_scenario.rpy"
    )
    gen_time = time.perf_counter() - start
    
    print(f"\n✓ Сценарий сгенерирован за {gen_time:.3f}с")
    print(f"  Размер: {len(script):,} байт")
    print(f"  Строк: {script.count(chr(10)):,}")
    print(f"  Сохранен в: demo_scenario.rpy")
    
    # Шаг 2: Бенчмарк
    print_subheader("ШАГ 2: Запуск бенчмарка")
    
    benchmark = PerformanceBenchmark(output_dir="demo_results")
    
    print("Запуск полного анализа...")
    result = benchmark.run_benchmark("demo_scenario.rpy", "demo_scenario")
    
    # Шаг 3: Вывод результатов
    print_subheader("ШАГ 3: Результаты анализа")
    
    print(f"\nСценарий: {result['script_name']}")
    print(f"Узлов: {result['node_count']}")
    print(f"Рёбер: {result['edge_count']}")
    
    print("\nВремя выполнения по этапам:")
    print(f"  Парсинг:            {result['timings'].get('parsing', 0):.3f}с")
    print(f"  Трансформация:      {result['timings'].get('transformation', 0):.3f}с")
    print(f"  Построение графа:   {result['timings'].get('graph_building', 0):.3f}с")
    print(f"  Достижимость:       {result['timings'].get('reachability', 0):.3f}с")
    print(f"  Мертвые концы:      {result['timings'].get('dead_ends', 0):.3f}с")
    print(f"  Бесконечные циклы:  {result['timings'].get('infinite_loops', 0):.3f}с")
    print(f"  Состояния:          {result['timings'].get('state_analysis', 0):.3f}с")
    print(f"  ─────────────────────────────────")
    print(f"  ИТОГО:              {result['timings'].get('total', 0):.3f}с")
    
    # Анализ bottleneck
    if result['timings'].get('state_analysis', 0) > 0:
        state_percent = result['timings']['state_analysis'] / result['timings']['total'] * 100
        print(f"\n  StateAnalyzer занимает: {state_percent:.1f}% времени")
        
        if state_percent > 80:
            print("  ⚠️  StateAnalyzer - основной bottleneck!")
            print("  💡 Рекомендуется использовать OptimizedStateAnalyzer")
    
    # Шаг 4: Демонстрация оптимизаций
    print_subheader("ШАГ 4: Применение оптимизаций")
    
    print("\nИмпорт оптимизированных анализаторов...")
    
    try:
        from core.analysis.optimized import (
            OptimizedReachabilityAnalyzer,
            OptimizedInfiniteLoopAnalyzer,
            OptimizedStateAnalyzer
        )
        
        print("✓ Оптимизированные анализаторы доступны")
        
        # Повторный анализ с оптимизациями
        print("\nЗапуск анализа с оптимизациями...")
        
        from core.parser.parser import RenPyParser
        from core.parser.transformer import RenPyTransformer
        from core.graph.builder import GraphBuilder
        
        parser = RenPyParser()
        transformer = RenPyTransformer()
        builder = GraphBuilder()
        
        tree = parser.parse_text(script)
        ir = transformer.transform(tree)
        graph = builder.build(ir)
        
        # Оптимизированный анализ
        opt_start = time.perf_counter()
        
        reach = OptimizedReachabilityAnalyzer()
        reach.find_unreachable(graph)
        
        loop = OptimizedInfiniteLoopAnalyzer()
        loop.find_infinite_loops(graph)
        
        state = OptimizedStateAnalyzer(max_depth=100, merge_states=True)
        state.analyze(ir)
        
        opt_time = time.perf_counter() - opt_start
        
        original_time = result['timings']['total']
        improvement = (original_time - opt_time) / original_time * 100 if original_time > 0 else 0
        
        print(f"\n✓ Оптимизированный анализ завершен за {opt_time:.3f}с")
        print(f"  Оригинальное время: {original_time:.3f}с")
        print(f"  Улучшение: {improvement:+.1f}%")
        
        if improvement > 20:
            print(f"  🎉 Отличное улучшение! Экономия: {original_time - opt_time:.3f}с")
        
    except ImportError as e:
        print(f"⚠️  Не удалось импортировать оптимизации: {e}")
        print("  Это нормально для демонстрации")
    
    # Шаг 5: Рекомендации
    print_subheader("ШАГ 5: Рекомендации")
    
    total_time = result['timings'].get('total', 0)
    
    if total_time < 1:
        print("✅ Производительность отличная!")
        print("   Текущая система справляется хорошо.")
    elif total_time < 10:
        print("⚠️  Производительность приемлемая.")
        print("   Для больших сценариев рекомендуются оптимизации.")
    else:
        print("❌ Производительность требует улучшения.")
        print("   Обязательно примените оптимизации из optimized.py")
    
    print("\nСледующие шаги:")
    print("  1. Запустить полный набор тестов: run_performance_tests.bat")
    print("  2. Проверить результаты: tests/results/performance/")
    print("  3. Применить оптимизации: core/analysis/optimized.py")
    print("  4. Прочитать документацию: PERFORMANCE_QUICKSTART.md")
    
    # Финал
    print_header("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    
    print("\nСозданные файлы:")
    print("  ✓ demo_scenario.rpy - тестовый сценарий")
    print("  ✓ demo_results/ - результаты бенчмарка")
    
    print("\nДокументация:")
    print("  📖 PERFORMANCE_QUICKSTART.md - быстрый старт")
    print("  📖 PERFORMANCE_FULL_GUIDE.md - полная инструкция")
    print("  📖 PERFORMANCE_ANALYSIS.md - анализ проблем")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    try:
        demo()
    except KeyboardInterrupt:
        print("\n\n⚠️  Демонстрация прервана пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Ошибка во время демонстрации: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
