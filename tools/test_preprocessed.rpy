# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
__UNKNOWN__
__UNKNOWN__
#image gus = im.Scale("gus.png", 480, 700)
__UNKNOWN__
__UNKNOWN__
__UNKNOWN__
__UNKNOWN__
__UNKNOWN__

#image map = im.Scale("map.jpg")
#image map buttons = im.Scale("map_buttons.jpg")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.



# Игра начинается здесь:
label start:

    $studik=False
    $alaska=False
    $zabil=False
    $bomb=False
    $skovorodka=False

    "В этой игре вы можете выбрать имя главного героя"

    __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__

    __UNKNOWN__
    "Теперь тебя зовут [name]"
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__
label tutorial:
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__
    menu:
        "Да":
            __UNKNOWN__
            jump tutorial
        "Я не знаю что такое студик":
            $renpy.notify("Слово \"студик\" добавлено в словарь")
            $studik=True
            __UNKNOWN__
            __UNKNOWN__
            __UNKNOWN__
            __UNKNOWN__

    menu:
        "Зайти в ГУК":
            jump story_11
    label story_11:
        __UNKNOWN__
        __UNKNOWN__
        "???" "Проходите, присаживайтесь... Всем здравствуйте! Я Елена Игоревна, ваш преподаватель истории."
        __UNKNOWN__
        __UNKNOWN__
            __UNKNOWN__
            __UNKNOWN__

        "смотрит на меня"
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        "кажется нужно как-то отреагировать"
        label .choice1:
            menu:
                "Но тут же летопись, а не парень":
                    __UNKNOWN__
                    $ renpy.notify("Слово \"Аляска\" добавлено в словарь")#В словарь
                    $alaska=True
                    __UNKNOWN__
                "-Промолчать-":
                    __UNKNOWN__
                    "какая-то девушка" "Эй! Это к тебе обратились."
                    __UNKNOWN__
                "Это летопись?":
                    ""
            __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        "*Кто-то с заднего ряда*" "Сейчас {color=#025}загуглим{/color}"
        $ renpy.notify("Нажми на строку поиска, чтобы выйти в Интернет")
        __UNKNOWN__
        "Ты решаешь тоже посмотреть в интеренете и открываешь свой ноутбук"




    label googling:
        __UNKNOWN__
        "Похоже этой летописи почти 700 лет"#тут кстати два синонима подряд
        $sosed_message=True
        $ renpy.notify("✉Новое уведомление от Вконтакте")
        "Кажется мне пришло какое-то сообщение"

        "Пара уже закончилась, посмотрю потом"
        __UNKNOWN__
        "Нужно вернуться в {color=#025}общагу{/color}"
        $ renpy.notify("Общежитие = кнопка №8")

    label story_12:


        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        menu:
            "Войти в общежитие":
                jump story_13

    label story_13:
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        menu:
            "Кого ты забил на пару? Праздник какой-то?":
                jump story_14
            "Почему?":
                jump story_15
    label story_14:
        __UNKNOWN__
        $renpy.notify("Слово \"Забил\" добавлено в словарь")
        $zabil=True
        __UNKNOWN__
        __UNKNOWN__

    label story_15:
        __UNKNOWN__
        menu:
            "Какая история в джунглях? Какие ещё бомбы?":
                jump story_16
            "Всё так плохо?":
                jump story_17

    label story_16:
        __UNKNOWN__
        $renpy.notify("Слово \"Бомбы\" добавлено в словарь")
        $bomb=True
        __UNKNOWN__

    label story_17:
        menu:
            "Мне тоже нужно подготовить бомбы":
                jump story_18
            "Какой же сложный русский язык!":
                jump story_18
    label story_18:
        __UNKNOWN__
        $renpy.notify("Слово \"Сковородка\" добавлено в словарь")
        $skovorodka=True
        __UNKNOWN__


    label browser:
        __UNKNOWN__
        "Это экран браузера, здесь можно переходить на сайты, нажимая на значки под строкой поиска"
    label brs:
        __UNKNOWN__
        "Место, куда преподаватели выставляют оценки"
        return
    label vk:
        __UNKNOWN__
        if sosed_message:
            __UNKNOWN__
        __UNKNOWN__
        "Место для общения с одногруппниками"
    label plan:
        __UNKNOWN__
        "Здесь можно посмотреть список предметов"
    label scheduele:
        __UNKNOWN__
        "Расписание занятий"
    label teams:
        __UNKNOWN__
        "Расписание занятий"
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__

    __UNKNOWN__
    menu:
        "Да":
            $start_flag=False
        "Нет":
            $start_flag=False
        "А что это":
            __UNKNOWN__
            $start_flag=True
            $ renpy.notify("Новое слово добавлено в словарь")

    __UNKNOWN__



    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__

    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__
    __UNKNOWN__



    label map:

        __UNKNOWN__

    label guk:
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        call map_done from _call_map_done
    label ineu:
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        jump map_done
    label stroika:
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        jump map_done
    label teplofuck:
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        jump map_done
    label fizteh:
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        jump map_done
    label chempion:
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        jump map_done
    label label_8:#todo Физ-ра
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        jump map_done
    label dormitory:
        __UNKNOWN__
        __UNKNOWN__
        jump story_12

        "Внимание, конец игры!"
        jump map_done
        return
    label inmt:
        __UNKNOWN__
        __UNKNOWN__
        __UNKNOWN__
        jump map_done
    label map_done:
        return
return

label dict:
    __UNKNOWN__
    return
label lapt:
    __UNKNOWN__
    "конец игры"
    "конец"





