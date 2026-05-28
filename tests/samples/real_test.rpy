# Инициализация персонажей
define s = Character("Сергей", color="#1e90ff")
define a = Character("Алиса", color="#ff69b4")

# Начало игры
label start:

    # 1. Фоновое изображение и появление персонажа
    scene bg office_morning
    show alice neutral at center

    # 2. Диалог
    a "Шеф, вы просили зайти..."
    a "Я принесла кофе, но у меня плохие новости."

    # 3. Смена эмоции персонажа
    show alice sad

    s "Что еще стряслось, Алиса?"

    # 4. Выбор игрока (Ветвление)
    menu:
        "Разозлиться":
            jump angry_route

        "Сохранить спокойствие":
            jump calm_route

# --- Ветка 1: Плохая концовка ---
label angry_route:
    s "Да сколько можно! Ты вообще работаешь?!"
    show alice crying
    a "Простите..."
    # Переход к следующей сцене
    jump ending

# --- Ветка 2: Хорошая концовка ---
label calm_route:
    s "Успокойся. Садись и рассказывай всё по порядку."
    show alice smile
    a "Спасибо, Сергей. Вы лучший."
    # Переход к следующей сцене
    jump ending

# --- Завершение ---
label ending:
    scene bg black
    "Конец примера сцены."
    return
