@echo off
echo ========================================================================
echo REGENERATING ALL PERFORMANCE TEST SCENARIOS
echo ========================================================================
echo.

echo [Step 1] Removing old scenarios...
if exist tests\samples\performance\*.rpy (
    del /Q tests\samples\performance\*.rpy
    echo Old scenarios removed.
) else (
    echo No old scenarios found.
)

echo.
echo [Step 2] Generating new scenarios...
python tests\generate_performance_scenarios.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to generate scenarios!
    pause
    exit /b 1
)

echo.
echo [Step 3] Testing generated scenarios...
python tests\test_generator.py

if errorlevel 1 (
    echo.
    echo ERROR: Generated scenarios failed to parse!
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo SUCCESS! All scenarios regenerated and validated.
echo ========================================================================
echo.
echo Generated files:
dir /B tests\samples\performance\*.rpy
echo.
echo Next steps:
echo   1. Run benchmarks: python tests\performance_benchmark.py --save
echo   2. Run full tests: run_performance_tests.bat
echo.
pause
