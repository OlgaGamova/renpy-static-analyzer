"""Test full pipeline with FakeStudent."""

from core.api import analyze_script, ScriptRequest

# Read the fake_student.rpy file
with open('tests/samples/fake_student.rpy', 'r', encoding='utf-8') as f:
    code = f.read()

print(f"Testing with FakeStudent ({len(code.split(chr(10)))} lines)...")
print("="*60)

req = ScriptRequest(code=code)
result = analyze_script(req)

if 'error' in result:
    print(f"\n[ERROR] ERROR: {result['error']}")
    import traceback
    print("\nFull traceback would appear here")
else:
    print(f"\n[OK] No parsing errors!")
    print(f"[OK] Nodes: {len(result['nodes'])}")
    print(f"[OK] Edges: {len(result['edges'])}")
    
    warnings = result.get('analysis', {}).get('warnings', [])
    print(f"\n[WARNINGS] Warnings: {len(warnings)}")
    
    for w in warnings[:5]:  # Show first 5 warnings
        print(f"  Line {w['line']}: {w['message']}")
    
    if len(warnings) > 5:
        print(f"  ... and {len(warnings) - 5} more warnings")

print("\n" + "="*60)
print("Test complete!")
