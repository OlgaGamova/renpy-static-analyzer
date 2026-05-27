#!/usr/bin/env python
"""Unit tests for StateAnalyzer: always-true conditions (E07) and flag contradictions (E08)."""

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.analysis.state import StateAnalyzer


def test_always_true_condition():
    parser = RenPyParser()
    tree = parser.parse_file('tests/samples/always_true.rpy')
    transformer = RenPyTransformer()
    script = transformer.transform(tree)

    analyzer = StateAnalyzer()
    results = analyzer.analyze(script)

    assert 'always_true_conditions' in results
    atcs = results['always_true_conditions']
    assert any(c['label'] == 'start' and c['var'] == 'points' for c in atcs), (
        f"Expected an always-true condition on 'points' in 'start', got: {atcs}"
    )


def test_flag_contradiction_and_impossible():
    parser = RenPyParser()
    tree = parser.parse_file('tests/samples/flag_conflict.rpy')
    transformer = RenPyTransformer()
    script = transformer.transform(tree)

    analyzer = StateAnalyzer()
    results = analyzer.analyze(script)

    # flag contradictions should be reported for label 'merge' and variable 'flag'
    fcs = results.get('flag_contradictions', [])
    assert any(fc['label'] == 'merge' and fc['var'] == 'flag' for fc in fcs), (
        f"Expected flag contradiction at 'merge' for 'flag', got: {fcs}"
    )

    # Also, on the path where flag==False the condition `if flag` is impossible
    imps = results.get('impossible_conditions', [])
    assert any(imp.get('label') == 'merge' and imp.get('type') == 'flag' for imp in imps), (
        f"Expected impossible flag condition at 'merge', got: {imps}"
    )


if __name__ == '__main__':
    test_always_true_condition()
    test_flag_contradiction_and_impossible()
    print('OK')

