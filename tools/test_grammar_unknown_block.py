import sys
sys.path.insert(0, '.')
from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer

# Test: __UNKNOWN__ with indented block
test_code = """label start:
    __UNKNOWN__
        label inner:
            "Hello"
    jump end

label end:
    return
"""

print("Testing grammar with __UNKNOWN__ + block...")
try:
    parser = RenPyParser()
    tree = parser.parse_text(test_code)
    script = RenPyTransformer().transform(tree)
    print(f"SUCCESS! Labels: {list(script.labels.keys())}")
except Exception as e:
    print(f"FAILED: {e}")

# Test: __UNKNOWN__ without block
test_code2 = """label start:
    __UNKNOWN__
    jump end

label end:
    return
"""

print("\nTesting grammar with __UNKNOWN__ without block...")
try:
    parser = RenPyParser()
    tree = parser.parse_text(test_code2)
    script = RenPyTransformer().transform(tree)
    print(f"SUCCESS! Labels: {list(script.labels.keys())}")
except Exception as e:
    print(f"FAILED: {e}")

# Test: __UNKNOWN__ at same level as label
test_code3 = """label start:
    __UNKNOWN__
    label inner:
        "Hello"
    jump end

label end:
    return
"""

print("\nTesting grammar with __UNKNOWN__ + label at same indent...")
try:
    parser = RenPyParser()
    tree = parser.parse_text(test_code3)
    script = RenPyTransformer().transform(tree)
    print(f"SUCCESS! Labels: {list(script.labels.keys())}")
except Exception as e:
    print(f"FAILED: {e}")
