label start:

    "Начало"

    menu:
        "Set True":
            $ flag = True
            jump merge

        "Set False":
            $ flag = False
            jump merge

label merge:

    if flag:
        jump ok

    "Флаг ложен"

    jump end

label ok:
    "Флаг истинен"

    jump end

label end:
    "Конец"

