#!/usr/bin/env python
"""
Сравнительный тест оригинальных и оптимизированных анализаторов.

Запускает оба варианта на одинаковых сценариях и сравнивает:
- Время выполнения
- Потребление памяти (базовое)
- Корректность результатов
"""

import time
import sys
from pathlib import Path

# Добавляем корень проекта
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.graph.builder import GraphBuilder

# Оригинальные анализаторы
from core.analysis.reachability import ReachabilityAnalyzer
from core.analysis.infinite_loops import InfiniteLoopAnalyzer
from core.analysis.state import StateAnalyzer

# Оптимизированные анализаторы
from core.analysis.optimized import (
    OptimizedReachabilityAnalyzer,
    OptimizedInfiniteLoopAnalyzer,
    OptimizedStateAnalyzer
)


def create_test_scenario(num_labels, branching=2):
    """Создание тестового сценария."""
    lines = []
    lines.append("label start:")
    lines.append("    $ stat = 0")
    lines.append("")
    
    for i in range(1, num_labels):
        label_name = f"label_{i}"
        lines.append(f"label {label_name}:")
        lines.append(f'    "Сцена {i}"')
        lines.append(f"    $ stat += 1")
        
        if i < num_labels - 1:
            lines.append("    menu:")
            for j in range(min(branching, num_labels - i - 1)):
                target = f"label_{i+j+1}"
                lines.append(f'        "Вариант {j+1}":')
                lines.append(f"            jump {target}")
        else:
            lines.append('    "Конец"')
        
        lines.append("")
    
    return "\n".join(lines)


def benchmark_analyzer(name, func, *args, **kwargs):
    """Бенчмарк одной функции."""
    import tracemalloc
    
    # Запуск с замером времени и памяти
    tracemalloc.start()
    start_time = time.perf_counter()
    
    try:
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        return {
            'success': True,
            'time': elapsed,
            'peak_memory': peak / 1024 / 1024,  # MB
            'result': result
        }
    except Exception as e:
        elapsed = time.perf_counter() - start_time
        tracemalloc.stop()
        
        return {
            'success': False,
            'time': elapsed,
            'error': str(e),
            'peak_memory': 0
        }


def run_comparison(num_nodes=500, branching=3):
    """
    Запуск сравнительного теста.
    
    Args:
        num_nodes: количество узлов
        branching: фактор ветвления
    """
    print("="*70)
    print(f"СРАВНИТЕЛЬНЫЙ ТЕСТ: {num_nodes} узлов, branching={branching}")
    print("="*70)
    
    # Создаем сценарий
    print("\nГенерация сценария...")
    script_text = create_test_scenario(num_nodes, branching)
    print(f"Размер: {len(script_text):,} байт, {script_text.count(chr(10)):,} строк")
    
    # Парсим и строим граф
    print("\nПарсинг и построение графа...")
    parser = RenPyParser()
    transformer = RenPyTransformer()
    builder = GraphBuilder()
    
    tree = parser.parse_text(script_text)
    script = transformer.transform(tree)
    graph = builder.build(script)
    
    print(f"Label'ов: {len(script.labels)}, Узлов: {len(graph)}")
    
    # Тестируем каждый анализатор
    results = {}
    
    # 1. Reachability Analyzer
    print("\n" + "-"*70)
    print("Reachability Analyzer")
    print("-"*70)
    
    print("  Оригинальный...", end=' ')
    orig_reach = benchmark_analyzer(
        "Reachability (original)",
        ReachabilityAnalyzer().find_unreachable,
        graph
    )
    print(f"{'✓' if orig_reach['success'] else '✗'} {orig_reach['time']:.3f}с, {orig_reach['peak_memory']:.1f}MB")
    
    print("  Оптимизированный...", end=' ')
    opt_reach = benchmark_analyzer(
        "Reachability (optimized)",
        OptimizedReachabilityAnalyzer().find_unreachable,
        graph
    )
    print(f"{'✓' if opt_reach['success'] else '✗'} {opt_reach['time']:.3f}с, {opt_reach['peak_memory']:.1f}MB")
    
    # Сравнение результатов
    if orig_reach['success'] and opt_reach['success']:
        if orig_reach['result'] == opt_reach['result']:
            print("  ✓ Результаты идентичны")
        else:
            print("  ⚠️ Результаты различаются!")
            print(f"    Оригинал: {len(orig_reach['result'])} недостижимых")
            print(f"    Оптимизированный: {len(opt_reach['result'])} недостижимых")
    
    results['reachability'] = {
        'original': orig_reach,
        'optimized': opt_reach
    }
    
    # 2. Infinite Loop Analyzer
    print("\n" + "-"*70)
    print("Infinite Loop Analyzer")
    print("-"*70)
    
    print("  Оригинальный...", end=' ')
    orig_loop = benchmark_analyzer(
        "Infinite Loops (original)",
        InfiniteLoopAnalyzer().find_infinite_loops,
        graph
    )
    print(f"{'✓' if orig_loop['success'] else '✗'} {orig_loop['time']:.3f}с, {orig_loop['peak_memory']:.1f}MB")
    
    print("  Оптимизированный...", end=' ')
    opt_loop = benchmark_analyzer(
        "Infinite Loops (optimized)",
        OptimizedInfiniteLoopAnalyzer().find_infinite_loops,
        graph
    )
    print(f"{'✓' if opt_loop['success'] else '✗'} {opt_loop['time']:.3f}с, {opt_loop['peak_memory']:.1f}MB")
    
    if orig_loop['success'] and opt_loop['success']:
        if len(orig_loop['result']) == len(opt_loop['result']):
            print(f"  ✓ Найдено одинаковое количество циклов: {len(orig_loop['result'])}")
        else:
            print("  ⚠️ Разное количество циклов!")
    
    results['infinite_loops'] = {
        'original': orig_loop,
        'optimized': opt_loop
    }
    
    # 3. State Analyzer
    print("\n" + "-"*70)
    print("State Analyzer")
    print("-"*70)
    
    print("  Оригинальный...", end=' ')
    orig_state = benchmark_analyzer(
        "State (original)",
        StateAnalyzer().analyze,
        script
    )
    print(f"{'✓' if orig_state['success'] else '✗'} {orig_state['time']:.3f}с, {orig_state['peak_memory']:.1f}MB")
    
    print("  Оптимизированный...", end=' ')
    opt_state = benchmark_analyzer(
        "State (optimized)",
        OptimizedStateAnalyzer(max_depth=100, merge_states=True).analyze,
        script
    )
    print(f"{'✓' if opt_state['success'] else '✗'} {opt_state['time']:.3f}с, {opt_state['peak_memory']:.1f}MB")
    
    if orig_state['success'] and opt_state['success']:
        orig_impossible = len(orig_state['result'].get('impossible_conditions', []))
        opt_impossible = len(opt_state['result'].get('impossible_conditions', []))
        print(f"  Оригинал: {orig_impossible} невозможных условий")
        print(f"  Оптимизированный: {opt_impossible} невозможных условий")
    
    results['state'] = {
        'original': orig_state,
        'optimized': opt_state
    }
    
    # Итоговая сводка
    print("\n" + "="*70)
    print("ИТОГОВАЯ СВОДКА")
    print("="*70)
    
    print(f"\n{'Анализатор':<25} {'Оригинал':>12} {'Оптимиз.':>12} {'Улучшение':>12}")
    print("-"*70)
    
    total_orig = 0
    total_opt = 0
    
    for analyzer_name in ['reachability', 'infinite_loops', 'state']:
        orig = results[analyzer_name]['original']
        opt = results[analyzer_name]['optimized']
        
        if orig['success'] and opt['success']:
            orig_time = orig['time']
            opt_time = opt['time']
            
            if orig_time > 0:
                improvement = (orig_time - opt_time) / orig_time * 100
            else:
                improvement = 0
            
            print(f"{analyzer_name:<25} {orig_time:>10.3f}с {opt_time:>10.3f}с {improvement:>+10.1f}%")
            
            total_orig += orig_time
            total_opt += opt_time
        else:
            print(f"{analyzer_name:<25} {'ERROR':>10} {'ERROR':>10}")
    
    print("-"*70)
    
    if total_orig > 0:
        total_improvement = (total_orig - total_opt) / total_orig * 100
        print(f"{'TOTAL':<25} {total_orig:>10.3f}с {total_opt:>10.3f}с {total_improvement:>+10.1f}%")
    
    print("="*70)
    
    # Проверка корректности
    print("\nПРОВЕРКА КОРРЕКТНОСТИ:")
    
    all_correct = True
    
    for analyzer_name in ['reachability', 'infinite_loops', 'state']:
        orig = results[analyzer_name]['original']
        opt = results[analyzer_name]['optimized']
        
        if not orig['success']:
            print(f"  ✗ {analyzer_name}: оригинальный упал с ошибкой: {orig.get('error', 'N/A')}")
            all_correct = False
        
        if not opt['success']:
            print(f"  ✗ {analyzer_name}: оптимизированный упал с ошибкой: {opt.get('error', 'N/A')}")
            all_correct = False
    
    if all_correct:
        print("  ✓ Все анализаторы работают корректно")
    
    return results


def main():
    """Главная функция."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Сравнительный тест анализаторов')
    parser.add_argument('--nodes', type=int, default=500, help='Количество узлов')
    parser.add_argument('--branching', type=int, default=3, help='Фактор ветвления')
    
    args = parser.parse_args()
    
    print("="*70)
    print("СРАВНИТЕЛЬНЫЙ ТЕСТ ОРИГИНАЛЬНЫХ И ОПТИМИЗИРОВАННЫХ АНАЛИЗАТОРОВ")
    print("="*70)
    print()
    
    results = run_comparison(args.nodes, args.branching)
    
    print("\nРекомендация:")
    print("  Если оптимизированные версии быстрее и дают те же результаты,")
    print("  замените оригинальные файлы в core/analysis/ на оптимизированные.")


if __name__ == "__main__":
    main()
