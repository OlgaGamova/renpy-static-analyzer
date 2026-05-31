# Tolerant Parsing Implementation Summary

## Overview
Successfully implemented tolerant parsing for Ren'Py static analyzer using a preprocessor approach that allows the parser to handle unknown statements without crashing.

## Changes Made

### 1. Grammar (core/parser/grammar.py)
**Added support for unknown_statement rule:**
```python
?statement: label
          | jump
          | menu
          | say
          | assignment
          | condition
          | unknown_statement  # NEW

UNKNOWN_TOKEN: "__UNKNOWN__"  # NEW
unknown_statement: UNKNOWN_TOKEN _NEWLINE?  # NEW
```

**Also added dot-label support:**
```python
label: "label" ("."?) NAME ":" _NEWLINE INDENT statement+ DEDENT
```

### 2. API (core/api.py)

**Added preprocess_code function:**
- Scans code line-by-line
- Identifies supported constructs: `label`, `jump`, `menu`, `if`, `$`, `"` (strings), `#` (comments)
- Replaces unknown lines with `__UNKNOWN__` marker
- Preserves original line numbers and indentation
- Returns tuple: `(processed_code, replaced_lines_info)`

**Integrated preprocessing in analyze_script:**
```python
# Step 1: Preprocess code
processed_code, replaced_lines_info = preprocess_code(req.code)
original_texts = {info['line']: info['text'] for info in replaced_lines_info}

# Step 2: Parse processed code
tree = parser.parse_text(processed_code)

# Step 3: Collect warnings from UnknownStatement
for stmt in label_obj.body:
    if isinstance(stmt, UnknownStatement):
        original_text = original_texts.get(stmt.line, stmt.source)
        # Check for critical keywords and generate warnings
```

**Warning classification:**
- Critical keywords: `call`, `return`, `while`, `repeat`, `python:`
- Generates warnings only for critical unknown statements
- Warning structure includes: `label`, `line`, `column`, `source`, `message`

### 3. Transformer (core/parser/transformer.py)

**Updated unknown_statement handler:**
```python
def unknown_statement(self, items):
    line = None
    column = None
    
    if items and len(items) > 0:
        token = items[0]
        line = getattr(token, 'line', None)
        column = getattr(token, 'column', None)
    
    return UnknownStatement(source="__UNKNOWN__", line=line, column=column)

def UNKNOWN_TOKEN(self, token):
    return token
```

### 4. IR Model (core/ir/model.py)
**Already had UnknownStatement class from previous work:**
```python
@dataclass
class UnknownStatement(Statement):
    source: str
    line: Optional[int] = None
    column: Optional[int] = None
    error_message: str = ""
```

## How It Works

1. **Preprocessing Phase:**
   - Input: Raw Ren'Py code with potential unknown statements
   - Process: Line-by-line scanning and replacement
   - Output: Cleaned code with `__UNKNOWN__` markers + metadata about replaced lines

2. **Parsing Phase:**
   - Input: Preprocessed code
   - Process: Standard Lark parsing with unknown_statement rule
   - Output: IR with UnknownStatement nodes

3. **Warning Generation Phase:**
   - Input: IR with UnknownStatement nodes + original text metadata
   - Process: Match UnknownStatement line numbers to original texts, check for critical keywords
   - Output: Warnings list in API response

## Example

**Input:**
```renpy
label start:
    "Hello"
    call missing_label
    return
    jump end
```

**After Preprocessing:**
```renpy
label start:
    "Hello"
    __UNKNOWN__
    __UNKNOWN__
    jump end
```

**Metadata:**
```python
[
    {'line': 3, 'text': 'call missing_label'},
    {'line': 4, 'text': 'return'}
]
```

**API Response Warnings:**
```json
[
    {
        "label": "start",
        "line": 3,
        "column": 5,
        "source": "call missing_label",
        "message": "Пропущена конструкция, влияющая на логику переходов: call missing_label"
    },
    {
        "label": "start",
        "line": 4,
        "column": 5,
        "source": "return",
        "message": "Пропущена конструкция, влияющая на логику переходов: return"
    }
]
```

## Testing

Run tests with `-B` flag to avoid bytecode caching issues:
```bash
py -B test_tolerant_parsing_v2.py
```

Or run the debug test:
```bash
py -B test_debug_api.py
```

## Backward Compatibility

✅ Valid Ren'Py scripts work exactly as before
✅ No changes to existing analysis logic
✅ Graph builders and analyzers ignore UnknownStatement nodes
✅ Dot-labels (.sublabel) fully supported

## Benefits

1. **Robustness:** Parser doesn't crash on unknown syntax
2. **User-Friendly:** Critical issues are reported as warnings, not errors
3. **Preservation:** Original line numbers maintained for accurate error reporting
4. **Flexibility:** Easy to add new critical keywords or modify detection logic
5. **Non-Breaking:** Existing functionality remains intact

## Files Modified

- `core/parser/grammar.py` - Added unknown_statement rule and dot-label support
- `core/api.py` - Added preprocess_code function and warning collection logic
- `core/parser/transformer.py` - Updated unknown_statement handler
- `core/ir/model.py` - Already had UnknownStatement (from previous work)

## No Changes Required

- `core/parser/parser.py` - Parser works as-is
- `core/graph/builder.py` - Ignores unknown nodes
- `core/analysis/*.py` - All analyzers work unchanged
