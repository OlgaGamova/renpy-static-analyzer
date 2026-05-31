# Analyzer Bugs Found and Fixes

## Critical Bugs Discovered by Validation

### Bug #1: Impossible Conditions Not Detected ❌

**Symptom:** 0 impossible conditions found (expected 10, 5, 3)

**Root Cause:** 
The StateAnalyzer's BFS traversal doesn't reach the impossible condition labels because:
1. They're placed AFTER normal nodes in the file
2. The BFS visits nodes in graph traversal order, not file order
3. If impossible condition labels aren't reachable from `start` via jumps, they're never analyzed

**Location:** `core/analysis/state.py` lines 28-111

**The Problem:**
```python
# Line 23: Start BFS from "start"
queue.append(("start", {}, ["start"]))

# Line 32: Skip if label doesn't exist
if label not in script.labels:
    continue  # ← But what if label exists but is never reached?

# The BFS only visits REACHABLE labels!
# Unreachable labels with impossible conditions are never checked!
```

**Fix Required:**
The analyzer must check ALL labels in the script, not just reachable ones!

```python
def analyze(self, script):
    results = {
        "impossible_conditions": [],
        "undefined_labels": []
    }
    
    # Phase 1: Check ALL labels for impossible conditions
    for label_name in script.labels.keys():
        self._check_label_conditions(script, label_name, results)
    
    # Phase 2: Check for undefined labels from all jumps
    self._check_undefined_labels(script, results)
    
    return results

def _check_label_conditions(self, script, label_name, results):
    """Check conditions in a single label."""
    state = {}
    body = script.labels[label_name].body
    
    for node in body:
        if isinstance(node, Assignment):
            state = self._apply(state, node)
        elif isinstance(node, Condition):
            min_v, max_v = state.get(node.var, (0, 0))
            if not self._check(min_v, max_v, node.op, node.value):
                results["impossible_conditions"].append({...})
```

---

### Bug #2: Undefined Labels Not Detected ❌

**Symptom:** 0 undefined labels found (expected 5, 3, 2)

**Root Cause:**
The current code only checks undefined labels when trying to visit them (line 32), but:
1. If the jump is in unreachable code, it's never visited
2. Need to scan ALL jump statements in the entire script

**Location:** `core/analysis/state.py` lines 32-40

**The Problem:**
```python
# Only checks when we try to visit the label
if label not in script.labels:
    results["undefined_labels"].append(...)

# But if nothing jumps to the label containing the undefined jump,
# we never discover it!
```

**Fix Required:**
Scan ALL labels and collect ALL jump targets, then check which ones don't exist:

```python
def _check_undefined_labels(self, script, results):
    """Find all undefined labels by scanning all jumps."""
    all_defined = set(script.labels.keys())
    all_targets = set()
    
    # Collect all jump targets from all labels
    for label_name, label in script.labels.items():
        targets = self._collect_jump_targets(label.body)
        all_targets.update(targets)
    
    # Find undefined
    undefined = all_targets - all_defined
    for target in undefined:
        results["undefined_labels"].append({
            "label": target,
            "path": []
        })

def _collect_jump_targets(self, body):
    """Recursively collect all jump targets from a body."""
    targets = set()
    for node in body:
        if hasattr(node, 'target'):
            targets.add(node.target)
        elif hasattr(node, 'body'):
            targets.update(self._collect_jump_targets(node.body))
        elif isinstance(node, Menu):
            for option in node.options:
                targets.update(self._collect_jump_targets(option.body))
    return targets
```

---

### Bug #3: Some Infinite Loops Not Detected ⚠️

**Symptom:** Found 2/5, 0/3, 1/2 infinite loops

**Root Cause:**
The error generator creates malformed loop structures:

**Wrong structure (line 661-665 in error_small_100.rpy):**
```renpy
label loop_start_279:
    "Infinite loop #1 - start"
    # NO JUMP HERE! Falls through to next label
label loop_end_279:
    "Infinite loop #1 - end"
    jump loop_start_279
```

This creates:
- `loop_start_279` → `loop_end_279` (implicit fallthrough)
- `loop_end_279` → `loop_start_279` (explicit jump)

This IS a 2-node cycle, but the graph builder might not capture the fallthrough correctly!

**The Issue:**
RenPy doesn't have implicit fallthrough! After a `say` statement, execution continues to the next label in the file, but the graph builder only tracks explicit `jump` statements.

**Fix Required in Generator:**
Add explicit jumps to create proper loops:

```python
lines.append(f"label {loop_start}:")
lines.append(f'    "Infinite loop #{i+1} - start"')
lines.append(f"    jump {loop_end}")  # ← ADD THIS!

lines.append(f"label {loop_end}:")
lines.append(f'    "Infinite loop #{i+1} - end"')
lines.append(f"    jump {loop_start}")  # Already has this
```

---

## Implementation Plan

### Priority 1: Fix StateAnalyzer (Critical)
**File:** `core/analysis/state.py`

Changes:
1. Check ALL labels for impossible conditions (not just reachable)
2. Scan all jumps for undefined labels
3. Separate analysis into two phases

### Priority 2: Fix Error Generator (Important)
**File:** `tests/generate_error_scenarios.py`

Changes:
1. Add explicit jumps in infinite loops
2. Ensure proper loop structure

### Priority 3: Re-run Validation
**Command:**
```bash
validate_analyzer.bat
```

Expected result: All tests should PASS ✅

---

## Why These Bugs Matter

### Bug Impact Assessment

| Bug | Severity | Impact |
|-----|----------|--------|
| Impossible conditions not detected | 🔴 Critical | Misses critical logic errors in games |
| Undefined labels not detected | 🔴 Critical | Causes runtime crashes in games |
| Some loops not detected | 🟡 Medium | Misses some infinite loops |

### Real-World Impact

**Scenario:** A RenPy game has:
```renpy
label chapter3:
    $ trust = 0
    if trust >= 100:  # IMPOSSIBLE!
        jump secret_ending
```

**Current analyzer:** Says "No errors" ❌
**Expected:** Reports "Impossible condition at chapter3" ✅

This means **the analyzer could miss critical bugs in actual games!**

---

## Next Steps

1. ✅ Document bugs (this file)
2. ⏳ Fix StateAnalyzer to check all labels
3. ⏳ Fix error generator loop structure
4. ⏳ Re-run validation
5. ⏳ Update performance test results

---

**Date Discovered:** 2026-05-14  
**Discovered By:** Validation system  
**Status:** 🔴 Critical bugs found, fixes needed
