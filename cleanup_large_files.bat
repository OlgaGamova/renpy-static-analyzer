@echo off
echo ========================================================================
echo CLEANING UP LARGE PERFORMANCE TEST FILES
echo ========================================================================
echo.
echo This will remove extremely large test files that are too big to analyze:
echo   - perf_deep_tree.rpy (20+ million lines)
echo   - perf_wide_tree.rpy (39K lines, optional)
echo.

echo Attempting to delete perf_deep_tree.rpy...
if exist tests\samples\performance\perf_deep_tree.rpy (
    echo File size:
    for %%A in (tests\samples\performance\perf_deep_tree.rpy) do (
        echo   %%~zA bytes
    )
    
    echo.
    echo IMPORTANT: Close any programs that might be using this file
    echo (text editors, IDE, file explorers, etc.)
    echo.
    pause
    
    del /F /Q tests\samples\performance\perf_deep_tree.rpy
    if errorlevel 1 (
        echo.
        echo Failed to delete! The file is locked.
        echo Please close all programs and try again manually:
        echo   del tests\samples\performance\perf_deep_tree.rpy
    ) else (
        echo Successfully deleted perf_deep_tree.rpy
    )
) else (
    echo File not found (already deleted).
)

echo.
echo Attempting to delete perf_wide_tree.rpy...
if exist tests\samples\performance\perf_wide_tree.rpy (
    del /F /Q tests\samples\performance\perf_wide_tree.rpy
    if errorlevel 1 (
        echo Failed to delete perf_wide_tree.rpy (locked).
    ) else (
        echo Successfully deleted perf_wide_tree.rpy
    )
) else (
    echo File not found (already deleted).
)

echo.
echo ========================================================================
echo Cleanup complete!
echo ========================================================================
echo.
echo Remaining test files:
dir /B tests\samples\performance\*.rpy 2>nul
echo.
echo To regenerate scenarios (without deep trees):
echo   python tests\generate_performance_scenarios.py
echo.
pause
