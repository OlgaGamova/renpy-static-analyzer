import pytest
from core.api import analyze_script


def test_infinite_loops_data_structure():
    """Test that infinite loops data structure matches frontend expectations"""
    # Test with loop script that should have infinite loops
    code = '''
label start:
    "Hello"
    jump loop

label loop:
    "Looping"
    jump loop
'''
    
    # Mock request
    class MockRequest:
        def __init__(self, code):
            self.code = code
    
    # Call the analysis function
    result = analyze_script(MockRequest(code))
    
    # Check infinite loops structure
    infinite_loops = result["analysis"]["infinite_loops"]
    
    # Should be list of lists (each loop is a list of nodes)
    assert isinstance(infinite_loops, list)
    
    # Each loop should be a list
    for loop in infinite_loops:
        assert isinstance(loop, list)
        
        # Each node in loop should be string or dict with 'node' key
        for node in loop:
            if isinstance(node, dict):
                assert "node" in node or "id" in node
            else:
                assert isinstance(node, str)


def test_unreachable_nodes_data_structure():
    """Test that unreachable nodes data structure matches frontend expectations"""
    # Test with unreachable script
    code = '''
label start:
    "Hello"
    jump end

label unreachable_label:
    "This is unreachable"

label end:
    "Goodbye"
'''
    
    # Mock request
    class MockRequest:
        def __init__(self, code):
            self.code = code
    
    # Call the analysis function
    result = analyze_script(MockRequest(code))
    
    # Check unreachable nodes structure
    unreachable = result["analysis"]["unreachable"]
    
    # Should be list of items
    assert isinstance(unreachable, list)
    
    # Each item should be string or dict with 'node' key
    for item in unreachable:
        if isinstance(item, dict):
            assert "node" in item or "id" in item
        else:
            assert isinstance(item, str)


def test_missing_nodes_data_structure():
    """Test that missing nodes data structure matches frontend expectations"""
    # Test with script that has missing jumps
    code = '''
label start:
    "Hello"
    jump missing_label
'''
    
    # Mock request
    class MockRequest:
        def __init__(self, code):
            self.code = code
    
    # Call the analysis function
    result = analyze_script(MockRequest(code))
    
    # Check missing nodes structure
    missing = result["analysis"]["missing"]
    
    # Should be list of strings
    assert isinstance(missing, list)
    for node in missing:
        assert isinstance(node, str)


def test_state_errors_data_structure():
    """Test that state errors data structure matches frontend expectations"""
    # Test with a script that has state errors
    code = '''
label start:
    $ strength = 0
    $ strength += 5
    
    if strength >= 50:
        jump impossible_win
    
    jump end

label impossible_win:
    "This should never happen"

label end:
    "The End"
'''
    
    # Mock request
    class MockRequest:
        def __init__(self, code):
            self.code = code
    
    # Call the analysis function
    result = analyze_script(MockRequest(code))
    
    # Check state errors structure
    state_errors = result["analysis"]["state"]["impossible_conditions"]
    
    # Should be list of dicts with required keys
    assert isinstance(state_errors, list)
    
    for error in state_errors:
        assert isinstance(error, dict)
        assert "label" in error
        assert "var" in error
        assert "required" in error
        assert "range" in error
        assert "path" in error


def test_huge_branching_secret_loop_detection():
    """Test that huge_branching.rpy correctly detects secret_loop"""
    from pathlib import Path
    
    # Load huge_branching sample
    samples_dir = Path(__file__).parent.parent / "samples"
    huge_code = (samples_dir / "huge_branching.rpy").read_text(encoding="utf-8")
    
    # Mock request
    class MockRequest:
        def __init__(self, code):
            self.code = code
    
    # Call the analysis function
    result = analyze_script(MockRequest(huge_code))
    
    # Check that secret_loop is in infinite loops
    infinite_loops = result["analysis"]["infinite_loops"]
    secret_loop_found = False
    
    for loop in infinite_loops:
        for node in loop:
            if isinstance(node, dict):
                if node.get("node") == "secret_loop" or node.get("id") == "secret_loop":
                    secret_loop_found = True
                    break
            elif isinstance(node, str) and node == "secret_loop":
                secret_loop_found = True
                break
        if secret_loop_found:
            break
    
    assert secret_loop_found, "secret_loop should be detected in huge_branching.rpy"

if __name__ == "__main__":
    pytest.main(["-v", __file__])
