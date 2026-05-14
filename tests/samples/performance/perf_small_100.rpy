label start:
    $ strength = 0
    $ intelligence = 0
    $ luck = 0
    $ charisma = 0

    if intelligence >= 19:
        jump label_0

label label_0:
    $ intelligence += 2
    menu:
        "Talk":
            jump label_1
        "Look around":
            jump label_2

label label_1:
    "Scene label_1"
    if intelligence >= 9:
        jump label_3

label label_3:
    $ intelligence += 4
    menu:
        "Explore":
            $ strength += 2
            jump label_4
        "Go back":
            $ intelligence += 3
            jump label_5

label label_4:
    "Scene label_4"
    menu:
        "Pick up item":
            jump label_6
        "Talk":
            $ charisma += 3
            jump label_7

label label_6:
    "Scene label_6"
    if charisma >= 11:
        jump label_8

label label_8:
    $ charisma += 3
    jump end_9

    jump label_9

label label_9:
    "Ветка false для label_8"
    jump end_10

label label_7:
    "Scene label_7"
    menu:
        "Explore":
            $ charisma += 1
            jump label_10
        "Use item":
            $ luck += 1
            jump label_11

label label_10:
    "Scene label_10"
    jump end_12

label label_11:
    "Scene label_11"
    jump end_12

label label_5:
    "Scene label_5"
    menu:
        "Use item":
            $ strength += 1
            jump label_12
        "Look around":
            jump label_13

label label_12:
    "Scene label_12"
    menu:
        "Use item":
            $ charisma += 1
            jump label_14
        "Talk":
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
        "Use item":
            jump label_16
        "Open door":
            $ strength += 3
            jump label_17

label label_16:
    "Scene label_16"
    jump end_18

label label_17:
    "Scene label_17"
    jump end_18

    jump label_18

label label_18:
    "Ветка false для label_3"
    menu:
        "Open door":
            $ strength += 3
            jump label_19
        "Look around":
            $ luck += 1
            jump label_20

label label_19:
    "Scene label_19"
    if intelligence >= 19:
        jump label_21

label label_21:
    $ intelligence += 3
    menu:
        "Pick up item":
            $ strength += 2
            jump label_22
        "Look around":
            $ strength += 1
            jump label_23

label label_22:
    "Scene label_22"
    jump end_24

label label_23:
    "Scene label_23"
    jump end_24

    jump label_24

label label_24:
    "Ветка false для label_21"
    menu:
        "Talk":
            $ charisma += 1
            jump label_25
        "Open door":
            jump label_26

label label_25:
    "Scene label_25"
    jump end_27

label label_26:
    "Scene label_26"
    jump end_27

label label_20:
    "Scene label_20"
    if strength >= 17:
        jump label_27

label label_27:
    $ strength += 4
    menu:
        "Go back":
            $ charisma += 1
            jump label_28
        "Use item":
            $ strength += 3
            jump label_29

label label_28:
    "Scene label_28"
    jump end_30

label label_29:
    "Scene label_29"
    jump end_30

    jump label_30

label label_30:
    "Ветка false для label_27"
    menu:
        "Explore":
            $ charisma += 3
            jump label_31
        "Talk":
            $ strength += 1
            jump label_32

label label_31:
    "Scene label_31"
    jump end_33

label label_32:
    "Scene label_32"
    jump end_33

label label_2:
    "Scene label_2"
    if strength >= 12:
        jump label_33

label label_33:
    $ strength += 5
    if intelligence >= 6:
        jump label_34

label label_34:
    $ intelligence += 2
    menu:
        "Go back":
            $ luck += 1
            jump label_35
        "Go back":
            $ luck += 2
            jump label_36

label label_35:
    "Scene label_35"
    menu:
        "Go forward":
            $ strength += 1
            jump label_37
        "Use item":
            jump label_38

label label_37:
    "Scene label_37"
    jump end_39

label label_38:
    "Scene label_38"
    jump end_39

label label_36:
    "Scene label_36"
    if luck >= 7:
        jump label_39

label label_39:
    $ luck += 3
    jump end_40

    jump label_40

label label_40:
    "Ветка false для label_39"
    jump end_41

    jump label_41

label label_41:
    "Ветка false для label_34"
    menu:
        "Pick up item":
            jump label_42
        "Go back":
            jump label_43

label label_42:
    "Scene label_42"
    menu:
        "Go back":
            jump label_44
        "Look around":
            jump label_45

label label_44:
    "Scene label_44"
    jump end_46

label label_45:
    "Scene label_45"
    jump end_46

label label_43:
    "Scene label_43"
    if strength >= 8:
        jump label_46

label label_46:
    $ strength += 3
    jump end_47

    jump label_47

label label_47:
    "Ветка false для label_46"
    jump end_48

    jump label_48

label label_48:
    "Ветка false для label_33"
    if intelligence >= 15:
        jump label_49

label label_49:
    $ intelligence += 3
    menu:
        "Pick up item":
            $ strength += 1
            jump label_50
        "Open door":
            jump label_51

label label_50:
    "Scene label_50"
    if luck >= 9:
        jump label_52

label label_52:
    $ luck += 4
    jump end_53

    jump label_53

label label_53:
    "Ветка false для label_52"
    jump end_54

label label_51:
    "Scene label_51"
    if charisma >= 18:
        jump label_54

label label_54:
    $ charisma += 2
    jump end_55

    jump label_55

label label_55:
    "Ветка false для label_54"
    jump end_56

    jump label_56

label label_56:
    "Ветка false для label_49"
    if intelligence >= 6:
        jump label_57

label label_57:
    $ intelligence += 4
    menu:
        "Open door":
            $ luck += 2
            jump label_58
        "Go forward":
            jump label_59

label label_58:
    "Scene label_58"
    jump end_60

label label_59:
    "Scene label_59"
    jump end_60

    jump label_60

label label_60:
    "Ветка false для label_57"
    if intelligence >= 8:
        jump label_61

label label_61:
    $ intelligence += 4
    jump end_62

    jump label_62

label label_62:
    "Ветка false для label_61"
    jump end_63

    jump label_63

label label_63:
    "Ветка false для label_0"
    menu:
        "Talk":
            jump label_64
        "Use item":
            jump label_65

label label_64:
    "Scene label_64"
    menu:
        "Open door":
            $ luck += 2
            jump label_66

label label_66:
    "Scene label_66"
label label_65:
    "Scene label_65"

label end_9:
    "Конец: end_9"

label end_10:
    "Конец: end_10"

label end_12:
    "Конец: end_12"

label end_12:
    "Конец: end_12"

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

label end_27:
    "Конец: end_27"

label end_27:
    "Конец: end_27"

label end_30:
    "Конец: end_30"

label end_30:
    "Конец: end_30"

label end_33:
    "Конец: end_33"

label end_33:
    "Конец: end_33"

label end_39:
    "Конец: end_39"

label end_39:
    "Конец: end_39"

label end_40:
    "Конец: end_40"

label end_41:
    "Конец: end_41"

label end_46:
    "Конец: end_46"

label end_46:
    "Конец: end_46"

label end_47:
    "Конец: end_47"

label end_48:
    "Конец: end_48"

label end_53:
    "Конец: end_53"

label end_54:
    "Конец: end_54"

label end_55:
    "Конец: end_55"

label end_56:
    "Конец: end_56"

label end_60:
    "Конец: end_60"

label end_60:
    "Конец: end_60"

label end_62:
    "Конец: end_62"

label end_63:
    "Конец: end_63"
