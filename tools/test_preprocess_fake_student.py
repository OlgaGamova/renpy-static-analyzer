"""Debug preprocessed FakeStudent."""

from core.api import preprocess_code

with open('tests/samples/fake_student.rpy', 'r', encoding='utf-8') as f:
    code = f.read()

processed, replacements = preprocess_code(code)

# Show lines 20-30
lines = processed.split('\n')
print("Lines 20-35 of processed code:")
for i in range(19, min(35, len(lines))):
    line_num = i + 1
    marker = ">>> " if line_num == 25 else "    "
    print(f"{marker}Line {line_num}: {repr(lines[i])}")

print(f"\nTotal lines: {len(lines)}")
print(f"Replacements: {len(replacements)}")

# Check if there are any issues with comments
print("\nChecking for problematic patterns:")
for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if stripped.startswith('#') and line != line.lstrip():
        print(f"  Line {i}: Indented comment: {repr(line)}")
