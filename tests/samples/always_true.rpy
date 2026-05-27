label start:

    "Начало истории"

    $ points = 5

    "Вы получили очки"

    if points >= 3:
        jump win

    "Это недостижимо"

    jump end


label win:
    "Победа"

    jump end


label end:
    "Конец"

