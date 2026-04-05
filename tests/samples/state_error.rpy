label start:

    "Начало истории"

    $ strength += 10
    $ strength += 10

    "Ты немного прокачался"

    if strength >= 30:
        jump win

    "Ты слишком слаб"

    jump end


label win:
    "Ты победил!"

    jump end


label end:
    "Конец игры"