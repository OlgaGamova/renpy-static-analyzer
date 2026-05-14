label start:
    $ strength = 0
    $ intelligence = 0
    $ luck = 0
    $ charisma = 0

    menu:
        "Go back":
            $ strength += 2
            jump label_0
        "Go forward":
            jump label_1

label label_0:
    "Scene label_0"
    if charisma >= 16:
        jump label_2

label label_2:
    $ charisma += 4
    menu:
        "Use item":
            $ intelligence += 2
            jump label_3
        "Explore":
            $ strength += 2
            jump label_4

label label_3:
    "Scene label_3"
    menu:
        "Explore":
            jump label_5
        "Look around":
            jump label_6
        "Go back":
            $ luck += 1
            jump label_7

label label_5:
    "Scene label_5"
    if charisma >= 16:
        jump label_8

label label_8:
    $ charisma += 4
    menu:
        "Open door":
            jump label_9
        "Use item":
            $ charisma += 1
            jump label_10

label label_9:
    "Scene label_9"
    menu:
        "Explore":
            $ luck += 3
            jump label_11
        "Explore":
            jump label_12

label label_11:
    "Scene label_11"
    if luck >= 14:
        jump label_13

label label_13:
    $ luck += 5
    jump end_14

    jump label_14

label label_14:
    "Ветка false для label_13"
    jump end_15

label label_12:
    "Scene label_12"
    menu:
        "Talk":
            $ charisma += 3
            jump label_15
        "Talk":
            jump label_16
        "Go back":
            $ strength += 2
            jump label_17

label label_15:
    "Scene label_15"
    jump end_18

label label_16:
    "Scene label_16"
    jump end_18

label label_17:
    "Scene label_17"
    jump end_18

label label_10:
    "Scene label_10"
    if charisma >= 15:
        jump label_18

label label_18:
    $ charisma += 5
    menu:
        "Pick up item":
            jump label_19
        "Talk":
            jump label_20

label label_19:
    "Scene label_19"
    jump end_21

label label_20:
    "Scene label_20"
    jump end_21

    jump label_21

label label_21:
    "Ветка false для label_18"
    if luck >= 7:
        jump label_22

label label_22:
    $ luck += 3
    jump end_23

    jump label_23

label label_23:
    "Ветка false для label_22"
    jump end_24

    jump label_24

label label_24:
    "Ветка false для label_8"
    menu:
        "Use item":
            $ strength += 1
            jump label_25
        "Pick up item":
            jump label_26

label label_25:
    "Scene label_25"
    menu:
        "Open door":
            jump label_27
        "Use item":
            jump label_28
        "Open door":
            $ intelligence += 1
            jump label_29

label label_27:
    "Scene label_27"
    menu:
        "Look around":
            jump label_30
        "Use item":
            $ charisma += 1
            jump label_31

label label_30:
    "Scene label_30"
    jump end_32

label label_31:
    "Scene label_31"
    jump end_32

label label_28:
    "Scene label_28"
    menu:
        "Pick up item":
            $ charisma += 3
            jump label_32
        "Explore":
            jump label_33

label label_32:
    "Scene label_32"
    jump end_34

label label_33:
    "Scene label_33"
    jump end_34

label label_29:
    "Scene label_29"
    menu:
        "Pick up item":
            jump label_34
        "Pick up item":
            $ intelligence += 3
            jump label_35
        "Go back":
            jump label_36

label label_34:
    "Scene label_34"
    jump end_37

label label_35:
    "Scene label_35"
    jump end_37

label label_36:
    "Scene label_36"
    jump end_37

label label_26:
    "Scene label_26"
    menu:
        "Go back":
            $ luck += 1
            jump label_37
        "Go back":
            $ strength += 1
            jump label_38

label label_37:
    "Scene label_37"
    if charisma >= 9:
        jump label_39

label label_39:
    $ charisma += 3
    jump end_40

    jump label_40

label label_40:
    "Ветка false для label_39"
    jump end_41

label label_38:
    "Scene label_38"
    if charisma >= 15:
        jump label_41

label label_41:
    $ charisma += 5
    jump end_42

    jump label_42

label label_42:
    "Ветка false для label_41"
    jump end_43

label label_6:
    "Scene label_6"
    menu:
        "Open door":
            $ strength += 3
            jump label_43
        "Open door":
            $ luck += 2
            jump label_44

label label_43:
    "Scene label_43"
    menu:
        "Use item":
            $ luck += 2
            jump label_45
        "Pick up item":
            $ luck += 3
            jump label_46
        "Open door":
            jump label_47

label label_45:
    "Scene label_45"
    menu:
        "Go forward":
            jump label_48
        "Go forward":
            $ charisma += 1
            jump label_49

label label_48:
    "Scene label_48"
    menu:
        "Go forward":
            $ luck += 1
            jump label_50
        "Pick up item":
            $ charisma += 2
            jump label_51

label label_50:
    "Scene label_50"
    jump end_52

label label_51:
    "Scene label_51"
    jump end_52

label label_49:
    "Scene label_49"
    menu:
        "Go back":
            jump label_52
        "Pick up item":
            $ strength += 2
            jump label_53
        "Use item":
            jump label_54

label label_52:
    "Scene label_52"
    jump end_55

label label_53:
    "Scene label_53"
    jump end_55

label label_54:
    "Scene label_54"
    jump end_55

label label_46:
    "Scene label_46"
    menu:
        "Go forward":
            jump label_55
        "Use item":
            jump label_56

label label_55:
    "Scene label_55"
    menu:
        "Talk":
            $ strength += 3
            jump label_57
        "Use item":
            $ luck += 2
            jump label_58

label label_57:
    "Scene label_57"
    jump end_59

label label_58:
    "Scene label_58"
    jump end_59

label label_56:
    "Scene label_56"
    if strength >= 10:
        jump label_59

label label_59:
    $ strength += 4
    jump end_60

    jump label_60

label label_60:
    "Ветка false для label_59"
    jump end_61

label label_47:
    "Scene label_47"
    if strength >= 14:
        jump label_61

label label_61:
    $ strength += 5
    menu:
        "Look around":
            jump label_62
        "Use item":
            $ luck += 3
            jump label_63

label label_62:
    "Scene label_62"
    jump end_64

label label_63:
    "Scene label_63"
    jump end_64

    jump label_64

label label_64:
    "Ветка false для label_61"
    menu:
        "Go forward":
            $ charisma += 3
            jump label_65
        "Explore":
            $ luck += 1
            jump label_66

label label_65:
    "Scene label_65"
    jump end_67

label label_66:
    "Scene label_66"
    jump end_67

label label_44:
    "Scene label_44"
    menu:
        "Look around":
            $ luck += 3
            jump label_67
        "Pick up item":
            jump label_68
        "Open door":
            $ luck += 3
            jump label_69

label label_67:
    "Scene label_67"
    menu:
        "Pick up item":
            $ luck += 2
            jump label_70
        "Use item":
            jump label_71
        "Look around":
            $ charisma += 1
            jump label_72

label label_70:
    "Scene label_70"
    menu:
        "Explore":
            $ luck += 1
            jump label_73
        "Pick up item":
            $ luck += 2
            jump label_74
        "Go back":
            jump label_75

label label_73:
    "Scene label_73"
    jump end_76

label label_74:
    "Scene label_74"
    jump end_76

label label_75:
    "Scene label_75"
    jump end_76

label label_71:
    "Scene label_71"
    menu:
        "Go forward":
            jump label_76
        "Use item":
            $ charisma += 2
            jump label_77
        "Use item":
            jump label_78

label label_76:
    "Scene label_76"
    jump end_79

label label_77:
    "Scene label_77"
    jump end_79

label label_78:
    "Scene label_78"
    jump end_79

label label_72:
    "Scene label_72"
    menu:
        "Pick up item":
            jump label_79
        "Look around":
            $ charisma += 3
            jump label_80
        "Use item":
            $ luck += 2
            jump label_81

label label_79:
    "Scene label_79"
    jump end_82

label label_80:
    "Scene label_80"
    jump end_82

label label_81:
    "Scene label_81"
    jump end_82

label label_68:
    "Scene label_68"
    menu:
        "Open door":
            jump label_82
        "Explore":
            $ charisma += 2
            jump label_83
        "Go back":
            $ strength += 3
            jump label_84

label label_82:
    "Scene label_82"
    if strength >= 10:
        jump label_85

label label_85:
    $ strength += 3
    jump end_86

    jump label_86

label label_86:
    "Ветка false для label_85"
    jump end_87

label label_83:
    "Scene label_83"
    if charisma >= 13:
        jump label_87

label label_87:
    $ charisma += 4
    jump end_88

    jump label_88

label label_88:
    "Ветка false для label_87"
    jump end_89

label label_84:
    "Scene label_84"
    menu:
        "Go back":
            $ intelligence += 2
            jump label_89
        "Go forward":
            jump label_90

label label_89:
    "Scene label_89"
    jump end_91

label label_90:
    "Scene label_90"
    jump end_91

label label_69:
    "Scene label_69"
    if strength >= 6:
        jump label_91

label label_91:
    $ strength += 4
    menu:
        "Pick up item":
            $ strength += 3
            jump label_92
        "Go back":
            $ charisma += 2
            jump label_93

label label_92:
    "Scene label_92"
    jump end_94

label label_93:
    "Scene label_93"
    jump end_94

    jump label_94

label label_94:
    "Ветка false для label_91"
    if strength >= 13:
        jump label_95

label label_95:
    $ strength += 5
    jump end_96

    jump label_96

label label_96:
    "Ветка false для label_95"
    jump end_97

label label_7:
    "Scene label_7"
    if strength >= 17:
        jump label_97

label label_97:
    $ strength += 5
    if strength >= 9:
        jump label_98

label label_98:
    $ strength += 3
    menu:
        "Look around":
            jump label_99
        "Look around":
            jump label_100
        "Open door":
            jump label_101

label label_99:
    "Scene label_99"
    menu:
        "Open door":
            $ charisma += 2
            jump label_102
        "Open door":
            $ strength += 3
            jump label_103

label label_102:
    "Scene label_102"
    jump end_104

label label_103:
    "Scene label_103"
    jump end_104

label label_100:
    "Scene label_100"
    menu:
        "Use item":
            jump label_104
        "Go back":
            jump label_105

label label_104:
    "Scene label_104"
    jump end_106

label label_105:
    "Scene label_105"
    jump end_106

label label_101:
    "Scene label_101"
    if intelligence >= 7:
        jump label_106

label label_106:
    $ intelligence += 3
    jump end_107

    jump label_107

label label_107:
    "Ветка false для label_106"
    jump end_108

    jump label_108

label label_108:
    "Ветка false для label_98"
    if charisma >= 20:
        jump label_109

label label_109:
    $ charisma += 4
    if luck >= 14:
        jump label_110

label label_110:
    $ luck += 5
    jump end_111

    jump label_111

label label_111:
    "Ветка false для label_110"
    jump end_112

    jump label_112

label label_112:
    "Ветка false для label_109"
    if intelligence >= 13:
        jump label_113

label label_113:
    $ intelligence += 3
    jump end_114

    jump label_114

label label_114:
    "Ветка false для label_113"
    jump end_115

    jump label_115

label label_115:
    "Ветка false для label_97"
    menu:
        "Talk":
            jump label_116
        "Talk":
            $ intelligence += 2
            jump label_117

label label_116:
    "Scene label_116"
    menu:
        "Pick up item":
            $ luck += 3
            jump label_118
        "Open door":
            jump label_119
        "Pick up item":
            $ strength += 2
            jump label_120

label label_118:
    "Scene label_118"
    menu:
        "Go forward":
            $ strength += 3
            jump label_121
        "Go back":
            jump label_122
        "Talk":
            $ charisma += 2
            jump label_123

label label_121:
    "Scene label_121"
    jump end_124

label label_122:
    "Scene label_122"
    jump end_124

label label_123:
    "Scene label_123"
    jump end_124

label label_119:
    "Scene label_119"
    if charisma >= 20:
        jump label_124

label label_124:
    $ charisma += 2
    jump end_125

    jump label_125

label label_125:
    "Ветка false для label_124"
    jump end_126

label label_120:
    "Scene label_120"
    menu:
        "Explore":
            $ strength += 1
            jump label_126
        "Explore":
            $ charisma += 2
            jump label_127
        "Open door":
            jump label_128

label label_126:
    "Scene label_126"
    jump end_129

label label_127:
    "Scene label_127"
    jump end_129

label label_128:
    "Scene label_128"
    jump end_129

label label_117:
    "Scene label_117"
    menu:
        "Look around":
            $ luck += 1
            jump label_129
        "Open door":
            jump label_130
        "Go forward":
            jump label_131

label label_129:
    "Scene label_129"
    menu:
        "Go forward":
            $ luck += 3
            jump label_132
        "Pick up item":
            jump label_133
        "Go forward":
            $ intelligence += 2
            jump label_134

label label_132:
    "Scene label_132"
    jump end_135

label label_133:
    "Scene label_133"
    jump end_135

label label_134:
    "Scene label_134"
    jump end_135

label label_130:
    "Scene label_130"
    menu:
        "Look around":
            $ intelligence += 3
            jump label_135
        "Talk":
            $ strength += 3
            jump label_136
        "Open door":
            $ strength += 2
            jump label_137

label label_135:
    "Scene label_135"
    jump end_138

label label_136:
    "Scene label_136"
    jump end_138

label label_137:
    "Scene label_137"
    jump end_138

label label_131:
    "Scene label_131"
    menu:
        "Pick up item":
            jump label_138
        "Go back":
            jump label_139

label label_138:
    "Scene label_138"
    jump end_140

label label_139:
    "Scene label_139"
    jump end_140

label label_4:
    "Scene label_4"
    if charisma >= 20:
        jump label_140

label label_140:
    $ charisma += 3
    menu:
        "Open door":
            $ intelligence += 1
            jump label_141
        "Go back":
            jump label_142

label label_141:
    "Scene label_141"
    menu:
        "Go back":
            jump label_143
        "Go back":
            jump label_144
        "Pick up item":
            jump label_145

label label_143:
    "Scene label_143"
    menu:
        "Explore":
            $ charisma += 2
            jump label_146
        "Explore":
            jump label_147
        "Use item":
            jump label_148

label label_146:
    "Scene label_146"
    if charisma >= 6:
        jump label_149

label label_149:
    $ charisma += 4
    jump end_150

    jump label_150

label label_150:
    "Ветка false для label_149"
    jump end_151

label label_147:
    "Scene label_147"
    menu:
        "Open door":
            jump label_151
        "Talk":
            $ strength += 1
            jump label_152
        "Explore":
            jump label_153

label label_151:
    "Scene label_151"
    jump end_154

label label_152:
    "Scene label_152"
    jump end_154

label label_153:
    "Scene label_153"
    jump end_154

label label_148:
    "Scene label_148"
    menu:
        "Look around":
            jump label_154
        "Pick up item":
            $ intelligence += 2
            jump label_155
        "Talk":
            $ luck += 2
            jump label_156

label label_154:
    "Scene label_154"
    jump end_157

label label_155:
    "Scene label_155"
    jump end_157

label label_156:
    "Scene label_156"
    jump end_157

label label_144:
    "Scene label_144"
    menu:
        "Look around":
            jump label_157
        "Open door":
            jump label_158
        "Pick up item":
            jump label_159

label label_157:
    "Scene label_157"
    if strength >= 12:
        jump label_160

label label_160:
    $ strength += 4
    jump end_161

    jump label_161

label label_161:
    "Ветка false для label_160"
label label_158:
    "Scene label_158"
label label_159:
    "Scene label_159"
label label_145:
    "Scene label_145"
label label_142:
    "Scene label_142"
label label_1:
    "Scene label_1"

label end_14:
    "Конец: end_14"

label end_15:
    "Конец: end_15"

label end_18:
    "Конец: end_18"

label end_18:
    "Конец: end_18"

label end_18:
    "Конец: end_18"

label end_21:
    "Конец: end_21"

label end_21:
    "Конец: end_21"

label end_23:
    "Конец: end_23"

label end_24:
    "Конец: end_24"

label end_32:
    "Конец: end_32"

label end_32:
    "Конец: end_32"

label end_34:
    "Конец: end_34"

label end_34:
    "Конец: end_34"

label end_37:
    "Конец: end_37"

label end_37:
    "Конец: end_37"

label end_37:
    "Конец: end_37"

label end_40:
    "Конец: end_40"

label end_41:
    "Конец: end_41"

label end_42:
    "Конец: end_42"

label end_43:
    "Конец: end_43"

label end_52:
    "Конец: end_52"

label end_52:
    "Конец: end_52"

label end_55:
    "Конец: end_55"

label end_55:
    "Конец: end_55"

label end_55:
    "Конец: end_55"

label end_59:
    "Конец: end_59"

label end_59:
    "Конец: end_59"

label end_60:
    "Конец: end_60"

label end_61:
    "Конец: end_61"

label end_64:
    "Конец: end_64"

label end_64:
    "Конец: end_64"

label end_67:
    "Конец: end_67"

label end_67:
    "Конец: end_67"

label end_76:
    "Конец: end_76"

label end_76:
    "Конец: end_76"

label end_76:
    "Конец: end_76"

label end_79:
    "Конец: end_79"

label end_79:
    "Конец: end_79"

label end_79:
    "Конец: end_79"

label end_82:
    "Конец: end_82"

label end_82:
    "Конец: end_82"

label end_82:
    "Конец: end_82"

label end_86:
    "Конец: end_86"

label end_87:
    "Конец: end_87"

label end_88:
    "Конец: end_88"

label end_89:
    "Конец: end_89"

label end_91:
    "Конец: end_91"

label end_91:
    "Конец: end_91"

label end_94:
    "Конец: end_94"

label end_94:
    "Конец: end_94"

label end_96:
    "Конец: end_96"

label end_97:
    "Конец: end_97"

label end_104:
    "Конец: end_104"

label end_104:
    "Конец: end_104"

label end_106:
    "Конец: end_106"

label end_106:
    "Конец: end_106"

label end_107:
    "Конец: end_107"

label end_108:
    "Конец: end_108"

label end_111:
    "Конец: end_111"

label end_112:
    "Конец: end_112"

label end_114:
    "Конец: end_114"

label end_115:
    "Конец: end_115"

label end_124:
    "Конец: end_124"

label end_124:
    "Конец: end_124"

label end_124:
    "Конец: end_124"

label end_125:
    "Конец: end_125"

label end_126:
    "Конец: end_126"

label end_129:
    "Конец: end_129"

label end_129:
    "Конец: end_129"

label end_129:
    "Конец: end_129"

label end_135:
    "Конец: end_135"

label end_135:
    "Конец: end_135"

label end_135:
    "Конец: end_135"

label end_138:
    "Конец: end_138"

label end_138:
    "Конец: end_138"

label end_138:
    "Конец: end_138"

label end_140:
    "Конец: end_140"

label end_140:
    "Конец: end_140"

label end_150:
    "Конец: end_150"

label end_151:
    "Конец: end_151"

label end_154:
    "Конец: end_154"

label end_154:
    "Конец: end_154"

label end_154:
    "Конец: end_154"

label end_157:
    "Конец: end_157"

label end_157:
    "Конец: end_157"

label end_157:
    "Конец: end_157"

label end_161:
    "Конец: end_161"
