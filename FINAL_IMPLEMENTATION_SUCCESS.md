# Tolerant Parsing Implementation - FINAL SUCCESS

## Summary

Successfully implemented tolerant parsing for the Ren'Py static analyzer that handles unknown/unrecognized statements without crashing, with full backward compatibility.

## Test Results

✅ **ALL TESTS PASS**: 40 passed, 1 skipped, 0 failures
✅ **FakeStudent scenario (296 lines)**: Parses successfully
  - 13 nodes (labels)
  - 10 edges (jumps/transitions)
  - 4 warnings for critical unknown statements

## Implementation Details

### 1. Preprocessor-Based Approach (`core/api.py`)

The `preprocess_code()` function scans Ren'Py code line-by-line before parsing:

**Key Features:**
- Preserves supported constructs: `label`, `jump`, `menu:`, `$`, `if`, dialogue strings
- Replaces unknown statements with `__UNKNOWN__` markers
- Preserves line numbers and indentation for accurate error reporting
- **Handles indented comments**: Converts them to empty lines to avoid breaking Lark's indenter
- **Handles block statements**: When replacing a block statement (like `python:`), also removes all child lines with greater indentation

**Critical Fixes:**
1. **Indented comments**: Lines like `    #comment` inside indented blocks were creating INDENT tokens followed by ignored comments, breaking the parser. Solution: Replace indented comments with empty lines.
2. **Block statement children**: When `python:` is replaced, its indented child lines must also be removed to avoid orphaned INDENT tokens.

### 2. Grammar Updates (`core/parser/grammar.py`)

**Flexible Assignment Support:**
```python
# Old (restrictive):
assignment: "$" NAME OP_ASSIGN (NUMBER | NAME) _NEWLINE?

# New (flexible):
assignment: DOLLAR_ASSIGN _NEWLINE?
DOLLAR_ASSIGN.2: "$" /[^\n]*/
```

The `.2` priority ensures the terminal doesn't compete with other terminals like NAME, STRING, etc.

**Supports:**
- `$studik=False` (no space)
- `$ points = 5` (with spaces)
- `$ renpy.notify("...")` (function calls)
- `$var=True` (boolean values)

### 3. Transformer Updates (`core/parser/transformer.py`)

The `assignment()` method now:
1. Extracts the full expression from `DOLLAR_ASSIGN` token (includes `$`)
2. Strips the leading `$` and whitespace
3. Uses regex to parse simple assignments: `(\w+)\s*([+]?=)\s*(.+)`
4. Extracts variable name, operator, and value
5. Converts `True`/`False` to `1`/`0`
6. Falls back to dummy Assignment for complex expressions like `renpy.notify(...)`

### 4. Warning Generation (`core/api.py`)

After parsing, the API:
1. Scans all labels for `UnknownStatement` nodes
2. Looks up the original source text using line numbers
3. Classifies warnings as critical if they contain keywords: `call`, `return`, `while`, `repeat`, `python:`
4. Adds warnings to the API response

## Files Modified

1. **`core/api.py`**
   - Added `preprocess_code()` function
   - Integrated preprocessing in `analyze_script()`
   - Added warning collection and classification

2. **`core/parser/grammar.py`**
   - Changed assignment rule to use `DOLLAR_ASSIGN` terminal
   - Added flexible regex pattern for assignments

3. **`core/parser/transformer.py`**
   - Updated `assignment()` to handle flexible format
   - Added `$` stripping and regex parsing

## Warnings Generated for FakeStudent

```
Line 34: Пропущена конструкция, влияющая на логику переходов: python:
Line 285: Пропущена конструкция, влияющая на логику переходов: call screen dictionary
Line 286: Пропущена конструкция, влияющая на логику переходов: return
Line 288: Пропущена конструкция, влияющая на логику переходов: call screen browser
```

All 4 warnings are correctly classified as **critical** because they contain keywords that affect control flow.

## Backward Compatibility

✅ All existing tests pass without modification
✅ All sample files parse correctly:
- `always_true.rpy` - Always-true condition detection
- `flag_conflict.rpy` - Flag contradiction detection
- `dead_end.rpy` - Dead end detection
- `unreachable.rpy` - Unreachable node detection
- `loop_story.rpy` - Infinite loop detection
- All performance test scenarios (50-5000 nodes)

## Key Lessons Learned

1. **Lark's indenter is sensitive to comments**: Indented comments create INDENT/DEDENT tokens even though the comment itself is ignored, breaking the parse tree.

2. **Terminal priority matters**: Anonymous terminals or high-priority named terminals can compete with other tokens. Using `.2` priority lowers precedence.

3. **Python bytecode caching**: Always use `py -B` or clear `__pycache__` when testing changes to avoid running stale code.

4. **Block statement handling**: When replacing unknown block statements, must also handle their indented children to maintain proper indentation structure.

5. **Preprocessor approach vs grammar fallback**: Grammar-based fallback with low-priority terminals causes LALR conflicts. Preprocessing before parsing is cleaner and more reliable.

## Production Ready

The implementation is production-ready and handles:
- ✅ Unknown statements without crashing
- ✅ Complex Ren'Py syntax (function calls, booleans, etc.)
- ✅ Indented comments correctly
- ✅ Block statements with children
- ✅ Warning generation for critical keywords
- ✅ Full backward compatibility
- ✅ All existing tests passing
