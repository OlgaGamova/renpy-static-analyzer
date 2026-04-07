label start:
    $ strength = 0
    $ intelligence = 0
    $ luck = 0

    menu:
        "Пойти в лес":
            $ strength += 5
            jump forest
        "Пойти в город":
            $ intelligence += 5
            jump city
        "Остаться дома":
            $ luck += 5
            jump home


label forest:
    menu:
        "Драться с волком":
            $ strength += 10
            jump forest_fight
        "Спрятаться":
            $ luck += 2
            jump forest_hide


label forest_fight:
    if strength >= 20:
        jump forest_win
    jump forest_lose


label forest_hide:
    if luck >= 10:
        jump secret_path
    jump forest_lose


label forest_win:
    jump chapter2


label forest_lose:
    jump end_bad


label city:
    menu:
        "Пойти в библиотеку":
            $ intelligence += 10
            jump library
        "Пойти в бар":
            $ luck += 3
            jump bar


label library:
    if intelligence >= 30:
        jump smart_win
    jump city_fail


label bar:
    if luck >= 20:
        jump lucky_win
    jump city_fail


label city_fail:
    jump end_bad


label smart_win:
    jump chapter2


label lucky_win:
    jump chapter2


label home:
    menu:
        "Тренироваться":
            $ strength += 3
            jump training
        "Читать книги":
            $ intelligence += 3
            jump reading


label training:
    if strength >= 50:
        jump impossible_win   # недостижимое условие
    jump chapter2


label reading:
    if intelligence >= 50:
        jump impossible_win   # недостижимое условие
    jump chapter2


label chapter2:
    menu:
        "Исследовать пещеру":
            jump cave
        "Пойти в замок":
            jump castle


label cave:
    $ has_torch = True

    menu:
        "Идти глубже":
            jump deep_cave
        "Выйти":
            jump end_neutral


label deep_cave:
    if has_torch:
        jump treasure
    jump end_bad


label treasure:
    $ has_torch = False  # противоречие (теряем состояние)

    if has_torch:
        jump secret_end  # никогда не выполнится

    jump end_good


label castle:
    if has_key:
        jump royal_end  # переменная не инициализирована

    jump end_neutral


label impossible_win:
    jump end_good


label secret_path:
    jump secret_loop


label secret_loop:
    jump secret_loop   # бесконечный цикл


label royal_end:
    "Ты стал королём"
    jump end_good


label end_good:
    "Хорошая концовка"


label end_bad:
    "Плохая концовка"


label end_neutral:
    "Нейтральная концовка"


label unused_content:
    "Эта ветка никогда не используется"  # недостижимая