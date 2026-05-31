#!/usr/bin/env python
"""
Quick test to verify the generator creates valid RenPy syntax.
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from tests.generate_performance_scenarios import RenPyScenarioGenerator
from core.parser.parser import RenPyParser

def test_generation():
    """Test that generated scenarios can be parsed."""
    
    print("Testing scenario generation...")
    print("="*70)
    
    # Create generator
    generator = RenPyScenarioGenerator(seed=42)
    
    # Generate a small scenario
    print("\n[1/3] Generating small scenario (50 nodes)...")
    try:
        script = generator.generate_scenario(
            num_nodes=50,
            branching_factor=2,
            max_depth=5,
            output_path="test_output.rpy"
        )
        print(f"✓ Generated {len(script)} bytes")
    except Exception as e:
        print(f"✗ Generation failed: {e}")
        return False
    
    # Try to parse it
    print("\n[2/3] Parsing generated scenario...")
    try:
        parser = RenPyParser()
        tree = parser.parse_text(script)
        print(f"✓ Parsing successful")
    except Exception as e:
        print(f"✗ Parsing failed: {e}")
        print("\nGenerated script (first 100 lines):")
        print("-"*70)
        for i, line in enumerate(script.split('\n')[:100], 1):
            print(f"{i:3d}: {line}")
        print("-"*70)
        return False
    
    # Generate another type
    print("\n[3/3] Generating deep tree scenario...")
    try:
        script2 = generator.generate_deep_tree_scenario(
            depth=10,
            branching=2,
            output_path="test_output_tree.rpy"
        )
        tree2 = parser.parse_text(script2)
        print(f"✓ Deep tree generated and parsed successfully")
    except Exception as e:
        print(f"✗ Deep tree generation failed: {e}")
        return False
    
    print("\n" + "="*70)
    print("All tests passed! ✓")
    return True

if __name__ == "__main__":
    success = test_generation()
    sys.exit(0 if success else 1)
