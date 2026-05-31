"""Test tolerant parsing with preprocessor approach."""

from core.api import preprocess_code, analyze_script, ScriptRequest
from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.ir.model import UnknownStatement


def test_preprocess_code_basic():
    """Test that preprocess_code correctly identifies and replaces unknown lines."""
    code = """label start:
    "Hello"
    jump end
    this is unknown syntax
    $ var = 1
    
label end:
    "End"
"""
    processed, replaced = preprocess_code(code)
    
    # Check that unknown line was replaced
    assert len(replaced) == 1
    assert replaced[0]['line'] == 4
    assert replaced[0]['text'] == "this is unknown syntax"
    
    # Check that processed code has __UNKNOWN__ marker
    assert '__UNKNOWN__' in processed
    assert 'this is unknown syntax' not in processed
    
    # Check that known constructs are preserved
    assert 'label start:' in processed
    assert '"Hello"' in processed
    assert 'jump end' in processed
    assert '$ var = 1' in processed
    
    print("[OK] Basic preprocessing works!")


def test_preprocess_code_preserves_line_numbers():
    """Test that preprocessing preserves original line numbers."""
    code = """label start:
    "Hello"
    jump end
    call some_label
    return
    $ var = 1
"""
    processed, replaced = preprocess_code(code)
    
    # Should have 2 replaced lines
    assert len(replaced) == 2
    
    # Check line numbers match original
    line_texts = {r['line']: r['text'] for r in replaced}
    assert 4 in line_texts
    assert line_texts[4] == "call some_label"
    assert 5 in line_texts
    assert line_texts[5] == "return"
    
    print("[OK] Line number preservation works!")


def test_parse_with_unknown_statements():
    """Test that parser can handle code with __UNKNOWN__ markers."""
    code = """label start:
    "Hello"
    __UNKNOWN__
    jump end
    
label end:
    "End"
"""
    parser = RenPyParser()
    tree = parser.parse_text(code)
    
    transformer = RenPyTransformer()
    script = transformer.transform(tree)
    
    # Check that labels are parsed
    assert "start" in script.labels
    assert "end" in script.labels
    
    # Check that UnknownStatement is in the body
    start_label = script.labels["start"]
    unknown_stmts = [stmt for stmt in start_label.body if isinstance(stmt, UnknownStatement)]
    
    assert len(unknown_stmts) == 1
    assert unknown_stmts[0].line is not None
    
    print("[OK] Parsing with __UNKNOWN__ works!")


def test_api_warnings_for_critical_keywords():
    """Test that API generates warnings for critical keywords in unknown statements."""
    code = """label start:
    "Hello"
    call missing_label
    return
    while True:
        pass
    jump end
    
label end:
    "End"
"""
    req = ScriptRequest(code=code)
    result = analyze_script(req)
    
    # Check that analysis contains warnings
    assert "analysis" in result
    assert "warnings" in result["analysis"]
    
    warnings = result["analysis"]["warnings"]
    
    # Should have warnings for critical keywords
    assert len(warnings) >= 3  # call, return, while
    
    # Check warning structure
    for w in warnings:
        assert "label" in w
        assert "line" in w
        assert "source" in w
        assert "message" in w
        # Verify that the source contains the critical keyword
        source_lower = w["source"].lower()
        has_keyword = any(kw in source_lower for kw in ['call', 'return', 'while', 'repeat', 'python:'])
        assert has_keyword, f"Warning should contain critical keyword: {w['source']}"
        print(f"  Warning: {w['message']}")
    
    print(f"[OK] API warnings work! Found {len(warnings)} warnings.")


def test_non_critical_unknown_no_warning():
    """Test that non-critical unknown statements don't generate warnings."""
    code = """label start:
    "Hello"
    some random text
    another unknown line
    jump end
    
label end:
    "End"
"""
    req = ScriptRequest(code=code)
    result = analyze_script(req)
    
    # Should have no warnings for non-critical unknowns
    warnings = result["analysis"]["warnings"]
    assert len(warnings) == 0
    
    print("[OK] Non-critical unknowns don't generate warnings!")


def test_backward_compatibility():
    """Test that valid scripts work exactly as before."""
    code = """label start:
    "Hello"
    $ points = 0
    jump middle
    
label middle:
    "Middle"
    if points > 5:
        jump good
    jump bad
    
label good:
    "Good ending"
    
label bad:
    "Bad ending"
"""
    req = ScriptRequest(code=code)
    result = analyze_script(req)
    
    # Should have no errors
    assert "error" not in result
    
    # Should have nodes and edges
    assert len(result["nodes"]) > 0
    assert len(result["edges"]) > 0
    
    # Should have no warnings (all lines are valid)
    warnings = result["analysis"]["warnings"]
    assert len(warnings) == 0
    
    # Check that all labels are parsed
    label_ids = [n["data"]["id"] for n in result["nodes"]]
    assert "start" in label_ids
    assert "middle" in label_ids
    assert "good" in label_ids
    assert "bad" in label_ids
    
    print("[OK] Backward compatibility maintained!")


def test_dot_labels_still_work():
    """Test that dot-labels (local labels) still work with preprocessing."""
    code = """label start:
    "Hello"
    
label .sublabel:
    "Sub"
    jump start
"""
    req = ScriptRequest(code=code)
    result = analyze_script(req)
    
    # Should have no errors
    assert "error" not in result
    
    # Check that dot-label is parsed
    label_ids = [n["data"]["id"] for n in result["nodes"]]
    assert ".sublabel" in label_ids
    
    print("[OK] Dot-labels still work!")


def test_mixed_valid_and_invalid():
    """Test complex scenario with both valid and invalid statements."""
    code = """label start:
    "Welcome"
    $ score = 0
    menu:
        "Choice 1":
            jump choice1
        "Choice 2":
            jump choice2
    
label choice1:
    call special_function
    "You chose 1"
    jump end
    
label choice2:
    repeat
    "You chose 2"
    jump end
    
label end:
    "The End"
"""
    req = ScriptRequest(code=code)
    result = analyze_script(req)
    
    # Should have no parsing errors
    assert "error" not in result
    
    # Should have warnings for 'call' and 'repeat'
    warnings = result["analysis"]["warnings"]
    assert len(warnings) >= 2
    
    warning_sources = [w["source"].lower() for w in warnings]
    assert any("call" in s for s in warning_sources)
    assert any("repeat" in s for s in warning_sources)
    
    print(f"[OK] Mixed scenario works! Found {len(warnings)} warnings.")


if __name__ == "__main__":
    print("Testing tolerant parsing with preprocessor approach...\n")
    
    test_preprocess_code_basic()
    print()
    
    test_preprocess_code_preserves_line_numbers()
    print()
    
    test_parse_with_unknown_statements()
    print()
    
    test_api_warnings_for_critical_keywords()
    print()
    
    test_non_critical_unknown_no_warning()
    print()
    
    test_backward_compatibility()
    print()
    
    test_dot_labels_still_work()
    print()
    
    test_mixed_valid_and_invalid()
    print()
    
    print("\n[SUCCESS] All tests passed!")
