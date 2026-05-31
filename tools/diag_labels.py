import sys
sys.path.insert(0, '.')
from core.api import preprocess_code
from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer

code = open('tests/samples/fake_student.rpy', encoding='utf-8-sig').read()
p, r = preprocess_code(code)

# Save preprocessed output
with open('test_preprocessed.rpy', 'w', encoding='utf-8') as f:
    f.write(p)

# Parse
tree = RenPyParser().parse_text(p)
script = RenPyTransformer().transform(tree)

print('Labels found:', list(script.labels.keys()))
print('Count:', len(script.labels))
print('Original lines:', len(code.split('\n')))
print('Processed lines:', len(p.split('\n')))
print('Lines LOST:', len(code.split('\n')) - len(p.split('\n')))
