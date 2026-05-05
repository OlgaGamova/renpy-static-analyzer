import pytest
from core.api import analyze_script


def test_frontend_infinite_loops_compatibility():
    """Test that infinite loops data structure is compatible with enhanced frontend logic"""
    # Test with loop script
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
    
    # Check that infinite loops structure matches frontend expectations
    # The enhanced frontend logic expects:
    # - infinite_loops to be an array of arrays
    # - Each inner array contains items that are either strings or objects with 'node' property
    # - The frontend should be able to extract nodeId from item.node or item.id or item itself
    
    infinite_loops = result["analysis"]["infinite_loops"]
    assert isinstance(infinite_loops, list)
    
    # Test the enhanced frontend logic extraction
    for loop in infinite_loops:
        assert isinstance(loop, list)
        for item in loop:
            # Frontend logic: const nodeId = typeof item === 'string' ? item : (item.node || item.id || item);
            if isinstance(item, str):
                node_id = item
            elif isinstance(item, dict):
                node_id = item.get("node") or item.get("id") or item
            else:
                node_id = item
            
            # Should be a string
            assert isinstance(node_id, str) or node_id is None


def test_frontend_unreachable_nodes_compatibility():
    """Test that unreachable nodes data structure is compatible with enhanced frontend logic"""
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
    assert isinstance(unreachable, list)
    
    # Test the enhanced frontend logic extraction
    for item in unreachable:
        # Frontend logic: const nodeId = typeof item === 'string' ? item : (item.node || item.id || item);
        if isinstance(item, str):
            node_id = item
        elif isinstance(item, dict):
            node_id = item.get("node") or item.get("id") or item
        else:
            node_id = item
        
        # Should be a string
        assert isinstance(node_id, str) or node_id is None


def test_frontend_missing_nodes_compatibility():
    """Test that missing nodes data structure is compatible with enhanced frontend logic"""
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
    assert isinstance(missing, list)
    
    # All missing nodes should be strings (frontend expects direct string IDs)
    for node in missing:
        assert isinstance(node, str)


def test_huge_branching_secret_loop_frontend_compatibility():
    """Test that huge_branching.rpy secret_loop is compatible with enhanced frontend logic"""
    from pathlib import Path
    
    # Load huge_branching sample
    samples_dir = Path(__file__).parent / "samples"
    huge_code = (samples_dir / "huge_branching.rpy").read_text(encoding="utf-8")
    
    # Mock request
    class MockRequest:
        def __init__(self, code):
            self.code = code
    
    # Call the analysis function
    result = analyze_script(MockRequest(huge_code))
    
    # Check that secret_loop is properly formatted for frontend
    infinite_loops = result["analysis"]["infinite_loops"]
    
    secret_loop_found = False
    for loop in infinite_loops:
        for item in loop:
            if isinstance(item, str) and item == "secret_loop":
                secret_loop_found = True
                break
            elif isinstance(item, dict):
                if item.get("node") == "secret_loop" or item.get("id") == "secret_loop":
                    secret_loop_found = True
                    break
        if secret_loop_found:
            break
    
    assert secret_loop_found, "secret_loop should be found in infinite_loops structure"
    
    # Test that the frontend logic would extract it correctly
    # const nodeId = typeof item === 'string' ? item : (item.node || item.id || item);
    # This should work for all possible formats
    
    # Also test that the enhanced fallback logic would work
    # The frontend now has: if (!node) { cy.add({ ... }); }
    # So even if secret_loop isn't in the initial graph, it will be added dynamically

if __name__ == "__main__":
    pytest.main(["-v", __file__])
