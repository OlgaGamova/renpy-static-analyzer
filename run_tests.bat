@echo off
echo ================================================================
echo REN'PY STATIC ANALYZER - RUNNING ALL TESTS
echo ================================================================
echo.

echo Running pytest on all tests...
python -m pytest tests/ -v --tb=short

echo.
echo ================================================================
echo TEST EXECUTION COMPLETE
echo ================================================================
pause
