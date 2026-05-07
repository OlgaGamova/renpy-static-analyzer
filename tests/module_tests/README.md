# Ren'Py Static Analyzer Test Suite

This test suite provides comprehensive coverage for the Ren'Py Static Analyzer project, including:

- Core analysis functionality (unreachable nodes, infinite loops, state errors)
- Web interface integration and API endpoints
- Graph highlighting functionality
- Line number propagation and error reporting

## Test Structure

The test suite is organized into three main categories:

### 1. Core Analysis Tests (`test_core_analysis.py`)
- Tests the fundamental analysis algorithms
- Validates detection of unreachable nodes, infinite loops, dead ends, and state errors
- Tests line number propagation through the AST
- Tests API endpoint integration logic

### 2. Web Interface Tests (`test_web_interface.py`)
- Tests that analysis results are formatted correctly for the web interface
- Validates data structures expected by the frontend JavaScript code
- Ensures recommendations are generated properly

### 3. Graph Highlighting Tests (`test_graph_highlighting.py`)
- Tests the specific data structures used for graph highlighting
- Validates that `secret_loop` and other problematic nodes are properly detected and formatted
- Ensures compatibility with the enhanced frontend highlighting logic

## Running Tests

### Prerequisites
- Python 3.8+
- pytest
- All project dependencies installed

### Basic Test Execution
```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_core_analysis.py -v

# Run specific test function
pytest tests/test_core_analysis.py::test_infinite_loop_detection -v
```

### Test Coverage
To check test coverage:
```bash
pip install pytest-cov
pytest tests/ --cov=core --cov-report=html
```

## Test Data

Test data is located in `tests/samples/` directory and includes:
- `huge_branching.rpy`: Complex branching scenario with `secret_loop`
- `loop_story.rpy`: Simple infinite loop example
- `state_error.rpy`: State validation errors
- `unreachable.rpy`: Unreachable node detection
- `dead_end.rpy`: Dead end detection

## Development Guidelines

- All new features should include corresponding tests
- Tests should be isolated and not depend on external services
- Use fixtures for shared test setup
- Tests should validate both success and error cases
- Test edge cases like missing line numbers, malformed scripts, etc.

## Contributing

When contributing to the test suite:
1. Add tests for new functionality before implementing the feature
2. Update existing tests when changing behavior
3. Ensure tests pass before submitting pull requests
4. Add documentation for new test patterns or fixtures

---

**Note**: These tests focus on the core logic and API structure. End-to-end browser testing would require additional tools like Selenium or Playwright.