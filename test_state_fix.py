#!/usr/bin/env python
"""Test script to verify state analyzer detects all impossible conditions."""

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.analysis.state import StateAnalyzer

def test_huge_branching():
    print("=" * 60)
    print("Testing State Analyzer on huge_branching.rpy")
    print("=" * 60)
    
    # Parse the file
    parser = RenPyParser()
    tree = parser.parse_file('tests/samples/huge_branching.rpy')
    
    # Transform to IR
    transformer = RenPyTransformer()
    script = transformer.transform(tree)
    
    # Run state analysis
    analyzer = StateAnalyzer()
    results = analyzer.analyze(script)
    
    # Display results
    print(f"\nFound {len(results['impossible_conditions'])} impossible condition(s):\n")
    
    for i, cond in enumerate(results['impossible_conditions'], 1):
        print(f"Error #{i}:")
        print(f"  Label: {cond['label']}")
        print(f"  Variable: {cond['var']}")
        print(f"  Required: {cond['var']} {cond['required']}")
        print(f"  Current Range: [{cond['range'][0]}, {cond['range'][1]}]")
        print(f"  Path: {' → '.join(cond['path'])}")
        if cond.get('line'):
            print(f"  Line: {cond['line']}")
        print()
    
    # Display undefined labels
    if results.get('undefined_labels'):
        print(f"Found {len(results['undefined_labels'])} undefined label(s):\n")
        for i, undef in enumerate(results['undefined_labels'], 1):
            print(f"Undefined Label #{i}:")
            print(f"  Label: {undef['label']}")
            print(f"  Referenced from path: {' → '.join(undef['path'])}")
            print()
    
    # Verify expected errors
    expected_errors = [
        {'label': 'training', 'var': 'strength'},
        {'label': 'reading', 'var': 'intelligence'},
    ]
    
    found_labels = {cond['label'] for cond in results['impossible_conditions']}
    expected_labels = {err['label'] for err in expected_errors}
    
    if found_labels == expected_labels:
        print("✓ SUCCESS: All expected errors were detected!")
        return True
    else:
        missing = expected_labels - found_labels
        extra = found_labels - expected_labels
        if missing:
            print(f"✗ FAIL: Missing errors for labels: {missing}")
        if extra:
            print(f"✗ FAIL: Unexpected errors for labels: {extra}")
        return False

if __name__ == '__main__':
    success = test_huge_branching()
    exit(0 if success else 1)
