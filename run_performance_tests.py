#!/usr/bin/env python
"""
Простой скрипт для запуска генерации сценариев и бенчмарков.
"""

import subprocess
import sys

def run_command(cmd, description):
    """Запуск команды и вывод результата."""
    print(f"\n{'='*70}")
    print(f"{description}")
    print(f"{'='*70}")
    
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=False,
        text=True
    )
    
    return result.returncode

def main():
    print("="*70)
    print("ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ RENPY АНАЛИЗАТОРА")
    print("="*70)
    
    # Шаг 1: Генерация сценариев
    exit_code = run_command(
        f"{sys.executable} tests\\generate_performance_scenarios.py",
        "ШАГ 1: ГЕНЕРАЦИЯ ТЕСТОВЫХ СЦЕНАРИЕВ"
    )
    
    if exit_code != 0:
        print(f"\n❌ Ошибка генерации сценариев (код {exit_code})")
        return
    
    # Шаг 2: Запуск бенчмарков
    exit_code = run_command(
        f"{sys.executable} tests\\performance_benchmark.py --generate --save",
        "ШАГ 2: ЗАПУСК БЕНЧМАРКОВ"
    )
    
    if exit_code != 0:
        print(f"\n❌ Ошибка бенчмарков (код {exit_code})")
        return
    
    print("\n" + "="*70)
    print("✅ ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО!")
    print("="*70)

if __name__ == "__main__":
    main()
