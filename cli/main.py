import sys
import os

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer

from core.graph.builder import GraphBuilder
from core.graph.visualizer import GraphVisualizer

from core.analysis.reachability import ReachabilityAnalyzer
from core.analysis.dead_ends import DeadEndAnalyzer
from core.analysis.infinite_loops import InfiniteLoopAnalyzer
from core.analysis.state import StateAnalyzer

# ВНИМАНИЕ: Данный скрипт является устаревшим и не используется в основном сервисе.
# Основная функциональность перенесена в веб-интерфейс (FastAPI + frontend).
# Оставлен только для возможного локального тестирования или отладки.

def analyze_file(file_path: str):
    print("\n" + "=" * 50)
    print(f"Analyzing: {file_path}")
    print("=" * 50)

    # -------------------------
    # ПАРСИНГ
    # -------------------------
    parser = RenPyParser()
    tree = parser.parse_file(file_path)

    print("\n=== PARSE TREE ===")
    print(tree.pretty())

    # -------------------------
    # ТРАНСФОРМАЦИЯ → IR
    # -------------------------
    transformer = RenPyTransformer()
    script = transformer.transform(tree)

    print("\n=== IR MODEL ===")
    print(script)

    # КРИТИЧЕСКИЙ ОТЛАДЧИК (показывает реальные ноды)
    print("\n=== DEBUG IR ===")
    for label in script.labels.values():
        print(f"\nLabel: {label.name}")
        for node in label.body:
            print("  ", type(node).__name__, node)

    # -------------------------
    # ГРАФ
    # -------------------------
    builder = GraphBuilder()
    graph = builder.build(script)

    print("\n=== GRAPH ===")
    for src, targets in graph.items():
        for tgt in targets:
            print(f"{src} -> {tgt}")

    # -------------------------
    # АНАЛИЗ
    # -------------------------
    print("\n=== ANALYSIS ===")

    reach = ReachabilityAnalyzer()
    dead = DeadEndAnalyzer()
    loops = InfiniteLoopAnalyzer()
    state = StateAnalyzer()

    unreachable = reach.find_unreachable(graph)
    dead_ends = dead.find_dead_ends(graph)
    infinite_loops = loops.find_infinite_loops(graph)
    state_result = state.analyze(script)

    print(f"\nUnreachable nodes: {unreachable}")
    print(f"Dead ends: {dead_ends}")
    print(f"Infinite loops: {infinite_loops}")

    print("\nState analysis:")
    if not state_result["impossible_conditions"]:
        print("  Нет ошибок состояний")
    else:
        for err in state_result["impossible_conditions"]:
            print(
                f"  {err['label']}: {err['var']} >= {err['required']}, "
                f"диапазон {err['range']}"
            )

    # -------------------------
    # ВИЗУАЛИЗАЦИЯ
    # -------------------------
    visualizer = GraphVisualizer()
    visualizer.render(graph, output_file=f"{file_path.split('/')[-1]}.html")


def main():
    if len(sys.argv) > 1:
        analyze_file(sys.argv[1])
    else:
        demo_files = [
            os.path.join(os.path.dirname(__file__), "..", "tests", "samples", "state_error.rpy")
        ]

        for file_path in demo_files:
            analyze_file(file_path)


if __name__ == "__main__":
    main()