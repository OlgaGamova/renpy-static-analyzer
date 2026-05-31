# 📚 Performance Testing - Index

## Добро пожаловать в систему тестирования производительности RenPy Static Analyzer!

Этот документ поможет вам быстро найти нужную информацию.

---

## 🚀 Быстрый старт

**Хочу сразу начать тестирование:**
1. 👉 [PERFORMANCE_QUICKSTART.md](PERFORMANCE_QUICKSTART.md) - начните отсюда!
2. Запустите: `run_performance_tests.bat` (Windows) или `python run_performance_tests.py`

**Хочу увидеть демонстрацию:**
```bash
python tests/demo_performance.py
```

---

## 📖 Документация по темам

### 🎯 Для новых пользователей

| Документ | Описание | Когда читать |
|----------|----------|--------------|
| [PERFORMANCE_QUICKSTART.md](PERFORMANCE_QUICKSTART.md) | Быстрый старт за 5 минут | ⭐ Начните здесь! |
| [PERFORMANCE_SUMMARY.md](PERFORMANCE_SUMMARY.md) | Общая сводка | Чтобы понять что сделано |

### 📊 Для тестирования

| Документ | Описание | Когда читать |
|----------|----------|--------------|
| [PERFORMANCE_TESTING.md](PERFORMANCE_TESTING.md) | Подробное руководство | Для глубокого понимания |
| [PERFORMANCE_FULL_GUIDE.md](PERFORMANCE_FULL_GUIDE.md) | Полная инструкция | Для всех деталей |

### 🔧 Для оптимизации

| Документ | Описание | Когда читать |
|----------|----------|--------------|
| [PERFORMANCE_ANALYSIS.md](PERFORMANCE_ANALYSIS.md) | Анализ проблем | Если есть проблемы с производительностью |
| [PERFORMANCE_INFRASTRUCTURE.md](PERFORMANCE_INFRASTRUCTURE.md) | Архитектура системы | Для понимания как работает |

---

## 🗂️ Компоненты системы

### Генерация сценариев
- **Файл:** `tests/generate_performance_scenarios.py`
- **Что делает:** Создает тестовые сценарии RenPy (50-5000 узлов)
- **Документация:** [PERFORMANCE_FULL_GUIDE.md#генерация-тестовых-сценариев](PERFORMANCE_FULL_GUIDE.md)

### Бенчмарки
- **Файл:** `tests/performance_benchmark.py`
- **Что делает:** Замеряет время каждого этапа анализа
- **Документация:** [PERFORMANCE_FULL_GUIDE.md#запуск-бенчмарков](PERFORMANCE_FULL_GUIDE.md)

### Сравнительные тесты
- **Файл:** `tests/compare_analyzers.py`
- **Что делает:** Сравнивает оригинальные и оптимизированные версии
- **Документация:** [PERFORMANCE_FULL_GUIDE.md#сравнительные-тесты](PERFORMANCE_FULL_GUIDE.md)

### Pytest тесты
- **Файл:** `tests/module_tests/test_performance.py`
- **Что делает:** Автоматические тесты для CI/CD
- **Документация:** [PERFORMANCE_FULL_GUIDE.md#pytest-тесты](PERFORMANCE_FULL_GUIDE.md)

### Оптимизации
- **Файл:** `core/analysis/optimized.py`
- **Что делает:** Улучшенные версии анализаторов (до 21x быстрее!)
- **Документация:** [PERFORMANCE_ANALYSIS.md](PERFORMANCE_ANALYSIS.md)

---

## 🎓 Обучение по уровням

### Уровень 1: Новичок

**Цель:** Запустить тесты и увидеть результаты

**Шаги:**
1. Прочитать: [PERFORMANCE_QUICKSTART.md](PERFORMANCE_QUICKSTART.md) (5 минут)
2. Запустить: `run_performance_tests.bat`
3. Посмотреть результаты в: `tests/results/performance/`

**Время:** 10 минут

### Уровень 2: Пользователь

**Цель:** Понять как работает система

**Шаги:**
1. Прочитать: [PERFORMANCE_TESTING.md](PERFORMANCE_TESTING.md) (15 минут)
2. Запустить: `python tests/demo_performance.py`
3. Попробовать: создать свой сценарий с разными параметрами

**Время:** 30 минут

### Уровень 3: Разработчик

**Цель:** Оптимизировать систему

**Шаги:**
1. Прочитать: [PERFORMANCE_ANALYSIS.md](PERFORMANCE_ANALYSIS.md) (20 минут)
2. Изучить: `core/analysis/optimized.py`
3. Применить оптимизации к основному коду
4. Запустить сравнительные тесты

**Время:** 2 часа

### Уровень 4: Эксперт

**Цель:** Расширить систему

**Шаги:**
1. Прочитать: [PERFORMANCE_INFRASTRUCTURE.md](PERFORMANCE_INFRASTRUCTURE.md) (30 минут)
2. Изучить архитектуру всех компонентов
3. Добавить новые метрики или тесты
4. Интегрировать с CI/CD

**Время:** 1 день

---

## 📋 Use Cases

### Use Case 1: Проверка производительности после изменений

**Задача:** Убедиться что изменения не замедлили систему

**Решение:**
```bash
# 1. Запустить бенчмарки
python tests/performance_benchmark.py --save --output-dir results_after

# 2. Сравнить с baseline
python scripts/check_regression.py results_before/benchmark.json results_after/
```

**Документация:** [PERFORMANCE_FULL_GUIDE.md#проверка-регрессий](PERFORMANCE_FULL_GUIDE.md)

### Use Case 2: Поиск bottleneck

**Задача:** Найти самый медленный компонент

**Решение:**
```bash
# Запустить бенчмарк с детальным выводом
python tests/performance_benchmark.py --scenarios my_scenario.rpy
```

Смотрите на проценты в выводе - самый большой = bottleneck

**Документация:** [PERFORMANCE_ANALYSIS.md#выявленные-проблемы](PERFORMANCE_ANALYSIS.md)

### Use Case 3: Стресс-тест

**Задача:** Проверить как система справляется с большими сценариями

**Решение:**
```python
from tests.generate_performance_scenarios import RenPyScenarioGenerator

gen = RenPyScenarioGenerator()
gen.generate_scenario(
    num_nodes=5000,
    branching_factor=4,
    max_depth=18,
    output_path="stress_test.rpy"
)

python tests/performance_benchmark.py --scenarios stress_test.rpy
```

**Документация:** [PERFORMANCE_FULL_GUIDE.md#кастомные-сценарии](PERFORMANCE_FULL_GUIDE.md)

### Use Case 4: Оптимизация StateAnalyzer

**Задача:** Ускорить самый медленный компонент

**Решение:**
```python
# Вместо:
from core.analysis.state import StateAnalyzer
state = StateAnalyzer()

# Используйте:
from core.analysis.optimized import OptimizedStateAnalyzer
state = OptimizedStateAnalyzer(
    max_depth=100,
    merge_states=True
)
```

**Документация:** [PERFORMANCE_ANALYSIS.md#решения](PERFORMANCE_ANALYSIS.md)

### Use Case 5: CI/CD интеграция

**Задача:** Автоматическое тестирование производительности

**Решение:** Добавьте в GitHub Actions:
```yaml
- name: Performance Tests
  run: |
    python tests/generate_performance_scenarios.py
    python tests/performance_benchmark.py --save
    pytest tests/module_tests/test_performance.py -v
```

**Документация:** [PERFORMANCE_FULL_GUIDE.md#интеграция-с-cicd](PERFORMANCE_FULL_GUIDE.md)

---

## 🔍 FAQ

### Как быстро проверить производительность?
```bash
run_performance_tests.bat  # или python run_performance_tests.py
```

### Где результаты?
`tests/results/performance/benchmark_YYYYMMDD_HHMMSS.json`

### Какой сценарий использовать для тестов?
- Быстрые тесты: `perf_small_100.rpy` (100 узлов)
- Стандартные: `perf_medium_500.rpy` (500 узлов)
- Полные: `perf_large_1000.rpy` (1000 узлов)

### Почему StateAnalyzer такой медленный?
Экспоненциальное количество путей: O(branching^depth)
Решение: используйте `OptimizedStateAnalyzer` с ограничениями

### Как применить оптимизации?
Замените импорты на `core/analysis/optimized.py`
Подробности: [PERFORMANCE_ANALYSIS.md](PERFORMANCE_ANALYSIS.md)

### Как создать свой сценарий?
```python
from tests.generate_performance_scenarios import RenPyScenarioGenerator
gen = RenPyScenarioGenerator(seed=42)
gen.generate_scenario(num_nodes=500, output_path="my.rpy")
```

### Тесты падают с RecursionError
```python
import sys
sys.setrecursionlimit(10000)
```
Или используйте итеративные версии из `optimized.py`

### Как сравнить до/после оптимизации?
```bash
python tests/compare_analyzers.py --nodes 500
```

---

## 📊 Quick Reference Card

### Основные команды

```bash
# Быстрый старт
run_performance_tests.bat

# Генерация сценариев
python tests/generate_performance_scenarios.py

# Бенчмарки
python tests/performance_benchmark.py --save

# Сравнение
python tests/compare_analyzers.py --nodes 500

# Pytest
pytest tests/module_tests/test_performance.py -v

# Демонстрация
python tests/demo_performance.py
```

### Файлы

| Файл | Назначение |
|------|------------|
| `tests/generate_performance_scenarios.py` | Генератор сценариев |
| `tests/performance_benchmark.py` | Бенчмарк |
| `tests/compare_analyzers.py` | Сравнение версий |
| `tests/module_tests/test_performance.py` | Pytest тесты |
| `core/analysis/optimized.py` | Оптимизации |
| `run_performance_tests.bat` | Windows раннер |
| `run_performance_tests.py` | Python раннер |

### Метрики

| Метрика | 50 узлов | 500 узлов | 1000 узлов |
|---------|----------|-----------|------------|
| Парсинг | < 0.1с | < 0.5с | < 1с |
| Граф | < 0.01с | < 0.1с | < 0.2с |
| **Состояния** | < 0.2с | < 5с | < 30с |
| **ИТОГО** | < 0.3с | < 10с | < 60с |

---

## 🎯 Рекомендации по чтению

### Если у вас мало времени (5 минут)
1. Прочитайте: [PERFORMANCE_QUICKSTART.md](PERFORMANCE_QUICKSTART.md)
2. Запустите: `run_performance_tests.bat`

### Если хотите разобраться (30 минут)
1. Прочитайте: [PERFORMANCE_SUMMARY.md](PERFORMANCE_SUMMARY.md)
2. Запустите: `python tests/demo_performance.py`
3. Изучите результаты

### Если нужно оптимизировать (2 часа)
1. Прочитайте: [PERFORMANCE_ANALYSIS.md](PERFORMANCE_ANALYSIS.md)
2. Примените оптимизации из `optimized.py`
3. Запустите сравнительные тесты

### Если интегрируете в проект (1 день)
1. Прочитайте: [PERFORMANCE_FULL_GUIDE.md](PERFORMANCE_FULL_GUIDE.md)
2. Настройте CI/CD
3. Добавьте мониторинг регрессий

---

## 📞 Помощь

### Что-то не работает?
1. Проверьте: [PERFORMANCE_QUICKSTART.md - Troubleshooting](PERFORMANCE_QUICKSTART.md)
2. Изучите: [PERFORMANCE_FULL_GUIDE.md - Troubleshooting](PERFORMANCE_FULL_GUIDE.md)
3. Создайте issue с результатами бенчмарка

### Хотите узнать больше?
- [PERFORMANCE_ANALYSIS.md](PERFORMANCE_ANALYSIS.md) - глубокий анализ проблем
- [PERFORMANCE_INFRASTRUCTURE.md](PERFORMANCE_INFRASTRUCTURE.md) - архитектура
- Исходный код: `core/analysis/optimized.py`

---

## ✅ Чеклист для начала

- [ ] Установить зависимости: `pip install -r requirements.txt`
- [ ] Прочитать: [PERFORMANCE_QUICKSTART.md](PERFORMANCE_QUICKSTART.md)
- [ ] Запустить: `run_performance_tests.bat`
- [ ] Проверить результаты: `tests/results/performance/`
- [ ] Попробовать оптимизации: `core/analysis/optimized.py`

---

**Версия:** 1.0  
**Дата:** 2026-05-14  
**Статус:** ✅ Готово к использованию
