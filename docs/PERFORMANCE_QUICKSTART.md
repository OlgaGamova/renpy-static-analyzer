# Performance Testing Quick Start

## Быстрый старт тестирования производительности

### 1. Автоматический запуск (рекомендуется)

**Windows:**
```bash
run_performance_tests.bat
```

**Linux/Mac:**
```bash
python run_performance_tests.py
```

Это выполнит:
1. ✅ Генерацию тестовых сценариев (50-5000 узлов)
2. ✅ Запуск бенчмарков с замером времени
3. ✅ Сохранение результатов в JSON

### 2. Ручной запуск

```bash
# Шаг 1: Генерация сценариев
python tests/generate_performance_scenarios.py

# Шаг 2: Бенчмарки
python tests/performance_benchmark.py --save

# Шаг 3: Сравнительный тест (опционально)
python tests/compare_analyzers.py --nodes 500

# Шаг 4: Pytest тесты
pytest tests/module_tests/test_performance.py -v
```

### 3. Что тестируется

| Компонент | Метод | Размер | Ожидаемое время |
|-----------|-------|--------|-----------------|
| Парсинг | Lark LALR | 500 узлов | < 0.5с |
| Трансформация | AST → IR | 500 узлов | < 0.1с |
| Граф | NetworkX | 500 узлов | < 0.1с |
| Достижимость | DFS | 500 узлов | < 0.1с |
| Мертвые концы | Scan | 500 узлов | < 0.01с |
| Циклы | Tarjan SCC | 500 узлов | < 0.1с |
| **Состояния** | **BFS** | **500 узлов** | **< 5с** |

⚠️ **StateAnalyzer** - самый медленный компонент (экспоненциальный рост)

### 4. Выявленные проблемы

#### 🔴 Критичные:
1. **Рекурсивный DFS** → RecursionError на глубине > 1000
2. **StateAnalyzer BFS** → экспоненциальное количество путей
3. **Рекурсивный Tarjan** → RecursionError на больших графах

#### 🟡 Умеренные:
1. Копирование словарей состояний
2. Хранение полных путей
3. Отсутствие кэширования парсера

### 5. Оптимизированные версии

Созданы в `core/analysis/optimized.py`:

```python
# Использование
from core.analysis.optimized import (
    OptimizedReachabilityAnalyzer,
    OptimizedInfiniteLoopAnalyzer,
    OptimizedStateAnalyzer
)

# Оптимизированный StateAnalyzer с ограничениями
state_analyzer = OptimizedStateAnalyzer(
    max_depth=100,        # Ограничение глубины
    max_path_length=50,   # Ограничение пути
    merge_states=True     # Объединение состояний
)
```

### 6. Сравнительный тест

```bash
# Сравнение оригинальных и оптимизированных версий
python tests/compare_analyzers.py --nodes 500
```

Вывод:
- Время выполнения каждого анализатора
- Потребление памяти
- Корректность результатов

### 7. Ожидаемые результаты

#### Малые сценарии (50-100 узлов)
```
✅ Парсинг: 0.1-0.3с
✅ Полный анализ: 0.3-0.8с
✅ Без ошибок
```

#### Средние сценарии (250-500 узлов)
```
✅ Парсинг: 0.3-1.0с
✅ Полный анализ: 2-10с
✅ Возможны задержки в StateAnalyzer
```

#### Большие сценарии (1000+ узлов)
```
⚠️ Парсинг: 1-5с
⚠️ Полный анализ: 30-120с
❌ StateAnalyzer может занять > 60с
❌ Возможны RecursionError без оптимизаций
```

### 8. Результаты

Сохраняются в: `tests/results/performance/benchmark_YYYYMMDD_HHMMSS.json`

Пример:
```json
{
  "script_name": "perf_medium_500.rpy",
  "node_count": 500,
  "edge_count": 750,
  "timings": {
    "parsing": 0.234,
    "transformation": 0.045,
    "graph_building": 0.012,
    "reachability": 0.008,
    "dead_ends": 0.002,
    "infinite_loops": 0.015,
    "state_analysis": 2.567,
    "total": 2.883
  }
}
```

### 9. Оптимизация

Если анализ занимает слишком много времени:

**Быстрые исправления (5 минут):**
```python
# В core/analysis/state.py добавить в начало analyze():
MAX_DEPTH = 100

while queue:
    label, state, path = queue.popleft()
    
    if len(path) > MAX_DEPTH:
        continue  # Skip deep paths
```

**Средние исправления (1 час):**
- Заменить рекурсивный DFS на итеративный
- Заменить рекурсивный Tarjan на итеративный
- Использовать оптимизированные версии из `optimized.py`

**Долгосрочные (1-2 дня):**
- Интеграция Z3 solver для symbolic execution
- Incremental analysis
- Parallel processing

### 10. CI/CD интеграция

```yaml
# .github/workflows/performance.yml
- name: Performance Tests
  run: |
    python tests/generate_performance_scenarios.py
    python tests/performance_benchmark.py --save
    pytest tests/module_tests/test_performance.py -v
```

### 11. Документация

Полная документация:
- 📖 [PERFORMANCE_TESTING.md](PERFORMANCE_TESTING.md) - подробное руководство
- 📖 [PERFORMANCE_INFRASTRUCTURE.md](PERFORMANCE_INFRASTRUCTURE.md) - архитектура
- 📖 [PERFORMANCE_ANALYSIS.md](PERFORMANCE_ANALYSIS.md) - анализ проблем

### 12. Troubleshooting

**Проблема:** RecursionError
```python
import sys
sys.setrecursionlimit(10000)
```

**Проблема:** StateAnalyzer слишком медленный
```python
# Использовать оптимизированную версию
from core.analysis.optimized import OptimizedStateAnalyzer
analyzer = OptimizedStateAnalyzer(max_depth=50)
```

**Проблема:** MemoryError
- Уменьшить `max_depth` и `max_path_length`
- Использовать `merge_states=True`
- Запускать на меньших сценариях

### 13. Следующие шаги

1. ✅ Запустить `run_performance_tests.bat`
2. ✅ Проверить результаты в `tests/results/performance/`
3. ✅ Запустить сравнительный тест
4. ✅ Применить оптимизации если нужно
5. ✅ Добавить в CI/CD

---

**Контакт:** При проблемах создайте issue с приложенными результатами бенчмарка.
