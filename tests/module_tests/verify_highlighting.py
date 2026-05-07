import sys
import os
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.graph.builder import GraphBuilder
from core.analysis.infinite_loops import InfiniteLoopAnalyzer
from core.api import analyze_script


def verify_secret_loop_detection():
    """Verify that secret_loop is detected and properly formatted for highlighting"""
    print("=== Verifying secret_loop detection and highlighting compatibility ===\n")
    
    # Load huge_branching sample
    samples_dir = Path(__file__).parent / "samples"
    huge_code = (samples_dir / "huge_branching.rpy").read_text(encoding="utf-8")
    
    print("1. Loading huge_branching.rpy...")
    print(f"   File size: {len(huge_code)} characters")
    
    # Parse and transform
    print("2. Parsing and transforming...")
    parser = RenPyParser()
    tree = parser.parse_text(huge_code)
    transformer = RenPyTransformer()
    script = transformer.transform(tree)
    
    # Build graph
    print("3. Building graph...")
    builder = GraphBuilder()
    graph = builder.build(script)
    
    # Analyze infinite loops
    print("4. Analyzing infinite loops...")
    analyzer = InfiniteLoopAnalyzer()
    loops = analyzer.find_infinite_loops(graph)
    
    print(f"5. Found {len(loops)} infinite loop(s)")
    
    # Check for secret_loop
    secret_loop_found = False
    for i, loop in enumerate(loops):
        if "secret_loop" in loop:
            secret_loop_found = True
            print(f"   ✓ secret_loop found in loop {i+1}: {loop}")
            break
    
    if not secret_loop_found:
        print("   ✗ secret_loop NOT found in any loop")
    
    # Test API analysis response
    print("\n6. Testing API analysis response structure...")
    
    # Mock request
    class MockRequest:
        def __init__(self, code):
            self.code = code
    
    result = analyze_script(MockRequest(huge_code))
    
    # Check analysis structure
    analysis = result.get("analysis", {})
    
    infinite_loops = analysis.get("infinite_loops", [])
    print(f"   infinite_loops structure: {type(infinite_loops).__name__} with {len(infinite_loops)} loops")
    
    # Check first loop structure
    if infinite_loops:
        first_loop = infinite_loops[0]
        print(f"   First loop: {type(first_loop).__name__} with {len(first_loop)} nodes")
        
        # Check node structure
        if first_loop:
            first_node = first_loop[0]
            print(f"   First node: {type(first_node).__name__} = {first_node}")
            
            # Test frontend extraction logic
            if isinstance(first_node, str):
                node_id = first_node
            elif isinstance(first_node, dict):
                node_id = first_node.get("node") or first_node.get("id") or first_node
            else:
                node_id = first_node
            
            print(f"   Frontend nodeId extraction: '{node_id}'")
    
    # Verify secret_loop is in API response
    secret_loop_in_api = False
    for loop in infinite_loops:
        for node in loop:
            if isinstance(node, str) and node == "secret_loop":
                secret_loop_in_api = True
                break
            elif isinstance(node, dict):
                if node.get("node") == "secret_loop" or node.get("id") == "secret_loop":
                    secret_loop_in_api = True
                    break
        if secret_loop_in_api:
            break
    
    print(f"\n7. secret_loop in API response: {'✓ YES' if secret_loop_in_api else '✗ NO'}")
    
    # Test frontend compatibility
    print("\n8. Testing frontend compatibility...")
    
    # Simulate frontend logic
    def extract_node_id(item):
        if isinstance(item, str):
            return item
        elif isinstance(item, dict):
            return item.get("node") or item.get("id") or item
        else:
            return item
    
    # Test all loops
    all_nodes = []
    for loop in infinite_loops:
        for node in loop:
            node_id = extract_node_id(node)
            all_nodes.append(node_id)
    
    secret_loop_frontend = "secret_loop" in all_nodes
    print(f"   Frontend extraction finds secret_loop: {'✓ YES' if secret_loop_frontend else '✗ NO'}")
    
    # Summary
    print("\n=== VERIFICATION SUMMARY ===")
    print(f"✓ secret_loop detected by analyzer: {secret_loop_found}")
    print(f"✓ secret_loop in API response: {secret_loop_in_api}")
    print(f"✓ secret_loop compatible with frontend logic: {secret_loop_frontend}")
    
    if secret_loop_found and secret_loop_in_api and secret_loop_frontend:
        print("\n🎉 ALL VERIFICATIONS PASSED!")
        print("The enhanced frontend highlighting logic will work correctly.")
        print("secret_loop and other problematic nodes will be properly highlighted on the graph.")
        return True
    else:
        print("\n❌ VERIFICATION FAILED!")
        print("Some aspect of the highlighting logic needs attention.")
        return False

if __name__ == "__main__":
    success = verify_secret_loop_detection()
    sys.exit(0 if success else 1)
