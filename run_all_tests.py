#!/usr/bin/env python
"""
Comprehensive test runner for the Ren'Py Static Analyzer project.
Runs all tests including module tests and the state analyzer fix verification.
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a command and report results."""
    print(f"\n{'='*70}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print('='*70)
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    if result.returncode == 0:
        print(f"✅ {description} - PASSED")
        return True
    else:
        print(f"❌ {description} - FAILED (exit code: {result.returncode})")
        return False

def main():
    print("\n" + "="*70)
    print("REN'PY STATIC ANALYZER - COMPREHENSIVE TEST SUITE")
    print("="*70)
    
    results = []
    
    # Test 1: Run pytest on all module tests
    results.append(run_command(
        [sys.executable, "-m", "pytest", "tests/module_tests/", "-v", "--tb=short"],
        "Module Tests (pytest)"
    ))
    
    # Test 2: Run the state analyzer fix verification
    results.append(run_command(
        [sys.executable, "test_state_fix.py"],
        "State Analyzer Fix Verification"
    ))
    
    # Test 3: Run specific core analysis tests
    results.append(run_command(
        [sys.executable, "-m", "pytest", "tests/module_tests/test_core_analysis.py", "-v"],
        "Core Analysis Tests"
    ))
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    total = len(results)
    passed = sum(results)
    failed = total - passed
    
    print(f"Total: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if all(results):
        print("\n✅ ALL TESTS PASSED!")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
