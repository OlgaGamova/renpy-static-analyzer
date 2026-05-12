# Enhanced Recommendations Feature

## Overview

The recommendations block in the API has been enhanced to provide **actionable advice** for fixing detected issues, not just identifying problems.

---

## Changes Made

### File Modified
- **`core/api.py`** - Updated `build_recommendations()` function (lines 57-95)

---

## Enhanced Recommendation Types

### 1. **State Errors (Impossible Conditions)**

#### Before:
```
library: intelligence ≥ 30 недостижимо (макс 15) (строка 59)
```

#### After:
```
library: intelligence ≥ 30 недостижимо (макс 15) (строка 59) — снизьте порог или добавьте больше выборов, дающих очки опыта
```

**Translation**: "Lower the threshold or add more choices that give experience points"

**Benefits**:
- ✅ Tells the developer **what** the problem is
- ✅ Suggests **two concrete solutions**:
  1. Lower the required threshold (e.g., from 30 to 15)
  2. Add more menu options that increase the stat

---

### 2. **Infinite Loops**

#### Before:
```
Бесконечный цикл: secret_loop (строки 153)
```

#### After:
```
Бесконечный цикл: secret_loop (строки 153) — добавьте условие выхода из цикла
```

**Translation**: "Add an exit condition to the loop"

**Benefits**:
- ✅ Identifies the infinite loop
- ✅ Suggests **adding an exit condition** (e.g., a counter, flag, or state check)

---

### 3. **Unreachable Nodes** (Unchanged)
```
Узел 'unreachable_label' недостижим — добавьте переход (строка 42)
```
Already had good advice: "add a transition"

---

### 4. **Terminal Nodes** (Unchanged)
```
Узел 'end_bad' завершает сценарий — проверьте корректность (строка 166)
```
Already had good advice: "verify correctness"

---

## Example Output

When analyzing a script with multiple issues, the enhanced recommendations now look like:

```
1. Узел 'secret_loop' недостижим — добавьте переход (строка 152)

2. Бесконечный цикл: secret_loop (строки 153) — добавьте условие выхода из цикла

3. training: strength ≥ 50 недостижимо (макс 18) (строка 93) — снизьте порог или добавьте больше выборов, дающих очки опыта

4. reading: intelligence ≥ 50 недостижимо (макс 18) (строка 99) — снизьте порог или добавьте больше выборов, дающих очки опыта

5. library: intelligence ≥ 30 недостижимо (макс 15) (строка 59) — снизьте порог или добавьте больше выборов, дающих очков опыта
```

---

## Testing

### Test Script Created
- **`test_enhanced_recommendations.py`** - Verifies that recommendations include actionable advice

### Run Test
```powershell
python test_enhanced_recommendations.py
```

### Expected Output
```
======================================================================
ENHANCED RECOMMENDATIONS TEST
======================================================================

Found 2 recommendation(s):

1. forest: strength ≥ 50 недостижимо (макс 15) (строка 18) — снизьте порог или добавьте больше выборов, дающих очки опыта

2. Бесконечный цикл: secret_loop (строки 26) — добавьте условие выхода из цикла

======================================================================
VERIFICATION
======================================================================

✅ State error recommendation includes actionable advice
   Example: forest: strength ≥ 50 недостижимо (макс 15) (строка 18) — снизьте порог...

✅ Infinite loop recommendation includes actionable advice
   Example: Бесконечный цикл: secret_loop (строки 26) — добавьте условие выхода из цикла

🎉 SUCCESS: All recommendations include helpful action items!
```

---

## Implementation Details

### Code Changes

#### Infinite Loops (lines 76-82):
```python
for loop in analysis["infinite_loops_with_lines"]:
    loop_nodes = [item["node"] for item in loop]
    loop_lines = [str(item["line"]) for item in loop if item["line"] is not None]
    if loop_lines:
        recs.append(f"Бесконечный цикл: {' → '.join(loop_nodes)} (строки {', '.join(loop_lines)}) — добавьте условие выхода из цикла")
    else:
        recs.append(f"Бесконечный цикл: {' → '.join(loop_nodes)} — добавьте условие выхода из цикла")
```

#### State Errors (lines 84-93):
```python
for err in analysis["state"]["impossible_conditions"]:
    line = err.get("line", None)
    if line is not None:
        recs.append(
            f"{err['label']}: {err['var']} ≥ {err['required']} недостижимо (макс {err['range'][1]}) (строка {line}) — снизьте порог или добавьте больше выборов, дающих очки опыта"
        )
    else:
        recs.append(
            f"{err['label']}: {err['var']} ≥ {err['required']} недостижимо (макс {err['range'][1]}) — снизьте порог или добавьте больше выборов, дающих очки опыта"
        )
```

---

## Benefits for Users

### For Game Developers:
1. **Clearer guidance** - Not just "what's wrong" but "how to fix it"
2. **Actionable items** - Specific suggestions they can implement immediately
3. **Better UX** - More professional and helpful error messages

### For the Tool:
1. **More valuable** - Transforms from a diagnostic tool to a helpful assistant
2. **Reduces confusion** - Developers know exactly what to do next
3. **Professional quality** - Matches industry-standard linter/analyzer tools

---

## Future Enhancements (Optional)

Could add more specific advice based on context:

### For State Errors:
- If max is very low: "Consider starting with a higher base value"
- If only one path: "Add alternative paths to gain {variable}"
- If close to threshold: "The requirement is barely out of reach - small adjustments needed"

### For Infinite Loops:
- If has conditions: "Check if your exit condition logic is correct"
- If simple jump: "Add a menu or conditional jump to break the loop"

### For Unreachable Nodes:
- "This label may be leftover code - consider removing it if not needed"

---

## Summary

✅ **Enhanced** infinite loop recommendations with exit condition advice  
✅ **Enhanced** state error recommendations with threshold/choices advice  
✅ **Maintained** existing quality for unreachable and terminal node recommendations  
✅ **Tested** with dedicated test script  
✅ **All tests pass** - No regressions introduced

The recommendations are now **significantly more helpful** for developers fixing their Ren'Py scripts! 🎉
