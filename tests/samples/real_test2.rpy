image bg room = "room.jpg"
screen extra:
    text "Привет"
python:
    x = 5
    y = x * 2

label start:
    $ points = 0
    $ has_key = False
    "Вы в комнате."
    menu:
        "Искать ключ":
            jump explore
        "Выйти":
            jump exit

label explore:
    $ points += 1
    scene corridor
    show door
    menu:
        "Найти ключ":
            $ has_key = True
            call notify
            jump corridor
        "Вернуться":
            jump start

label notify:
    "Вы нашли ключ!"
    return

label corridor:
    if has_key:
        $ points += 10
        call door
    else:
        jump start

label door:
    if points >= 15:
        jump good_ending
    else:
        jump bad_ending

label exit:
    "Вы вышли."
    jump start

label good_ending:
    "Победа!"
    jump end

label bad_ending:
    "Поражение"
    jump end

label end:
    "Конец"

label unused_label:
    "Никогда не будет вызвана"

label infinite_loop:
    jump infinite_loop

label impossible_condition:
    if points >= 100:
        jump win
    else:
        jump lose

label flag_error:
    if not has_key:
        jump wrong
    else:
        jump ok

call screen extra
return