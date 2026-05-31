import sys
sys.path.insert(0, '.')
from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer

# Test: __UNKNOWN__ with indented block containing label
test_code = """label start:
    __UNKNOWN__
        label inner:
            "Hello"
    jump end

label end:
    return
"""

print("Testing __UNKNOWN__ with indented label inside...")
try:
    parser = RenPyParser()
    tree = parser.parse_text(test_code)
    script = RenPyTransformer().transform(tree)
    print(f"SUCCESS! Labels: {list(script.labels.keys())}")
    for name, label_obj in script.labels.items():
        print(f"  {name}: {len(label_obj.body)} statements")
        for stmt in label_obj.body:
            print(f"    - {stmt.__class__.__name__}")
except Exception as e:
    print(f"FAILED: {e}")

# Now test what fake_student actually looks like after preprocessing
# The nested labels are at the SAME indent as other statements inside start
test_code2 = """label start:
    __UNKNOWN__
    __UNKNOWN__
    "Hello"
    __UNKNOWN__
    label story_11:
        "Story 11"
        jump end

label end:
    return
"""

print("\nTesting nested labels at same indent as __UNKNOWN__...")
try:
    parser = RenPyParser()
    tree = parser.parse_text(test_code2)
    script = RenPyTransformer().transform(tree)
    print(f"SUCCESS! Labels: {list(script.labels.keys())}")
except Exception as e:
    print(f"FAILED: {e}")
