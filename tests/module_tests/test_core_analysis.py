import pytest
import os
from pathlib import Path
from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.graph.builder import GraphBuilder
from core.analysis.reachability import ReachabilityAnalyzer
from core.analysis.dead_ends import DeadEndAnalyzer
from core.analysis.infinite_loops import InfiniteLoopAnalyzer
from core.analysis.state import StateAnalyzer


def load_sample_script(filename):
    """Load a sample script from tests/samples directory"""
    # Samples are in tests/samples, not tests/module_tests/samples
    samples_dir = Path(__file__).parent.parent / "samples"
    file_path = samples_dir / filename
    return file_path.read_text(encoding="utf-8")


def test_unreachable_nodes_detection():
    """Test detection of unreachable nodes"""
    # Load unreachable sample
    code = load_sample_script("unreachable.rpy")
    
    # Parse and transform
    parser = RenPyParser()
    tree = parser.parse_text(code)
    transformer = RenPyTransformer()
    script = transformer.transform(tree)
    
    # Build graph
    builder = GraphBuilder()
    graph = builder.build(script)
    
    # Analyze
    analyzer = ReachabilityAnalyzer()
    unreachable = analyzer.find_unreachable(graph)
    
    # Check that unreachable nodes are detected
    assert "unreachable" in unreachable


def test_infinite_loop_detection():
    """Test detection of infinite loops"""
    # Load loop sample
    code = load_sample_script("loop_story.rpy")
    
    # Parse and transform
    parser = RenPyParser()
    tree = parser.parse_text(code)
    transformer = RenPyTransformer()
    script = transformer.transform(tree)
    
    # Build graph
    builder = GraphBuilder()
    graph = builder.build(script)
    
    # Analyze
    analyzer = InfiniteLoopAnalyzer()
    loops = analyzer.find_infinite_loops(graph)
    
    # Check that infinite loops are detected
    assert len(loops) > 0
    
    # Check that secret_loop is detected in huge_branching
    huge_code = load_sample_script("huge_branching.rpy")
    huge_tree = parser.parse_text(huge_code)
    huge_script = transformer.transform(huge_tree)
    huge_graph = builder.build(huge_script)
    huge_loops = analyzer.find_infinite_loops(huge_graph)
    
    # Look for secret_loop in any loop
    secret_loop_found = False
    for loop in huge_loops:
        if "secret_loop" in loop:
            secret_loop_found = True
            break
    
    assert secret_loop_found, "secret_loop should be detected in huge_branching.rpy"


def test_state_error_detection():
    """Test detection of state errors"""
    # Load state error sample
    code = load_sample_script("state_error.rpy")
    
    # Parse and transform
    parser = RenPyParser()
    tree = parser.parse_text(code)
    transformer = RenPyTransformer()
    script = transformer.transform(tree)
    
    # Analyze
    analyzer = StateAnalyzer()
    result = analyzer.analyze(script)
    
    # Check that state errors are detected
    assert len(result["impossible_conditions"]) > 0


def test_dead_end_detection():
    """Test detection of dead ends"""
    # Load dead end sample
    code = load_sample_script("dead_end.rpy")
    
    # Parse and transform
    parser = RenPyParser()
    tree = parser.parse_text(code)
    transformer = RenPyTransformer()
    script = transformer.transform(tree)
    
    # Build graph
    builder = GraphBuilder()
    graph = builder.build(script)
    
    # Analyze
    analyzer = DeadEndAnalyzer()
    dead_ends = analyzer.find_dead_ends(graph)
    
    # Check that dead ends are detected
    assert len(dead_ends) > 0


def test_line_number_propagation():
    """Test that line numbers are properly propagated through the AST"""
    # Load a simple script with known line numbers
    code = '''
label start:
    "Hello world"
    jump end

label end:
    "Goodbye"
'''
    
    # Parse and transform
    parser = RenPyParser()
    tree = parser.parse_text(code)
    transformer = RenPyTransformer()
    script = transformer.transform(tree)
    
    # Check that labels have line numbers
    assert "start" in script.labels
    # Line numbers start from the actual line in the string (line 2 since line 1 is empty)
    assert script.labels["start"].line == 2
    
    assert "end" in script.labels
    assert script.labels["end"].line == 6


def test_api_endpoint_integration():
    """Test the FastAPI endpoint integration"""
    # This would require running the FastAPI server, so we'll test the underlying logic
    # instead of the actual HTTP endpoint
    from core.api import analyze_script
    
    # Test with a simple script
    code = '''
label start:
    "Hello"
    jump end

label end:
    "Goodbye"
'''
    
    # Mock request
    class MockRequest:
        def __init__(self, code):
            self.code = code
    
    # Call the analysis function
    result = analyze_script(MockRequest(code))
    
    # Check that result has expected structure
    assert "nodes" in result
    assert "edges" in result
    assert "analysis" in result
    assert "recommendations" in result

if __name__ == "__main__":
    pytest.main(["-v", __file__])
