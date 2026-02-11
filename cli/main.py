from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer

def main():
    parser = RenPyParser()
    tree = parser.parse_file("tests/samples/simple_menu.rpy")

    print("=== PARSE TREE ===")
    print(tree.pretty())

    transformer = RenPyTransformer()
    script = transformer.transform(tree)

    print("\n=== IR MODEL ===")
    print(script)

if __name__ == "__main__":
    main()
