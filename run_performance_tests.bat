@echo off
echo ========================================================================
echo ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ RENPY STATIC ANALYZER
echo ========================================================================
echo.

echo [Шаг 1] Генерация тестовых сценариев...
python tests\generate_performance_scenarios.py
if errorlevel 1 (
    echo.
    echo ОШИБКА: Не удалось сгенерировать сценарии
    pause
    exit /b 1
)

echo.
echo [Шаг 2] Запуск бенчмарков...
python tests\performance_benchmark.py --save
if errorlevel 1 (
    echo.
    echo ОШИБКА: Не удалось запустить бенчмарки
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО!
echo ========================================================================
echo.
echo Результаты сохранены в: tests\results\performance\
echo.
pause
