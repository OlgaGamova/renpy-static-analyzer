label start:
    $ strength = 0
    $ intelligence = 0
    $ luck = 0
    $ charisma = 0

    menu:
        "Go back":
            $ intelligence += 3
            jump label_0
        "Look around":
            jump label_1

label label_0:
    "Scene label_0"
    menu:
        "Open door":
            $ strength += 1
            jump label_2
        "Use item":
            jump label_3

label label_2:
    "Scene label_2"
    if intelligence >= 18:
        jump label_4

label label_4:
    $ intelligence += 3
    menu:
        "Go forward":
            jump label_5
        "Talk":
            jump label_6

label label_5:
    "Scene label_5"
    menu:
        "Use item":
            jump label_7
        "Explore":
            $ charisma += 1
            jump label_8

label label_7:
    "Scene label_7"
    jump end_9

label label_8:
    "Scene label_8"
    jump end_9

label label_6:
    "Scene label_6"
    menu:
        "Go back":
            jump label_9
        "Pick up item":
            jump label_10

label label_9:
    "Scene label_9"
    jump end_11

label label_10:
    "Scene label_10"
    jump end_11

    jump label_11

label label_11:
    "Ветка false для label_4"
    menu:
        "Look around":
            jump label_12
        "Explore":
            jump label_13

label label_12:
    "Scene label_12"
    menu:
        "Use item":
            jump label_14
        "Look around":
            jump label_15

label label_14:
    "Scene label_14"
    jump end_16

label label_15:
    "Scene label_15"
    jump end_16

label label_13:
    "Scene label_13"
    menu:
        "Go back":
            $ luck += 1
            jump label_16
        "Explore":
            $ luck += 3
            jump label_17

label label_16:
    "Scene label_16"
    jump end_18

label label_17:
    "Scene label_17"
    jump end_18

label label_3:
    "Scene label_3"
    menu:
        "Talk":
            jump label_18
        "Use item":
            $ charisma += 2
            jump label_19

label label_18:
    "Scene label_18"
    menu:
        "Explore":
            jump label_20
        "Go forward":
            $ strength += 2
            jump label_21

label label_20:
    "Scene label_20"
    menu:
        "Use item":
            jump label_22
        "Explore":
            $ charisma += 2
            jump label_23

label label_22:
    "Scene label_22"
    jump end_24

label label_23:
    "Scene label_23"
    jump end_24

label label_21:
    "Scene label_21"
    menu:
        "Talk":
            $ intelligence += 3
            jump label_24
        "Go back":
            jump label_25

label label_24:
    "Scene label_24"
    jump end_26

label label_25:
    "Scene label_25"
    jump end_26

label label_19:
    "Scene label_19"
    menu:
        "Explore":
            $ intelligence += 3
            jump label_26
        "Pick up item":
            $ strength += 1
            jump label_27

label label_26:
    "Scene label_26"
    if intelligence >= 18:
        jump label_28

label label_28:
    $ intelligence += 2
    jump end_29

    jump label_29

label label_29:
    "Ветка false для label_28"
    jump end_30

label label_27:
    "Scene label_27"
    menu:
        "Go back":
            jump label_30
        "Go forward":
            jump label_31

label label_30:
    "Scene label_30"
    jump end_32

label label_31:
    "Scene label_31"
    jump end_32

label label_1:
    "Scene label_1"
    if luck >= 15:
        jump label_32

label label_32:
    $ luck += 2

label end_9:
    "Конец: end_9"

label end_9:
    "Конец: end_9"

label end_11:
    "Конец: end_11"

label end_11:
    "Конец: end_11"

label end_16:
    "Конец: end_16"

label end_16:
    "Конец: end_16"

label end_18:
    "Конец: end_18"

label end_18:
    "Конец: end_18"

label end_24:
    "Конец: end_24"

label end_24:
    "Конец: end_24"

label end_26:
    "Конец: end_26"

label end_26:
    "Конец: end_26"

label end_29:
    "Конец: end_29"

label end_30:
    "Конец: end_30"

label end_32:
    "Конец: end_32"

label end_32:
    "Конец: end_32"
