#!/usr/bin/env python
"""Simple test runner that executes pytest programmatically."""

import pytest
import sys

if __name__ == "__main__":
    print("="*70)
    print("RUNNING ALL TESTS")
    print("="*70)
    
    # Run pytest on the tests directory
    exit_code = pytest.main([
        "tests/",
        "-v",
        "--tb=short",
        "--color=yes"
    ])
    
    if exit_code == 0:
        print("\n✅ ALL TESTS PASSED!")
    else:
        print(f"\n❌ TESTS FAILED WITH EXIT CODE: {exit_code}")
    
    sys.exit(exit_code)
