# Инфраструктура тестирования производительности

## Обзор

Создана комплексная система для тестирования производительности статического анализатора RenPy, которая позволяет:

1. **Генерировать** большие тестовые сценарии с контролируемыми параметрами
2. **Измерять** время выполнения каждого этапа анализа
3. **Выявлять** bottlenecks и проблемы производительности
4. **Отслеживать** регрессии производительности

## Созданные компоненты

### 1. Генератор тестовых сценариев
**Файл:** `tests/generate_performance_scenarios.py`

Генерирует сценарии RenPy с настраиваемыми параметрами:
- Количество узлов (labels)
- Фактор ветвления (branching factor)
- Глубина дерева
- Соотношение условий и menu

**Типы генерируемых сценариев:**
- Случайные с ветвлениями (50-5000 узлов)
- Линейные (без ветвлений)
- Глубокие деревья (depth=20)
- Широкие деревья (branching=5)

### 2. Бенчмарк производительности
**Файл:** `tests/performance_benchmark.py`

Измеряет время выполнения 7 этапов анализа:
1. Парсинг (Lark parser)
2. Трансформация (AST → IR)
3. Построение графа
4. Анализ достижимости (DFS)
5. Анализ мертвых концов
6. Анализ бесконечных циклов (Tarjan's SCC)
7. Анализ состояния (BFS с отслеживанием переменных)

**Вывод:**
- Консольный вывод с таймингами
- JSON файл с детальными результатами
- Сводная таблица по всем сценариям

### 3. Pytest тесты
**Файл:** `tests/module_tests/test_performance.py`

Автоматические тесты для CI/CD:
- Тесты для разных размеров (50, 100, 250, 500, 1000 узлов)
- Проверка отсутствия ошибок на больших сценариях
- Тесты масштабирования
- Тесты на утечки памяти

### 4. Скрипты запуска
- `run_performance_tests.py` - Python скрипт
- `run_performance_tests.bat` - Windows batch файл

## Быстрый старт

### Windows (автоматический режим)
```bash
run_performance_tests.bat
```

### Кроссплатформенно
```bash
# Генерация сценариев
python tests/generate_performance_scenarios.py

# Запуск бенчмарков
python tests/performance_benchmark.py --save

# Или всё вместе
python run_performance_tests.py
```

### Запуск pytest тестов
```bash
# Быстрые тесты
pytest tests/module_tests/test_performance.py -v

# Все тесты включая медленные
pytest tests/module_tests/test_performance.py -v -m slow

# Только маленькие сценарии
pytest tests/module_tests/test_performance.py::TestPerformanceSmall -v
```

## Ожидаемые результаты

### Таблица производительности

| Размер сценария | Узлы | Ожидаемое время | Статус |
|-----------------|------|-----------------|--------|
| Маленький | 50 | < 0.5с | ✅ Обязательно |
| Маленький | 100 | < 1с | ✅ Обязательно |
| Средний | 250 | < 5с | ✅ Обязательно |
| Средний | 500 | < 15с | ✅ Обязательно |
| Большой | 1000 | < 60с | ⚠️ Желательно |
| Очень большой | 5000 | < 300с | ⚠️ Опционально |

### Пример вывода бенчмарка

```
======================================================================
БЕНЧМАРК: perf_medium_500.rpy
======================================================================
Размер файла: 45,678 байт
Количество строк: 1,234

[1/7] Парсинг... ✓ 0.234с
[2/7] Трансформация... ✓ 0.045с (500 label'ов)
[3/7] Построение графа... ✓ 0.012с (500 узлов, 750 рёбер)
[4/7] Анализ достижимости... ✓ 0.008с (5 недостижимых)
[5/7] Анализ мертвых концов... ✓ 0.002с (10 мертвых концов)
[6/7] Анализ бесконечных циклов... ✓ 0.015с (1 циклов)
[7/7] Анализ состояния... ✓ 0.567с (3 невозможных условий, 0 undefined)

======================================================================
ОБЩЕЕ ВРЕМЯ: 0.883с
======================================================================
```

## Типичные проблемы и решения

### Проблема 1: Медленный парсинг (>5с для 500 узлов)

**Симптомы:**
- Парсинг занимает больше всего времени
- Время растет экспоненциально с размером

**Возможные причины:**
- Неоптимальная грамматика Lark
- Использование earley вместо lalr
- Слишком сложные правила

**Решения:**
```python
# В core/parser/parser.py
# Проверить использование lalr
self._parser = Lark(
    RENPY_GRAMMAR,
    parser="lalr",  # ✓ Быстрее
    # parser="earley",  # ✗ Медленнее
    ...
)
```

### Проблема 2: Медленный анализ состояния (>10с)

**Симптомы:**
- StateAnalyzer занимает больше всего времени
- Большое количество путей в visited

**Возможные причины:**
- Экспоненциальное количество путей из-за ветвлений
- Копирование состояний на каждом шаге
- Отсутствие ограничения глубины

**Решения:**

**Вариант A:** Ограничить глубину анализа
```python
# В core/analysis/state.py
MAX_DEPTH = 100  # Ограничить глубину обхода

while queue:
    if len(path) > MAX_DEPTH:
        continue  # Пропустить слишком глубокие пути
    ...
```

**Вариант B:** Оптимизировать состояния
```python
# Вместо полного копирования использовать immutable структуры
from functools import lru_cache

@lru_cache(maxsize=10000)
def analyze_state(label, state_key):
    ...
```

**Вариант C:** Incremental analysis
```python
# Анализировать только измененные части
def analyze_incremental(script, previous_results):
    changed_labels = find_changes(script, previous_results)
    # Переанализировать только changed_labels
```

### Проблема 3: RecursionError (переполнение стека)

**Симптомы:**
```
RecursionError: maximum recursion depth exceeded
```

**Возможные причины:**
- Рекурсивный DFS в ReachabilityAnalyzer
- Рекурсивный алгоритм Тарьяна в InfiniteLoopAnalyzer
- Глубокие деревья (>1000 уровней)

**Решения:**

**Вариант A:** Увеличить лимит рекурсии
```python
import sys
sys.setrecursionlimit(10000)  # По умолчанию 1000
```

**Вариант B:** Преобразовать в итеративный обход
```python
# Вместо рекурсивного DFS
def find_unreachable(self, graph, start="start"):
    visited = set()
    stack = [start]  # Использовать стек вместо рекурсии
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)
    
    return set(graph.keys()) - visited
```

### Проблема 4: Высокое потребление памяти

**Симптомы:**
- MemoryError
- Процесс занимает >1GB RAM

**Возможные причины:**
- Хранение всех путей в анализе состояний
- Большое количество состояний в visited
- Копирование словарей состояний

**Решения:**

**Вариант A:** Ограничить хранение путей
```python
# Сохранять только первые N элементов пути
MAX_PATH_LENGTH = 50

if len(path) > MAX_PATH_LENGTH:
    path = path[:MAX_PATH_LENGTH] + ["..."]
```

**Вариант B:** Использовать более компактные структуры
```python
# Вместо dict использовать tuple или named tuple
from collections import namedtuple
State = namedtuple('State', ['min_val', 'max_val'])
```

**Вариант C:** Garbage collection
```python
import gc

# Периодически вызывать GC
if len(visited) % 1000 == 0:
    gc.collect()
```

## Мониторинг производительности

### Запуск регулярных тестов

Добавьте в CI/CD pipeline:

```yaml
# .github/workflows/performance.yml
name: Performance Tests
on:
  push:
    branches: [main]
  schedule:
    - cron: '0 0 * * 1'  # Каждый понедельник

jobs:
  performance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Generate scenarios
        run: python tests/generate_performance_scenarios.py
      
      - name: Run benchmarks
        run: python tests/performance_benchmark.py --save
      
      - name: Run pytest
        run: pytest tests/module_tests/test_performance.py -v
      
      - name: Upload results
        uses: actions/upload-artifact@v2
        with:
          name: performance-results
          path: tests/results/performance/
```

### Сравнение результатов

```python
import json

# Загрузка двух результатов
with open('benchmark_old.json') as f:
    old_results = json.load(f)

with open('benchmark_new.json') as f:
    new_results = json.load(f)

# Сравнение
for old, new in zip(old_results, new_results):
    name = old['script_name']
    old_time = old['timings']['total']
    new_time = new['timings']['total']
    
    change = (new_time - old_time) / old_time * 100
    
    print(f"{name}: {old_time:.3f}с → {new_time:.3f}с ({change:+.1f}%)")
    
    if change > 20:
        print(f"  ⚠️ Регрессия производительности!")
```

## Архитектурные рекомендации

### Для улучшения производительности системы:

1. **Парсинг:**
   - Кэшировать скомпилированный парсер
   - Использовать incremental parsing для изменений
   - Рассмотреть hand-written parser для критичных участков

2. **Анализ графа:**
   - Использовать NetworkX или graph-tool для оптимизированных алгоритмов
   - Применять параллельный анализ для независимых компонент
   - Реализовать lazy evaluation для больших графов

3. **Анализ состояний:**
   - Использовать SMT solver (Z3) вместо brute-force
   - Применять abstract interpretation
   - Реализовать symbolic execution

4. **Общие оптимизации:**
   - Профилировать с cProfile перед оптимизацией
   - Использовать __slots__ для уменьшения памяти
   - Применять Cython для hot paths
   - Рассмотреть multiprocessing для параллелизма

## Следующие шаги

1. **Запустить тесты** на разных размерах сценариев
2. **Собрать baseline** производительности
3. **Идентифицировать bottlenecks** с помощью профилирования
4. **Оптимизировать** самые медленные компоненты
5. **Настроить CI/CD** для автоматического мониторинга
6. **Документировать** результаты и решения

## Поддержка

При возникновении проблем:
1. Проверьте логи бенчмарка
2. Запустите с меньшими сценариями
3. Используйте `--scenarios` для изоляции проблемы
4. Создайте issue с приложенными результатами
