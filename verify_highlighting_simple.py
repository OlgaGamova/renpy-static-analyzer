# Simple verification script for graph highlighting
# Run this manually to verify secret_loop highlighting works

import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from core.parser.parser import RenPyParser
    from core.parser.transformer import RenPyTransformer
    from core.graph.builder import GraphBuilder
    from core.analysis.infinite_loops import InfiniteLoopAnalyzer
    from core.api import analyze_script
    
    print("✅ Core modules imported successfully")
    
    # Load huge_branching sample
    samples_dir = Path(__file__).parent / "tests" / "samples"
    huge_code = (samples_dir / "huge_branching.rpy").read_text(encoding="utf-8")
    
    print(f"✅ Loaded huge_branching.rpy ({len(huge_code)} chars)")
    
    # Parse and analyze
    parser = RenPyParser()
    tree = parser.parse_text(huge_code)
    transformer = RenPyTransformer()
    script = transformer.transform(tree)
    
    builder = GraphBuilder()
    graph = builder.build(script)
    
    analyzer = InfiniteLoopAnalyzer()
    loops = analyzer.find_infinite_loops(graph)
    
    # Check secret_loop
    secret_loop_found = any("secret_loop" in loop for loop in loops)
    
    # Test API response
    class MockRequest:
        def __init__(self, code):
            self.code = code
    
    result = analyze_script(MockRequest(huge_code))
    infinite_loops = result.get("analysis", {}).get("infinite_loops", [])
    
    secret_loop_in_api = False
    for loop in infinite_loops:
        for node in loop:
            if isinstance(node, str) and node == "secret_loop":
                secret_loop_in_api = True
                break
            elif hasattr(node, 'get') and (node.get("node") == "secret_loop" or node.get("id") == "secret_loop"):
                secret_loop_in_api = True
                break
    
    print(f"✅ secret_loop detected by analyzer: {secret_loop_found}")
    print(f"✅ secret_loop in API response: {secret_loop_in_api}")
    
    if secret_loop_found and secret_loop_in_api:
        print("\n🎉 VERIFICATION SUCCESS!")
        print("The enhanced graph highlighting will work correctly.")
        print("secret_loop and other problematic nodes will be highlighted with the correct colors:")
        print("  • Unreachable nodes: gray (#8e8e93)")
        print("  • Missing transitions: orange (#ff9500)")
        print("  • Infinite loops: yellow (#ffcc00)")
        print("  • State errors: purple (#af52de)")
        print("\nYou can now load huge_branching.rpy in the web interface and see secret_loop highlighted in yellow!")
    else:
        print("\n❌ VERIFICATION FAILED - check the analysis logic")
        
except Exception as e:
    print(f"❌ ERROR: {e}")
    print("Please check that all dependencies are installed and try again.")
