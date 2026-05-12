#!/usr/bin/env python
"""Test script to verify enhanced recommendations with actionable advice."""

from core.api import analyze_script

def test_enhanced_recommendations():
    """Test that recommendations include helpful action items."""
    
    # Test script with multiple issues
    code = '''
label start:
    $ strength = 0
    $ strength += 5
    
    menu:
        "Go to forest":
            $ strength += 10
            jump forest
        "Stay home":
            jump home

label forest:
    if strength >= 50:
        jump impossible_win
    jump end

label home:
    jump secret_loop

label secret_loop:
    jump secret_loop

label impossible_win:
    "You won!"

label end:
    "The End"
'''
    
    # Mock request
    class MockRequest:
        def __init__(self, code):
            self.code = code
    
    # Call the analysis function
    result = analyze_script(MockRequest(code))
    
    print("="*70)
    print("ENHANCED RECOMMENDATIONS TEST")
    print("="*70)
    print()
    
    # Display all recommendations
    recommendations = result["recommendations"]
    print(f"Found {len(recommendations)} recommendation(s):\n")
    
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")
        print()
    
    # Verify enhanced recommendations
    print("="*70)
    print("VERIFICATION")
    print("="*70)
    print()
    
    has_state_error_advice = False
    has_loop_advice = False
    
    for rec in recommendations:
        if "снизьте порог или добавьте больше выборов" in rec:
            has_state_error_advice = True
            print("✅ State error recommendation includes actionable advice")
            print(f"   Example: {rec[:80]}...")
            print()
        
        if "добавьте условие выхода из цикла" in rec:
            has_loop_advice = True
            print("✅ Infinite loop recommendation includes actionable advice")
            print(f"   Example: {rec}")
            print()
    
    if has_state_error_advice and has_loop_advice:
        print("🎉 SUCCESS: All recommendations include helpful action items!")
        return True
    else:
        if not has_state_error_advice:
            print("❌ FAIL: State error recommendations missing actionable advice")
        if not has_loop_advice:
            print("❌ FAIL: Infinite loop recommendations missing actionable advice")
        return False

if __name__ == '__main__':
    import sys
    success = test_enhanced_recommendations()
    sys.exit(0 if success else 1)
