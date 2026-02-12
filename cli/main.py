import sys
from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.graph.builder import GraphBuilder
from core.graph.visualizer import GraphVisualizer


def analyze_file(file_path: str):
    print("\n" + "=" * 50)
    print(f"Analyzing: {file_path}")
    print("=" * 50)

    parser = RenPyParser()
    tree = parser.parse_file(file_path)

    print("\n=== PARSE TREE ===")
    print(tree.pretty())

    transformer = RenPyTransformer()
    script = transformer.transform(tree)

    print("\n=== IR MODEL ===")
    print(script)

    builder = GraphBuilder()
    graph = builder.build(script)

    visualizer = GraphVisualizer()
    visualizer.render(graph, output_file=f"{file_path.split('/')[-1]}.html")

    print("\n=== GRAPH ===")
    for src, targets in graph.items():
        for tgt in targets:
            print(f"{src} -> {tgt}")


def main():

    if len(sys.argv) > 1:
        analyze_file(sys.argv[1])
    else:
        demo_files = [
            "tests/samples/branching_complex.rpy",
            "tests/samples/loop_story.rpy",
            "tests/samples/nonlinear_story.rpy"
        ]

        for file_path in demo_files:
            analyze_file(file_path)


if __name__ == "__main__":
    main()
