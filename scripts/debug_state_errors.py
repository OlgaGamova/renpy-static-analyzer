#!/usr/bin/env python
"""Debug script to check state analysis results"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.analysis.state import StateAnalyzer

# Read the test file
with open("tests/samples/performance/perf_xlarge_5000.rpy", "r", encoding="utf-8") as f:
    code = f.read()

print("Parsing file...")
parser = RenPyParser()
tree = parser.parse_text(code)

print("Transforming...")
transformer = RenPyTransformer()
script = transformer.transform(tree)

print(f"Total labels: {len(script.labels)}")
print("Running state analyzer...")

analyzer = StateAnalyzer()
results = analyzer.analyze(script)

print(f"\nFound {len(results['impossible_conditions'])} impossible conditions:")
for i, err in enumerate(results['impossible_conditions'][:20], 1):  # Show first 20
    print(f"{i}. Label: {err['label']}, Var: {err['var']}, Required: {err['required']}, Range: {err['range']}, Path: {' → '.join(err['path'][:5])}")

if len(results['impossible_conditions']) > 20:
    print(f"... and {len(results['impossible_conditions']) - 20} more errors")

print(f"\nUndefined labels: {len(results['undefined_labels'])}")
