from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.graph.builder import GraphBuilder


def main():
    parser = RenPyParser()
    tree = parser.parse_file("tests/samples/simple_menu.rpy")

    print("=== PARSE TREE ===")
    print(tree.pretty())

    transformer = RenPyTransformer()
    script = transformer.transform(tree)

    print("\n=== IR MODEL ===")
    print(script)

    builder = GraphBuilder()
    graph = builder.build(script)

    print("\n=== GRAPH ===")
    for src, targets in graph.items():
        for tgt in targets:
            print(f"{src} -> {tgt}")

if __name__ == "__main__":
    main()
