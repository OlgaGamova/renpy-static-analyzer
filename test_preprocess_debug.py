"""Test preprocess_code with FakeStudent patterns."""

from core.api import preprocess_code

# Test cases from fake_student.rpy
test_code = """label start:
    $studik=False
    $alaska=False
    $ renpy.notify("test")
    "Hello"
    scene guk
    show gus
    menu:
        "Choice":
            jump end
    python:
        name = renpy.input("Enter")
    if studik:
        jump tutorial
    
label end:
    "End"
"""

print("Original code:")
print(test_code)
print("\n" + "="*60 + "\n")

processed, replacements = preprocess_code(test_code)

print("Processed code:")
print(processed)
print("\n" + "="*60 + "\n")

print("Replacements:")
for r in replacements:
    print(f"  Line {r['line']}: {r['text']}")

print("\n" + "="*60 + "\n")

# Verify that $ assignments are NOT replaced
lines = processed.split('\n')
for i, line in enumerate(lines, 1):
    if '__UNKNOWN__' in line:
        print(f"WARNING: Line {i} was replaced: {line}")
    elif line.strip().startswith('$'):
        print(f"OK: Line {i} preserved assignment: {line.strip()}")

print("\n" + "="*60 + "\n")
print("Verification:")
print(f"Total lines: {len(test_code.split(chr(10)))}")
print(f"Replaced lines: {len(replacements)}")
print(f"Preserved lines: {len(test_code.split(chr(10))) - len(replacements)}")
