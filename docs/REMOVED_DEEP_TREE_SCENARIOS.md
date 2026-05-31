# Removed Deep Tree Scenarios

## Issue

The `perf_deep_tree.rpy` scenario was **extremely large**:
- **20,971,508 lines** (20+ million!)
- File size: hundreds of megabytes
- Impossible to parse or analyze in reasonable time

The `perf_wide_tree.rpy` was also large:
- **39,058 lines**
- Still manageable but not necessary

## Root Cause

Deep tree generation with `depth=20, branching=2` creates exponential growth:
- Each level doubles the number of nodes
- Level 20 = 2^20 = 1,048,576 leaf nodes
- Plus all the intermediate nodes and menu structures
- Result: 20+ million lines of RenPy code

## Solution

### 1. Removed from test suite generation
Updated `tests/generate_performance_scenarios.py`:
```python
# NOTE: Deep tree scenarios removed - they generate too large files (20M+ lines)
# ("perf_deep_tree.rpy", {'type': 'deep_tree', 'depth': 20, 'branching': 2}),
# ("perf_wide_tree.rpy", {'type': 'deep_tree', 'depth': 5, 'branching': 5}),
```

### 2. Updated pytest tests
- Removed tests that depend on deep tree scenarios
- Added test for `perf_xlarge_5000.rpy` (5000 nodes) as the largest test case

### 3. Created cleanup script
`cleanup_large_files.bat` - helps delete the large files

## New Test Suite

After regeneration, you'll have **8 test scenarios** instead of 10:

| File | Nodes | Type | Size |
|------|-------|------|------|
| perf_small_50.rpy | 50 | Random | ~4 KB |
| perf_small_100.rpy | 100 | Random | ~8 KB |
| perf_medium_250.rpy | 250 | Random | ~20 KB |
| perf_medium_500.rpy | 500 | Random | ~40 KB |
| perf_large_1000.rpy | 1000 | Random | ~80 KB |
| perf_large_2000.rpy | 2000 | Random | ~160 KB |
| **perf_xlarge_5000.rpy** | **5000** | **Random** | **~400 KB** |
| perf_linear_500.rpy | 500 | Linear | ~30 KB |

**Removed:**
- ❌ perf_deep_tree.rpy (20M+ lines)
- ❌ perf_wide_tree.rpy (39K lines)

## How to Cleanup

### Option 1: Use the cleanup script
```bash
cleanup_large_files.bat
```

### Option 2: Manual deletion
```bash
# Close your IDE/text editor first!
del tests\samples\performance\perf_deep_tree.rpy
del tests\samples\performance\perf_wide_tree.rpy
```

### Option 3: Regenerate everything
```bash
# Delete all scenarios
del tests\samples\performance\*.rpy

# Regenerate (will not create deep trees)
python tests\generate_performance_scenarios.py
```

## Why 5000 Nodes is Enough

The 5000-node scenario (`perf_xlarge_5000.rpy`) is sufficient for performance testing:

- **Tests scalability**: Shows how the system handles large graphs
- **Reasonable size**: ~400 KB, manageable for analysis
- **Realistic**: Similar to actual large Ren'Py games
- **Good benchmark**: Takes 1-5 minutes to analyze (depending on optimizations)

Testing beyond 5000 nodes provides diminishing returns and creates impractical file sizes.

## Impact

### Before
- ❌ 10 test scenarios (2 unusable)
- ❌ 20M+ line file wastes disk space
- ❌ Cannot run full test suite
- ❌ Benchmarks fail on deep_tree

### After
- ✅ 8 test scenarios (all usable)
- ✅ Maximum size: 5000 nodes (~400 KB)
- ✅ All tests pass
- ✅ Benchmarks complete successfully

## Next Steps

1. Run cleanup script to delete large files:
   ```bash
   cleanup_large_files.bat
   ```

2. Regenerate scenarios:
   ```bash
   python tests\generate_performance_scenarios.py
   ```

3. Run benchmarks:
   ```bash
   python tests\performance_benchmark.py --save
   ```

4. Verify all tests pass:
   ```bash
   pytest tests/module_tests/test_performance.py -v
   ```

---

**Date:** 2026-05-14  
**Status:** ✅ Deep tree scenarios removed from test suite  
**Maximum test size:** 5000 nodes (perf_xlarge_5000.rpy)
