"""Debug assignment parsing."""

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer

parser = RenPyParser()
tree = parser.parse_file('tests/samples/always_true.rpy')

transformer = RenPyTransformer()
script = transformer.transform(tree)

print("Labels:", list(script.labels.keys()))
print()

for label_name, label_obj in script.labels.items():
    print(f"Label: {label_name}")
    for stmt in label_obj.body:
        print(f"  {type(stmt).__name__}: {stmt}")
    print()
