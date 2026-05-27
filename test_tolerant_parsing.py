"""Test tolerant parsing with unknown statements and dot-labels."""

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.ir.model import UnknownStatement


def test_unknown_statement():
    """Test that unknown statements are parsed without errors."""
    code = """
label start:
    "Hello"
    jump end
    
    this is unknown syntax
    $ var = 1
    
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
    
    # Check that unknown statement is in the body
    start_label = script.labels["start"]
    unknown_stmts = [stmt for stmt in start_label.body if isinstance(stmt, UnknownStatement)]
    
    assert len(unknown_stmts) == 1
    assert "this is unknown syntax" in unknown_stmts[0].source
    assert unknown_stmts[0].line is not None
    
    print("✓ Unknown statement parsing works!")


def test_dot_label():
    """Test that dot-labels (local labels) are parsed correctly."""
    code = """
label start:
    "Hello"
    
label .sublabel:
    "Sub"
    jump start
"""
    parser = RenPyParser()
    tree = parser.parse_text(code)
    
    transformer = RenPyTransformer()
    script = transformer.transform(tree)
    
    # Check that dot-label is parsed
    assert ".sublabel" in script.labels
    
    sublabel = script.labels[".sublabel"]
    assert sublabel.name == ".sublabel"
    
    print("✓ Dot-label parsing works!")


def test_api_warnings():
    """Test that critical unknown statements generate warnings in API."""
    from core.api import analyze_script
    from core.api import ScriptRequest
    
    code = """
label start:
    "Hello"
    call missing_label
    return
    jump end
    
label end:
    "End"
"""
    # This should not raise an error
    req = ScriptRequest(code=code)
    result = analyze_script(req)
    
    # Check that warnings are in the analysis
    assert "analysis" in result
    assert "warnings" in result["analysis"]
    
    # Check that we got warnings for call and return
    warnings = result["analysis"]["warnings"]
    assert len(warnings) > 0
    
    # Check warning structure
    for w in warnings:
        assert "label" in w
        assert "line" in w
        assert "source" in w
        assert "message" in w
        print(f"  Warning: {w['message']}")
    
    print(f"✓ API warnings work! Found {len(warnings)} warnings.")


if __name__ == "__main__":
    print("Testing tolerant parsing improvements...\n")
    
    test_unknown_statement()
    print()
    
    test_dot_label()
    print()
    
    test_api_warnings()
    print()
    
    print("\n✓ All tests passed!")
