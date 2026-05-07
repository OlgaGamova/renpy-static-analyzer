import pytest
from pathlib import Path


def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "unit: mark test as unit test"
    )


def pytest_addoption(parser):
    """Add command line options"""
    parser.addoption(
        "--run-slow", 
        action="store_true",
        default=False,
        help="run slow tests"
    )


def pytest_collection_modifyitems(config, items):
    """Skip slow tests unless --run-slow is specified"""
    if config.getoption("--run-slow"):
        return
    skip_slow = pytest.mark.skip(reason="need --run-slow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)

# Test fixtures
@pytest.fixture
def sample_scripts():
    """Load all sample scripts"""
    samples_dir = Path(__file__).parent / "samples"
    scripts = {}
    for file_path in samples_dir.glob("*.rpy"):
        scripts[file_path.stem] = file_path.read_text(encoding="utf-8")
    return scripts

@pytest.fixture
def huge_branching_script(sample_scripts):
    """Get huge_branching.rpy script"""
    return sample_scripts.get("huge_branching", "")

@pytest.fixture
def loop_story_script(sample_scripts):
    """Get loop_story.rpy script"""
    return sample_scripts.get("loop_story", "")
