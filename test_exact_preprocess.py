"""Debug exact preprocessing output for FakeStudent lines 23-30."""

from core.api import preprocess_code

with open('tests/samples/fake_student.rpy', 'r', encoding='utf-8') as f:
    code = f.read()

processed, replacements = preprocess_code(code)

lines = processed.split('\n')

print("Lines 23-30 of PREPROCESSED code (with repr):")
for i in range(22, 30):
    line_num = i + 1
    print(f"Line {line_num}: {repr(lines[i])}")

print("\n" + "="*60)
print("\nFirst 40 lines of processed code (visible):")
for i in range(40):
    if i < len(lines):
        print(f"{i+1:3d}: {lines[i]}")
