# Analyzer Validation - Testing Error Detection

## Problem Identified

You asked a critical question: **"Does the analyzer actually find errors correctly?"**

The answer revealed a major gap: **The generated scenarios didn't contain any errors!**

### Original Issue

When you ran `perf_xlarge_5000.rpy` through the analyzer, it reported:
```
- Unreachable nodes: 0
- Infinite loops: 0
- Impossible conditions: 1
- Dead ends: 937
```

**This is suspicious because:**
1. Random scenarios should have some unreachable nodes
2. No infinite loops in 5000 nodes is unlikely
3. 937 dead ends suggests most nodes are terminal (normal for generated code)
4. Only 1 impossible condition seems too low

**Root cause:** The generator created **clean, error-free scenarios** that don't test the analyzer's ability to find bugs!

---

## Solution: Error Injection Generator

Created `tests/generate_error_scenarios.py` - a generator that **deliberately injects errors**:

### Types of Injected Errors

1. **Unreachable Nodes** (5-10 per scenario)
   ```renpy
   label unreachable_123:
       "This node is never reached"
       $ strength += 10
       jump normal_45
   ```
   - These labels exist but nothing jumps to them
   - Should be detected by `ReachabilityAnalyzer`

2. **Infinite Loops** (2-5 per scenario)
   ```renpy
   # Type 1: Self-loop
   label loop_start_100:
       "Loop start"
       jump loop_start_100  # Jumps to itself!
   
   # Type 2: Two-node loop
   label loop_start_101:
       "Loop start"
   label loop_end_101:
       "Loop end"
       jump loop_start_101  # No exit!
   ```
   - Cycles with no way out
   - Should be detected by `InfiniteLoopAnalyzer`

3. **Impossible Conditions** (3-10 per scenario)
   ```renpy
   label impossible_200:
       $ strength = 0  # Set to 0
       if strength >= 100:  # Check if >= 100 (IMPOSSIBLE!)
           "This never executes"
   ```
   - Condition can never be true
   - Should be detected by `StateAnalyzer`

4. **Dead Ends** (2-5 per scenario)
   ```renpy
   label dead_end_300:
       "No way out!"
       $ strength += 1
       # NO JUMP - dead end!
   ```
   - Nodes with no outgoing edges
   - Should be detected by `DeadEndAnalyzer`

5. **Undefined Labels** (2-5 per scenario)
   ```renpy
   label jump_to_undefined_400:
       "Jumping nowhere"
       jump undefined_label_1  # Doesn't exist!
   ```
   - Jumps to non-existent labels
   - Should be detected by `StateAnalyzer`

---

## Test Scenarios Generated

| File | Nodes | Unreachable | Loops | Impossible | Dead Ends | Undefined |
|------|-------|-------------|-------|------------|-----------|-----------|
| error_small_100.rpy | 100 | 3 | 2 | 3 | 2 | 2 |
| error_medium_500.rpy | 500 | 5 | 3 | 5 | 3 | 3 |
| error_large_1000.rpy | 1000 | 10 | 5 | 10 | 5 | 5 |

---

## How to Validate

### Quick Validation (Recommended)

```bash
validate_analyzer.bat
```

This will:
1. Generate scenarios with known errors
2. Run the analyzer
3. Compare results with expected errors
4. Report pass/fail for each error type

### Manual Validation

```bash
# Step 1: Generate error scenarios
python tests/generate_error_scenarios.py

# Step 2: Run validation
python tests/validate_analyzer.py
```

### Analyze Single File

```bash
python tests/validate_analyzer.py --scenarios tests/samples/performance_with_errors/error_medium_500.rpy
```

---

## Expected Output

### Successful Validation

```
======================================================================
ВАЛИДАЦИЯ: error_medium_500.rpy
======================================================================

Недостижимые узлы:
  Ожидалось: 5
  Найдено: 5
  Статус: ✓ PASS

Мертвые концы:
  Ожидалось: 3
  Найдено: 3
  Статус: ✓ PASS

Бесконечные циклы:
  Ожидалось: 3
  Найдено: 3
  Статус: ✓ PASS

Невозможные условия:
  Ожидалось: 5
  Найдено: 5
  Статус: ✓ PASS

Неопределенные метки:
  Ожидалось: 3
  Найдено: 3
  Статус: ✓ PASS

======================================================================
✅ ВСЕ ОШИБКИ НАЙДЕНЫ ПРАВИЛЬНО!
======================================================================
```

### Failed Validation

```
======================================================================
❌ НЕ ВСЕ ОШИБКИ НАЙДЕНЫ!

Возможные причины:
  1. Алгоритм анализа имеет баги
  2. Ошибки слишком сложные для обнаружения
  3. Некоторые ошибки считаются нормальным поведением
======================================================================
```

---

## Interpreting Results

### If All Tests Pass ✅

**Your analyzer is working correctly!** It can detect:
- Unreachable code
- Infinite loops
- Impossible conditions
- Dead ends
- Undefined labels

### If Some Tests Fail ❌

Common issues:

#### 1. Unreachable nodes not found
**Possible causes:**
- All nodes are actually reachable (check scenario generation)
- DFS bug in `ReachabilityAnalyzer`
- Start node assumption is wrong

**Fix:**
```python
# Check that start node is correct
unreachable = reach.find_unreachable(graph, start="start")
```

#### 2. Infinite loops not found
**Possible causes:**
- Tarjan's algorithm bug
- Self-loops not detected
- Exit detection logic is wrong

**Fix:**
Check `core/analysis/infinite_loops.py` - ensure self-loops are detected:
```python
if len(component) == 1:
    node = component[0]
    if node in graph.get(node, set()):
        # This IS an infinite loop!
```

#### 3. Impossible conditions not found
**Possible causes:**
- State tracking bug
- Condition checking logic incorrect
- State merging loses information

**Fix:**
Check `core/analysis/state.py` - verify `_check()` method:
```python
def _check(self, min_v, max_v, op, value):
    if op == ">=":
        return max_v >= value  # Should return False if max_v < value
```

#### 4. Dead ends not found
**Possible causes:**
- Graph building adds implicit edges
- Dead end definition is wrong

**Note:** Dead ends are nodes with NO outgoing edges. If every node has a jump, there are no dead ends.

#### 5. Undefined labels not found
**Possible causes:**
- Not checking jump targets
- Missing label validation

**Fix:**
Check that all jump targets exist in the script:
```python
for node in all_nodes:
    if node not in script.labels:
        # Undefined label!
```

---

## Using Error Scenarios for Performance Testing

### Why Use Error Scenarios?

1. **Correctness verification** - Ensures analyzer finds bugs
2. **Performance benchmarking** - Tests with realistic error patterns
3. **Regression testing** - Catches bugs introduced by optimizations

### Recommended Workflow

```bash
# 1. Validate correctness first
validate_analyzer.bat

# 2. If all pass, run performance tests
python tests/performance_benchmark.py --save

# 3. Compare results
# - Error scenarios should find all injected errors
# - Performance should be acceptable
```

---

## Next Steps

### Immediate
1. ✅ Run `validate_analyzer.bat`
2. ✅ Check if all errors are detected
3. ✅ If not, fix the analyzer bugs

### Short-term
1. Add more complex error patterns
   - Nested impossible conditions
   - Multi-node cycles (3+ nodes)
   - Conditional unreachable nodes
2. Test edge cases
   - Empty scenarios
   - Single-node scenarios
   - Fully connected graphs

### Long-term
1. Create comprehensive test suite
2. Add to CI/CD pipeline
3. Track detection accuracy over time

---

## Files Created

| File | Purpose |
|------|---------|
| `tests/generate_error_scenarios.py` | Generates scenarios with known errors |
| `tests/validate_analyzer.py` | Validates analyzer finds all errors |
| `validate_analyzer.bat` | Automated validation script |
| `ANALYZER_VALIDATION_GUIDE.md` | This documentation |

---

## Summary

**Your question revealed a critical gap:** The original scenarios were too clean and didn't test error detection!

**Solution:** Created error injection generator + validation system

**Result:** Now you can verify that your analyzer:
- ✅ Finds unreachable nodes
- ✅ Detects infinite loops
- ✅ Identifies impossible conditions
- ✅ Reports dead ends
- ✅ Catches undefined labels

Run `validate_analyzer.bat` to test your analyzer now! 🎯
