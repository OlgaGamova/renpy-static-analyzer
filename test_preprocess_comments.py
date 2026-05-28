#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test to verify preprocess_code with comment-based replacement
"""

import sys
sys.path.insert(0, '.')

from core.api import preprocess_code
from core.parser.parser import RenPyParser

def test_fake_student():
    """Test preprocessing and parsing fake_student.rpy"""
    
    print("=" * 80)
    print("TEST: preprocess_code with comment-based replacement")
    print("=" * 80)
    
    # Load fake_student.rpy
    with open('tests/samples/fake_student.rpy', encoding='utf-8-sig') as f:
        code = f.read()
    
    print(f"\nOriginal code: {len(code.split(chr(10)))} lines")
    
    # Preprocess
    processed_code, replaced_info = preprocess_code(code)
    
    print(f"Processed code: {len(processed_code.split(chr(10)))} lines")
    print(f"Replaced constructs: {len(replaced_info)}")
    
    # Show some examples of replacements
    print("\n" + "=" * 80)
    print("Examples of replaced constructs:")
    print("=" * 80)
    
    for i, info in enumerate(replaced_info[:10]):
        print(f"  {i+1}. Line {info['line']}: {info['text'][:60]}")
    
    if len(replaced_info) > 10:
        print(f"  ... and {len(replaced_info) - 10} more")
    
    # Show a snippet of processed code
    print("\n" + "=" * 80)
    print("Processed code snippet (lines 35-45):")
    print("=" * 80)
    
    lines = processed_code.split('\n')
    for i in range(34, min(45, len(lines))):
        line_num = i + 1
        line = lines[i]
        if '# UNSUPPORTED:' in line:
            print(f"  {line_num:3d}: {line}  <-- COMMENTED")
        elif line.strip() == '':
            print(f"  {line_num:3d}: (empty)")
        else:
            print(f"  {line_num:3d}: {line}")
    
    # Try to parse
    print("\n" + "=" * 80)
    print("Parsing processed code...")
    print("=" * 80)
    
    try:
        parser = RenPyParser()
        tree = parser.parse_text(processed_code)
        
        print("✓ SUCCESS: Code parsed without errors!")
        
        # Count labels
        from core.parser.transformer import RenPyTransformer
        transformer = RenPyTransformer()
        script = transformer.transform(tree)
        
        print(f"✓ Found {len(script.labels)} labels:")
        for label_name in list(script.labels.keys())[:10]:
            print(f"  - {label_name}")
        
        if len(script.labels) > 10:
            print(f"  ... and {len(script.labels) - 10} more")
        
        return True
        
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_simple():
    """Test simple preprocessing"""
    
    print("\n" + "=" * 80)
    print("TEST: Simple preprocessing")
    print("=" * 80)
    
    code = """label start:
    scene bg room
    show character
    "Hello"
    if condition:
        jump yes
    else:
        jump no

label yes:
    return

label no:
    return
"""
    
    processed, replaced = preprocess_code(code)
    
    print("\nOriginal code:")
    for i, line in enumerate(code.split('\n'), 1):
        print(f"  {i:3d}: {line}")
    
    print("\nProcessed code:")
    for i, line in enumerate(processed.split('\n'), 1):
        if '# UNSUPPORTED:' in line:
            print(f"  {i:3d}: {line}  <-- COMMENTED")
        else:
            print(f"  {i:3d}: {line}")
    
    print(f"\nReplaced {len(replaced)} constructs")
    
    # Verify it can be parsed
    try:
        parser = RenPyParser()
        tree = parser.parse_text(processed)
        print("✓ Parsed successfully")
        return True
    except Exception as e:
        print(f"✗ Parse failed: {e}")
        return False

if __name__ == '__main__':
    test1 = test_simple()
    test2 = test_fake_student()
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Simple test: {'✓ PASS' if test1 else '✗ FAIL'}")
    print(f"Fake student test: {'✓ PASS' if test2 else '✗ FAIL'}")
    
    if test1 and test2:
        print("\n✓ All tests passed!")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed")
        sys.exit(1)
