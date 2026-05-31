@echo off
echo ========================================================================
echo RE-VALIDATING ANALYZER WITH FIXES APPLIED
echo ========================================================================
echo.
echo This will:
echo   1. Regenerate error scenarios with fixed loop structure
echo   2. Run the fixed analyzer
echo   3. Check if ALL bugs are now detected
echo.

echo [Step 1] Regenerating scenarios with fixed structures...
python tests\generate_error_scenarios.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to generate error scenarios!
    pause
    exit /b 1
)

echo.
echo [Step 2] Running analyzer validation with FIXED StateAnalyzer...
python tests\validate_analyzer.py

if errorlevel 1 (
    echo.
    echo ========================================================================
    echo WARNING: Still some issues found!
    echo ========================================================================
    echo.
    echo The analyzer has been improved but may still have limitations.
    echo Check ANALYZER_BUGS_AND_FIXES.md for details.
) else (
    echo.
    echo ========================================================================
    echo SUCCESS! All errors now detected correctly!
    echo ========================================================================
    echo.
    echo The analyzer bugs have been fixed:
    echo   ^[1^] Impossible conditions - NOW DETECTED
    echo   ^[2^] Undefined labels - NOW DETECTED
    echo   ^[3^] Infinite loops - IMPROVED DETECTION
)

echo.
echo ========================================================================
echo RE-VALIDATION COMPLETE
echo ========================================================================
echo.
pause
