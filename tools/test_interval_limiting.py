"""Test interval limiting in StateAnalyzer"""
import sys
sys.path.insert(0, '.')

from core.ir.model import Script, Label, Assignment, Condition
from core.analysis.state import StateAnalyzer, MAX_INTERVAL

def test_interval_limiting():
    """Test that intervals are properly limited to MAX_INTERVAL"""
    
    # Create a script with a loop that increments a variable many times
    script = Script()
    script.labels['start'] = Label(name='start', body=[
        Assignment(var='counter', op='=', value=0),
        # Simulate multiple increments (would normally cause state explosion)
        Assignment(var='counter', op='+=', value=1),
        Assignment(var='counter', op='+=', value=1),
        Assignment(var='counter', op='+=', value=1),
    ])
    
    analyzer = StateAnalyzer()
    results = analyzer.analyze(script)
    
    # Check that no interval limit warnings occurred (values are small)
    assert len(results['interval_limit_warnings']) == 0, \
        f"Expected no warnings for small values, got {len(results['interval_limit_warnings'])}"
    
    print("✓ Test 1 passed: No warnings for small values")
    
    # Create a script that would exceed MAX_INTERVAL
    script2 = Script()
    assignments = [Assignment(var='counter', op='=', value=0)]
    # Add enough += operations to exceed MAX_INTERVAL
    for i in range(MAX_INTERVAL + 100):
        assignments.append(Assignment(var='counter', op='+=', value=1))
    
    script2.labels['start'] = Label(name='start', body=assignments)
    
    results2 = analyzer.analyze(script2)
    
    # Check that interval limit warnings were generated
    assert len(results2['interval_limit_warnings']) > 0, \
        "Expected interval limit warnings for large values"
    
    # Verify the warning contains correct information
    warning = results2['interval_limit_warnings'][0]
    assert warning['var'] == 'counter'
    assert warning['operation'] == '+='
    assert warning['limited_range'][1] == MAX_INTERVAL
    assert warning['max_interval'] == MAX_INTERVAL
    
    print(f"✓ Test 2 passed: Generated {len(results2['interval_limit_warnings'])} warning(s)")
    print(f"  - Variable: {warning['var']}")
    print(f"  - Original range: {warning['original_range']}")
    print(f"  - Limited range: {warning['limited_range']}")
    
    # Test negative interval limiting with -=
    script3 = Script()
    assignments3 = [Assignment(var='counter', op='=', value=0)]
    for i in range(MAX_INTERVAL + 100):
        assignments3.append(Assignment(var='counter', op='-=', value=1))
    
    script3.labels['start'] = Label(name='start', body=assignments3)
    
    results3 = analyzer.analyze(script3)
    
    # Check that interval limit warnings were generated for negative values
    assert len(results3['interval_limit_warnings']) > 0, \
        "Expected interval limit warnings for large negative values"
    
    warning3 = results3['interval_limit_warnings'][0]
    assert warning3['var'] == 'counter'
    assert warning3['operation'] == '-='
    assert warning3['limited_range'][0] == -MAX_INTERVAL
    
    print(f"✓ Test 3 passed: Generated warning for negative values")
    print(f"  - Limited range: {warning3['limited_range']}")
    
    print("\n✅ All tests passed!")
    print(f"   MAX_INTERVAL = {MAX_INTERVAL}")
    print(f"   Total warnings in test 2: {len(results2['interval_limit_warnings'])}")
    print(f"   Total warnings in test 3: {len(results3['interval_limit_warnings'])}")

if __name__ == '__main__':
    test_interval_limiting()
