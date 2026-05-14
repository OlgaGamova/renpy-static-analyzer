label start:
    $ strength = 0
    $ intelligence = 0
    $ luck = 0
    $ charisma = 0

    if charisma >= 15:
        jump label_0

label label_0:
    $ charisma += 3
    if strength >= 18:
        jump label_1

label label_1:
    $ strength += 4
    menu:
        "Explore":
            $ intelligence += 3
            jump label_2
        "Go forward":
            jump label_3

label label_2:
    "Scene label_2"
    menu:
        "Use item":
            jump label_4
        "Open door":
            jump label_5

label label_4:
    "Scene label_4"
    if strength >= 7:
        jump label_6

label label_6:
    $ strength += 5
    if intelligence >= 6:
        jump label_7

label label_7:
    $ intelligence += 3
    menu:
        "Look around":
            $ intelligence += 1
            jump label_8
        "Look around":
            $ charisma += 2
            jump label_9

label label_8:
    "Scene label_8"
    if intelligence >= 12:
        jump label_10

label label_10:
    $ intelligence += 5
    if intelligence >= 14:
        jump label_11

label label_11:
    $ intelligence += 4
    menu:
        "Use item":
            $ charisma += 1
            jump label_12
        "Explore":
            $ intelligence += 2
            jump label_13
        "Pick up item":
            $ charisma += 1
            jump label_14
        "Pick up item":
            $ charisma += 2
            jump label_15

label label_12:
    "Scene label_12"
    menu:
        "Talk":
            jump label_16
        "Talk":
            $ charisma += 2
            jump label_17
        "Pick up item":
            $ charisma += 1
            jump label_18

label label_16:
    "Scene label_16"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_19
        "Go forward":
            jump label_20
        "Explore":
            $ charisma += 2
            jump label_21
        "Explore":
            $ luck += 3
            jump label_22

label label_19:
    "Scene label_19"
    menu:
        "Open door":
            jump label_23
        "Look around":
            $ intelligence += 1
            jump label_24

label label_23:
    "Scene label_23"
    menu:
        "Explore":
            jump label_25
        "Pick up item":
            jump label_26
        "Explore":
            jump label_27

label label_25:
    "Scene label_25"
    menu:
        "Use item":
            $ strength += 2
            jump label_28
        "Go forward":
            jump label_29
        "Talk":
            $ charisma += 3
            jump label_30

label label_28:
    "Scene label_28"
    if intelligence >= 10:
        jump label_31

label label_31:
    $ intelligence += 2
    if strength >= 17:
        jump label_32

label label_32:
    $ strength += 5
    menu:
        "Use item":
            jump label_33
        "Talk":
            jump label_34

label label_33:
    "Scene label_33"
    jump end_35

label label_34:
    "Scene label_34"
    jump end_35

    jump label_35

label label_35:
    "Ветка false для label_32"
    if luck >= 17:
        jump label_36

label label_36:
    $ luck += 4
    jump end_37

    jump label_37

label label_37:
    "Ветка false для label_36"
    jump end_38

    jump label_38

label label_38:
    "Ветка false для label_31"
    menu:
        "Look around":
            $ luck += 1
            jump label_39
        "Go back":
            jump label_40
        "Open door":
            jump label_41
        "Go forward":
            jump label_42

label label_39:
    "Scene label_39"
    menu:
        "Look around":
            $ charisma += 3
            jump label_43
        "Open door":
            jump label_44

label label_43:
    "Scene label_43"
    jump end_45

label label_44:
    "Scene label_44"
    jump end_45

label label_40:
    "Scene label_40"
    menu:
        "Talk":
            $ intelligence += 1
            jump label_45
        "Pick up item":
            $ strength += 2
            jump label_46

label label_45:
    "Scene label_45"
    jump end_47

label label_46:
    "Scene label_46"
    jump end_47

label label_41:
    "Scene label_41"
    menu:
        "Talk":
            $ intelligence += 1
            jump label_47
        "Go back":
            jump label_48

label label_47:
    "Scene label_47"
    jump end_49

label label_48:
    "Scene label_48"
    jump end_49

label label_42:
    "Scene label_42"
    menu:
        "Look around":
            jump label_49
        "Talk":
            $ strength += 2
            jump label_50
        "Look around":
            $ luck += 1
            jump label_51

label label_49:
    "Scene label_49"
    jump end_52

label label_50:
    "Scene label_50"
    jump end_52

label label_51:
    "Scene label_51"
    jump end_52

label label_29:
    "Scene label_29"
    menu:
        "Pick up item":
            jump label_52
        "Look around":
            $ luck += 1
            jump label_53
        "Go forward":
            $ strength += 2
            jump label_54

label label_52:
    "Scene label_52"
    menu:
        "Pick up item":
            $ luck += 3
            jump label_55
        "Open door":
            $ luck += 2
            jump label_56
        "Use item":
            jump label_57

label label_55:
    "Scene label_55"
    menu:
        "Go forward":
            jump label_58
        "Explore":
            jump label_59
        "Go forward":
            $ charisma += 3
            jump label_60

label label_58:
    "Scene label_58"
    jump end_61

label label_59:
    "Scene label_59"
    jump end_61

label label_60:
    "Scene label_60"
    jump end_61

label label_56:
    "Scene label_56"
    menu:
        "Go forward":
            jump label_61
        "Go back":
            jump label_62

label label_61:
    "Scene label_61"
    jump end_63

label label_62:
    "Scene label_62"
    jump end_63

label label_57:
    "Scene label_57"
    menu:
        "Explore":
            $ charisma += 3
            jump label_63
        "Open door":
            jump label_64

label label_63:
    "Scene label_63"
    jump end_65

label label_64:
    "Scene label_64"
    jump end_65

label label_53:
    "Scene label_53"
    if luck >= 5:
        jump label_65

label label_65:
    $ luck += 4
    menu:
        "Explore":
            jump label_66
        "Use item":
            jump label_67
        "Open door":
            jump label_68
        "Look around":
            $ charisma += 3
            jump label_69

label label_66:
    "Scene label_66"
    jump end_70

label label_67:
    "Scene label_67"
    jump end_70

label label_68:
    "Scene label_68"
    jump end_70

label label_69:
    "Scene label_69"
    jump end_70

    jump label_70

label label_70:
    "Ветка false для label_65"
    menu:
        "Open door":
            $ intelligence += 3
            jump label_71
        "Talk":
            jump label_72

label label_71:
    "Scene label_71"
    jump end_73

label label_72:
    "Scene label_72"
    jump end_73

label label_54:
    "Scene label_54"
    menu:
        "Go forward":
            $ strength += 2
            jump label_73
        "Pick up item":
            $ charisma += 1
            jump label_74
        "Pick up item":
            jump label_75
        "Use item":
            $ intelligence += 3
            jump label_76

label label_73:
    "Scene label_73"
    menu:
        "Open door":
            jump label_77
        "Go forward":
            $ luck += 2
            jump label_78

label label_77:
    "Scene label_77"
    jump end_79

label label_78:
    "Scene label_78"
    jump end_79

label label_74:
    "Scene label_74"
    menu:
        "Go back":
            jump label_79
        "Look around":
            jump label_80

label label_79:
    "Scene label_79"
    jump end_81

label label_80:
    "Scene label_80"
    jump end_81

label label_75:
    "Scene label_75"
    menu:
        "Pick up item":
            $ luck += 1
            jump label_81
        "Look around":
            jump label_82
        "Open door":
            jump label_83
        "Open door":
            jump label_84

label label_81:
    "Scene label_81"
    jump end_85

label label_82:
    "Scene label_82"
    jump end_85

label label_83:
    "Scene label_83"
    jump end_85

label label_84:
    "Scene label_84"
    jump end_85

label label_76:
    "Scene label_76"
    menu:
        "Use item":
            $ strength += 2
            jump label_85
        "Look around":
            $ luck += 3
            jump label_86
        "Use item":
            jump label_87

label label_85:
    "Scene label_85"
    jump end_88

label label_86:
    "Scene label_86"
    jump end_88

label label_87:
    "Scene label_87"
    jump end_88

label label_30:
    "Scene label_30"
    if luck >= 9:
        jump label_88

label label_88:
    $ luck += 4
    menu:
        "Go forward":
            $ intelligence += 2
            jump label_89
        "Open door":
            $ luck += 3
            jump label_90
        "Talk":
            jump label_91
        "Use item":
            $ strength += 3
            jump label_92

label label_89:
    "Scene label_89"
    menu:
        "Talk":
            jump label_93
        "Go back":
            jump label_94
        "Pick up item":
            jump label_95

label label_93:
    "Scene label_93"
    jump end_96

label label_94:
    "Scene label_94"
    jump end_96

label label_95:
    "Scene label_95"
    jump end_96

label label_90:
    "Scene label_90"
    if luck >= 9:
        jump label_96

label label_96:
    $ luck += 2
    jump end_97

    jump label_97

label label_97:
    "Ветка false для label_96"
    jump end_98

label label_91:
    "Scene label_91"
    menu:
        "Look around":
            $ charisma += 3
            jump label_98
        "Use item":
            $ charisma += 1
            jump label_99
        "Explore":
            $ intelligence += 3
            jump label_100

label label_98:
    "Scene label_98"
    jump end_101

label label_99:
    "Scene label_99"
    jump end_101

label label_100:
    "Scene label_100"
    jump end_101

label label_92:
    "Scene label_92"
    menu:
        "Go forward":
            jump label_101
        "Talk":
            jump label_102

label label_101:
    "Scene label_101"
    jump end_103

label label_102:
    "Scene label_102"
    jump end_103

    jump label_103

label label_103:
    "Ветка false для label_88"
    menu:
        "Talk":
            jump label_104
        "Open door":
            $ charisma += 2
            jump label_105
        "Open door":
            $ luck += 2
            jump label_106

label label_104:
    "Scene label_104"
    menu:
        "Open door":
            $ luck += 3
            jump label_107
        "Go forward":
            jump label_108

label label_107:
    "Scene label_107"
    jump end_109

label label_108:
    "Scene label_108"
    jump end_109

label label_105:
    "Scene label_105"
    menu:
        "Talk":
            jump label_109
        "Pick up item":
            jump label_110
        "Go back":
            jump label_111

label label_109:
    "Scene label_109"
    jump end_112

label label_110:
    "Scene label_110"
    jump end_112

label label_111:
    "Scene label_111"
    jump end_112

label label_106:
    "Scene label_106"
    if intelligence >= 5:
        jump label_112

label label_112:
    $ intelligence += 4
    jump end_113

    jump label_113

label label_113:
    "Ветка false для label_112"
    jump end_114

label label_26:
    "Scene label_26"
    menu:
        "Look around":
            jump label_114
        "Talk":
            $ charisma += 3
            jump label_115
        "Talk":
            jump label_116
        "Look around":
            $ charisma += 1
            jump label_117

label label_114:
    "Scene label_114"
    menu:
        "Explore":
            jump label_118
        "Talk":
            jump label_119

label label_118:
    "Scene label_118"
    menu:
        "Look around":
            $ charisma += 2
            jump label_120
        "Talk":
            jump label_121

label label_120:
    "Scene label_120"
    menu:
        "Look around":
            jump label_122
        "Open door":
            $ charisma += 2
            jump label_123
        "Go forward":
            $ strength += 1
            jump label_124
        "Pick up item":
            jump label_125

label label_122:
    "Scene label_122"
    jump end_126

label label_123:
    "Scene label_123"
    jump end_126

label label_124:
    "Scene label_124"
    jump end_126

label label_125:
    "Scene label_125"
    jump end_126

label label_121:
    "Scene label_121"
    menu:
        "Go forward":
            jump label_126
        "Pick up item":
            $ strength += 3
            jump label_127

label label_126:
    "Scene label_126"
    jump end_128

label label_127:
    "Scene label_127"
    jump end_128

label label_119:
    "Scene label_119"
    if charisma >= 18:
        jump label_128

label label_128:
    $ charisma += 4
    menu:
        "Explore":
            $ intelligence += 2
            jump label_129
        "Go forward":
            $ charisma += 1
            jump label_130

label label_129:
    "Scene label_129"
    jump end_131

label label_130:
    "Scene label_130"
    jump end_131

    jump label_131

label label_131:
    "Ветка false для label_128"
    menu:
        "Look around":
            jump label_132
        "Use item":
            jump label_133
        "Look around":
            $ intelligence += 1
            jump label_134
        "Pick up item":
            jump label_135

label label_132:
    "Scene label_132"
    jump end_136

label label_133:
    "Scene label_133"
    jump end_136

label label_134:
    "Scene label_134"
    jump end_136

label label_135:
    "Scene label_135"
    jump end_136

label label_115:
    "Scene label_115"
    if intelligence >= 11:
        jump label_136

label label_136:
    $ intelligence += 3
    if luck >= 6:
        jump label_137

label label_137:
    $ luck += 2
    menu:
        "Go back":
            $ intelligence += 2
            jump label_138
        "Go forward":
            $ strength += 3
            jump label_139
        "Go back":
            jump label_140
        "Pick up item":
            $ charisma += 3
            jump label_141

label label_138:
    "Scene label_138"
    jump end_142

label label_139:
    "Scene label_139"
    jump end_142

label label_140:
    "Scene label_140"
    jump end_142

label label_141:
    "Scene label_141"
    jump end_142

    jump label_142

label label_142:
    "Ветка false для label_137"
    menu:
        "Use item":
            jump label_143
        "Go forward":
            $ intelligence += 1
            jump label_144
        "Go back":
            jump label_145

label label_143:
    "Scene label_143"
    jump end_146

label label_144:
    "Scene label_144"
    jump end_146

label label_145:
    "Scene label_145"
    jump end_146

    jump label_146

label label_146:
    "Ветка false для label_136"
    if intelligence >= 11:
        jump label_147

label label_147:
    $ intelligence += 4
    if charisma >= 7:
        jump label_148

label label_148:
    $ charisma += 4
    jump end_149

    jump label_149

label label_149:
    "Ветка false для label_148"
    jump end_150

    jump label_150

label label_150:
    "Ветка false для label_147"
    if intelligence >= 17:
        jump label_151

label label_151:
    $ intelligence += 5
    jump end_152

    jump label_152

label label_152:
    "Ветка false для label_151"
    jump end_153

label label_116:
    "Scene label_116"
    if luck >= 18:
        jump label_153

label label_153:
    $ luck += 3
    menu:
        "Go back":
            jump label_154
        "Use item":
            jump label_155

label label_154:
    "Scene label_154"
    menu:
        "Talk":
            $ intelligence += 2
            jump label_156
        "Open door":
            $ intelligence += 1
            jump label_157
        "Go back":
            $ strength += 3
            jump label_158
        "Open door":
            $ strength += 2
            jump label_159

label label_156:
    "Scene label_156"
    jump end_160

label label_157:
    "Scene label_157"
    jump end_160

label label_158:
    "Scene label_158"
    jump end_160

label label_159:
    "Scene label_159"
    jump end_160

label label_155:
    "Scene label_155"
    menu:
        "Talk":
            jump label_160
        "Use item":
            $ strength += 2
            jump label_161
        "Use item":
            $ strength += 1
            jump label_162

label label_160:
    "Scene label_160"
    jump end_163

label label_161:
    "Scene label_161"
    jump end_163

label label_162:
    "Scene label_162"
    jump end_163

    jump label_163

label label_163:
    "Ветка false для label_153"
    if luck >= 20:
        jump label_164

label label_164:
    $ luck += 2
    menu:
        "Go back":
            jump label_165
        "Look around":
            jump label_166
        "Talk":
            $ charisma += 1
            jump label_167
        "Explore":
            jump label_168

label label_165:
    "Scene label_165"
    jump end_169

label label_166:
    "Scene label_166"
    jump end_169

label label_167:
    "Scene label_167"
    jump end_169

label label_168:
    "Scene label_168"
    jump end_169

    jump label_169

label label_169:
    "Ветка false для label_164"
    menu:
        "Open door":
            $ intelligence += 2
            jump label_170
        "Go forward":
            jump label_171
        "Talk":
            jump label_172
        "Talk":
            $ luck += 1
            jump label_173

label label_170:
    "Scene label_170"
    jump end_174

label label_171:
    "Scene label_171"
    jump end_174

label label_172:
    "Scene label_172"
    jump end_174

label label_173:
    "Scene label_173"
    jump end_174

label label_117:
    "Scene label_117"
    menu:
        "Explore":
            jump label_174
        "Use item":
            jump label_175
        "Open door":
            jump label_176
        "Talk":
            $ luck += 2
            jump label_177

label label_174:
    "Scene label_174"
    menu:
        "Open door":
            jump label_178
        "Use item":
            $ strength += 2
            jump label_179
        "Open door":
            jump label_180

label label_178:
    "Scene label_178"
    menu:
        "Look around":
            $ intelligence += 1
            jump label_181
        "Talk":
            jump label_182
        "Look around":
            jump label_183
        "Pick up item":
            jump label_184

label label_181:
    "Scene label_181"
    jump end_185

label label_182:
    "Scene label_182"
    jump end_185

label label_183:
    "Scene label_183"
    jump end_185

label label_184:
    "Scene label_184"
    jump end_185

label label_179:
    "Scene label_179"
    if charisma >= 9:
        jump label_185

label label_185:
    $ charisma += 5
    jump end_186

    jump label_186

label label_186:
    "Ветка false для label_185"
    jump end_187

label label_180:
    "Scene label_180"
    menu:
        "Look around":
            $ intelligence += 3
            jump label_187
        "Go forward":
            jump label_188
        "Explore":
            $ strength += 3
            jump label_189
        "Pick up item":
            jump label_190

label label_187:
    "Scene label_187"
    jump end_191

label label_188:
    "Scene label_188"
    jump end_191

label label_189:
    "Scene label_189"
    jump end_191

label label_190:
    "Scene label_190"
    jump end_191

label label_175:
    "Scene label_175"
    menu:
        "Use item":
            $ luck += 1
            jump label_191
        "Explore":
            jump label_192
        "Open door":
            $ intelligence += 2
            jump label_193
        "Look around":
            $ intelligence += 3
            jump label_194

label label_191:
    "Scene label_191"
    menu:
        "Go back":
            $ luck += 2
            jump label_195
        "Use item":
            $ charisma += 1
            jump label_196

label label_195:
    "Scene label_195"
    jump end_197

label label_196:
    "Scene label_196"
    jump end_197

label label_192:
    "Scene label_192"
    menu:
        "Go forward":
            jump label_197
        "Pick up item":
            $ strength += 3
            jump label_198
        "Pick up item":
            $ luck += 1
            jump label_199
        "Go forward":
            $ intelligence += 2
            jump label_200

label label_197:
    "Scene label_197"
    jump end_201

label label_198:
    "Scene label_198"
    jump end_201

label label_199:
    "Scene label_199"
    jump end_201

label label_200:
    "Scene label_200"
    jump end_201

label label_193:
    "Scene label_193"
    menu:
        "Open door":
            $ strength += 3
            jump label_201
        "Talk":
            $ charisma += 1
            jump label_202

label label_201:
    "Scene label_201"
    jump end_203

label label_202:
    "Scene label_202"
    jump end_203

label label_194:
    "Scene label_194"
    if luck >= 12:
        jump label_203

label label_203:
    $ luck += 5
    jump end_204

    jump label_204

label label_204:
    "Ветка false для label_203"
    jump end_205

label label_176:
    "Scene label_176"
    menu:
        "Explore":
            $ intelligence += 3
            jump label_205
        "Go back":
            $ charisma += 3
            jump label_206
        "Pick up item":
            $ luck += 3
            jump label_207

label label_205:
    "Scene label_205"
    menu:
        "Use item":
            $ luck += 1
            jump label_208
        "Talk":
            $ luck += 1
            jump label_209
        "Talk":
            jump label_210

label label_208:
    "Scene label_208"
    jump end_211

label label_209:
    "Scene label_209"
    jump end_211

label label_210:
    "Scene label_210"
    jump end_211

label label_206:
    "Scene label_206"
    menu:
        "Go back":
            $ charisma += 3
            jump label_211
        "Pick up item":
            jump label_212
        "Talk":
            $ charisma += 3
            jump label_213
        "Open door":
            $ strength += 1
            jump label_214

label label_211:
    "Scene label_211"
    jump end_215

label label_212:
    "Scene label_212"
    jump end_215

label label_213:
    "Scene label_213"
    jump end_215

label label_214:
    "Scene label_214"
    jump end_215

label label_207:
    "Scene label_207"
    if luck >= 5:
        jump label_215

label label_215:
    $ luck += 3
    jump end_216

    jump label_216

label label_216:
    "Ветка false для label_215"
    jump end_217

label label_177:
    "Scene label_177"
    if luck >= 18:
        jump label_217

label label_217:
    $ luck += 2
    menu:
        "Go back":
            $ charisma += 1
            jump label_218
        "Talk":
            jump label_219
        "Talk":
            $ strength += 2
            jump label_220

label label_218:
    "Scene label_218"
    jump end_221

label label_219:
    "Scene label_219"
    jump end_221

label label_220:
    "Scene label_220"
    jump end_221

    jump label_221

label label_221:
    "Ветка false для label_217"
    menu:
        "Open door":
            $ strength += 3
            jump label_222
        "Talk":
            $ intelligence += 1
            jump label_223

label label_222:
    "Scene label_222"
    jump end_224

label label_223:
    "Scene label_223"
    jump end_224

label label_27:
    "Scene label_27"
    if charisma >= 6:
        jump label_224

label label_224:
    $ charisma += 4
    menu:
        "Open door":
            $ intelligence += 1
            jump label_225
        "Go forward":
            $ luck += 3
            jump label_226

label label_225:
    "Scene label_225"
    menu:
        "Use item":
            $ charisma += 1
            jump label_227
        "Open door":
            jump label_228

label label_227:
    "Scene label_227"
    menu:
        "Explore":
            $ luck += 3
            jump label_229
        "Open door":
            $ strength += 1
            jump label_230
        "Go forward":
            $ luck += 1
            jump label_231

label label_229:
    "Scene label_229"
    jump end_232

label label_230:
    "Scene label_230"
    jump end_232

label label_231:
    "Scene label_231"
    jump end_232

label label_228:
    "Scene label_228"
    if luck >= 8:
        jump label_232

label label_232:
    $ luck += 5
    jump end_233

    jump label_233

label label_233:
    "Ветка false для label_232"
    jump end_234

label label_226:
    "Scene label_226"
    if charisma >= 16:
        jump label_234

label label_234:
    $ charisma += 4
    menu:
        "Go forward":
            jump label_235
        "Talk":
            $ luck += 3
            jump label_236

label label_235:
    "Scene label_235"
    jump end_237

label label_236:
    "Scene label_236"
    jump end_237

    jump label_237

label label_237:
    "Ветка false для label_234"
    menu:
        "Explore":
            $ luck += 1
            jump label_238
        "Open door":
            $ strength += 1
            jump label_239
        "Look around":
            $ intelligence += 1
            jump label_240
        "Pick up item":
            jump label_241

label label_238:
    "Scene label_238"
    jump end_242

label label_239:
    "Scene label_239"
    jump end_242

label label_240:
    "Scene label_240"
    jump end_242

label label_241:
    "Scene label_241"
    jump end_242

    jump label_242

label label_242:
    "Ветка false для label_224"
    if luck >= 14:
        jump label_243

label label_243:
    $ luck += 5
    menu:
        "Talk":
            $ intelligence += 2
            jump label_244
        "Go back":
            jump label_245

label label_244:
    "Scene label_244"
    menu:
        "Explore":
            jump label_246
        "Pick up item":
            jump label_247
        "Look around":
            jump label_248
        "Look around":
            $ strength += 1
            jump label_249

label label_246:
    "Scene label_246"
    jump end_250

label label_247:
    "Scene label_247"
    jump end_250

label label_248:
    "Scene label_248"
    jump end_250

label label_249:
    "Scene label_249"
    jump end_250

label label_245:
    "Scene label_245"
    menu:
        "Talk":
            $ strength += 3
            jump label_250
        "Use item":
            jump label_251
        "Open door":
            $ strength += 1
            jump label_252
        "Pick up item":
            jump label_253

label label_250:
    "Scene label_250"
    jump end_254

label label_251:
    "Scene label_251"
    jump end_254

label label_252:
    "Scene label_252"
    jump end_254

label label_253:
    "Scene label_253"
    jump end_254

    jump label_254

label label_254:
    "Ветка false для label_243"
    menu:
        "Open door":
            jump label_255
        "Use item":
            $ intelligence += 3
            jump label_256
        "Use item":
            jump label_257

label label_255:
    "Scene label_255"
    if charisma >= 13:
        jump label_258

label label_258:
    $ charisma += 4
    jump end_259

    jump label_259

label label_259:
    "Ветка false для label_258"
    jump end_260

label label_256:
    "Scene label_256"
    menu:
        "Go back":
            jump label_260
        "Talk":
            $ intelligence += 2
            jump label_261
        "Go forward":
            jump label_262

label label_260:
    "Scene label_260"
    jump end_263

label label_261:
    "Scene label_261"
    jump end_263

label label_262:
    "Scene label_262"
    jump end_263

label label_257:
    "Scene label_257"
    menu:
        "Talk":
            $ strength += 3
            jump label_263
        "Use item":
            jump label_264
        "Use item":
            jump label_265

label label_263:
    "Scene label_263"
    jump end_266

label label_264:
    "Scene label_264"
    jump end_266

label label_265:
    "Scene label_265"
    jump end_266

label label_24:
    "Scene label_24"
    if luck >= 16:
        jump label_266

label label_266:
    $ luck += 4
    if luck >= 9:
        jump label_267

label label_267:
    $ luck += 5
    menu:
        "Explore":
            jump label_268
        "Go forward":
            jump label_269
        "Use item":
            jump label_270

label label_268:
    "Scene label_268"
    if luck >= 5:
        jump label_271

label label_271:
    $ luck += 2
    menu:
        "Open door":
            jump label_272
        "Go back":
            jump label_273
        "Use item":
            jump label_274
        "Use item":
            $ intelligence += 3
            jump label_275

label label_272:
    "Scene label_272"
    jump end_276

label label_273:
    "Scene label_273"
    jump end_276

label label_274:
    "Scene label_274"
    jump end_276

label label_275:
    "Scene label_275"
    jump end_276

    jump label_276

label label_276:
    "Ветка false для label_271"
    menu:
        "Talk":
            $ charisma += 2
            jump label_277
        "Talk":
            jump label_278
        "Look around":
            $ charisma += 1
            jump label_279

label label_277:
    "Scene label_277"
    jump end_280

label label_278:
    "Scene label_278"
    jump end_280

label label_279:
    "Scene label_279"
    jump end_280

label label_269:
    "Scene label_269"
    menu:
        "Use item":
            jump label_280
        "Talk":
            jump label_281

label label_280:
    "Scene label_280"
    if intelligence >= 10:
        jump label_282

label label_282:
    $ intelligence += 5
    jump end_283

    jump label_283

label label_283:
    "Ветка false для label_282"
    jump end_284

label label_281:
    "Scene label_281"
    menu:
        "Look around":
            $ charisma += 1
            jump label_284
        "Pick up item":
            jump label_285

label label_284:
    "Scene label_284"
    jump end_286

label label_285:
    "Scene label_285"
    jump end_286

label label_270:
    "Scene label_270"
    menu:
        "Talk":
            jump label_286
        "Go forward":
            jump label_287

label label_286:
    "Scene label_286"
    menu:
        "Look around":
            jump label_288
        "Go forward":
            $ strength += 2
            jump label_289

label label_288:
    "Scene label_288"
    jump end_290

label label_289:
    "Scene label_289"
    jump end_290

label label_287:
    "Scene label_287"
    if strength >= 5:
        jump label_290

label label_290:
    $ strength += 2
    jump end_291

    jump label_291

label label_291:
    "Ветка false для label_290"
    jump end_292

    jump label_292

label label_292:
    "Ветка false для label_267"
    menu:
        "Look around":
            $ charisma += 3
            jump label_293
        "Pick up item":
            jump label_294
        "Go back":
            $ intelligence += 1
            jump label_295

label label_293:
    "Scene label_293"
    if luck >= 8:
        jump label_296

label label_296:
    $ luck += 2
    menu:
        "Go back":
            $ charisma += 1
            jump label_297
        "Go forward":
            jump label_298

label label_297:
    "Scene label_297"
    jump end_299

label label_298:
    "Scene label_298"
    jump end_299

    jump label_299

label label_299:
    "Ветка false для label_296"
    if charisma >= 17:
        jump label_300

label label_300:
    $ charisma += 3
    jump end_301

    jump label_301

label label_301:
    "Ветка false для label_300"
    jump end_302

label label_294:
    "Scene label_294"
    menu:
        "Use item":
            jump label_302
        "Open door":
            jump label_303
        "Look around":
            $ strength += 1
            jump label_304

label label_302:
    "Scene label_302"
    if luck >= 16:
        jump label_305

label label_305:
    $ luck += 2
    jump end_306

    jump label_306

label label_306:
    "Ветка false для label_305"
    jump end_307

label label_303:
    "Scene label_303"
    menu:
        "Explore":
            jump label_307
        "Look around":
            jump label_308

label label_307:
    "Scene label_307"
    jump end_309

label label_308:
    "Scene label_308"
    jump end_309

label label_304:
    "Scene label_304"
    menu:
        "Open door":
            jump label_309
        "Talk":
            jump label_310

label label_309:
    "Scene label_309"
    jump end_311

label label_310:
    "Scene label_310"
    jump end_311

label label_295:
    "Scene label_295"
    if luck >= 14:
        jump label_311

label label_311:
    $ luck += 4
    menu:
        "Pick up item":
            jump label_312
        "Go back":
            jump label_313
        "Look around":
            jump label_314

label label_312:
    "Scene label_312"
    jump end_315

label label_313:
    "Scene label_313"
    jump end_315

label label_314:
    "Scene label_314"
    jump end_315

    jump label_315

label label_315:
    "Ветка false для label_311"
    menu:
        "Talk":
            $ charisma += 2
            jump label_316
        "Pick up item":
            jump label_317

label label_316:
    "Scene label_316"
    jump end_318

label label_317:
    "Scene label_317"
    jump end_318

    jump label_318

label label_318:
    "Ветка false для label_266"
    if charisma >= 13:
        jump label_319

label label_319:
    $ charisma += 3
    if intelligence >= 10:
        jump label_320

label label_320:
    $ intelligence += 5
    menu:
        "Open door":
            $ charisma += 3
            jump label_321
        "Explore":
            $ intelligence += 2
            jump label_322
        "Open door":
            jump label_323

label label_321:
    "Scene label_321"
    menu:
        "Use item":
            $ charisma += 3
            jump label_324
        "Use item":
            jump label_325
        "Use item":
            $ intelligence += 1
            jump label_326

label label_324:
    "Scene label_324"
    jump end_327

label label_325:
    "Scene label_325"
    jump end_327

label label_326:
    "Scene label_326"
    jump end_327

label label_322:
    "Scene label_322"
    menu:
        "Talk":
            jump label_327
        "Go forward":
            jump label_328
        "Explore":
            jump label_329

label label_327:
    "Scene label_327"
    jump end_330

label label_328:
    "Scene label_328"
    jump end_330

label label_329:
    "Scene label_329"
    jump end_330

label label_323:
    "Scene label_323"
    menu:
        "Go back":
            $ charisma += 1
            jump label_330
        "Use item":
            jump label_331

label label_330:
    "Scene label_330"
    jump end_332

label label_331:
    "Scene label_331"
    jump end_332

    jump label_332

label label_332:
    "Ветка false для label_320"
    if intelligence >= 8:
        jump label_333

label label_333:
    $ intelligence += 3
    menu:
        "Open door":
            $ strength += 3
            jump label_334
        "Look around":
            $ intelligence += 1
            jump label_335

label label_334:
    "Scene label_334"
    jump end_336

label label_335:
    "Scene label_335"
    jump end_336

    jump label_336

label label_336:
    "Ветка false для label_333"
    if intelligence >= 7:
        jump label_337

label label_337:
    $ intelligence += 3
    jump end_338

    jump label_338

label label_338:
    "Ветка false для label_337"
    jump end_339

    jump label_339

label label_339:
    "Ветка false для label_319"
    if charisma >= 9:
        jump label_340

label label_340:
    $ charisma += 3
    menu:
        "Go back":
            $ luck += 2
            jump label_341
        "Go forward":
            $ intelligence += 1
            jump label_342

label label_341:
    "Scene label_341"
    menu:
        "Talk":
            jump label_343
        "Go forward":
            $ charisma += 3
            jump label_344

label label_343:
    "Scene label_343"
    jump end_345

label label_344:
    "Scene label_344"
    jump end_345

label label_342:
    "Scene label_342"
    menu:
        "Go back":
            jump label_345
        "Go back":
            jump label_346
        "Open door":
            jump label_347

label label_345:
    "Scene label_345"
    jump end_348

label label_346:
    "Scene label_346"
    jump end_348

label label_347:
    "Scene label_347"
    jump end_348

    jump label_348

label label_348:
    "Ветка false для label_340"
    if strength >= 17:
        jump label_349

label label_349:
    $ strength += 3
    menu:
        "Go forward":
            $ intelligence += 3
            jump label_350
        "Look around":
            jump label_351
        "Pick up item":
            $ charisma += 2
            jump label_352

label label_350:
    "Scene label_350"
    jump end_353

label label_351:
    "Scene label_351"
    jump end_353

label label_352:
    "Scene label_352"
    jump end_353

    jump label_353

label label_353:
    "Ветка false для label_349"
    if luck >= 18:
        jump label_354

label label_354:
    $ luck += 3
    jump end_355

    jump label_355

label label_355:
    "Ветка false для label_354"
    jump end_356

label label_20:
    "Scene label_20"
    if strength >= 7:
        jump label_356

label label_356:
    $ strength += 4
    menu:
        "Go forward":
            $ intelligence += 3
            jump label_357
        "Look around":
            $ strength += 2
            jump label_358
        "Use item":
            jump label_359

label label_357:
    "Scene label_357"
    menu:
        "Use item":
            $ strength += 3
            jump label_360
        "Pick up item":
            $ luck += 1
            jump label_361

label label_360:
    "Scene label_360"
    menu:
        "Explore":
            jump label_362
        "Open door":
            jump label_363

label label_362:
    "Scene label_362"
    menu:
        "Explore":
            jump label_364
        "Look around":
            $ strength += 3
            jump label_365
        "Talk":
            $ charisma += 2
            jump label_366

label label_364:
    "Scene label_364"
    menu:
        "Go back":
            $ charisma += 1
            jump label_367
        "Look around":
            jump label_368

label label_367:
    "Scene label_367"
    jump end_369

label label_368:
    "Scene label_368"
    jump end_369

label label_365:
    "Scene label_365"
    if intelligence >= 9:
        jump label_369

label label_369:
    $ intelligence += 3
    jump end_370

    jump label_370

label label_370:
    "Ветка false для label_369"
    jump end_371

label label_366:
    "Scene label_366"
    menu:
        "Explore":
            $ intelligence += 2
            jump label_371
        "Go back":
            $ charisma += 1
            jump label_372
        "Open door":
            $ strength += 1
            jump label_373
        "Pick up item":
            $ strength += 1
            jump label_374

label label_371:
    "Scene label_371"
    jump end_375

label label_372:
    "Scene label_372"
    jump end_375

label label_373:
    "Scene label_373"
    jump end_375

label label_374:
    "Scene label_374"
    jump end_375

label label_363:
    "Scene label_363"
    menu:
        "Look around":
            $ charisma += 2
            jump label_375
        "Talk":
            jump label_376
        "Talk":
            $ luck += 2
            jump label_377

label label_375:
    "Scene label_375"
    if intelligence >= 19:
        jump label_378

label label_378:
    $ intelligence += 4
    jump end_379

    jump label_379

label label_379:
    "Ветка false для label_378"
    jump end_380

label label_376:
    "Scene label_376"
    menu:
        "Pick up item":
            jump label_380
        "Talk":
            jump label_381
        "Pick up item":
            $ luck += 2
            jump label_382

label label_380:
    "Scene label_380"
    jump end_383

label label_381:
    "Scene label_381"
    jump end_383

label label_382:
    "Scene label_382"
    jump end_383

label label_377:
    "Scene label_377"
    menu:
        "Talk":
            $ luck += 2
            jump label_383
        "Look around":
            jump label_384
        "Pick up item":
            $ strength += 3
            jump label_385
        "Go forward":
            jump label_386

label label_383:
    "Scene label_383"
    jump end_387

label label_384:
    "Scene label_384"
    jump end_387

label label_385:
    "Scene label_385"
    jump end_387

label label_386:
    "Scene label_386"
    jump end_387

label label_361:
    "Scene label_361"
    if strength >= 9:
        jump label_387

label label_387:
    $ strength += 2
    if intelligence >= 17:
        jump label_388

label label_388:
    $ intelligence += 2
    if charisma >= 7:
        jump label_389

label label_389:
    $ charisma += 4
    jump end_390

    jump label_390

label label_390:
    "Ветка false для label_389"
    jump end_391

    jump label_391

label label_391:
    "Ветка false для label_388"
    menu:
        "Pick up item":
            $ intelligence += 3
            jump label_392
        "Look around":
            jump label_393
        "Open door":
            jump label_394
        "Use item":
            $ strength += 2
            jump label_395

label label_392:
    "Scene label_392"
    jump end_396

label label_393:
    "Scene label_393"
    jump end_396

label label_394:
    "Scene label_394"
    jump end_396

label label_395:
    "Scene label_395"
    jump end_396

    jump label_396

label label_396:
    "Ветка false для label_387"
    menu:
        "Pick up item":
            $ charisma += 1
            jump label_397
        "Go back":
            $ intelligence += 2
            jump label_398
        "Talk":
            jump label_399
        "Explore":
            jump label_400

label label_397:
    "Scene label_397"
    menu:
        "Go forward":
            jump label_401
        "Explore":
            jump label_402
        "Pick up item":
            $ intelligence += 1
            jump label_403

label label_401:
    "Scene label_401"
    jump end_404

label label_402:
    "Scene label_402"
    jump end_404

label label_403:
    "Scene label_403"
    jump end_404

label label_398:
    "Scene label_398"
    menu:
        "Open door":
            $ intelligence += 1
            jump label_404
        "Talk":
            $ charisma += 1
            jump label_405
        "Go back":
            jump label_406
        "Pick up item":
            jump label_407

label label_404:
    "Scene label_404"
    jump end_408

label label_405:
    "Scene label_405"
    jump end_408

label label_406:
    "Scene label_406"
    jump end_408

label label_407:
    "Scene label_407"
    jump end_408

label label_399:
    "Scene label_399"
    menu:
        "Go back":
            $ strength += 1
            jump label_408
        "Open door":
            $ luck += 1
            jump label_409
        "Use item":
            $ charisma += 2
            jump label_410
        "Pick up item":
            jump label_411

label label_408:
    "Scene label_408"
    jump end_412

label label_409:
    "Scene label_409"
    jump end_412

label label_410:
    "Scene label_410"
    jump end_412

label label_411:
    "Scene label_411"
    jump end_412

label label_400:
    "Scene label_400"
    menu:
        "Open door":
            $ charisma += 1
            jump label_412
        "Use item":
            $ intelligence += 2
            jump label_413
        "Explore":
            $ charisma += 1
            jump label_414
        "Pick up item":
            jump label_415

label label_412:
    "Scene label_412"
    jump end_416

label label_413:
    "Scene label_413"
    jump end_416

label label_414:
    "Scene label_414"
    jump end_416

label label_415:
    "Scene label_415"
    jump end_416

label label_358:
    "Scene label_358"
    if charisma >= 13:
        jump label_416

label label_416:
    $ charisma += 2
    menu:
        "Pick up item":
            jump label_417
        "Look around":
            $ intelligence += 2
            jump label_418

label label_417:
    "Scene label_417"
    menu:
        "Open door":
            $ intelligence += 1
            jump label_419
        "Go forward":
            $ luck += 1
            jump label_420

label label_419:
    "Scene label_419"
    menu:
        "Look around":
            jump label_421
        "Pick up item":
            $ luck += 2
            jump label_422
        "Open door":
            jump label_423

label label_421:
    "Scene label_421"
    jump end_424

label label_422:
    "Scene label_422"
    jump end_424

label label_423:
    "Scene label_423"
    jump end_424

label label_420:
    "Scene label_420"
    menu:
        "Talk":
            $ luck += 1
            jump label_424
        "Talk":
            jump label_425

label label_424:
    "Scene label_424"
    jump end_426

label label_425:
    "Scene label_425"
    jump end_426

label label_418:
    "Scene label_418"
    menu:
        "Open door":
            jump label_426
        "Look around":
            jump label_427
        "Look around":
            $ strength += 3
            jump label_428
        "Open door":
            $ strength += 3
            jump label_429

label label_426:
    "Scene label_426"
    menu:
        "Go forward":
            jump label_430
        "Open door":
            $ charisma += 3
            jump label_431
        "Open door":
            $ charisma += 1
            jump label_432
        "Explore":
            jump label_433

label label_430:
    "Scene label_430"
    jump end_434

label label_431:
    "Scene label_431"
    jump end_434

label label_432:
    "Scene label_432"
    jump end_434

label label_433:
    "Scene label_433"
    jump end_434

label label_427:
    "Scene label_427"
    menu:
        "Open door":
            $ luck += 1
            jump label_434
        "Go back":
            $ luck += 2
            jump label_435
        "Open door":
            jump label_436

label label_434:
    "Scene label_434"
    jump end_437

label label_435:
    "Scene label_435"
    jump end_437

label label_436:
    "Scene label_436"
    jump end_437

label label_428:
    "Scene label_428"
    if charisma >= 6:
        jump label_437

label label_437:
    $ charisma += 2
    jump end_438

    jump label_438

label label_438:
    "Ветка false для label_437"
    jump end_439

label label_429:
    "Scene label_429"
    if luck >= 15:
        jump label_439

label label_439:
    $ luck += 4
    jump end_440

    jump label_440

label label_440:
    "Ветка false для label_439"
    jump end_441

    jump label_441

label label_441:
    "Ветка false для label_416"
    if charisma >= 12:
        jump label_442

label label_442:
    $ charisma += 5
    if charisma >= 6:
        jump label_443

label label_443:
    $ charisma += 5
    if charisma >= 10:
        jump label_444

label label_444:
    $ charisma += 5
    jump end_445

    jump label_445

label label_445:
    "Ветка false для label_444"
    jump end_446

    jump label_446

label label_446:
    "Ветка false для label_443"
    menu:
        "Talk":
            $ strength += 3
            jump label_447
        "Talk":
            jump label_448
        "Open door":
            jump label_449
        "Go back":
            jump label_450

label label_447:
    "Scene label_447"
    jump end_451

label label_448:
    "Scene label_448"
    jump end_451

label label_449:
    "Scene label_449"
    jump end_451

label label_450:
    "Scene label_450"
    jump end_451

    jump label_451

label label_451:
    "Ветка false для label_442"
    if luck >= 11:
        jump label_452

label label_452:
    $ luck += 2
    if charisma >= 5:
        jump label_453

label label_453:
    $ charisma += 3
    jump end_454

    jump label_454

label label_454:
    "Ветка false для label_453"
    jump end_455

    jump label_455

label label_455:
    "Ветка false для label_452"
    if strength >= 17:
        jump label_456

label label_456:
    $ strength += 2
    jump end_457

    jump label_457

label label_457:
    "Ветка false для label_456"
    jump end_458

label label_359:
    "Scene label_359"
    menu:
        "Pick up item":
            jump label_458
        "Explore":
            $ intelligence += 2
            jump label_459

label label_458:
    "Scene label_458"
    if intelligence >= 17:
        jump label_460

label label_460:
    $ intelligence += 4
    menu:
        "Look around":
            jump label_461
        "Go forward":
            jump label_462
        "Look around":
            $ strength += 1
            jump label_463

label label_461:
    "Scene label_461"
    if luck >= 10:
        jump label_464

label label_464:
    $ luck += 2
    jump end_465

    jump label_465

label label_465:
    "Ветка false для label_464"
    jump end_466

label label_462:
    "Scene label_462"
    if luck >= 11:
        jump label_466

label label_466:
    $ luck += 5
    jump end_467

    jump label_467

label label_467:
    "Ветка false для label_466"
    jump end_468

label label_463:
    "Scene label_463"
    if strength >= 18:
        jump label_468

label label_468:
    $ strength += 2
    jump end_469

    jump label_469

label label_469:
    "Ветка false для label_468"
    jump end_470

    jump label_470

label label_470:
    "Ветка false для label_460"
    menu:
        "Look around":
            $ charisma += 2
            jump label_471
        "Explore":
            jump label_472
        "Pick up item":
            jump label_473
        "Talk":
            $ intelligence += 3
            jump label_474

label label_471:
    "Scene label_471"
    menu:
        "Go forward":
            $ luck += 2
            jump label_475
        "Pick up item":
            jump label_476
        "Go forward":
            $ luck += 1
            jump label_477
        "Use item":
            jump label_478

label label_475:
    "Scene label_475"
    jump end_479

label label_476:
    "Scene label_476"
    jump end_479

label label_477:
    "Scene label_477"
    jump end_479

label label_478:
    "Scene label_478"
    jump end_479

label label_472:
    "Scene label_472"
    menu:
        "Talk":
            $ luck += 1
            jump label_479
        "Use item":
            $ intelligence += 1
            jump label_480
        "Look around":
            jump label_481
        "Talk":
            $ charisma += 1
            jump label_482

label label_479:
    "Scene label_479"
    jump end_483

label label_480:
    "Scene label_480"
    jump end_483

label label_481:
    "Scene label_481"
    jump end_483

label label_482:
    "Scene label_482"
    jump end_483

label label_473:
    "Scene label_473"
    menu:
        "Go back":
            $ charisma += 2
            jump label_483
        "Open door":
            jump label_484
        "Go back":
            $ luck += 2
            jump label_485

label label_483:
    "Scene label_483"
    jump end_486

label label_484:
    "Scene label_484"
    jump end_486

label label_485:
    "Scene label_485"
    jump end_486

label label_474:
    "Scene label_474"
    if luck >= 10:
        jump label_486

label label_486:
    $ luck += 3
    jump end_487

    jump label_487

label label_487:
    "Ветка false для label_486"
    jump end_488

label label_459:
    "Scene label_459"
    menu:
        "Open door":
            jump label_488
        "Open door":
            jump label_489
        "Go back":
            jump label_490

label label_488:
    "Scene label_488"
    menu:
        "Open door":
            $ luck += 2
            jump label_491
        "Look around":
            $ strength += 3
            jump label_492
        "Go back":
            jump label_493
        "Go back":
            jump label_494

label label_491:
    "Scene label_491"
    menu:
        "Explore":
            $ strength += 1
            jump label_495
        "Explore":
            $ intelligence += 2
            jump label_496
        "Use item":
            $ luck += 2
            jump label_497
        "Talk":
            jump label_498

label label_495:
    "Scene label_495"
    jump end_499

label label_496:
    "Scene label_496"
    jump end_499

label label_497:
    "Scene label_497"
    jump end_499

label label_498:
    "Scene label_498"
    jump end_499

label label_492:
    "Scene label_492"
    if luck >= 5:
        jump label_499

label label_499:
    $ luck += 4
    jump end_500

    jump label_500

label label_500:
    "Ветка false для label_499"
    jump end_501

label label_493:
    "Scene label_493"
    if luck >= 12:
        jump label_501

label label_501:
    $ luck += 2
    jump end_502

    jump label_502

label label_502:
    "Ветка false для label_501"
    jump end_503

label label_494:
    "Scene label_494"
    menu:
        "Use item":
            jump label_503
        "Look around":
            jump label_504
        "Look around":
            jump label_505
        "Open door":
            jump label_506

label label_503:
    "Scene label_503"
    jump end_507

label label_504:
    "Scene label_504"
    jump end_507

label label_505:
    "Scene label_505"
    jump end_507

label label_506:
    "Scene label_506"
    jump end_507

label label_489:
    "Scene label_489"
    menu:
        "Use item":
            $ charisma += 2
            jump label_507
        "Go forward":
            jump label_508
        "Open door":
            $ charisma += 1
            jump label_509

label label_507:
    "Scene label_507"
    menu:
        "Open door":
            $ strength += 2
            jump label_510
        "Go forward":
            jump label_511
        "Go forward":
            jump label_512
        "Go back":
            $ charisma += 1
            jump label_513

label label_510:
    "Scene label_510"
    jump end_514

label label_511:
    "Scene label_511"
    jump end_514

label label_512:
    "Scene label_512"
    jump end_514

label label_513:
    "Scene label_513"
    jump end_514

label label_508:
    "Scene label_508"
    menu:
        "Go forward":
            $ strength += 1
            jump label_514
        "Pick up item":
            $ charisma += 3
            jump label_515
        "Go back":
            $ luck += 2
            jump label_516
        "Look around":
            jump label_517

label label_514:
    "Scene label_514"
    jump end_518

label label_515:
    "Scene label_515"
    jump end_518

label label_516:
    "Scene label_516"
    jump end_518

label label_517:
    "Scene label_517"
    jump end_518

label label_509:
    "Scene label_509"
    menu:
        "Go forward":
            $ charisma += 2
            jump label_518
        "Look around":
            jump label_519
        "Look around":
            $ strength += 1
            jump label_520
        "Talk":
            $ luck += 3
            jump label_521

label label_518:
    "Scene label_518"
    jump end_522

label label_519:
    "Scene label_519"
    jump end_522

label label_520:
    "Scene label_520"
    jump end_522

label label_521:
    "Scene label_521"
    jump end_522

label label_490:
    "Scene label_490"
    menu:
        "Talk":
            $ luck += 3
            jump label_522
        "Go forward":
            jump label_523

label label_522:
    "Scene label_522"
    menu:
        "Go forward":
            $ luck += 1
            jump label_524
        "Go back":
            $ charisma += 2
            jump label_525
        "Talk":
            jump label_526

label label_524:
    "Scene label_524"
    jump end_527

label label_525:
    "Scene label_525"
    jump end_527

label label_526:
    "Scene label_526"
    jump end_527

label label_523:
    "Scene label_523"
    menu:
        "Talk":
            $ intelligence += 3
            jump label_527
        "Open door":
            jump label_528

label label_527:
    "Scene label_527"
    jump end_529

label label_528:
    "Scene label_528"
    jump end_529

    jump label_529

label label_529:
    "Ветка false для label_356"
    menu:
        "Use item":
            jump label_530
        "Pick up item":
            jump label_531
        "Explore":
            jump label_532
        "Pick up item":
            $ luck += 2
            jump label_533

label label_530:
    "Scene label_530"
    menu:
        "Use item":
            jump label_534
        "Use item":
            jump label_535
        "Look around":
            jump label_536

label label_534:
    "Scene label_534"
    if strength >= 11:
        jump label_537

label label_537:
    $ strength += 5
    menu:
        "Pick up item":
            $ intelligence += 3
            jump label_538
        "Explore":
            jump label_539

label label_538:
    "Scene label_538"
    menu:
        "Talk":
            jump label_540
        "Look around":
            jump label_541
        "Use item":
            jump label_542

label label_540:
    "Scene label_540"
    jump end_543

label label_541:
    "Scene label_541"
    jump end_543

label label_542:
    "Scene label_542"
    jump end_543

label label_539:
    "Scene label_539"
    menu:
        "Use item":
            jump label_543
        "Use item":
            $ charisma += 1
            jump label_544
        "Go back":
            jump label_545

label label_543:
    "Scene label_543"
    jump end_546

label label_544:
    "Scene label_544"
    jump end_546

label label_545:
    "Scene label_545"
    jump end_546

    jump label_546

label label_546:
    "Ветка false для label_537"
    menu:
        "Talk":
            $ strength += 3
            jump label_547
        "Look around":
            $ charisma += 1
            jump label_548

label label_547:
    "Scene label_547"
    if charisma >= 19:
        jump label_549

label label_549:
    $ charisma += 4
    jump end_550

    jump label_550

label label_550:
    "Ветка false для label_549"
    jump end_551

label label_548:
    "Scene label_548"
    if strength >= 16:
        jump label_551

label label_551:
    $ strength += 5
    jump end_552

    jump label_552

label label_552:
    "Ветка false для label_551"
    jump end_553

label label_535:
    "Scene label_535"
    if charisma >= 18:
        jump label_553

label label_553:
    $ charisma += 4
    if luck >= 16:
        jump label_554

label label_554:
    $ luck += 2
    if charisma >= 18:
        jump label_555

label label_555:
    $ charisma += 3
    jump end_556

    jump label_556

label label_556:
    "Ветка false для label_555"
    jump end_557

    jump label_557

label label_557:
    "Ветка false для label_554"
    if charisma >= 10:
        jump label_558

label label_558:
    $ charisma += 4
    jump end_559

    jump label_559

label label_559:
    "Ветка false для label_558"
    jump end_560

    jump label_560

label label_560:
    "Ветка false для label_553"
    menu:
        "Open door":
            $ strength += 3
            jump label_561
        "Use item":
            jump label_562
        "Use item":
            $ strength += 3
            jump label_563

label label_561:
    "Scene label_561"
    if strength >= 8:
        jump label_564

label label_564:
    $ strength += 4
    jump end_565

    jump label_565

label label_565:
    "Ветка false для label_564"
    jump end_566

label label_562:
    "Scene label_562"
    if charisma >= 17:
        jump label_566

label label_566:
    $ charisma += 5
    jump end_567

    jump label_567

label label_567:
    "Ветка false для label_566"
    jump end_568

label label_563:
    "Scene label_563"
    if luck >= 20:
        jump label_568

label label_568:
    $ luck += 3
    jump end_569

    jump label_569

label label_569:
    "Ветка false для label_568"
    jump end_570

label label_536:
    "Scene label_536"
    if intelligence >= 16:
        jump label_570

label label_570:
    $ intelligence += 4
    menu:
        "Go forward":
            $ charisma += 3
            jump label_571
        "Go back":
            jump label_572
        "Use item":
            $ strength += 1
            jump label_573

label label_571:
    "Scene label_571"
    if charisma >= 9:
        jump label_574

label label_574:
    $ charisma += 2
    jump end_575

    jump label_575

label label_575:
    "Ветка false для label_574"
    jump end_576

label label_572:
    "Scene label_572"
    menu:
        "Explore":
            $ luck += 1
            jump label_576
        "Talk":
            jump label_577
        "Go forward":
            jump label_578

label label_576:
    "Scene label_576"
    jump end_579

label label_577:
    "Scene label_577"
    jump end_579

label label_578:
    "Scene label_578"
    jump end_579

label label_573:
    "Scene label_573"
    menu:
        "Go forward":
            $ intelligence += 2
            jump label_579
        "Look around":
            $ strength += 3
            jump label_580
        "Go back":
            jump label_581
        "Talk":
            jump label_582

label label_579:
    "Scene label_579"
    jump end_583

label label_580:
    "Scene label_580"
    jump end_583

label label_581:
    "Scene label_581"
    jump end_583

label label_582:
    "Scene label_582"
    jump end_583

    jump label_583

label label_583:
    "Ветка false для label_570"
    menu:
        "Go back":
            jump label_584
        "Explore":
            $ luck += 3
            jump label_585

label label_584:
    "Scene label_584"
    if charisma >= 13:
        jump label_586

label label_586:
    $ charisma += 4
    jump end_587

    jump label_587

label label_587:
    "Ветка false для label_586"
    jump end_588

label label_585:
    "Scene label_585"
    menu:
        "Go back":
            jump label_588
        "Pick up item":
            $ strength += 1
            jump label_589
        "Open door":
            jump label_590

label label_588:
    "Scene label_588"
    jump end_591

label label_589:
    "Scene label_589"
    jump end_591

label label_590:
    "Scene label_590"
    jump end_591

label label_531:
    "Scene label_531"
    menu:
        "Explore":
            $ intelligence += 3
            jump label_591
        "Open door":
            $ strength += 1
            jump label_592

label label_591:
    "Scene label_591"
    menu:
        "Look around":
            jump label_593
        "Pick up item":
            jump label_594
        "Talk":
            $ luck += 2
            jump label_595

label label_593:
    "Scene label_593"
    menu:
        "Go back":
            $ strength += 3
            jump label_596
        "Explore":
            jump label_597
        "Look around":
            $ charisma += 3
            jump label_598

label label_596:
    "Scene label_596"
    menu:
        "Go back":
            $ strength += 2
            jump label_599
        "Talk":
            $ intelligence += 3
            jump label_600
        "Go back":
            jump label_601

label label_599:
    "Scene label_599"
    jump end_602

label label_600:
    "Scene label_600"
    jump end_602

label label_601:
    "Scene label_601"
    jump end_602

label label_597:
    "Scene label_597"
    menu:
        "Pick up item":
            $ luck += 1
            jump label_602
        "Pick up item":
            $ luck += 3
            jump label_603
        "Look around":
            $ luck += 1
            jump label_604

label label_602:
    "Scene label_602"
    jump end_605

label label_603:
    "Scene label_603"
    jump end_605

label label_604:
    "Scene label_604"
    jump end_605

label label_598:
    "Scene label_598"
    menu:
        "Go forward":
            $ intelligence += 2
            jump label_605
        "Go back":
            jump label_606
        "Talk":
            jump label_607
        "Go back":
            $ intelligence += 2
            jump label_608

label label_605:
    "Scene label_605"
    jump end_609

label label_606:
    "Scene label_606"
    jump end_609

label label_607:
    "Scene label_607"
    jump end_609

label label_608:
    "Scene label_608"
    jump end_609

label label_594:
    "Scene label_594"
    menu:
        "Go back":
            $ charisma += 2
            jump label_609
        "Use item":
            jump label_610

label label_609:
    "Scene label_609"
    menu:
        "Open door":
            jump label_611
        "Look around":
            jump label_612
        "Go back":
            jump label_613

label label_611:
    "Scene label_611"
    jump end_614

label label_612:
    "Scene label_612"
    jump end_614

label label_613:
    "Scene label_613"
    jump end_614

label label_610:
    "Scene label_610"
    if charisma >= 15:
        jump label_614

label label_614:
    $ charisma += 3
    jump end_615

    jump label_615

label label_615:
    "Ветка false для label_614"
    jump end_616

label label_595:
    "Scene label_595"
    menu:
        "Go back":
            $ intelligence += 2
            jump label_616
        "Go back":
            $ charisma += 3
            jump label_617

label label_616:
    "Scene label_616"
    if charisma >= 8:
        jump label_618

label label_618:
    $ charisma += 3
    jump end_619

    jump label_619

label label_619:
    "Ветка false для label_618"
    jump end_620

label label_617:
    "Scene label_617"
    menu:
        "Explore":
            jump label_620
        "Explore":
            $ charisma += 2
            jump label_621
        "Open door":
            jump label_622
        "Pick up item":
            $ strength += 2
            jump label_623

label label_620:
    "Scene label_620"
    jump end_624

label label_621:
    "Scene label_621"
    jump end_624

label label_622:
    "Scene label_622"
    jump end_624

label label_623:
    "Scene label_623"
    jump end_624

label label_592:
    "Scene label_592"
    if intelligence >= 14:
        jump label_624

label label_624:
    $ intelligence += 3
    menu:
        "Talk":
            jump label_625
        "Go back":
            $ charisma += 1
            jump label_626
        "Open door":
            jump label_627

label label_625:
    "Scene label_625"
    menu:
        "Pick up item":
            jump label_628
        "Look around":
            $ strength += 2
            jump label_629
        "Look around":
            jump label_630
        "Pick up item":
            jump label_631

label label_628:
    "Scene label_628"
    jump end_632

label label_629:
    "Scene label_629"
    jump end_632

label label_630:
    "Scene label_630"
    jump end_632

label label_631:
    "Scene label_631"
    jump end_632

label label_626:
    "Scene label_626"
    menu:
        "Go forward":
            jump label_632
        "Talk":
            jump label_633

label label_632:
    "Scene label_632"
    jump end_634

label label_633:
    "Scene label_633"
    jump end_634

label label_627:
    "Scene label_627"
    menu:
        "Use item":
            jump label_634
        "Talk":
            $ luck += 3
            jump label_635

label label_634:
    "Scene label_634"
    jump end_636

label label_635:
    "Scene label_635"
    jump end_636

    jump label_636

label label_636:
    "Ветка false для label_624"
    menu:
        "Pick up item":
            jump label_637
        "Use item":
            $ strength += 1
            jump label_638

label label_637:
    "Scene label_637"
    menu:
        "Look around":
            $ strength += 2
            jump label_639
        "Go forward":
            jump label_640

label label_639:
    "Scene label_639"
    jump end_641

label label_640:
    "Scene label_640"
    jump end_641

label label_638:
    "Scene label_638"
    menu:
        "Look around":
            $ charisma += 1
            jump label_641
        "Use item":
            jump label_642

label label_641:
    "Scene label_641"
    jump end_643

label label_642:
    "Scene label_642"
    jump end_643

label label_532:
    "Scene label_532"
    menu:
        "Pick up item":
            jump label_643
        "Look around":
            $ strength += 1
            jump label_644
        "Talk":
            jump label_645
        "Use item":
            $ intelligence += 2
            jump label_646

label label_643:
    "Scene label_643"
    menu:
        "Look around":
            jump label_647
        "Pick up item":
            $ luck += 2
            jump label_648
        "Open door":
            jump label_649

label label_647:
    "Scene label_647"
    if charisma >= 18:
        jump label_650

label label_650:
    $ charisma += 3
    if charisma >= 8:
        jump label_651

label label_651:
    $ charisma += 5
    jump end_652

    jump label_652

label label_652:
    "Ветка false для label_651"
    jump end_653

    jump label_653

label label_653:
    "Ветка false для label_650"
    if luck >= 6:
        jump label_654

label label_654:
    $ luck += 5
    jump end_655

    jump label_655

label label_655:
    "Ветка false для label_654"
    jump end_656

label label_648:
    "Scene label_648"
    if luck >= 9:
        jump label_656

label label_656:
    $ luck += 5
    menu:
        "Go back":
            $ intelligence += 2
            jump label_657
        "Use item":
            $ charisma += 3
            jump label_658
        "Look around":
            $ intelligence += 2
            jump label_659

label label_657:
    "Scene label_657"
    jump end_660

label label_658:
    "Scene label_658"
    jump end_660

label label_659:
    "Scene label_659"
    jump end_660

    jump label_660

label label_660:
    "Ветка false для label_656"
    menu:
        "Explore":
            $ intelligence += 2
            jump label_661
        "Go back":
            jump label_662
        "Look around":
            jump label_663
        "Pick up item":
            $ charisma += 3
            jump label_664

label label_661:
    "Scene label_661"
    jump end_665

label label_662:
    "Scene label_662"
    jump end_665

label label_663:
    "Scene label_663"
    jump end_665

label label_664:
    "Scene label_664"
    jump end_665

label label_649:
    "Scene label_649"
    menu:
        "Go back":
            $ luck += 3
            jump label_665
        "Explore":
            jump label_666
        "Open door":
            $ strength += 3
            jump label_667
        "Talk":
            $ strength += 2
            jump label_668

label label_665:
    "Scene label_665"
    menu:
        "Explore":
            jump label_669
        "Use item":
            $ intelligence += 3
            jump label_670
        "Open door":
            jump label_671

label label_669:
    "Scene label_669"
    jump end_672

label label_670:
    "Scene label_670"
    jump end_672

label label_671:
    "Scene label_671"
    jump end_672

label label_666:
    "Scene label_666"
    menu:
        "Go forward":
            jump label_672
        "Look around":
            $ strength += 2
            jump label_673

label label_672:
    "Scene label_672"
    jump end_674

label label_673:
    "Scene label_673"
    jump end_674

label label_667:
    "Scene label_667"
    menu:
        "Go forward":
            jump label_674
        "Explore":
            $ charisma += 2
            jump label_675
        "Talk":
            jump label_676
        "Use item":
            $ charisma += 2
            jump label_677

label label_674:
    "Scene label_674"
    jump end_678

label label_675:
    "Scene label_675"
    jump end_678

label label_676:
    "Scene label_676"
    jump end_678

label label_677:
    "Scene label_677"
    jump end_678

label label_668:
    "Scene label_668"
    menu:
        "Use item":
            jump label_678
        "Open door":
            jump label_679

label label_678:
    "Scene label_678"
    jump end_680

label label_679:
    "Scene label_679"
    jump end_680

label label_644:
    "Scene label_644"
    menu:
        "Look around":
            jump label_680
        "Look around":
            $ intelligence += 1
            jump label_681

label label_680:
    "Scene label_680"
    menu:
        "Look around":
            $ charisma += 1
            jump label_682
        "Use item":
            jump label_683
        "Pick up item":
            jump label_684

label label_682:
    "Scene label_682"
    menu:
        "Talk":
            jump label_685
        "Pick up item":
            $ charisma += 1
            jump label_686
        "Look around":
            $ luck += 1
            jump label_687
        "Look around":
            $ strength += 3
            jump label_688

label label_685:
    "Scene label_685"
    jump end_689

label label_686:
    "Scene label_686"
    jump end_689

label label_687:
    "Scene label_687"
    jump end_689

label label_688:
    "Scene label_688"
    jump end_689

label label_683:
    "Scene label_683"
    menu:
        "Use item":
            jump label_689
        "Go back":
            jump label_690

label label_689:
    "Scene label_689"
    jump end_691

label label_690:
    "Scene label_690"
    jump end_691

label label_684:
    "Scene label_684"
    if luck >= 7:
        jump label_691

label label_691:
    $ luck += 3
    jump end_692

    jump label_692

label label_692:
    "Ветка false для label_691"
    jump end_693

label label_681:
    "Scene label_681"
    menu:
        "Use item":
            jump label_693
        "Go back":
            $ strength += 3
            jump label_694

label label_693:
    "Scene label_693"
    menu:
        "Pick up item":
            jump label_695
        "Go back":
            jump label_696

label label_695:
    "Scene label_695"
    jump end_697

label label_696:
    "Scene label_696"
    jump end_697

label label_694:
    "Scene label_694"
    if charisma >= 13:
        jump label_697

label label_697:
    $ charisma += 3
    jump end_698

    jump label_698

label label_698:
    "Ветка false для label_697"
    jump end_699

label label_645:
    "Scene label_645"
    menu:
        "Talk":
            $ luck += 3
            jump label_699
        "Go forward":
            $ strength += 3
            jump label_700

label label_699:
    "Scene label_699"
    menu:
        "Go forward":
            $ strength += 2
            jump label_701
        "Look around":
            jump label_702
        "Pick up item":
            jump label_703
        "Go back":
            jump label_704

label label_701:
    "Scene label_701"
    if charisma >= 12:
        jump label_705

label label_705:
    $ charisma += 4
    jump end_706

    jump label_706

label label_706:
    "Ветка false для label_705"
    jump end_707

label label_702:
    "Scene label_702"
    menu:
        "Use item":
            $ strength += 1
            jump label_707
        "Use item":
            jump label_708
        "Open door":
            jump label_709

label label_707:
    "Scene label_707"
    jump end_710

label label_708:
    "Scene label_708"
    jump end_710

label label_709:
    "Scene label_709"
    jump end_710

label label_703:
    "Scene label_703"
    menu:
        "Pick up item":
            $ charisma += 3
            jump label_710
        "Talk":
            $ charisma += 3
            jump label_711
        "Talk":
            $ strength += 3
            jump label_712
        "Explore":
            $ luck += 2
            jump label_713

label label_710:
    "Scene label_710"
    jump end_714

label label_711:
    "Scene label_711"
    jump end_714

label label_712:
    "Scene label_712"
    jump end_714

label label_713:
    "Scene label_713"
    jump end_714

label label_704:
    "Scene label_704"
    menu:
        "Use item":
            $ strength += 1
            jump label_714
        "Open door":
            jump label_715

label label_714:
    "Scene label_714"
    jump end_716

label label_715:
    "Scene label_715"
    jump end_716

label label_700:
    "Scene label_700"
    menu:
        "Go forward":
            jump label_716
        "Go forward":
            jump label_717
        "Use item":
            jump label_718
        "Look around":
            $ charisma += 1
            jump label_719

label label_716:
    "Scene label_716"
    if luck >= 16:
        jump label_720

label label_720:
    $ luck += 3
    jump end_721

    jump label_721

label label_721:
    "Ветка false для label_720"
    jump end_722

label label_717:
    "Scene label_717"
    menu:
        "Open door":
            $ strength += 3
            jump label_722
        "Look around":
            $ intelligence += 2
            jump label_723

label label_722:
    "Scene label_722"
    jump end_724

label label_723:
    "Scene label_723"
    jump end_724

label label_718:
    "Scene label_718"
    menu:
        "Use item":
            $ luck += 2
            jump label_724
        "Go back":
            jump label_725
        "Use item":
            jump label_726

label label_724:
    "Scene label_724"
    jump end_727

label label_725:
    "Scene label_725"
    jump end_727

label label_726:
    "Scene label_726"
    jump end_727

label label_719:
    "Scene label_719"
    if strength >= 6:
        jump label_727

label label_727:
    $ strength += 4
    jump end_728

    jump label_728

label label_728:
    "Ветка false для label_727"
    jump end_729

label label_646:
    "Scene label_646"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_729
        "Use item":
            $ intelligence += 1
            jump label_730
        "Explore":
            jump label_731
        "Talk":
            $ intelligence += 3
            jump label_732

label label_729:
    "Scene label_729"
    menu:
        "Look around":
            $ strength += 2
            jump label_733
        "Go back":
            jump label_734
        "Go back":
            jump label_735

label label_733:
    "Scene label_733"
    if luck >= 17:
        jump label_736

label label_736:
    $ luck += 5
    jump end_737

    jump label_737

label label_737:
    "Ветка false для label_736"
    jump end_738

label label_734:
    "Scene label_734"
    if charisma >= 17:
        jump label_738

label label_738:
    $ charisma += 5
    jump end_739

    jump label_739

label label_739:
    "Ветка false для label_738"
    jump end_740

label label_735:
    "Scene label_735"
    if intelligence >= 17:
        jump label_740

label label_740:
    $ intelligence += 3
    jump end_741

    jump label_741

label label_741:
    "Ветка false для label_740"
    jump end_742

label label_730:
    "Scene label_730"
    menu:
        "Go forward":
            jump label_742
        "Go forward":
            jump label_743
        "Explore":
            jump label_744
        "Explore":
            jump label_745

label label_742:
    "Scene label_742"
    menu:
        "Use item":
            jump label_746
        "Explore":
            jump label_747
        "Open door":
            jump label_748
        "Go forward":
            jump label_749

label label_746:
    "Scene label_746"
    jump end_750

label label_747:
    "Scene label_747"
    jump end_750

label label_748:
    "Scene label_748"
    jump end_750

label label_749:
    "Scene label_749"
    jump end_750

label label_743:
    "Scene label_743"
    menu:
        "Go back":
            jump label_750
        "Pick up item":
            $ luck += 1
            jump label_751
        "Open door":
            $ intelligence += 1
            jump label_752
        "Go forward":
            $ luck += 1
            jump label_753

label label_750:
    "Scene label_750"
    jump end_754

label label_751:
    "Scene label_751"
    jump end_754

label label_752:
    "Scene label_752"
    jump end_754

label label_753:
    "Scene label_753"
    jump end_754

label label_744:
    "Scene label_744"
    menu:
        "Go back":
            $ charisma += 1
            jump label_754
        "Go back":
            $ luck += 3
            jump label_755
        "Go forward":
            $ luck += 2
            jump label_756
        "Talk":
            $ strength += 2
            jump label_757

label label_754:
    "Scene label_754"
    jump end_758

label label_755:
    "Scene label_755"
    jump end_758

label label_756:
    "Scene label_756"
    jump end_758

label label_757:
    "Scene label_757"
    jump end_758

label label_745:
    "Scene label_745"
    if strength >= 16:
        jump label_758

label label_758:
    $ strength += 5
    jump end_759

    jump label_759

label label_759:
    "Ветка false для label_758"
    jump end_760

label label_731:
    "Scene label_731"
    menu:
        "Use item":
            $ strength += 2
            jump label_760
        "Explore":
            jump label_761
        "Pick up item":
            $ luck += 2
            jump label_762
        "Pick up item":
            $ intelligence += 1
            jump label_763

label label_760:
    "Scene label_760"
    menu:
        "Go forward":
            $ strength += 1
            jump label_764
        "Pick up item":
            jump label_765
        "Go forward":
            jump label_766
        "Use item":
            $ luck += 2
            jump label_767

label label_764:
    "Scene label_764"
    jump end_768

label label_765:
    "Scene label_765"
    jump end_768

label label_766:
    "Scene label_766"
    jump end_768

label label_767:
    "Scene label_767"
    jump end_768

label label_761:
    "Scene label_761"
    if luck >= 6:
        jump label_768

label label_768:
    $ luck += 3
    jump end_769

    jump label_769

label label_769:
    "Ветка false для label_768"
    jump end_770

label label_762:
    "Scene label_762"
    menu:
        "Pick up item":
            $ strength += 1
            jump label_770
        "Use item":
            $ luck += 3
            jump label_771

label label_770:
    "Scene label_770"
    jump end_772

label label_771:
    "Scene label_771"
    jump end_772

label label_763:
    "Scene label_763"
    menu:
        "Open door":
            jump label_772
        "Talk":
            $ luck += 2
            jump label_773
        "Open door":
            jump label_774
        "Explore":
            $ luck += 3
            jump label_775

label label_772:
    "Scene label_772"
    jump end_776

label label_773:
    "Scene label_773"
    jump end_776

label label_774:
    "Scene label_774"
    jump end_776

label label_775:
    "Scene label_775"
    jump end_776

label label_732:
    "Scene label_732"
    if luck >= 6:
        jump label_776

label label_776:
    $ luck += 4
    menu:
        "Go forward":
            $ intelligence += 2
            jump label_777
        "Explore":
            jump label_778
        "Open door":
            jump label_779
        "Go forward":
            jump label_780

label label_777:
    "Scene label_777"
    jump end_781

label label_778:
    "Scene label_778"
    jump end_781

label label_779:
    "Scene label_779"
    jump end_781

label label_780:
    "Scene label_780"
    jump end_781

    jump label_781

label label_781:
    "Ветка false для label_776"
    if strength >= 7:
        jump label_782

label label_782:
    $ strength += 3
    jump end_783

    jump label_783

label label_783:
    "Ветка false для label_782"
    jump end_784

label label_533:
    "Scene label_533"
    menu:
        "Open door":
            jump label_784
        "Look around":
            jump label_785
        "Go forward":
            jump label_786
        "Pick up item":
            $ intelligence += 3
            jump label_787

label label_784:
    "Scene label_784"
    if intelligence >= 15:
        jump label_788

label label_788:
    $ intelligence += 3
    menu:
        "Use item":
            $ strength += 3
            jump label_789
        "Use item":
            $ charisma += 2
            jump label_790
        "Look around":
            $ strength += 2
            jump label_791

label label_789:
    "Scene label_789"
    menu:
        "Use item":
            $ charisma += 1
            jump label_792
        "Talk":
            jump label_793
        "Use item":
            jump label_794
        "Open door":
            jump label_795

label label_792:
    "Scene label_792"
    jump end_796

label label_793:
    "Scene label_793"
    jump end_796

label label_794:
    "Scene label_794"
    jump end_796

label label_795:
    "Scene label_795"
    jump end_796

label label_790:
    "Scene label_790"
    menu:
        "Go back":
            jump label_796
        "Explore":
            $ strength += 2
            jump label_797
        "Open door":
            jump label_798
        "Talk":
            jump label_799

label label_796:
    "Scene label_796"
    jump end_800

label label_797:
    "Scene label_797"
    jump end_800

label label_798:
    "Scene label_798"
    jump end_800

label label_799:
    "Scene label_799"
    jump end_800

label label_791:
    "Scene label_791"
    menu:
        "Talk":
            jump label_800
        "Go forward":
            $ charisma += 2
            jump label_801

label label_800:
    "Scene label_800"
    jump end_802

label label_801:
    "Scene label_801"
    jump end_802

    jump label_802

label label_802:
    "Ветка false для label_788"
    menu:
        "Pick up item":
            jump label_803
        "Talk":
            jump label_804
        "Open door":
            $ intelligence += 1
            jump label_805
        "Talk":
            jump label_806

label label_803:
    "Scene label_803"
    menu:
        "Open door":
            $ charisma += 3
            jump label_807
        "Use item":
            jump label_808
        "Look around":
            $ luck += 3
            jump label_809

label label_807:
    "Scene label_807"
    jump end_810

label label_808:
    "Scene label_808"
    jump end_810

label label_809:
    "Scene label_809"
    jump end_810

label label_804:
    "Scene label_804"
    menu:
        "Go forward":
            $ luck += 2
            jump label_810
        "Open door":
            jump label_811

label label_810:
    "Scene label_810"
    jump end_812

label label_811:
    "Scene label_811"
    jump end_812

label label_805:
    "Scene label_805"
    menu:
        "Go back":
            jump label_812
        "Talk":
            jump label_813
        "Look around":
            $ strength += 3
            jump label_814

label label_812:
    "Scene label_812"
    jump end_815

label label_813:
    "Scene label_813"
    jump end_815

label label_814:
    "Scene label_814"
    jump end_815

label label_806:
    "Scene label_806"
    menu:
        "Pick up item":
            $ charisma += 1
            jump label_815
        "Go back":
            jump label_816
        "Look around":
            $ charisma += 2
            jump label_817
        "Go forward":
            jump label_818

label label_815:
    "Scene label_815"
    jump end_819

label label_816:
    "Scene label_816"
    jump end_819

label label_817:
    "Scene label_817"
    jump end_819

label label_818:
    "Scene label_818"
    jump end_819

label label_785:
    "Scene label_785"
    menu:
        "Open door":
            $ charisma += 2
            jump label_819
        "Talk":
            jump label_820
        "Go forward":
            jump label_821
        "Use item":
            $ luck += 3
            jump label_822

label label_819:
    "Scene label_819"
    menu:
        "Look around":
            $ intelligence += 1
            jump label_823
        "Go back":
            $ charisma += 1
            jump label_824
        "Talk":
            $ luck += 3
            jump label_825

label label_823:
    "Scene label_823"
    menu:
        "Go back":
            $ intelligence += 3
            jump label_826
        "Talk":
            $ strength += 3
            jump label_827

label label_826:
    "Scene label_826"
    jump end_828

label label_827:
    "Scene label_827"
    jump end_828

label label_824:
    "Scene label_824"
    menu:
        "Go forward":
            $ strength += 2
            jump label_828
        "Use item":
            $ charisma += 3
            jump label_829

label label_828:
    "Scene label_828"
    jump end_830

label label_829:
    "Scene label_829"
    jump end_830

label label_825:
    "Scene label_825"
    menu:
        "Pick up item":
            $ strength += 3
            jump label_830
        "Look around":
            $ charisma += 2
            jump label_831

label label_830:
    "Scene label_830"
    jump end_832

label label_831:
    "Scene label_831"
    jump end_832

label label_820:
    "Scene label_820"
    if intelligence >= 13:
        jump label_832

label label_832:
    $ intelligence += 2
    menu:
        "Use item":
            jump label_833
        "Explore":
            $ luck += 2
            jump label_834

label label_833:
    "Scene label_833"
    jump end_835

label label_834:
    "Scene label_834"
    jump end_835

    jump label_835

label label_835:
    "Ветка false для label_832"
    menu:
        "Look around":
            jump label_836
        "Explore":
            jump label_837
        "Go forward":
            $ luck += 1
            jump label_838
        "Go forward":
            jump label_839

label label_836:
    "Scene label_836"
    jump end_840

label label_837:
    "Scene label_837"
    jump end_840

label label_838:
    "Scene label_838"
    jump end_840

label label_839:
    "Scene label_839"
    jump end_840

label label_821:
    "Scene label_821"
    menu:
        "Talk":
            jump label_840
        "Use item":
            jump label_841

label label_840:
    "Scene label_840"
    if intelligence >= 20:
        jump label_842

label label_842:
    $ intelligence += 3
    jump end_843

    jump label_843

label label_843:
    "Ветка false для label_842"
    jump end_844

label label_841:
    "Scene label_841"
    menu:
        "Talk":
            $ strength += 3
            jump label_844
        "Use item":
            $ strength += 2
            jump label_845
        "Use item":
            jump label_846

label label_844:
    "Scene label_844"
    jump end_847

label label_845:
    "Scene label_845"
    jump end_847

label label_846:
    "Scene label_846"
    jump end_847

label label_822:
    "Scene label_822"
    if luck >= 17:
        jump label_847

label label_847:
    $ luck += 3
    menu:
        "Talk":
            jump label_848
        "Use item":
            jump label_849
        "Pick up item":
            $ charisma += 3
            jump label_850

label label_848:
    "Scene label_848"
    jump end_851

label label_849:
    "Scene label_849"
    jump end_851

label label_850:
    "Scene label_850"
    jump end_851

    jump label_851

label label_851:
    "Ветка false для label_847"
    menu:
        "Go back":
            $ strength += 2
            jump label_852
        "Open door":
            jump label_853
        "Explore":
            $ charisma += 1
            jump label_854

label label_852:
    "Scene label_852"
    jump end_855

label label_853:
    "Scene label_853"
    jump end_855

label label_854:
    "Scene label_854"
    jump end_855

label label_786:
    "Scene label_786"
    if luck >= 8:
        jump label_855

label label_855:
    $ luck += 4
    menu:
        "Talk":
            jump label_856
        "Pick up item":
            jump label_857
        "Pick up item":
            jump label_858
        "Use item":
            $ luck += 3
            jump label_859

label label_856:
    "Scene label_856"
    if charisma >= 6:
        jump label_860

label label_860:
    $ charisma += 4
    jump end_861

    jump label_861

label label_861:
    "Ветка false для label_860"
    jump end_862

label label_857:
    "Scene label_857"
    if luck >= 18:
        jump label_862

label label_862:
    $ luck += 5
    jump end_863

    jump label_863

label label_863:
    "Ветка false для label_862"
    jump end_864

label label_858:
    "Scene label_858"
    menu:
        "Open door":
            $ strength += 2
            jump label_864
        "Pick up item":
            jump label_865
        "Explore":
            jump label_866

label label_864:
    "Scene label_864"
    jump end_867

label label_865:
    "Scene label_865"
    jump end_867

label label_866:
    "Scene label_866"
    jump end_867

label label_859:
    "Scene label_859"
    if charisma >= 18:
        jump label_867

label label_867:
    $ charisma += 3
    jump end_868

    jump label_868

label label_868:
    "Ветка false для label_867"
    jump end_869

    jump label_869

label label_869:
    "Ветка false для label_855"
    menu:
        "Use item":
            jump label_870
        "Look around":
            jump label_871

label label_870:
    "Scene label_870"
    menu:
        "Talk":
            jump label_872
        "Go forward":
            jump label_873
        "Go forward":
            jump label_874

label label_872:
    "Scene label_872"
    jump end_875

label label_873:
    "Scene label_873"
    jump end_875

label label_874:
    "Scene label_874"
    jump end_875

label label_871:
    "Scene label_871"
    if luck >= 16:
        jump label_875

label label_875:
    $ luck += 2
    jump end_876

    jump label_876

label label_876:
    "Ветка false для label_875"
    jump end_877

label label_787:
    "Scene label_787"
    menu:
        "Use item":
            $ intelligence += 1
            jump label_877
        "Open door":
            jump label_878
        "Use item":
            $ intelligence += 2
            jump label_879
        "Explore":
            $ intelligence += 1
            jump label_880

label label_877:
    "Scene label_877"
    if strength >= 8:
        jump label_881

label label_881:
    $ strength += 5
    menu:
        "Talk":
            $ strength += 1
            jump label_882
        "Use item":
            $ strength += 2
            jump label_883

label label_882:
    "Scene label_882"
    jump end_884

label label_883:
    "Scene label_883"
    jump end_884

    jump label_884

label label_884:
    "Ветка false для label_881"
    menu:
        "Go back":
            jump label_885
        "Look around":
            $ charisma += 1
            jump label_886

label label_885:
    "Scene label_885"
    jump end_887

label label_886:
    "Scene label_886"
    jump end_887

label label_878:
    "Scene label_878"
    if intelligence >= 8:
        jump label_887

label label_887:
    $ intelligence += 5
    if luck >= 15:
        jump label_888

label label_888:
    $ luck += 5
    jump end_889

    jump label_889

label label_889:
    "Ветка false для label_888"
    jump end_890

    jump label_890

label label_890:
    "Ветка false для label_887"
    menu:
        "Go back":
            $ intelligence += 1
            jump label_891
        "Go back":
            jump label_892

label label_891:
    "Scene label_891"
    jump end_893

label label_892:
    "Scene label_892"
    jump end_893

label label_879:
    "Scene label_879"
    menu:
        "Go back":
            $ intelligence += 2
            jump label_893
        "Go back":
            $ intelligence += 2
            jump label_894
        "Go forward":
            jump label_895

label label_893:
    "Scene label_893"
    menu:
        "Look around":
            $ strength += 2
            jump label_896
        "Use item":
            $ charisma += 3
            jump label_897
        "Look around":
            jump label_898

label label_896:
    "Scene label_896"
    jump end_899

label label_897:
    "Scene label_897"
    jump end_899

label label_898:
    "Scene label_898"
    jump end_899

label label_894:
    "Scene label_894"
    menu:
        "Look around":
            $ intelligence += 1
            jump label_899
        "Pick up item":
            jump label_900
        "Look around":
            $ charisma += 3
            jump label_901
        "Use item":
            $ charisma += 2
            jump label_902

label label_899:
    "Scene label_899"
    jump end_903

label label_900:
    "Scene label_900"
    jump end_903

label label_901:
    "Scene label_901"
    jump end_903

label label_902:
    "Scene label_902"
    jump end_903

label label_895:
    "Scene label_895"
    menu:
        "Explore":
            jump label_903
        "Go forward":
            $ charisma += 1
            jump label_904
        "Go back":
            jump label_905
        "Pick up item":
            jump label_906

label label_903:
    "Scene label_903"
    jump end_907

label label_904:
    "Scene label_904"
    jump end_907

label label_905:
    "Scene label_905"
    jump end_907

label label_906:
    "Scene label_906"
    jump end_907

label label_880:
    "Scene label_880"
    menu:
        "Use item":
            $ charisma += 3
            jump label_907
        "Look around":
            jump label_908
        "Open door":
            jump label_909
        "Open door":
            $ strength += 1
            jump label_910

label label_907:
    "Scene label_907"
    menu:
        "Talk":
            $ strength += 1
            jump label_911
        "Open door":
            $ charisma += 1
            jump label_912

label label_911:
    "Scene label_911"
    jump end_913

label label_912:
    "Scene label_912"
    jump end_913

label label_908:
    "Scene label_908"
    menu:
        "Open door":
            $ luck += 1
            jump label_913
        "Open door":
            jump label_914
        "Go back":
            jump label_915
        "Explore":
            jump label_916

label label_913:
    "Scene label_913"
    jump end_917

label label_914:
    "Scene label_914"
    jump end_917

label label_915:
    "Scene label_915"
    jump end_917

label label_916:
    "Scene label_916"
    jump end_917

label label_909:
    "Scene label_909"
    if luck >= 11:
        jump label_917

label label_917:
    $ luck += 4
    jump end_918

    jump label_918

label label_918:
    "Ветка false для label_917"
    jump end_919

label label_910:
    "Scene label_910"
    menu:
        "Pick up item":
            $ luck += 3
            jump label_919
        "Talk":
            $ charisma += 1
            jump label_920
        "Explore":
            $ intelligence += 2
            jump label_921

label label_919:
    "Scene label_919"
    jump end_922

label label_920:
    "Scene label_920"
    jump end_922

label label_921:
    "Scene label_921"
    jump end_922

label label_21:
    "Scene label_21"
    if strength >= 14:
        jump label_922

label label_922:
    $ strength += 3
    if strength >= 19:
        jump label_923

label label_923:
    $ strength += 4
    if charisma >= 10:
        jump label_924

label label_924:
    $ charisma += 2
    menu:
        "Use item":
            $ strength += 1
            jump label_925
        "Go back":
            $ charisma += 3
            jump label_926
        "Go back":
            $ charisma += 2
            jump label_927
        "Use item":
            $ intelligence += 1
            jump label_928

label label_925:
    "Scene label_925"
    menu:
        "Talk":
            $ strength += 1
            jump label_929
        "Open door":
            $ luck += 3
            jump label_930
        "Pick up item":
            $ strength += 1
            jump label_931

label label_929:
    "Scene label_929"
    menu:
        "Talk":
            $ charisma += 1
            jump label_932
        "Explore":
            $ strength += 1
            jump label_933

label label_932:
    "Scene label_932"
    jump end_934

label label_933:
    "Scene label_933"
    jump end_934

label label_930:
    "Scene label_930"
    menu:
        "Open door":
            jump label_934
        "Explore":
            $ strength += 1
            jump label_935
        "Open door":
            $ charisma += 3
            jump label_936

label label_934:
    "Scene label_934"
    jump end_937

label label_935:
    "Scene label_935"
    jump end_937

label label_936:
    "Scene label_936"
    jump end_937

label label_931:
    "Scene label_931"
    menu:
        "Explore":
            jump label_937
        "Use item":
            jump label_938
        "Go back":
            jump label_939

label label_937:
    "Scene label_937"
    jump end_940

label label_938:
    "Scene label_938"
    jump end_940

label label_939:
    "Scene label_939"
    jump end_940

label label_926:
    "Scene label_926"
    menu:
        "Pick up item":
            $ luck += 3
            jump label_940
        "Look around":
            jump label_941
        "Open door":
            jump label_942
        "Talk":
            $ luck += 2
            jump label_943

label label_940:
    "Scene label_940"
    menu:
        "Open door":
            $ intelligence += 2
            jump label_944
        "Explore":
            $ strength += 1
            jump label_945
        "Pick up item":
            $ intelligence += 1
            jump label_946

label label_944:
    "Scene label_944"
    jump end_947

label label_945:
    "Scene label_945"
    jump end_947

label label_946:
    "Scene label_946"
    jump end_947

label label_941:
    "Scene label_941"
    menu:
        "Look around":
            jump label_947
        "Go back":
            jump label_948
        "Go forward":
            jump label_949

label label_947:
    "Scene label_947"
    jump end_950

label label_948:
    "Scene label_948"
    jump end_950

label label_949:
    "Scene label_949"
    jump end_950

label label_942:
    "Scene label_942"
    if luck >= 20:
        jump label_950

label label_950:
    $ luck += 5
    jump end_951

    jump label_951

label label_951:
    "Ветка false для label_950"
    jump end_952

label label_943:
    "Scene label_943"
    if luck >= 13:
        jump label_952

label label_952:
    $ luck += 2
    jump end_953

    jump label_953

label label_953:
    "Ветка false для label_952"
    jump end_954

label label_927:
    "Scene label_927"
    menu:
        "Pick up item":
            jump label_954
        "Pick up item":
            $ charisma += 3
            jump label_955

label label_954:
    "Scene label_954"
    menu:
        "Look around":
            $ strength += 3
            jump label_956
        "Talk":
            jump label_957
        "Talk":
            jump label_958
        "Talk":
            $ strength += 1
            jump label_959

label label_956:
    "Scene label_956"
    jump end_960

label label_957:
    "Scene label_957"
    jump end_960

label label_958:
    "Scene label_958"
    jump end_960

label label_959:
    "Scene label_959"
    jump end_960

label label_955:
    "Scene label_955"
    menu:
        "Go forward":
            $ luck += 1
            jump label_960
        "Go forward":
            $ luck += 3
            jump label_961
        "Talk":
            jump label_962
        "Explore":
            jump label_963

label label_960:
    "Scene label_960"
    jump end_964

label label_961:
    "Scene label_961"
    jump end_964

label label_962:
    "Scene label_962"
    jump end_964

label label_963:
    "Scene label_963"
    jump end_964

label label_928:
    "Scene label_928"
    menu:
        "Open door":
            jump label_964
        "Go forward":
            $ intelligence += 3
            jump label_965
        "Go back":
            $ charisma += 1
            jump label_966

label label_964:
    "Scene label_964"
    if intelligence >= 18:
        jump label_967

label label_967:
    $ intelligence += 3
    jump end_968

    jump label_968

label label_968:
    "Ветка false для label_967"
    jump end_969

label label_965:
    "Scene label_965"
    menu:
        "Go back":
            $ luck += 1
            jump label_969
        "Explore":
            $ strength += 3
            jump label_970

label label_969:
    "Scene label_969"
    jump end_971

label label_970:
    "Scene label_970"
    jump end_971

label label_966:
    "Scene label_966"
    menu:
        "Look around":
            jump label_971
        "Talk":
            jump label_972

label label_971:
    "Scene label_971"
    jump end_973

label label_972:
    "Scene label_972"
    jump end_973

    jump label_973

label label_973:
    "Ветка false для label_924"
    if strength >= 10:
        jump label_974

label label_974:
    $ strength += 2
    if luck >= 19:
        jump label_975

label label_975:
    $ luck += 2
    menu:
        "Go back":
            jump label_976
        "Use item":
            jump label_977

label label_976:
    "Scene label_976"
    jump end_978

label label_977:
    "Scene label_977"
    jump end_978

    jump label_978

label label_978:
    "Ветка false для label_975"
    menu:
        "Go forward":
            $ luck += 1
            jump label_979
        "Go back":
            $ luck += 2
            jump label_980
        "Use item":
            jump label_981

label label_979:
    "Scene label_979"
    jump end_982

label label_980:
    "Scene label_980"
    jump end_982

label label_981:
    "Scene label_981"
    jump end_982

    jump label_982

label label_982:
    "Ветка false для label_974"
    if intelligence >= 10:
        jump label_983

label label_983:
    $ intelligence += 4
    if charisma >= 13:
        jump label_984

label label_984:
    $ charisma += 2
    jump end_985

    jump label_985

label label_985:
    "Ветка false для label_984"
    jump end_986

    jump label_986

label label_986:
    "Ветка false для label_983"
    menu:
        "Explore":
            $ charisma += 3
            jump label_987
        "Talk":
            $ charisma += 1
            jump label_988
        "Use item":
            jump label_989
        "Open door":
            $ luck += 1
            jump label_990

label label_987:
    "Scene label_987"
    jump end_991

label label_988:
    "Scene label_988"
    jump end_991

label label_989:
    "Scene label_989"
    jump end_991

label label_990:
    "Scene label_990"
    jump end_991

    jump label_991

label label_991:
    "Ветка false для label_923"
    menu:
        "Go back":
            $ intelligence += 2
            jump label_992
        "Use item":
            $ strength += 1
            jump label_993
        "Talk":
            $ charisma += 3
            jump label_994
        "Explore":
            $ charisma += 3
            jump label_995

label label_992:
    "Scene label_992"
    menu:
        "Explore":
            jump label_996
        "Explore":
            jump label_997

label label_996:
    "Scene label_996"
    if charisma >= 20:
        jump label_998

label label_998:
    $ charisma += 4
    menu:
        "Talk":
            jump label_999
        "Go back":
            $ intelligence += 1
            jump label_1000

label label_999:
    "Scene label_999"
    jump end_1001

label label_1000:
    "Scene label_1000"
    jump end_1001

    jump label_1001

label label_1001:
    "Ветка false для label_998"
    menu:
        "Pick up item":
            jump label_1002
        "Open door":
            jump label_1003
        "Pick up item":
            jump label_1004
        "Go back":
            jump label_1005

label label_1002:
    "Scene label_1002"
    jump end_1006

label label_1003:
    "Scene label_1003"
    jump end_1006

label label_1004:
    "Scene label_1004"
    jump end_1006

label label_1005:
    "Scene label_1005"
    jump end_1006

label label_997:
    "Scene label_997"
    menu:
        "Open door":
            $ intelligence += 3
            jump label_1006
        "Look around":
            $ luck += 3
            jump label_1007
        "Open door":
            jump label_1008

label label_1006:
    "Scene label_1006"
    if intelligence >= 14:
        jump label_1009

label label_1009:
    $ intelligence += 3
    jump end_1010

    jump label_1010

label label_1010:
    "Ветка false для label_1009"
    jump end_1011

label label_1007:
    "Scene label_1007"
    menu:
        "Talk":
            $ luck += 1
            jump label_1011
        "Look around":
            $ intelligence += 2
            jump label_1012
        "Pick up item":
            $ charisma += 1
            jump label_1013
        "Talk":
            $ intelligence += 2
            jump label_1014

label label_1011:
    "Scene label_1011"
    jump end_1015

label label_1012:
    "Scene label_1012"
    jump end_1015

label label_1013:
    "Scene label_1013"
    jump end_1015

label label_1014:
    "Scene label_1014"
    jump end_1015

label label_1008:
    "Scene label_1008"
    menu:
        "Use item":
            jump label_1015
        "Open door":
            $ intelligence += 1
            jump label_1016

label label_1015:
    "Scene label_1015"
    jump end_1017

label label_1016:
    "Scene label_1016"
    jump end_1017

label label_993:
    "Scene label_993"
    menu:
        "Go forward":
            $ luck += 1
            jump label_1017
        "Pick up item":
            jump label_1018
        "Open door":
            jump label_1019

label label_1017:
    "Scene label_1017"
    menu:
        "Open door":
            jump label_1020
        "Use item":
            jump label_1021
        "Look around":
            $ luck += 1
            jump label_1022
        "Open door":
            jump label_1023

label label_1020:
    "Scene label_1020"
    menu:
        "Open door":
            jump label_1024
        "Look around":
            $ strength += 1
            jump label_1025
        "Talk":
            jump label_1026
        "Explore":
            $ strength += 3
            jump label_1027

label label_1024:
    "Scene label_1024"
    jump end_1028

label label_1025:
    "Scene label_1025"
    jump end_1028

label label_1026:
    "Scene label_1026"
    jump end_1028

label label_1027:
    "Scene label_1027"
    jump end_1028

label label_1021:
    "Scene label_1021"
    menu:
        "Look around":
            jump label_1028
        "Talk":
            $ strength += 1
            jump label_1029
        "Go back":
            $ luck += 2
            jump label_1030

label label_1028:
    "Scene label_1028"
    jump end_1031

label label_1029:
    "Scene label_1029"
    jump end_1031

label label_1030:
    "Scene label_1030"
    jump end_1031

label label_1022:
    "Scene label_1022"
    menu:
        "Talk":
            $ charisma += 3
            jump label_1031
        "Pick up item":
            $ charisma += 1
            jump label_1032
        "Talk":
            $ strength += 2
            jump label_1033

label label_1031:
    "Scene label_1031"
    jump end_1034

label label_1032:
    "Scene label_1032"
    jump end_1034

label label_1033:
    "Scene label_1033"
    jump end_1034

label label_1023:
    "Scene label_1023"
    menu:
        "Look around":
            jump label_1034
        "Open door":
            jump label_1035
        "Go forward":
            $ intelligence += 3
            jump label_1036

label label_1034:
    "Scene label_1034"
    jump end_1037

label label_1035:
    "Scene label_1035"
    jump end_1037

label label_1036:
    "Scene label_1036"
    jump end_1037

label label_1018:
    "Scene label_1018"
    menu:
        "Pick up item":
            $ charisma += 2
            jump label_1037
        "Go forward":
            $ luck += 3
            jump label_1038
        "Look around":
            jump label_1039
        "Pick up item":
            jump label_1040

label label_1037:
    "Scene label_1037"
    menu:
        "Explore":
            jump label_1041
        "Explore":
            $ intelligence += 2
            jump label_1042
        "Open door":
            jump label_1043
        "Look around":
            $ luck += 3
            jump label_1044

label label_1041:
    "Scene label_1041"
    jump end_1045

label label_1042:
    "Scene label_1042"
    jump end_1045

label label_1043:
    "Scene label_1043"
    jump end_1045

label label_1044:
    "Scene label_1044"
    jump end_1045

label label_1038:
    "Scene label_1038"
    menu:
        "Pick up item":
            $ charisma += 2
            jump label_1045
        "Go forward":
            $ charisma += 2
            jump label_1046

label label_1045:
    "Scene label_1045"
    jump end_1047

label label_1046:
    "Scene label_1046"
    jump end_1047

label label_1039:
    "Scene label_1039"
    menu:
        "Explore":
            $ luck += 3
            jump label_1047
        "Go back":
            jump label_1048
        "Go forward":
            jump label_1049
        "Talk":
            $ charisma += 1
            jump label_1050

label label_1047:
    "Scene label_1047"
    jump end_1051

label label_1048:
    "Scene label_1048"
    jump end_1051

label label_1049:
    "Scene label_1049"
    jump end_1051

label label_1050:
    "Scene label_1050"
    jump end_1051

label label_1040:
    "Scene label_1040"
    menu:
        "Go forward":
            jump label_1051
        "Explore":
            jump label_1052
        "Open door":
            $ strength += 3
            jump label_1053

label label_1051:
    "Scene label_1051"
    jump end_1054

label label_1052:
    "Scene label_1052"
    jump end_1054

label label_1053:
    "Scene label_1053"
    jump end_1054

label label_1019:
    "Scene label_1019"
    if intelligence >= 20:
        jump label_1054

label label_1054:
    $ intelligence += 5
    menu:
        "Pick up item":
            jump label_1055
        "Use item":
            jump label_1056
        "Pick up item":
            $ luck += 2
            jump label_1057

label label_1055:
    "Scene label_1055"
    jump end_1058

label label_1056:
    "Scene label_1056"
    jump end_1058

label label_1057:
    "Scene label_1057"
    jump end_1058

    jump label_1058

label label_1058:
    "Ветка false для label_1054"
    if strength >= 17:
        jump label_1059

label label_1059:
    $ strength += 2
    jump end_1060

    jump label_1060

label label_1060:
    "Ветка false для label_1059"
    jump end_1061

label label_994:
    "Scene label_994"
    menu:
        "Go back":
            $ strength += 1
            jump label_1061
        "Go back":
            jump label_1062
        "Look around":
            jump label_1063
        "Open door":
            jump label_1064

label label_1061:
    "Scene label_1061"
    menu:
        "Go back":
            jump label_1065
        "Use item":
            jump label_1066
        "Go forward":
            $ charisma += 1
            jump label_1067
        "Open door":
            $ intelligence += 2
            jump label_1068

label label_1065:
    "Scene label_1065"
    menu:
        "Open door":
            jump label_1069
        "Go back":
            $ charisma += 1
            jump label_1070

label label_1069:
    "Scene label_1069"
    jump end_1071

label label_1070:
    "Scene label_1070"
    jump end_1071

label label_1066:
    "Scene label_1066"
    if charisma >= 9:
        jump label_1071

label label_1071:
    $ charisma += 4
    jump end_1072

    jump label_1072

label label_1072:
    "Ветка false для label_1071"
    jump end_1073

label label_1067:
    "Scene label_1067"
    if luck >= 8:
        jump label_1073

label label_1073:
    $ luck += 3
    jump end_1074

    jump label_1074

label label_1074:
    "Ветка false для label_1073"
    jump end_1075

label label_1068:
    "Scene label_1068"
    if luck >= 12:
        jump label_1075

label label_1075:
    $ luck += 2
    jump end_1076

    jump label_1076

label label_1076:
    "Ветка false для label_1075"
    jump end_1077

label label_1062:
    "Scene label_1062"
    menu:
        "Pick up item":
            jump label_1077
        "Explore":
            jump label_1078
        "Pick up item":
            jump label_1079
        "Go forward":
            $ luck += 2
            jump label_1080

label label_1077:
    "Scene label_1077"
    menu:
        "Pick up item":
            jump label_1081
        "Pick up item":
            $ intelligence += 3
            jump label_1082

label label_1081:
    "Scene label_1081"
    jump end_1083

label label_1082:
    "Scene label_1082"
    jump end_1083

label label_1078:
    "Scene label_1078"
    menu:
        "Go forward":
            jump label_1083
        "Look around":
            jump label_1084
        "Explore":
            $ luck += 2
            jump label_1085

label label_1083:
    "Scene label_1083"
    jump end_1086

label label_1084:
    "Scene label_1084"
    jump end_1086

label label_1085:
    "Scene label_1085"
    jump end_1086

label label_1079:
    "Scene label_1079"
    if luck >= 19:
        jump label_1086

label label_1086:
    $ luck += 5
    jump end_1087

    jump label_1087

label label_1087:
    "Ветка false для label_1086"
    jump end_1088

label label_1080:
    "Scene label_1080"
    if intelligence >= 16:
        jump label_1088

label label_1088:
    $ intelligence += 5
    jump end_1089

    jump label_1089

label label_1089:
    "Ветка false для label_1088"
    jump end_1090

label label_1063:
    "Scene label_1063"
    menu:
        "Go back":
            jump label_1090
        "Pick up item":
            jump label_1091

label label_1090:
    "Scene label_1090"
    menu:
        "Talk":
            $ strength += 1
            jump label_1092
        "Open door":
            $ strength += 3
            jump label_1093
        "Go back":
            $ intelligence += 3
            jump label_1094
        "Open door":
            jump label_1095

label label_1092:
    "Scene label_1092"
    jump end_1096

label label_1093:
    "Scene label_1093"
    jump end_1096

label label_1094:
    "Scene label_1094"
    jump end_1096

label label_1095:
    "Scene label_1095"
    jump end_1096

label label_1091:
    "Scene label_1091"
    menu:
        "Open door":
            jump label_1096
        "Go back":
            $ luck += 3
            jump label_1097

label label_1096:
    "Scene label_1096"
    jump end_1098

label label_1097:
    "Scene label_1097"
    jump end_1098

label label_1064:
    "Scene label_1064"
    if luck >= 17:
        jump label_1098

label label_1098:
    $ luck += 3
    menu:
        "Pick up item":
            $ charisma += 1
            jump label_1099
        "Talk":
            $ strength += 3
            jump label_1100
        "Explore":
            jump label_1101

label label_1099:
    "Scene label_1099"
    jump end_1102

label label_1100:
    "Scene label_1100"
    jump end_1102

label label_1101:
    "Scene label_1101"
    jump end_1102

    jump label_1102

label label_1102:
    "Ветка false для label_1098"
    menu:
        "Look around":
            $ charisma += 2
            jump label_1103
        "Open door":
            $ strength += 3
            jump label_1104
        "Use item":
            $ strength += 3
            jump label_1105
        "Open door":
            jump label_1106

label label_1103:
    "Scene label_1103"
    jump end_1107

label label_1104:
    "Scene label_1104"
    jump end_1107

label label_1105:
    "Scene label_1105"
    jump end_1107

label label_1106:
    "Scene label_1106"
    jump end_1107

label label_995:
    "Scene label_995"
    menu:
        "Talk":
            jump label_1107
        "Pick up item":
            jump label_1108

label label_1107:
    "Scene label_1107"
    menu:
        "Open door":
            jump label_1109
        "Use item":
            jump label_1110

label label_1109:
    "Scene label_1109"
    if luck >= 12:
        jump label_1111

label label_1111:
    $ luck += 3
    jump end_1112

    jump label_1112

label label_1112:
    "Ветка false для label_1111"
    jump end_1113

label label_1110:
    "Scene label_1110"
    menu:
        "Use item":
            $ luck += 1
            jump label_1113
        "Go forward":
            $ charisma += 2
            jump label_1114
        "Use item":
            jump label_1115
        "Pick up item":
            jump label_1116

label label_1113:
    "Scene label_1113"
    jump end_1117

label label_1114:
    "Scene label_1114"
    jump end_1117

label label_1115:
    "Scene label_1115"
    jump end_1117

label label_1116:
    "Scene label_1116"
    jump end_1117

label label_1108:
    "Scene label_1108"
    menu:
        "Look around":
            jump label_1117
        "Explore":
            jump label_1118
        "Talk":
            $ strength += 1
            jump label_1119

label label_1117:
    "Scene label_1117"
    menu:
        "Open door":
            jump label_1120
        "Pick up item":
            jump label_1121
        "Look around":
            jump label_1122
        "Go back":
            jump label_1123

label label_1120:
    "Scene label_1120"
    jump end_1124

label label_1121:
    "Scene label_1121"
    jump end_1124

label label_1122:
    "Scene label_1122"
    jump end_1124

label label_1123:
    "Scene label_1123"
    jump end_1124

label label_1118:
    "Scene label_1118"
    menu:
        "Go forward":
            $ strength += 2
            jump label_1124
        "Open door":
            jump label_1125
        "Go forward":
            $ charisma += 2
            jump label_1126
        "Look around":
            $ luck += 3
            jump label_1127

label label_1124:
    "Scene label_1124"
    jump end_1128

label label_1125:
    "Scene label_1125"
    jump end_1128

label label_1126:
    "Scene label_1126"
    jump end_1128

label label_1127:
    "Scene label_1127"
    jump end_1128

label label_1119:
    "Scene label_1119"
    menu:
        "Talk":
            $ luck += 1
            jump label_1128
        "Use item":
            jump label_1129

label label_1128:
    "Scene label_1128"
    jump end_1130

label label_1129:
    "Scene label_1129"
    jump end_1130

    jump label_1130

label label_1130:
    "Ветка false для label_922"
    if strength >= 15:
        jump label_1131

label label_1131:
    $ strength += 2
    menu:
        "Pick up item":
            jump label_1132
        "Go back":
            $ charisma += 2
            jump label_1133
        "Pick up item":
            jump label_1134
        "Go back":
            jump label_1135

label label_1132:
    "Scene label_1132"
    menu:
        "Go back":
            $ luck += 3
            jump label_1136
        "Explore":
            jump label_1137

label label_1136:
    "Scene label_1136"
    menu:
        "Talk":
            jump label_1138
        "Go back":
            $ charisma += 3
            jump label_1139
        "Go back":
            $ intelligence += 1
            jump label_1140
        "Go back":
            jump label_1141

label label_1138:
    "Scene label_1138"
    if intelligence >= 5:
        jump label_1142

label label_1142:
    $ intelligence += 3
    jump end_1143

    jump label_1143

label label_1143:
    "Ветка false для label_1142"
    jump end_1144

label label_1139:
    "Scene label_1139"
    menu:
        "Go forward":
            $ charisma += 2
            jump label_1144
        "Talk":
            jump label_1145

label label_1144:
    "Scene label_1144"
    jump end_1146

label label_1145:
    "Scene label_1145"
    jump end_1146

label label_1140:
    "Scene label_1140"
    menu:
        "Explore":
            jump label_1146
        "Open door":
            jump label_1147
        "Pick up item":
            jump label_1148
        "Pick up item":
            $ charisma += 1
            jump label_1149

label label_1146:
    "Scene label_1146"
    jump end_1150

label label_1147:
    "Scene label_1147"
    jump end_1150

label label_1148:
    "Scene label_1148"
    jump end_1150

label label_1149:
    "Scene label_1149"
    jump end_1150

label label_1141:
    "Scene label_1141"
    menu:
        "Explore":
            $ intelligence += 1
            jump label_1150
        "Talk":
            $ strength += 3
            jump label_1151

label label_1150:
    "Scene label_1150"
    jump end_1152

label label_1151:
    "Scene label_1151"
    jump end_1152

label label_1137:
    "Scene label_1137"
    if charisma >= 19:
        jump label_1152

label label_1152:
    $ charisma += 2
    menu:
        "Use item":
            jump label_1153
        "Explore":
            jump label_1154
        "Open door":
            jump label_1155
        "Explore":
            jump label_1156

label label_1153:
    "Scene label_1153"
    jump end_1157

label label_1154:
    "Scene label_1154"
    jump end_1157

label label_1155:
    "Scene label_1155"
    jump end_1157

label label_1156:
    "Scene label_1156"
    jump end_1157

    jump label_1157

label label_1157:
    "Ветка false для label_1152"
    if strength >= 6:
        jump label_1158

label label_1158:
    $ strength += 5
    jump end_1159

    jump label_1159

label label_1159:
    "Ветка false для label_1158"
    jump end_1160

label label_1133:
    "Scene label_1133"
    menu:
        "Use item":
            $ intelligence += 3
            jump label_1160
        "Use item":
            $ charisma += 1
            jump label_1161

label label_1160:
    "Scene label_1160"
    if luck >= 13:
        jump label_1162

label label_1162:
    $ luck += 2
    menu:
        "Look around":
            jump label_1163
        "Talk":
            jump label_1164
        "Go forward":
            $ intelligence += 3
            jump label_1165
        "Pick up item":
            $ strength += 2
            jump label_1166

label label_1163:
    "Scene label_1163"
    jump end_1167

label label_1164:
    "Scene label_1164"
    jump end_1167

label label_1165:
    "Scene label_1165"
    jump end_1167

label label_1166:
    "Scene label_1166"
    jump end_1167

    jump label_1167

label label_1167:
    "Ветка false для label_1162"
    menu:
        "Use item":
            $ charisma += 1
            jump label_1168
        "Pick up item":
            $ intelligence += 3
            jump label_1169

label label_1168:
    "Scene label_1168"
    jump end_1170

label label_1169:
    "Scene label_1169"
    jump end_1170

label label_1161:
    "Scene label_1161"
    menu:
        "Go forward":
            jump label_1170
        "Look around":
            jump label_1171
        "Pick up item":
            jump label_1172
        "Use item":
            jump label_1173

label label_1170:
    "Scene label_1170"
    menu:
        "Go forward":
            $ charisma += 3
            jump label_1174
        "Go back":
            $ intelligence += 2
            jump label_1175
        "Pick up item":
            jump label_1176

label label_1174:
    "Scene label_1174"
    jump end_1177

label label_1175:
    "Scene label_1175"
    jump end_1177

label label_1176:
    "Scene label_1176"
    jump end_1177

label label_1171:
    "Scene label_1171"
    menu:
        "Go back":
            jump label_1177
        "Use item":
            $ luck += 3
            jump label_1178
        "Pick up item":
            $ intelligence += 2
            jump label_1179

label label_1177:
    "Scene label_1177"
    jump end_1180

label label_1178:
    "Scene label_1178"
    jump end_1180

label label_1179:
    "Scene label_1179"
    jump end_1180

label label_1172:
    "Scene label_1172"
    if charisma >= 20:
        jump label_1180

label label_1180:
    $ charisma += 3
    jump end_1181

    jump label_1181

label label_1181:
    "Ветка false для label_1180"
    jump end_1182

label label_1173:
    "Scene label_1173"
    if charisma >= 14:
        jump label_1182

label label_1182:
    $ charisma += 2
    jump end_1183

    jump label_1183

label label_1183:
    "Ветка false для label_1182"
    jump end_1184

label label_1134:
    "Scene label_1134"
    menu:
        "Explore":
            jump label_1184
        "Talk":
            $ strength += 1
            jump label_1185
        "Use item":
            $ luck += 2
            jump label_1186

label label_1184:
    "Scene label_1184"
    menu:
        "Look around":
            jump label_1187
        "Use item":
            jump label_1188
        "Talk":
            $ intelligence += 2
            jump label_1189

label label_1187:
    "Scene label_1187"
    menu:
        "Talk":
            $ charisma += 3
            jump label_1190
        "Open door":
            jump label_1191

label label_1190:
    "Scene label_1190"
    jump end_1192

label label_1191:
    "Scene label_1191"
    jump end_1192

label label_1188:
    "Scene label_1188"
    if luck >= 20:
        jump label_1192

label label_1192:
    $ luck += 4
    jump end_1193

    jump label_1193

label label_1193:
    "Ветка false для label_1192"
    jump end_1194

label label_1189:
    "Scene label_1189"
    menu:
        "Explore":
            jump label_1194
        "Explore":
            $ charisma += 3
            jump label_1195
        "Open door":
            jump label_1196

label label_1194:
    "Scene label_1194"
    jump end_1197

label label_1195:
    "Scene label_1195"
    jump end_1197

label label_1196:
    "Scene label_1196"
    jump end_1197

label label_1185:
    "Scene label_1185"
    if charisma >= 6:
        jump label_1197

label label_1197:
    $ charisma += 5
    menu:
        "Pick up item":
            jump label_1198
        "Go forward":
            jump label_1199

label label_1198:
    "Scene label_1198"
    jump end_1200

label label_1199:
    "Scene label_1199"
    jump end_1200

    jump label_1200

label label_1200:
    "Ветка false для label_1197"
    if luck >= 14:
        jump label_1201

label label_1201:
    $ luck += 4
    jump end_1202

    jump label_1202

label label_1202:
    "Ветка false для label_1201"
    jump end_1203

label label_1186:
    "Scene label_1186"
    if charisma >= 17:
        jump label_1203

label label_1203:
    $ charisma += 4
    menu:
        "Use item":
            jump label_1204
        "Pick up item":
            jump label_1205
        "Look around":
            $ intelligence += 2
            jump label_1206
        "Pick up item":
            jump label_1207

label label_1204:
    "Scene label_1204"
    jump end_1208

label label_1205:
    "Scene label_1205"
    jump end_1208

label label_1206:
    "Scene label_1206"
    jump end_1208

label label_1207:
    "Scene label_1207"
    jump end_1208

    jump label_1208

label label_1208:
    "Ветка false для label_1203"
    menu:
        "Open door":
            jump label_1209
        "Pick up item":
            $ charisma += 1
            jump label_1210

label label_1209:
    "Scene label_1209"
    jump end_1211

label label_1210:
    "Scene label_1210"
    jump end_1211

label label_1135:
    "Scene label_1135"
    if luck >= 13:
        jump label_1211

label label_1211:
    $ luck += 4
    menu:
        "Look around":
            $ strength += 2
            jump label_1212
        "Open door":
            jump label_1213
        "Talk":
            jump label_1214

label label_1212:
    "Scene label_1212"
    menu:
        "Look around":
            $ luck += 3
            jump label_1215
        "Go back":
            jump label_1216
        "Go back":
            jump label_1217
        "Talk":
            jump label_1218

label label_1215:
    "Scene label_1215"
    jump end_1219

label label_1216:
    "Scene label_1216"
    jump end_1219

label label_1217:
    "Scene label_1217"
    jump end_1219

label label_1218:
    "Scene label_1218"
    jump end_1219

label label_1213:
    "Scene label_1213"
    if luck >= 16:
        jump label_1219

label label_1219:
    $ luck += 5
    jump end_1220

    jump label_1220

label label_1220:
    "Ветка false для label_1219"
    jump end_1221

label label_1214:
    "Scene label_1214"
    menu:
        "Talk":
            $ intelligence += 2
            jump label_1221
        "Explore":
            $ luck += 2
            jump label_1222

label label_1221:
    "Scene label_1221"
    jump end_1223

label label_1222:
    "Scene label_1222"
    jump end_1223

    jump label_1223

label label_1223:
    "Ветка false для label_1211"
    menu:
        "Talk":
            $ charisma += 2
            jump label_1224
        "Open door":
            jump label_1225

label label_1224:
    "Scene label_1224"
    menu:
        "Go forward":
            jump label_1226
        "Explore":
            $ charisma += 1
            jump label_1227
        "Explore":
            jump label_1228
        "Pick up item":
            $ luck += 3
            jump label_1229

label label_1226:
    "Scene label_1226"
    jump end_1230

label label_1227:
    "Scene label_1227"
    jump end_1230

label label_1228:
    "Scene label_1228"
    jump end_1230

label label_1229:
    "Scene label_1229"
    jump end_1230

label label_1225:
    "Scene label_1225"
    if strength >= 7:
        jump label_1230

label label_1230:
    $ strength += 2
    jump end_1231

    jump label_1231

label label_1231:
    "Ветка false для label_1230"
    jump end_1232

    jump label_1232

label label_1232:
    "Ветка false для label_1131"
    menu:
        "Look around":
            jump label_1233
        "Pick up item":
            jump label_1234
        "Use item":
            jump label_1235
        "Open door":
            jump label_1236

label label_1233:
    "Scene label_1233"
    menu:
        "Talk":
            jump label_1237
        "Look around":
            $ luck += 2
            jump label_1238
        "Open door":
            jump label_1239
        "Open door":
            jump label_1240

label label_1237:
    "Scene label_1237"
    if charisma >= 5:
        jump label_1241

label label_1241:
    $ charisma += 2
    if charisma >= 9:
        jump label_1242

label label_1242:
    $ charisma += 4
    jump end_1243

    jump label_1243

label label_1243:
    "Ветка false для label_1242"
    jump end_1244

    jump label_1244

label label_1244:
    "Ветка false для label_1241"
    menu:
        "Explore":
            jump label_1245
        "Use item":
            jump label_1246
        "Explore":
            jump label_1247
        "Talk":
            $ intelligence += 1
            jump label_1248

label label_1245:
    "Scene label_1245"
    jump end_1249

label label_1246:
    "Scene label_1246"
    jump end_1249

label label_1247:
    "Scene label_1247"
    jump end_1249

label label_1248:
    "Scene label_1248"
    jump end_1249

label label_1238:
    "Scene label_1238"
    menu:
        "Go forward":
            jump label_1249
        "Go forward":
            jump label_1250

label label_1249:
    "Scene label_1249"
    menu:
        "Explore":
            jump label_1251
        "Use item":
            jump label_1252

label label_1251:
    "Scene label_1251"
    jump end_1253

label label_1252:
    "Scene label_1252"
    jump end_1253

label label_1250:
    "Scene label_1250"
    if intelligence >= 18:
        jump label_1253

label label_1253:
    $ intelligence += 4
    jump end_1254

    jump label_1254

label label_1254:
    "Ветка false для label_1253"
    jump end_1255

label label_1239:
    "Scene label_1239"
    if intelligence >= 16:
        jump label_1255

label label_1255:
    $ intelligence += 2
    if charisma >= 8:
        jump label_1256

label label_1256:
    $ charisma += 5
    jump end_1257

    jump label_1257

label label_1257:
    "Ветка false для label_1256"
    jump end_1258

    jump label_1258

label label_1258:
    "Ветка false для label_1255"
    if intelligence >= 17:
        jump label_1259

label label_1259:
    $ intelligence += 2
    jump end_1260

    jump label_1260

label label_1260:
    "Ветка false для label_1259"
    jump end_1261

label label_1240:
    "Scene label_1240"
    menu:
        "Use item":
            $ charisma += 3
            jump label_1261
        "Look around":
            $ intelligence += 3
            jump label_1262
        "Look around":
            $ intelligence += 1
            jump label_1263

label label_1261:
    "Scene label_1261"
    menu:
        "Explore":
            jump label_1264
        "Explore":
            $ intelligence += 1
            jump label_1265
        "Explore":
            $ strength += 2
            jump label_1266
        "Go forward":
            $ charisma += 2
            jump label_1267

label label_1264:
    "Scene label_1264"
    jump end_1268

label label_1265:
    "Scene label_1265"
    jump end_1268

label label_1266:
    "Scene label_1266"
    jump end_1268

label label_1267:
    "Scene label_1267"
    jump end_1268

label label_1262:
    "Scene label_1262"
    menu:
        "Explore":
            $ luck += 1
            jump label_1268
        "Open door":
            jump label_1269

label label_1268:
    "Scene label_1268"
    jump end_1270

label label_1269:
    "Scene label_1269"
    jump end_1270

label label_1263:
    "Scene label_1263"
    menu:
        "Look around":
            jump label_1270
        "Open door":
            jump label_1271

label label_1270:
    "Scene label_1270"
    jump end_1272

label label_1271:
    "Scene label_1271"
    jump end_1272

label label_1234:
    "Scene label_1234"
    if luck >= 15:
        jump label_1272

label label_1272:
    $ luck += 2
    if intelligence >= 10:
        jump label_1273

label label_1273:
    $ intelligence += 2
    if intelligence >= 9:
        jump label_1274

label label_1274:
    $ intelligence += 5
    jump end_1275

    jump label_1275

label label_1275:
    "Ветка false для label_1274"
    jump end_1276

    jump label_1276

label label_1276:
    "Ветка false для label_1273"
    menu:
        "Use item":
            jump label_1277
        "Go back":
            $ charisma += 1
            jump label_1278

label label_1277:
    "Scene label_1277"
    jump end_1279

label label_1278:
    "Scene label_1278"
    jump end_1279

    jump label_1279

label label_1279:
    "Ветка false для label_1272"
    menu:
        "Talk":
            jump label_1280
        "Talk":
            $ strength += 1
            jump label_1281

label label_1280:
    "Scene label_1280"
    if intelligence >= 14:
        jump label_1282

label label_1282:
    $ intelligence += 5
    jump end_1283

    jump label_1283

label label_1283:
    "Ветка false для label_1282"
    jump end_1284

label label_1281:
    "Scene label_1281"
    menu:
        "Explore":
            $ strength += 2
            jump label_1284
        "Go forward":
            jump label_1285
        "Go forward":
            jump label_1286

label label_1284:
    "Scene label_1284"
    jump end_1287

label label_1285:
    "Scene label_1285"
    jump end_1287

label label_1286:
    "Scene label_1286"
    jump end_1287

label label_1235:
    "Scene label_1235"
    if charisma >= 6:
        jump label_1287

label label_1287:
    $ charisma += 5
    menu:
        "Talk":
            $ strength += 2
            jump label_1288
        "Use item":
            $ strength += 1
            jump label_1289
        "Pick up item":
            $ charisma += 3
            jump label_1290
        "Pick up item":
            $ strength += 2
            jump label_1291

label label_1288:
    "Scene label_1288"
    menu:
        "Talk":
            $ luck += 3
            jump label_1292
        "Look around":
            $ intelligence += 1
            jump label_1293
        "Use item":
            jump label_1294

label label_1292:
    "Scene label_1292"
    jump end_1295

label label_1293:
    "Scene label_1293"
    jump end_1295

label label_1294:
    "Scene label_1294"
    jump end_1295

label label_1289:
    "Scene label_1289"
    menu:
        "Use item":
            jump label_1295
        "Look around":
            jump label_1296

label label_1295:
    "Scene label_1295"
    jump end_1297

label label_1296:
    "Scene label_1296"
    jump end_1297

label label_1290:
    "Scene label_1290"
    if strength >= 12:
        jump label_1297

label label_1297:
    $ strength += 3
    jump end_1298

    jump label_1298

label label_1298:
    "Ветка false для label_1297"
    jump end_1299

label label_1291:
    "Scene label_1291"
    if luck >= 15:
        jump label_1299

label label_1299:
    $ luck += 5
    jump end_1300

    jump label_1300

label label_1300:
    "Ветка false для label_1299"
    jump end_1301

    jump label_1301

label label_1301:
    "Ветка false для label_1287"
    menu:
        "Go back":
            jump label_1302
        "Talk":
            $ luck += 3
            jump label_1303
        "Talk":
            jump label_1304
        "Go forward":
            jump label_1305

label label_1302:
    "Scene label_1302"
    menu:
        "Go forward":
            jump label_1306
        "Talk":
            $ strength += 1
            jump label_1307
        "Talk":
            $ strength += 3
            jump label_1308
        "Pick up item":
            $ luck += 1
            jump label_1309

label label_1306:
    "Scene label_1306"
    jump end_1310

label label_1307:
    "Scene label_1307"
    jump end_1310

label label_1308:
    "Scene label_1308"
    jump end_1310

label label_1309:
    "Scene label_1309"
    jump end_1310

label label_1303:
    "Scene label_1303"
    menu:
        "Open door":
            $ intelligence += 2
            jump label_1310
        "Go back":
            jump label_1311
        "Look around":
            jump label_1312
        "Explore":
            $ intelligence += 2
            jump label_1313

label label_1310:
    "Scene label_1310"
    jump end_1314

label label_1311:
    "Scene label_1311"
    jump end_1314

label label_1312:
    "Scene label_1312"
    jump end_1314

label label_1313:
    "Scene label_1313"
    jump end_1314

label label_1304:
    "Scene label_1304"
    menu:
        "Pick up item":
            jump label_1314
        "Explore":
            jump label_1315
        "Go back":
            $ luck += 2
            jump label_1316

label label_1314:
    "Scene label_1314"
    jump end_1317

label label_1315:
    "Scene label_1315"
    jump end_1317

label label_1316:
    "Scene label_1316"
    jump end_1317

label label_1305:
    "Scene label_1305"
    menu:
        "Talk":
            $ charisma += 1
            jump label_1317
        "Look around":
            jump label_1318
        "Go back":
            $ luck += 2
            jump label_1319
        "Pick up item":
            $ strength += 3
            jump label_1320

label label_1317:
    "Scene label_1317"
    jump end_1321

label label_1318:
    "Scene label_1318"
    jump end_1321

label label_1319:
    "Scene label_1319"
    jump end_1321

label label_1320:
    "Scene label_1320"
    jump end_1321

label label_1236:
    "Scene label_1236"
    if intelligence >= 9:
        jump label_1321

label label_1321:
    $ intelligence += 3
    menu:
        "Explore":
            jump label_1322
        "Talk":
            jump label_1323

label label_1322:
    "Scene label_1322"
    menu:
        "Explore":
            jump label_1324
        "Talk":
            $ strength += 3
            jump label_1325

label label_1324:
    "Scene label_1324"
    jump end_1326

label label_1325:
    "Scene label_1325"
    jump end_1326

label label_1323:
    "Scene label_1323"
    if intelligence >= 9:
        jump label_1326

label label_1326:
    $ intelligence += 5
    jump end_1327

    jump label_1327

label label_1327:
    "Ветка false для label_1326"
    jump end_1328

    jump label_1328

label label_1328:
    "Ветка false для label_1321"
    menu:
        "Go forward":
            jump label_1329
        "Open door":
            $ charisma += 2
            jump label_1330
        "Pick up item":
            $ luck += 1
            jump label_1331

label label_1329:
    "Scene label_1329"
    if luck >= 11:
        jump label_1332

label label_1332:
    $ luck += 2
    jump end_1333

    jump label_1333

label label_1333:
    "Ветка false для label_1332"
    jump end_1334

label label_1330:
    "Scene label_1330"
    if charisma >= 9:
        jump label_1334

label label_1334:
    $ charisma += 3
    jump end_1335

    jump label_1335

label label_1335:
    "Ветка false для label_1334"
    jump end_1336

label label_1331:
    "Scene label_1331"
    menu:
        "Use item":
            $ intelligence += 3
            jump label_1336
        "Open door":
            $ intelligence += 1
            jump label_1337

label label_1336:
    "Scene label_1336"
    jump end_1338

label label_1337:
    "Scene label_1337"
    jump end_1338

label label_22:
    "Scene label_22"
    menu:
        "Use item":
            jump label_1338
        "Go back":
            $ charisma += 1
            jump label_1339

label label_1338:
    "Scene label_1338"
    menu:
        "Talk":
            $ intelligence += 3
            jump label_1340
        "Go back":
            jump label_1341
        "Go forward":
            jump label_1342
        "Go back":
            jump label_1343

label label_1340:
    "Scene label_1340"
    menu:
        "Pick up item":
            $ charisma += 2
            jump label_1344
        "Look around":
            jump label_1345
        "Pick up item":
            $ luck += 2
            jump label_1346
        "Go forward":
            $ luck += 1
            jump label_1347

label label_1344:
    "Scene label_1344"
    menu:
        "Talk":
            jump label_1348
        "Pick up item":
            jump label_1349
        "Use item":
            jump label_1350

label label_1348:
    "Scene label_1348"
    if luck >= 12:
        jump label_1351

label label_1351:
    $ luck += 5
    menu:
        "Open door":
            $ strength += 2
            jump label_1352
        "Go back":
            jump label_1353
        "Explore":
            $ luck += 2
            jump label_1354

label label_1352:
    "Scene label_1352"
    jump end_1355

label label_1353:
    "Scene label_1353"
    jump end_1355

label label_1354:
    "Scene label_1354"
    jump end_1355

    jump label_1355

label label_1355:
    "Ветка false для label_1351"
    if strength >= 20:
        jump label_1356

label label_1356:
    $ strength += 3
    jump end_1357

    jump label_1357

label label_1357:
    "Ветка false для label_1356"
    jump end_1358

label label_1349:
    "Scene label_1349"
    menu:
        "Open door":
            jump label_1358
        "Look around":
            jump label_1359

label label_1358:
    "Scene label_1358"
    menu:
        "Open door":
            jump label_1360
        "Open door":
            $ strength += 3
            jump label_1361
        "Look around":
            jump label_1362

label label_1360:
    "Scene label_1360"
    jump end_1363

label label_1361:
    "Scene label_1361"
    jump end_1363

label label_1362:
    "Scene label_1362"
    jump end_1363

label label_1359:
    "Scene label_1359"
    if intelligence >= 16:
        jump label_1363

label label_1363:
    $ intelligence += 5
    jump end_1364

    jump label_1364

label label_1364:
    "Ветка false для label_1363"
    jump end_1365

label label_1350:
    "Scene label_1350"
    menu:
        "Go forward":
            $ charisma += 2
            jump label_1365
        "Go forward":
            jump label_1366
        "Open door":
            jump label_1367
        "Go forward":
            $ intelligence += 1
            jump label_1368

label label_1365:
    "Scene label_1365"
    menu:
        "Look around":
            $ charisma += 1
            jump label_1369
        "Pick up item":
            jump label_1370
        "Go back":
            $ luck += 2
            jump label_1371

label label_1369:
    "Scene label_1369"
    jump end_1372

label label_1370:
    "Scene label_1370"
    jump end_1372

label label_1371:
    "Scene label_1371"
    jump end_1372

label label_1366:
    "Scene label_1366"
    menu:
        "Go back":
            $ strength += 2
            jump label_1372
        "Pick up item":
            jump label_1373

label label_1372:
    "Scene label_1372"
    jump end_1374

label label_1373:
    "Scene label_1373"
    jump end_1374

label label_1367:
    "Scene label_1367"
    menu:
        "Use item":
            jump label_1374
        "Explore":
            jump label_1375

label label_1374:
    "Scene label_1374"
    jump end_1376

label label_1375:
    "Scene label_1375"
    jump end_1376

label label_1368:
    "Scene label_1368"
    menu:
        "Pick up item":
            jump label_1376
        "Explore":
            $ intelligence += 2
            jump label_1377

label label_1376:
    "Scene label_1376"
    jump end_1378

label label_1377:
    "Scene label_1377"
    jump end_1378

label label_1345:
    "Scene label_1345"
    menu:
        "Look around":
            jump label_1378
        "Explore":
            jump label_1379

label label_1378:
    "Scene label_1378"
    menu:
        "Use item":
            $ charisma += 2
            jump label_1380
        "Explore":
            jump label_1381
        "Explore":
            jump label_1382

label label_1380:
    "Scene label_1380"
    menu:
        "Go forward":
            $ luck += 3
            jump label_1383
        "Go back":
            jump label_1384
        "Talk":
            $ strength += 1
            jump label_1385

label label_1383:
    "Scene label_1383"
    jump end_1386

label label_1384:
    "Scene label_1384"
    jump end_1386

label label_1385:
    "Scene label_1385"
    jump end_1386

label label_1381:
    "Scene label_1381"
    if charisma >= 13:
        jump label_1386

label label_1386:
    $ charisma += 3
    jump end_1387

    jump label_1387

label label_1387:
    "Ветка false для label_1386"
    jump end_1388

label label_1382:
    "Scene label_1382"
    menu:
        "Explore":
            $ charisma += 1
            jump label_1388
        "Go back":
            jump label_1389
        "Look around":
            $ intelligence += 2
            jump label_1390
        "Go forward":
            $ intelligence += 3
            jump label_1391

label label_1388:
    "Scene label_1388"
    jump end_1392

label label_1389:
    "Scene label_1389"
    jump end_1392

label label_1390:
    "Scene label_1390"
    jump end_1392

label label_1391:
    "Scene label_1391"
    jump end_1392

label label_1379:
    "Scene label_1379"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_1392
        "Use item":
            $ intelligence += 1
            jump label_1393

label label_1392:
    "Scene label_1392"
    if intelligence >= 5:
        jump label_1394

label label_1394:
    $ intelligence += 5
    jump end_1395

    jump label_1395

label label_1395:
    "Ветка false для label_1394"
    jump end_1396

label label_1393:
    "Scene label_1393"
    menu:
        "Use item":
            $ charisma += 3
            jump label_1396
        "Open door":
            jump label_1397
        "Explore":
            jump label_1398

label label_1396:
    "Scene label_1396"
    jump end_1399

label label_1397:
    "Scene label_1397"
    jump end_1399

label label_1398:
    "Scene label_1398"
    jump end_1399

label label_1346:
    "Scene label_1346"
    if luck >= 16:
        jump label_1399

label label_1399:
    $ luck += 3
    menu:
        "Look around":
            jump label_1400
        "Talk":
            $ intelligence += 3
            jump label_1401
        "Talk":
            $ charisma += 3
            jump label_1402

label label_1400:
    "Scene label_1400"
    menu:
        "Use item":
            jump label_1403
        "Use item":
            $ strength += 2
            jump label_1404
        "Pick up item":
            $ charisma += 1
            jump label_1405
        "Talk":
            $ charisma += 3
            jump label_1406

label label_1403:
    "Scene label_1403"
    jump end_1407

label label_1404:
    "Scene label_1404"
    jump end_1407

label label_1405:
    "Scene label_1405"
    jump end_1407

label label_1406:
    "Scene label_1406"
    jump end_1407

label label_1401:
    "Scene label_1401"
    menu:
        "Pick up item":
            jump label_1407
        "Talk":
            $ luck += 1
            jump label_1408
        "Go back":
            jump label_1409

label label_1407:
    "Scene label_1407"
    jump end_1410

label label_1408:
    "Scene label_1408"
    jump end_1410

label label_1409:
    "Scene label_1409"
    jump end_1410

label label_1402:
    "Scene label_1402"
    menu:
        "Go forward":
            jump label_1410
        "Pick up item":
            $ intelligence += 2
            jump label_1411
        "Use item":
            jump label_1412
        "Go back":
            jump label_1413

label label_1410:
    "Scene label_1410"
    jump end_1414

label label_1411:
    "Scene label_1411"
    jump end_1414

label label_1412:
    "Scene label_1412"
    jump end_1414

label label_1413:
    "Scene label_1413"
    jump end_1414

    jump label_1414

label label_1414:
    "Ветка false для label_1399"
    menu:
        "Use item":
            jump label_1415
        "Open door":
            $ luck += 1
            jump label_1416
        "Go forward":
            jump label_1417

label label_1415:
    "Scene label_1415"
    menu:
        "Look around":
            jump label_1418
        "Open door":
            jump label_1419

label label_1418:
    "Scene label_1418"
    jump end_1420

label label_1419:
    "Scene label_1419"
    jump end_1420

label label_1416:
    "Scene label_1416"
    menu:
        "Talk":
            jump label_1420
        "Go forward":
            jump label_1421

label label_1420:
    "Scene label_1420"
    jump end_1422

label label_1421:
    "Scene label_1421"
    jump end_1422

label label_1417:
    "Scene label_1417"
    menu:
        "Explore":
            $ charisma += 3
            jump label_1422
        "Open door":
            jump label_1423

label label_1422:
    "Scene label_1422"
    jump end_1424

label label_1423:
    "Scene label_1423"
    jump end_1424

label label_1347:
    "Scene label_1347"
    menu:
        "Talk":
            jump label_1424
        "Talk":
            $ luck += 1
            jump label_1425
        "Open door":
            jump label_1426

label label_1424:
    "Scene label_1424"
    menu:
        "Go back":
            $ intelligence += 2
            jump label_1427
        "Look around":
            $ strength += 3
            jump label_1428

label label_1427:
    "Scene label_1427"
    if strength >= 6:
        jump label_1429

label label_1429:
    $ strength += 4
    jump end_1430

    jump label_1430

label label_1430:
    "Ветка false для label_1429"
    jump end_1431

label label_1428:
    "Scene label_1428"
    if strength >= 5:
        jump label_1431

label label_1431:
    $ strength += 2
    jump end_1432

    jump label_1432

label label_1432:
    "Ветка false для label_1431"
    jump end_1433

label label_1425:
    "Scene label_1425"
    menu:
        "Go forward":
            jump label_1433
        "Explore":
            jump label_1434
        "Talk":
            $ charisma += 1
            jump label_1435

label label_1433:
    "Scene label_1433"
    menu:
        "Look around":
            jump label_1436
        "Talk":
            jump label_1437
        "Talk":
            jump label_1438

label label_1436:
    "Scene label_1436"
    jump end_1439

label label_1437:
    "Scene label_1437"
    jump end_1439

label label_1438:
    "Scene label_1438"
    jump end_1439

label label_1434:
    "Scene label_1434"
    menu:
        "Talk":
            jump label_1439
        "Pick up item":
            $ strength += 3
            jump label_1440

label label_1439:
    "Scene label_1439"
    jump end_1441

label label_1440:
    "Scene label_1440"
    jump end_1441

label label_1435:
    "Scene label_1435"
    menu:
        "Go back":
            jump label_1441
        "Look around":
            $ intelligence += 3
            jump label_1442

label label_1441:
    "Scene label_1441"
    jump end_1443

label label_1442:
    "Scene label_1442"
    jump end_1443

label label_1426:
    "Scene label_1426"
    menu:
        "Pick up item":
            $ intelligence += 3
            jump label_1443
        "Explore":
            jump label_1444

label label_1443:
    "Scene label_1443"
    menu:
        "Open door":
            jump label_1445
        "Look around":
            jump label_1446
        "Look around":
            $ luck += 1
            jump label_1447
        "Use item":
            jump label_1448

label label_1445:
    "Scene label_1445"
    jump end_1449

label label_1446:
    "Scene label_1446"
    jump end_1449

label label_1447:
    "Scene label_1447"
    jump end_1449

label label_1448:
    "Scene label_1448"
    jump end_1449

label label_1444:
    "Scene label_1444"
    menu:
        "Go forward":
            $ charisma += 3
            jump label_1449
        "Look around":
            jump label_1450
        "Look around":
            jump label_1451

label label_1449:
    "Scene label_1449"
    jump end_1452

label label_1450:
    "Scene label_1450"
    jump end_1452

label label_1451:
    "Scene label_1451"
    jump end_1452

label label_1341:
    "Scene label_1341"
    menu:
        "Open door":
            jump label_1452
        "Use item":
            $ intelligence += 2
            jump label_1453
        "Use item":
            $ charisma += 2
            jump label_1454
        "Open door":
            $ charisma += 1
            jump label_1455

label label_1452:
    "Scene label_1452"
    menu:
        "Pick up item":
            jump label_1456
        "Go back":
            $ luck += 3
            jump label_1457
        "Go forward":
            jump label_1458

label label_1456:
    "Scene label_1456"
    if strength >= 14:
        jump label_1459

label label_1459:
    $ strength += 3
    menu:
        "Go forward":
            jump label_1460
        "Go forward":
            jump label_1461
        "Open door":
            $ strength += 3
            jump label_1462
        "Open door":
            jump label_1463

label label_1460:
    "Scene label_1460"
    jump end_1464

label label_1461:
    "Scene label_1461"
    jump end_1464

label label_1462:
    "Scene label_1462"
    jump end_1464

label label_1463:
    "Scene label_1463"
    jump end_1464

    jump label_1464

label label_1464:
    "Ветка false для label_1459"
    menu:
        "Explore":
            jump label_1465
        "Go forward":
            jump label_1466

label label_1465:
    "Scene label_1465"
    jump end_1467

label label_1466:
    "Scene label_1466"
    jump end_1467

label label_1457:
    "Scene label_1457"
    if intelligence >= 12:
        jump label_1467

label label_1467:
    $ intelligence += 4
    if intelligence >= 20:
        jump label_1468

label label_1468:
    $ intelligence += 3
    jump end_1469

    jump label_1469

label label_1469:
    "Ветка false для label_1468"
    jump end_1470

    jump label_1470

label label_1470:
    "Ветка false для label_1467"
    menu:
        "Go forward":
            $ charisma += 1
            jump label_1471
        "Look around":
            jump label_1472
        "Go forward":
            jump label_1473
        "Explore":
            jump label_1474

label label_1471:
    "Scene label_1471"
    jump end_1475

label label_1472:
    "Scene label_1472"
    jump end_1475

label label_1473:
    "Scene label_1473"
    jump end_1475

label label_1474:
    "Scene label_1474"
    jump end_1475

label label_1458:
    "Scene label_1458"
    menu:
        "Explore":
            jump label_1475
        "Open door":
            $ intelligence += 3
            jump label_1476

label label_1475:
    "Scene label_1475"
    if luck >= 18:
        jump label_1477

label label_1477:
    $ luck += 4
    jump end_1478

    jump label_1478

label label_1478:
    "Ветка false для label_1477"
    jump end_1479

label label_1476:
    "Scene label_1476"
    if luck >= 18:
        jump label_1479

label label_1479:
    $ luck += 2
    jump end_1480

    jump label_1480

label label_1480:
    "Ветка false для label_1479"
    jump end_1481

label label_1453:
    "Scene label_1453"
    menu:
        "Open door":
            $ intelligence += 2
            jump label_1481
        "Go back":
            jump label_1482
        "Open door":
            $ charisma += 1
            jump label_1483

label label_1481:
    "Scene label_1481"
    menu:
        "Look around":
            jump label_1484
        "Look around":
            $ charisma += 1
            jump label_1485

label label_1484:
    "Scene label_1484"
    if luck >= 10:
        jump label_1486

label label_1486:
    $ luck += 4
    jump end_1487

    jump label_1487

label label_1487:
    "Ветка false для label_1486"
    jump end_1488

label label_1485:
    "Scene label_1485"
    menu:
        "Open door":
            $ luck += 2
            jump label_1488
        "Go back":
            $ strength += 2
            jump label_1489
        "Use item":
            jump label_1490
        "Pick up item":
            $ strength += 2
            jump label_1491

label label_1488:
    "Scene label_1488"
    jump end_1492

label label_1489:
    "Scene label_1489"
    jump end_1492

label label_1490:
    "Scene label_1490"
    jump end_1492

label label_1491:
    "Scene label_1491"
    jump end_1492

label label_1482:
    "Scene label_1482"
    menu:
        "Use item":
            $ charisma += 1
            jump label_1492
        "Look around":
            jump label_1493

label label_1492:
    "Scene label_1492"
    menu:
        "Open door":
            jump label_1494
        "Pick up item":
            jump label_1495

label label_1494:
    "Scene label_1494"
    jump end_1496

label label_1495:
    "Scene label_1495"
    jump end_1496

label label_1493:
    "Scene label_1493"
    menu:
        "Use item":
            jump label_1496
        "Explore":
            $ strength += 1
            jump label_1497

label label_1496:
    "Scene label_1496"
    jump end_1498

label label_1497:
    "Scene label_1497"
    jump end_1498

label label_1483:
    "Scene label_1483"
    menu:
        "Talk":
            $ intelligence += 3
            jump label_1498
        "Go forward":
            $ intelligence += 2
            jump label_1499
        "Look around":
            $ intelligence += 2
            jump label_1500

label label_1498:
    "Scene label_1498"
    menu:
        "Go forward":
            jump label_1501
        "Look around":
            jump label_1502
        "Go back":
            jump label_1503

label label_1501:
    "Scene label_1501"
    jump end_1504

label label_1502:
    "Scene label_1502"
    jump end_1504

label label_1503:
    "Scene label_1503"
    jump end_1504

label label_1499:
    "Scene label_1499"
    if luck >= 6:
        jump label_1504

label label_1504:
    $ luck += 2
    jump end_1505

    jump label_1505

label label_1505:
    "Ветка false для label_1504"
    jump end_1506

label label_1500:
    "Scene label_1500"
    menu:
        "Go forward":
            jump label_1506
        "Talk":
            jump label_1507
        "Explore":
            $ intelligence += 1
            jump label_1508

label label_1506:
    "Scene label_1506"
    jump end_1509

label label_1507:
    "Scene label_1507"
    jump end_1509

label label_1508:
    "Scene label_1508"
    jump end_1509

label label_1454:
    "Scene label_1454"
    menu:
        "Open door":
            $ strength += 2
            jump label_1509
        "Look around":
            jump label_1510

label label_1509:
    "Scene label_1509"
    menu:
        "Look around":
            $ charisma += 3
            jump label_1511
        "Open door":
            $ charisma += 2
            jump label_1512

label label_1511:
    "Scene label_1511"
    menu:
        "Pick up item":
            jump label_1513
        "Explore":
            jump label_1514

label label_1513:
    "Scene label_1513"
    jump end_1515

label label_1514:
    "Scene label_1514"
    jump end_1515

label label_1512:
    "Scene label_1512"
    menu:
        "Talk":
            $ luck += 1
            jump label_1515
        "Talk":
            $ intelligence += 2
            jump label_1516
        "Go back":
            jump label_1517

label label_1515:
    "Scene label_1515"
    jump end_1518

label label_1516:
    "Scene label_1516"
    jump end_1518

label label_1517:
    "Scene label_1517"
    jump end_1518

label label_1510:
    "Scene label_1510"
    menu:
        "Open door":
            jump label_1518
        "Talk":
            $ charisma += 3
            jump label_1519

label label_1518:
    "Scene label_1518"
    menu:
        "Open door":
            $ luck += 1
            jump label_1520
        "Open door":
            $ charisma += 2
            jump label_1521

label label_1520:
    "Scene label_1520"
    jump end_1522

label label_1521:
    "Scene label_1521"
    jump end_1522

label label_1519:
    "Scene label_1519"
    menu:
        "Open door":
            $ luck += 2
            jump label_1522
        "Open door":
            $ intelligence += 1
            jump label_1523
        "Use item":
            jump label_1524

label label_1522:
    "Scene label_1522"
    jump end_1525

label label_1523:
    "Scene label_1523"
    jump end_1525

label label_1524:
    "Scene label_1524"
    jump end_1525

label label_1455:
    "Scene label_1455"
    menu:
        "Explore":
            jump label_1525
        "Open door":
            $ luck += 1
            jump label_1526
        "Open door":
            $ strength += 3
            jump label_1527
        "Pick up item":
            $ charisma += 1
            jump label_1528

label label_1525:
    "Scene label_1525"
    if luck >= 10:
        jump label_1529

label label_1529:
    $ luck += 5
    menu:
        "Talk":
            jump label_1530
        "Go forward":
            jump label_1531
        "Open door":
            jump label_1532

label label_1530:
    "Scene label_1530"
    jump end_1533

label label_1531:
    "Scene label_1531"
    jump end_1533

label label_1532:
    "Scene label_1532"
    jump end_1533

    jump label_1533

label label_1533:
    "Ветка false для label_1529"
    if intelligence >= 17:
        jump label_1534

label label_1534:
    $ intelligence += 3
    jump end_1535

    jump label_1535

label label_1535:
    "Ветка false для label_1534"
    jump end_1536

label label_1526:
    "Scene label_1526"
    if luck >= 19:
        jump label_1536

label label_1536:
    $ luck += 3
    menu:
        "Pick up item":
            $ strength += 3
            jump label_1537
        "Look around":
            jump label_1538

label label_1537:
    "Scene label_1537"
    jump end_1539

label label_1538:
    "Scene label_1538"
    jump end_1539

    jump label_1539

label label_1539:
    "Ветка false для label_1536"
    if strength >= 6:
        jump label_1540

label label_1540:
    $ strength += 4
    jump end_1541

    jump label_1541

label label_1541:
    "Ветка false для label_1540"
    jump end_1542

label label_1527:
    "Scene label_1527"
    menu:
        "Explore":
            $ intelligence += 1
            jump label_1542
        "Go back":
            jump label_1543
        "Explore":
            jump label_1544

label label_1542:
    "Scene label_1542"
    menu:
        "Pick up item":
            $ intelligence += 2
            jump label_1545
        "Go back":
            $ intelligence += 1
            jump label_1546
        "Talk":
            $ charisma += 1
            jump label_1547

label label_1545:
    "Scene label_1545"
    jump end_1548

label label_1546:
    "Scene label_1546"
    jump end_1548

label label_1547:
    "Scene label_1547"
    jump end_1548

label label_1543:
    "Scene label_1543"
    menu:
        "Pick up item":
            jump label_1548
        "Go back":
            jump label_1549
        "Use item":
            jump label_1550
        "Talk":
            jump label_1551

label label_1548:
    "Scene label_1548"
    jump end_1552

label label_1549:
    "Scene label_1549"
    jump end_1552

label label_1550:
    "Scene label_1550"
    jump end_1552

label label_1551:
    "Scene label_1551"
    jump end_1552

label label_1544:
    "Scene label_1544"
    if strength >= 9:
        jump label_1552

label label_1552:
    $ strength += 5
    jump end_1553

    jump label_1553

label label_1553:
    "Ветка false для label_1552"
    jump end_1554

label label_1528:
    "Scene label_1528"
    menu:
        "Talk":
            jump label_1554
        "Explore":
            jump label_1555
        "Talk":
            $ strength += 2
            jump label_1556

label label_1554:
    "Scene label_1554"
    menu:
        "Explore":
            jump label_1557
        "Look around":
            jump label_1558
        "Look around":
            $ luck += 3
            jump label_1559
        "Open door":
            jump label_1560

label label_1557:
    "Scene label_1557"
    jump end_1561

label label_1558:
    "Scene label_1558"
    jump end_1561

label label_1559:
    "Scene label_1559"
    jump end_1561

label label_1560:
    "Scene label_1560"
    jump end_1561

label label_1555:
    "Scene label_1555"
    if intelligence >= 15:
        jump label_1561

label label_1561:
    $ intelligence += 4
    jump end_1562

    jump label_1562

label label_1562:
    "Ветка false для label_1561"
    jump end_1563

label label_1556:
    "Scene label_1556"
    menu:
        "Explore":
            jump label_1563
        "Pick up item":
            $ charisma += 1
            jump label_1564

label label_1563:
    "Scene label_1563"
    jump end_1565

label label_1564:
    "Scene label_1564"
    jump end_1565

label label_1342:
    "Scene label_1342"
    menu:
        "Use item":
            jump label_1565
        "Go forward":
            $ intelligence += 1
            jump label_1566
        "Use item":
            jump label_1567

label label_1565:
    "Scene label_1565"
    if charisma >= 15:
        jump label_1568

label label_1568:
    $ charisma += 2
    if charisma >= 7:
        jump label_1569

label label_1569:
    $ charisma += 4
    menu:
        "Go forward":
            jump label_1570
        "Go forward":
            $ intelligence += 2
            jump label_1571

label label_1570:
    "Scene label_1570"
    jump end_1572

label label_1571:
    "Scene label_1571"
    jump end_1572

    jump label_1572

label label_1572:
    "Ветка false для label_1569"
    menu:
        "Go back":
            jump label_1573
        "Explore":
            $ charisma += 2
            jump label_1574

label label_1573:
    "Scene label_1573"
    jump end_1575

label label_1574:
    "Scene label_1574"
    jump end_1575

    jump label_1575

label label_1575:
    "Ветка false для label_1568"
    menu:
        "Explore":
            jump label_1576
        "Use item":
            $ luck += 1
            jump label_1577

label label_1576:
    "Scene label_1576"
    menu:
        "Look around":
            jump label_1578
        "Explore":
            jump label_1579
        "Look around":
            $ intelligence += 1
            jump label_1580
        "Use item":
            $ luck += 1
            jump label_1581

label label_1578:
    "Scene label_1578"
    jump end_1582

label label_1579:
    "Scene label_1579"
    jump end_1582

label label_1580:
    "Scene label_1580"
    jump end_1582

label label_1581:
    "Scene label_1581"
    jump end_1582

label label_1577:
    "Scene label_1577"
    if intelligence >= 7:
        jump label_1582

label label_1582:
    $ intelligence += 2
    jump end_1583

    jump label_1583

label label_1583:
    "Ветка false для label_1582"
    jump end_1584

label label_1566:
    "Scene label_1566"
    if strength >= 15:
        jump label_1584

label label_1584:
    $ strength += 2
    if charisma >= 15:
        jump label_1585

label label_1585:
    $ charisma += 2
    menu:
        "Talk":
            $ strength += 1
            jump label_1586
        "Look around":
            jump label_1587

label label_1586:
    "Scene label_1586"
    jump end_1588

label label_1587:
    "Scene label_1587"
    jump end_1588

    jump label_1588

label label_1588:
    "Ветка false для label_1585"
    if charisma >= 12:
        jump label_1589

label label_1589:
    $ charisma += 3
    jump end_1590

    jump label_1590

label label_1590:
    "Ветка false для label_1589"
    jump end_1591

    jump label_1591

label label_1591:
    "Ветка false для label_1584"
    if strength >= 17:
        jump label_1592

label label_1592:
    $ strength += 4
    menu:
        "Pick up item":
            jump label_1593
        "Pick up item":
            jump label_1594

label label_1593:
    "Scene label_1593"
    jump end_1595

label label_1594:
    "Scene label_1594"
    jump end_1595

    jump label_1595

label label_1595:
    "Ветка false для label_1592"
    if luck >= 6:
        jump label_1596

label label_1596:
    $ luck += 5
    jump end_1597

    jump label_1597

label label_1597:
    "Ветка false для label_1596"
    jump end_1598

label label_1567:
    "Scene label_1567"
    if strength >= 7:
        jump label_1598

label label_1598:
    $ strength += 3
    menu:
        "Talk":
            jump label_1599
        "Use item":
            jump label_1600
        "Look around":
            $ luck += 1
            jump label_1601

label label_1599:
    "Scene label_1599"
    if luck >= 18:
        jump label_1602

label label_1602:
    $ luck += 4
    jump end_1603

    jump label_1603

label label_1603:
    "Ветка false для label_1602"
    jump end_1604

label label_1600:
    "Scene label_1600"
    if luck >= 16:
        jump label_1604

label label_1604:
    $ luck += 3
    jump end_1605

    jump label_1605

label label_1605:
    "Ветка false для label_1604"
    jump end_1606

label label_1601:
    "Scene label_1601"
    menu:
        "Go back":
            $ intelligence += 1
            jump label_1606
        "Go forward":
            $ luck += 3
            jump label_1607
        "Go forward":
            jump label_1608
        "Open door":
            $ charisma += 1
            jump label_1609

label label_1606:
    "Scene label_1606"
    jump end_1610

label label_1607:
    "Scene label_1607"
    jump end_1610

label label_1608:
    "Scene label_1608"
    jump end_1610

label label_1609:
    "Scene label_1609"
    jump end_1610

    jump label_1610

label label_1610:
    "Ветка false для label_1598"
    menu:
        "Look around":
            $ luck += 3
            jump label_1611
        "Look around":
            jump label_1612
        "Explore":
            $ charisma += 2
            jump label_1613
        "Pick up item":
            $ charisma += 2
            jump label_1614

label label_1611:
    "Scene label_1611"
    menu:
        "Use item":
            $ intelligence += 1
            jump label_1615
        "Explore":
            $ charisma += 2
            jump label_1616
        "Open door":
            $ charisma += 2
            jump label_1617
        "Talk":
            $ charisma += 2
            jump label_1618

label label_1615:
    "Scene label_1615"
    jump end_1619

label label_1616:
    "Scene label_1616"
    jump end_1619

label label_1617:
    "Scene label_1617"
    jump end_1619

label label_1618:
    "Scene label_1618"
    jump end_1619

label label_1612:
    "Scene label_1612"
    menu:
        "Explore":
            $ intelligence += 2
            jump label_1619
        "Explore":
            $ intelligence += 1
            jump label_1620

label label_1619:
    "Scene label_1619"
    jump end_1621

label label_1620:
    "Scene label_1620"
    jump end_1621

label label_1613:
    "Scene label_1613"
    menu:
        "Use item":
            $ charisma += 2
            jump label_1621
        "Talk":
            $ intelligence += 1
            jump label_1622

label label_1621:
    "Scene label_1621"
    jump end_1623

label label_1622:
    "Scene label_1622"
    jump end_1623

label label_1614:
    "Scene label_1614"
    menu:
        "Go back":
            jump label_1623
        "Go back":
            $ charisma += 3
            jump label_1624

label label_1623:
    "Scene label_1623"
    jump end_1625

label label_1624:
    "Scene label_1624"
    jump end_1625

label label_1343:
    "Scene label_1343"
    menu:
        "Open door":
            jump label_1625
        "Talk":
            $ strength += 2
            jump label_1626
        "Look around":
            $ luck += 3
            jump label_1627

label label_1625:
    "Scene label_1625"
    menu:
        "Talk":
            $ charisma += 1
            jump label_1628
        "Open door":
            $ luck += 3
            jump label_1629
        "Talk":
            $ luck += 3
            jump label_1630

label label_1628:
    "Scene label_1628"
    menu:
        "Look around":
            jump label_1631
        "Go back":
            $ luck += 3
            jump label_1632
        "Talk":
            $ charisma += 1
            jump label_1633
        "Go forward":
            $ charisma += 1
            jump label_1634

label label_1631:
    "Scene label_1631"
    if luck >= 12:
        jump label_1635

label label_1635:
    $ luck += 4
    jump end_1636

    jump label_1636

label label_1636:
    "Ветка false для label_1635"
    jump end_1637

label label_1632:
    "Scene label_1632"
    menu:
        "Go back":
            jump label_1637
        "Explore":
            jump label_1638
        "Talk":
            jump label_1639

label label_1637:
    "Scene label_1637"
    jump end_1640

label label_1638:
    "Scene label_1638"
    jump end_1640

label label_1639:
    "Scene label_1639"
    jump end_1640

label label_1633:
    "Scene label_1633"
    menu:
        "Use item":
            jump label_1640
        "Use item":
            jump label_1641
        "Use item":
            $ charisma += 1
            jump label_1642
        "Explore":
            jump label_1643

label label_1640:
    "Scene label_1640"
    jump end_1644

label label_1641:
    "Scene label_1641"
    jump end_1644

label label_1642:
    "Scene label_1642"
    jump end_1644

label label_1643:
    "Scene label_1643"
    jump end_1644

label label_1634:
    "Scene label_1634"
    if intelligence >= 15:
        jump label_1644

label label_1644:
    $ intelligence += 2
    jump end_1645

    jump label_1645

label label_1645:
    "Ветка false для label_1644"
    jump end_1646

label label_1629:
    "Scene label_1629"
    menu:
        "Go back":
            $ charisma += 1
            jump label_1646
        "Go back":
            jump label_1647
        "Explore":
            jump label_1648

label label_1646:
    "Scene label_1646"
    if intelligence >= 12:
        jump label_1649

label label_1649:
    $ intelligence += 2
    jump end_1650

    jump label_1650

label label_1650:
    "Ветка false для label_1649"
    jump end_1651

label label_1647:
    "Scene label_1647"
    menu:
        "Pick up item":
            jump label_1651
        "Go back":
            jump label_1652
        "Pick up item":
            jump label_1653
        "Use item":
            jump label_1654

label label_1651:
    "Scene label_1651"
    jump end_1655

label label_1652:
    "Scene label_1652"
    jump end_1655

label label_1653:
    "Scene label_1653"
    jump end_1655

label label_1654:
    "Scene label_1654"
    jump end_1655

label label_1648:
    "Scene label_1648"
    menu:
        "Look around":
            $ strength += 3
            jump label_1655
        "Use item":
            jump label_1656
        "Go back":
            $ charisma += 2
            jump label_1657
        "Go forward":
            $ intelligence += 1
            jump label_1658

label label_1655:
    "Scene label_1655"
    jump end_1659

label label_1656:
    "Scene label_1656"
    jump end_1659

label label_1657:
    "Scene label_1657"
    jump end_1659

label label_1658:
    "Scene label_1658"
    jump end_1659

label label_1630:
    "Scene label_1630"
    if strength >= 18:
        jump label_1659

label label_1659:
    $ strength += 2
    menu:
        "Pick up item":
            jump label_1660
        "Talk":
            jump label_1661

label label_1660:
    "Scene label_1660"
    jump end_1662

label label_1661:
    "Scene label_1661"
    jump end_1662

    jump label_1662

label label_1662:
    "Ветка false для label_1659"
    menu:
        "Go back":
            $ intelligence += 3
            jump label_1663
        "Pick up item":
            $ intelligence += 2
            jump label_1664

label label_1663:
    "Scene label_1663"
    jump end_1665

label label_1664:
    "Scene label_1664"
    jump end_1665

label label_1626:
    "Scene label_1626"
    menu:
        "Go forward":
            jump label_1665
        "Pick up item":
            $ luck += 3
            jump label_1666

label label_1665:
    "Scene label_1665"
    menu:
        "Open door":
            jump label_1667
        "Open door":
            $ strength += 3
            jump label_1668

label label_1667:
    "Scene label_1667"
    if strength >= 6:
        jump label_1669

label label_1669:
    $ strength += 3
    jump end_1670

    jump label_1670

label label_1670:
    "Ветка false для label_1669"
    jump end_1671

label label_1668:
    "Scene label_1668"
    menu:
        "Talk":
            $ intelligence += 3
            jump label_1671
        "Use item":
            $ luck += 2
            jump label_1672

label label_1671:
    "Scene label_1671"
    jump end_1673

label label_1672:
    "Scene label_1672"
    jump end_1673

label label_1666:
    "Scene label_1666"
    menu:
        "Explore":
            jump label_1673
        "Pick up item":
            $ strength += 3
            jump label_1674
        "Open door":
            jump label_1675

label label_1673:
    "Scene label_1673"
    menu:
        "Look around":
            jump label_1676
        "Pick up item":
            $ luck += 1
            jump label_1677

label label_1676:
    "Scene label_1676"
    jump end_1678

label label_1677:
    "Scene label_1677"
    jump end_1678

label label_1674:
    "Scene label_1674"
    if strength >= 6:
        jump label_1678

label label_1678:
    $ strength += 3
    jump end_1679

    jump label_1679

label label_1679:
    "Ветка false для label_1678"
    jump end_1680

label label_1675:
    "Scene label_1675"
    menu:
        "Use item":
            jump label_1680
        "Talk":
            jump label_1681

label label_1680:
    "Scene label_1680"
    jump end_1682

label label_1681:
    "Scene label_1681"
    jump end_1682

label label_1627:
    "Scene label_1627"
    if luck >= 15:
        jump label_1682

label label_1682:
    $ luck += 5
    menu:
        "Open door":
            $ luck += 2
            jump label_1683
        "Go forward":
            jump label_1684
        "Open door":
            jump label_1685
        "Go forward":
            $ strength += 1
            jump label_1686

label label_1683:
    "Scene label_1683"
    if charisma >= 5:
        jump label_1687

label label_1687:
    $ charisma += 4
    jump end_1688

    jump label_1688

label label_1688:
    "Ветка false для label_1687"
    jump end_1689

label label_1684:
    "Scene label_1684"
    menu:
        "Explore":
            jump label_1689
        "Talk":
            $ intelligence += 3
            jump label_1690
        "Go forward":
            jump label_1691
        "Go back":
            $ luck += 3
            jump label_1692

label label_1689:
    "Scene label_1689"
    jump end_1693

label label_1690:
    "Scene label_1690"
    jump end_1693

label label_1691:
    "Scene label_1691"
    jump end_1693

label label_1692:
    "Scene label_1692"
    jump end_1693

label label_1685:
    "Scene label_1685"
    menu:
        "Go back":
            $ luck += 2
            jump label_1693
        "Open door":
            $ luck += 2
            jump label_1694

label label_1693:
    "Scene label_1693"
    jump end_1695

label label_1694:
    "Scene label_1694"
    jump end_1695

label label_1686:
    "Scene label_1686"
    if charisma >= 11:
        jump label_1695

label label_1695:
    $ charisma += 3
    jump end_1696

    jump label_1696

label label_1696:
    "Ветка false для label_1695"
    jump end_1697

    jump label_1697

label label_1697:
    "Ветка false для label_1682"
    if charisma >= 8:
        jump label_1698

label label_1698:
    $ charisma += 3
    if luck >= 11:
        jump label_1699

label label_1699:
    $ luck += 4
    jump end_1700

    jump label_1700

label label_1700:
    "Ветка false для label_1699"
    jump end_1701

    jump label_1701

label label_1701:
    "Ветка false для label_1698"
    menu:
        "Use item":
            jump label_1702
        "Go back":
            $ strength += 2
            jump label_1703

label label_1702:
    "Scene label_1702"
    jump end_1704

label label_1703:
    "Scene label_1703"
    jump end_1704

label label_1339:
    "Scene label_1339"
    if intelligence >= 15:
        jump label_1704

label label_1704:
    $ intelligence += 3
    menu:
        "Open door":
            jump label_1705
        "Pick up item":
            jump label_1706
        "Talk":
            jump label_1707
        "Pick up item":
            jump label_1708

label label_1705:
    "Scene label_1705"
    if intelligence >= 7:
        jump label_1709

label label_1709:
    $ intelligence += 2
    menu:
        "Go forward":
            jump label_1710
        "Go back":
            jump label_1711

label label_1710:
    "Scene label_1710"
    menu:
        "Talk":
            $ luck += 1
            jump label_1712
        "Use item":
            jump label_1713
        "Explore":
            $ charisma += 3
            jump label_1714

label label_1712:
    "Scene label_1712"
    jump end_1715

label label_1713:
    "Scene label_1713"
    jump end_1715

label label_1714:
    "Scene label_1714"
    jump end_1715

label label_1711:
    "Scene label_1711"
    if strength >= 8:
        jump label_1715

label label_1715:
    $ strength += 4
    jump end_1716

    jump label_1716

label label_1716:
    "Ветка false для label_1715"
    jump end_1717

    jump label_1717

label label_1717:
    "Ветка false для label_1709"
    if charisma >= 11:
        jump label_1718

label label_1718:
    $ charisma += 2
    menu:
        "Go forward":
            jump label_1719
        "Pick up item":
            $ strength += 1
            jump label_1720
        "Use item":
            $ luck += 2
            jump label_1721
        "Go forward":
            jump label_1722

label label_1719:
    "Scene label_1719"
    jump end_1723

label label_1720:
    "Scene label_1720"
    jump end_1723

label label_1721:
    "Scene label_1721"
    jump end_1723

label label_1722:
    "Scene label_1722"
    jump end_1723

    jump label_1723

label label_1723:
    "Ветка false для label_1718"
    menu:
        "Talk":
            $ charisma += 3
            jump label_1724
        "Open door":
            $ charisma += 2
            jump label_1725
        "Pick up item":
            $ strength += 3
            jump label_1726
        "Go forward":
            jump label_1727

label label_1724:
    "Scene label_1724"
    jump end_1728

label label_1725:
    "Scene label_1725"
    jump end_1728

label label_1726:
    "Scene label_1726"
    jump end_1728

label label_1727:
    "Scene label_1727"
    jump end_1728

label label_1706:
    "Scene label_1706"
    menu:
        "Go back":
            jump label_1728
        "Use item":
            jump label_1729
        "Go forward":
            jump label_1730

label label_1728:
    "Scene label_1728"
    menu:
        "Use item":
            jump label_1731
        "Go forward":
            jump label_1732

label label_1731:
    "Scene label_1731"
    if charisma >= 20:
        jump label_1733

label label_1733:
    $ charisma += 3
    jump end_1734

    jump label_1734

label label_1734:
    "Ветка false для label_1733"
    jump end_1735

label label_1732:
    "Scene label_1732"
    menu:
        "Go forward":
            $ strength += 3
            jump label_1735
        "Explore":
            $ charisma += 3
            jump label_1736
        "Talk":
            $ luck += 3
            jump label_1737
        "Talk":
            $ luck += 2
            jump label_1738

label label_1735:
    "Scene label_1735"
    jump end_1739

label label_1736:
    "Scene label_1736"
    jump end_1739

label label_1737:
    "Scene label_1737"
    jump end_1739

label label_1738:
    "Scene label_1738"
    jump end_1739

label label_1729:
    "Scene label_1729"
    if charisma >= 16:
        jump label_1739

label label_1739:
    $ charisma += 5
    menu:
        "Talk":
            jump label_1740
        "Pick up item":
            jump label_1741
        "Open door":
            $ charisma += 1
            jump label_1742

label label_1740:
    "Scene label_1740"
    jump end_1743

label label_1741:
    "Scene label_1741"
    jump end_1743

label label_1742:
    "Scene label_1742"
    jump end_1743

    jump label_1743

label label_1743:
    "Ветка false для label_1739"
    menu:
        "Explore":
            jump label_1744
        "Pick up item":
            $ intelligence += 1
            jump label_1745

label label_1744:
    "Scene label_1744"
    jump end_1746

label label_1745:
    "Scene label_1745"
    jump end_1746

label label_1730:
    "Scene label_1730"
    menu:
        "Talk":
            jump label_1746
        "Talk":
            jump label_1747
        "Talk":
            jump label_1748
        "Use item":
            jump label_1749

label label_1746:
    "Scene label_1746"
    menu:
        "Look around":
            jump label_1750
        "Go forward":
            jump label_1751
        "Go forward":
            $ intelligence += 3
            jump label_1752

label label_1750:
    "Scene label_1750"
    jump end_1753

label label_1751:
    "Scene label_1751"
    jump end_1753

label label_1752:
    "Scene label_1752"
    jump end_1753

label label_1747:
    "Scene label_1747"
    if luck >= 20:
        jump label_1753

label label_1753:
    $ luck += 2
    jump end_1754

    jump label_1754

label label_1754:
    "Ветка false для label_1753"
    jump end_1755

label label_1748:
    "Scene label_1748"
    menu:
        "Open door":
            jump label_1755
        "Open door":
            $ luck += 3
            jump label_1756
        "Open door":
            jump label_1757

label label_1755:
    "Scene label_1755"
    jump end_1758

label label_1756:
    "Scene label_1756"
    jump end_1758

label label_1757:
    "Scene label_1757"
    jump end_1758

label label_1749:
    "Scene label_1749"
    menu:
        "Pick up item":
            $ intelligence += 3
            jump label_1758
        "Go forward":
            jump label_1759

label label_1758:
    "Scene label_1758"
    jump end_1760

label label_1759:
    "Scene label_1759"
    jump end_1760

label label_1707:
    "Scene label_1707"
    menu:
        "Pick up item":
            $ strength += 3
            jump label_1760
        "Go back":
            $ charisma += 2
            jump label_1761

label label_1760:
    "Scene label_1760"
    menu:
        "Look around":
            jump label_1762
        "Use item":
            $ strength += 2
            jump label_1763
        "Look around":
            $ strength += 1
            jump label_1764
        "Go back":
            $ strength += 2
            jump label_1765

label label_1762:
    "Scene label_1762"
    menu:
        "Open door":
            $ luck += 2
            jump label_1766
        "Open door":
            $ luck += 2
            jump label_1767
        "Pick up item":
            jump label_1768
        "Go forward":
            jump label_1769

label label_1766:
    "Scene label_1766"
    jump end_1770

label label_1767:
    "Scene label_1767"
    jump end_1770

label label_1768:
    "Scene label_1768"
    jump end_1770

label label_1769:
    "Scene label_1769"
    jump end_1770

label label_1763:
    "Scene label_1763"
    menu:
        "Explore":
            $ luck += 3
            jump label_1770
        "Pick up item":
            jump label_1771
        "Open door":
            jump label_1772

label label_1770:
    "Scene label_1770"
    jump end_1773

label label_1771:
    "Scene label_1771"
    jump end_1773

label label_1772:
    "Scene label_1772"
    jump end_1773

label label_1764:
    "Scene label_1764"
    menu:
        "Explore":
            jump label_1773
        "Pick up item":
            jump label_1774
        "Open door":
            $ charisma += 1
            jump label_1775

label label_1773:
    "Scene label_1773"
    jump end_1776

label label_1774:
    "Scene label_1774"
    jump end_1776

label label_1775:
    "Scene label_1775"
    jump end_1776

label label_1765:
    "Scene label_1765"
    menu:
        "Look around":
            $ strength += 2
            jump label_1776
        "Open door":
            jump label_1777
        "Use item":
            jump label_1778
        "Pick up item":
            $ luck += 3
            jump label_1779

label label_1776:
    "Scene label_1776"
    jump end_1780

label label_1777:
    "Scene label_1777"
    jump end_1780

label label_1778:
    "Scene label_1778"
    jump end_1780

label label_1779:
    "Scene label_1779"
    jump end_1780

label label_1761:
    "Scene label_1761"
    menu:
        "Use item":
            jump label_1780
        "Look around":
            $ intelligence += 3
            jump label_1781
        "Go forward":
            jump label_1782

label label_1780:
    "Scene label_1780"
    menu:
        "Talk":
            $ charisma += 3
            jump label_1783
        "Go forward":
            $ strength += 3
            jump label_1784
        "Pick up item":
            $ charisma += 2
            jump label_1785
        "Talk":
            $ luck += 2
            jump label_1786

label label_1783:
    "Scene label_1783"
    jump end_1787

label label_1784:
    "Scene label_1784"
    jump end_1787

label label_1785:
    "Scene label_1785"
    jump end_1787

label label_1786:
    "Scene label_1786"
    jump end_1787

label label_1781:
    "Scene label_1781"
    if intelligence >= 7:
        jump label_1787

label label_1787:
    $ intelligence += 3
    jump end_1788

    jump label_1788

label label_1788:
    "Ветка false для label_1787"
    jump end_1789

label label_1782:
    "Scene label_1782"
    menu:
        "Go forward":
            $ intelligence += 2
            jump label_1789
        "Go forward":
            $ intelligence += 2
            jump label_1790

label label_1789:
    "Scene label_1789"
    jump end_1791

label label_1790:
    "Scene label_1790"
    jump end_1791

label label_1708:
    "Scene label_1708"
    menu:
        "Pick up item":
            $ charisma += 3
            jump label_1791
        "Look around":
            $ intelligence += 1
            jump label_1792
        "Go forward":
            $ luck += 3
            jump label_1793
        "Open door":
            $ luck += 3
            jump label_1794

label label_1791:
    "Scene label_1791"
    menu:
        "Pick up item":
            $ charisma += 3
            jump label_1795
        "Open door":
            $ strength += 2
            jump label_1796
        "Explore":
            $ intelligence += 1
            jump label_1797

label label_1795:
    "Scene label_1795"
    if intelligence >= 7:
        jump label_1798

label label_1798:
    $ intelligence += 3
    jump end_1799

    jump label_1799

label label_1799:
    "Ветка false для label_1798"
    jump end_1800

label label_1796:
    "Scene label_1796"
    menu:
        "Explore":
            jump label_1800
        "Pick up item":
            $ intelligence += 3
            jump label_1801
        "Open door":
            $ strength += 1
            jump label_1802

label label_1800:
    "Scene label_1800"
    jump end_1803

label label_1801:
    "Scene label_1801"
    jump end_1803

label label_1802:
    "Scene label_1802"
    jump end_1803

label label_1797:
    "Scene label_1797"
    if luck >= 9:
        jump label_1803

label label_1803:
    $ luck += 5
    jump end_1804

    jump label_1804

label label_1804:
    "Ветка false для label_1803"
    jump end_1805

label label_1792:
    "Scene label_1792"
    if strength >= 5:
        jump label_1805

label label_1805:
    $ strength += 2
    menu:
        "Go forward":
            $ intelligence += 2
            jump label_1806
        "Use item":
            jump label_1807
        "Use item":
            $ charisma += 2
            jump label_1808

label label_1806:
    "Scene label_1806"
    jump end_1809

label label_1807:
    "Scene label_1807"
    jump end_1809

label label_1808:
    "Scene label_1808"
    jump end_1809

    jump label_1809

label label_1809:
    "Ветка false для label_1805"
    menu:
        "Talk":
            $ strength += 1
            jump label_1810
        "Talk":
            jump label_1811

label label_1810:
    "Scene label_1810"
    jump end_1812

label label_1811:
    "Scene label_1811"
    jump end_1812

label label_1793:
    "Scene label_1793"
    if strength >= 20:
        jump label_1812

label label_1812:
    $ strength += 2
    menu:
        "Open door":
            jump label_1813
        "Explore":
            jump label_1814

label label_1813:
    "Scene label_1813"
    jump end_1815

label label_1814:
    "Scene label_1814"
    jump end_1815

    jump label_1815

label label_1815:
    "Ветка false для label_1812"
    menu:
        "Go forward":
            jump label_1816
        "Go forward":
            jump label_1817
        "Open door":
            $ luck += 2
            jump label_1818

label label_1816:
    "Scene label_1816"
    jump end_1819

label label_1817:
    "Scene label_1817"
    jump end_1819

label label_1818:
    "Scene label_1818"
    jump end_1819

label label_1794:
    "Scene label_1794"
    menu:
        "Talk":
            $ charisma += 3
            jump label_1819
        "Talk":
            $ luck += 2
            jump label_1820

label label_1819:
    "Scene label_1819"
    menu:
        "Go forward":
            $ strength += 3
            jump label_1821
        "Talk":
            jump label_1822
        "Go forward":
            $ charisma += 2
            jump label_1823

label label_1821:
    "Scene label_1821"
    jump end_1824

label label_1822:
    "Scene label_1822"
    jump end_1824

label label_1823:
    "Scene label_1823"
    jump end_1824

label label_1820:
    "Scene label_1820"
    menu:
        "Go back":
            jump label_1824
        "Explore":
            jump label_1825
        "Pick up item":
            jump label_1826

label label_1824:
    "Scene label_1824"
    jump end_1827

label label_1825:
    "Scene label_1825"
    jump end_1827

label label_1826:
    "Scene label_1826"
    jump end_1827

    jump label_1827

label label_1827:
    "Ветка false для label_1704"
    menu:
        "Talk":
            $ strength += 3
            jump label_1828
        "Pick up item":
            jump label_1829
        "Look around":
            $ luck += 2
            jump label_1830
        "Go back":
            jump label_1831

label label_1828:
    "Scene label_1828"
    if luck >= 12:
        jump label_1832

label label_1832:
    $ luck += 3
    menu:
        "Use item":
            jump label_1833
        "Open door":
            $ charisma += 3
            jump label_1834
        "Use item":
            jump label_1835

label label_1833:
    "Scene label_1833"
    menu:
        "Go back":
            $ luck += 3
            jump label_1836
        "Explore":
            $ charisma += 3
            jump label_1837

label label_1836:
    "Scene label_1836"
    jump end_1838

label label_1837:
    "Scene label_1837"
    jump end_1838

label label_1834:
    "Scene label_1834"
    menu:
        "Go back":
            jump label_1838
        "Use item":
            jump label_1839

label label_1838:
    "Scene label_1838"
    jump end_1840

label label_1839:
    "Scene label_1839"
    jump end_1840

label label_1835:
    "Scene label_1835"
    menu:
        "Talk":
            jump label_1840
        "Pick up item":
            $ charisma += 2
            jump label_1841
        "Go back":
            jump label_1842

label label_1840:
    "Scene label_1840"
    jump end_1843

label label_1841:
    "Scene label_1841"
    jump end_1843

label label_1842:
    "Scene label_1842"
    jump end_1843

    jump label_1843

label label_1843:
    "Ветка false для label_1832"
    menu:
        "Talk":
            $ strength += 2
            jump label_1844
        "Look around":
            jump label_1845
        "Open door":
            $ intelligence += 2
            jump label_1846

label label_1844:
    "Scene label_1844"
    menu:
        "Go back":
            jump label_1847
        "Open door":
            $ strength += 2
            jump label_1848
        "Pick up item":
            jump label_1849

label label_1847:
    "Scene label_1847"
    jump end_1850

label label_1848:
    "Scene label_1848"
    jump end_1850

label label_1849:
    "Scene label_1849"
    jump end_1850

label label_1845:
    "Scene label_1845"
    menu:
        "Explore":
            $ intelligence += 1
            jump label_1850
        "Explore":
            jump label_1851
        "Go forward":
            $ strength += 2
            jump label_1852

label label_1850:
    "Scene label_1850"
    jump end_1853

label label_1851:
    "Scene label_1851"
    jump end_1853

label label_1852:
    "Scene label_1852"
    jump end_1853

label label_1846:
    "Scene label_1846"
    if luck >= 9:
        jump label_1853

label label_1853:
    $ luck += 2
    jump end_1854

    jump label_1854

label label_1854:
    "Ветка false для label_1853"
    jump end_1855

label label_1829:
    "Scene label_1829"
    menu:
        "Open door":
            $ strength += 1
            jump label_1855
        "Look around":
            $ luck += 2
            jump label_1856
        "Open door":
            $ intelligence += 3
            jump label_1857
        "Go back":
            jump label_1858

label label_1855:
    "Scene label_1855"
    menu:
        "Talk":
            $ luck += 1
            jump label_1859
        "Talk":
            jump label_1860

label label_1859:
    "Scene label_1859"
    menu:
        "Go forward":
            jump label_1861
        "Look around":
            jump label_1862

label label_1861:
    "Scene label_1861"
    jump end_1863

label label_1862:
    "Scene label_1862"
    jump end_1863

label label_1860:
    "Scene label_1860"
    menu:
        "Pick up item":
            $ intelligence += 2
            jump label_1863
        "Use item":
            $ intelligence += 1
            jump label_1864
        "Use item":
            $ strength += 1
            jump label_1865

label label_1863:
    "Scene label_1863"
    jump end_1866

label label_1864:
    "Scene label_1864"
    jump end_1866

label label_1865:
    "Scene label_1865"
    jump end_1866

label label_1856:
    "Scene label_1856"
    menu:
        "Open door":
            $ intelligence += 1
            jump label_1866
        "Look around":
            $ charisma += 2
            jump label_1867
        "Talk":
            jump label_1868

label label_1866:
    "Scene label_1866"
    menu:
        "Open door":
            $ luck += 1
            jump label_1869
        "Pick up item":
            $ luck += 2
            jump label_1870
        "Go forward":
            $ charisma += 2
            jump label_1871
        "Use item":
            $ strength += 3
            jump label_1872

label label_1869:
    "Scene label_1869"
    jump end_1873

label label_1870:
    "Scene label_1870"
    jump end_1873

label label_1871:
    "Scene label_1871"
    jump end_1873

label label_1872:
    "Scene label_1872"
    jump end_1873

label label_1867:
    "Scene label_1867"
    menu:
        "Open door":
            $ charisma += 1
            jump label_1873
        "Use item":
            $ charisma += 2
            jump label_1874
        "Use item":
            jump label_1875
        "Use item":
            $ charisma += 1
            jump label_1876

label label_1873:
    "Scene label_1873"
    jump end_1877

label label_1874:
    "Scene label_1874"
    jump end_1877

label label_1875:
    "Scene label_1875"
    jump end_1877

label label_1876:
    "Scene label_1876"
    jump end_1877

label label_1868:
    "Scene label_1868"
    menu:
        "Use item":
            jump label_1877
        "Look around":
            $ strength += 2
            jump label_1878
        "Explore":
            $ strength += 2
            jump label_1879
        "Open door":
            jump label_1880

label label_1877:
    "Scene label_1877"
    jump end_1881

label label_1878:
    "Scene label_1878"
    jump end_1881

label label_1879:
    "Scene label_1879"
    jump end_1881

label label_1880:
    "Scene label_1880"
    jump end_1881

label label_1857:
    "Scene label_1857"
    menu:
        "Open door":
            $ intelligence += 2
            jump label_1881
        "Explore":
            jump label_1882

label label_1881:
    "Scene label_1881"
    if intelligence >= 10:
        jump label_1883

label label_1883:
    $ intelligence += 3
    jump end_1884

    jump label_1884

label label_1884:
    "Ветка false для label_1883"
    jump end_1885

label label_1882:
    "Scene label_1882"
    menu:
        "Use item":
            jump label_1885
        "Open door":
            $ intelligence += 1
            jump label_1886
        "Talk":
            $ strength += 2
            jump label_1887
        "Look around":
            jump label_1888

label label_1885:
    "Scene label_1885"
    jump end_1889

label label_1886:
    "Scene label_1886"
    jump end_1889

label label_1887:
    "Scene label_1887"
    jump end_1889

label label_1888:
    "Scene label_1888"
    jump end_1889

label label_1858:
    "Scene label_1858"
    if intelligence >= 14:
        jump label_1889

label label_1889:
    $ intelligence += 3
    menu:
        "Talk":
            $ luck += 1
            jump label_1890
        "Look around":
            $ strength += 3
            jump label_1891
        "Go forward":
            jump label_1892

label label_1890:
    "Scene label_1890"
    jump end_1893

label label_1891:
    "Scene label_1891"
    jump end_1893

label label_1892:
    "Scene label_1892"
    jump end_1893

    jump label_1893

label label_1893:
    "Ветка false для label_1889"
    menu:
        "Talk":
            $ charisma += 2
            jump label_1894
        "Talk":
            $ intelligence += 3
            jump label_1895
        "Look around":
            $ strength += 2
            jump label_1896
        "Talk":
            jump label_1897

label label_1894:
    "Scene label_1894"
    jump end_1898

label label_1895:
    "Scene label_1895"
    jump end_1898

label label_1896:
    "Scene label_1896"
    jump end_1898

label label_1897:
    "Scene label_1897"
    jump end_1898

label label_1830:
    "Scene label_1830"
    menu:
        "Explore":
            jump label_1898
        "Talk":
            jump label_1899
        "Talk":
            $ strength += 2
            jump label_1900
        "Talk":
            jump label_1901

label label_1898:
    "Scene label_1898"
    menu:
        "Go forward":
            $ intelligence += 1
            jump label_1902
        "Pick up item":
            $ intelligence += 1
            jump label_1903

label label_1902:
    "Scene label_1902"
    menu:
        "Go back":
            $ charisma += 1
            jump label_1904
        "Look around":
            jump label_1905
        "Talk":
            jump label_1906

label label_1904:
    "Scene label_1904"
    jump end_1907

label label_1905:
    "Scene label_1905"
    jump end_1907

label label_1906:
    "Scene label_1906"
    jump end_1907

label label_1903:
    "Scene label_1903"
    menu:
        "Open door":
            $ luck += 2
            jump label_1907
        "Pick up item":
            jump label_1908

label label_1907:
    "Scene label_1907"
    jump end_1909

label label_1908:
    "Scene label_1908"
    jump end_1909

label label_1899:
    "Scene label_1899"
    menu:
        "Open door":
            jump label_1909
        "Pick up item":
            jump label_1910
        "Explore":
            jump label_1911
        "Open door":
            jump label_1912

label label_1909:
    "Scene label_1909"
    menu:
        "Talk":
            jump label_1913
        "Pick up item":
            $ strength += 1
            jump label_1914
        "Look around":
            jump label_1915

label label_1913:
    "Scene label_1913"
    jump end_1916

label label_1914:
    "Scene label_1914"
    jump end_1916

label label_1915:
    "Scene label_1915"
    jump end_1916

label label_1910:
    "Scene label_1910"
    menu:
        "Look around":
            jump label_1916
        "Open door":
            $ luck += 2
            jump label_1917
        "Go forward":
            $ intelligence += 1
            jump label_1918

label label_1916:
    "Scene label_1916"
    jump end_1919

label label_1917:
    "Scene label_1917"
    jump end_1919

label label_1918:
    "Scene label_1918"
    jump end_1919

label label_1911:
    "Scene label_1911"
    if intelligence >= 19:
        jump label_1919

label label_1919:
    $ intelligence += 3
    jump end_1920

    jump label_1920

label label_1920:
    "Ветка false для label_1919"
    jump end_1921

label label_1912:
    "Scene label_1912"
    menu:
        "Open door":
            $ strength += 1
            jump label_1921
        "Pick up item":
            $ charisma += 2
            jump label_1922
        "Pick up item":
            $ intelligence += 2
            jump label_1923

label label_1921:
    "Scene label_1921"
    jump end_1924

label label_1922:
    "Scene label_1922"
    jump end_1924

label label_1923:
    "Scene label_1923"
    jump end_1924

label label_1900:
    "Scene label_1900"
    if strength >= 12:
        jump label_1924

label label_1924:
    $ strength += 3
    menu:
        "Go back":
            $ luck += 2
            jump label_1925
        "Open door":
            jump label_1926

label label_1925:
    "Scene label_1925"
    jump end_1927

label label_1926:
    "Scene label_1926"
    jump end_1927

    jump label_1927

label label_1927:
    "Ветка false для label_1924"
    menu:
        "Go back":
            $ charisma += 1
            jump label_1928
        "Pick up item":
            $ luck += 1
            jump label_1929

label label_1928:
    "Scene label_1928"
    jump end_1930

label label_1929:
    "Scene label_1929"
    jump end_1930

label label_1901:
    "Scene label_1901"
    menu:
        "Talk":
            $ strength += 1
            jump label_1930
        "Go back":
            $ intelligence += 3
            jump label_1931
        "Explore":
            $ charisma += 2
            jump label_1932
        "Pick up item":
            $ luck += 2
            jump label_1933

label label_1930:
    "Scene label_1930"
    menu:
        "Look around":
            jump label_1934
        "Pick up item":
            $ strength += 3
            jump label_1935
        "Look around":
            jump label_1936
        "Talk":
            jump label_1937

label label_1934:
    "Scene label_1934"
    jump end_1938

label label_1935:
    "Scene label_1935"
    jump end_1938

label label_1936:
    "Scene label_1936"
    jump end_1938

label label_1937:
    "Scene label_1937"
    jump end_1938

label label_1931:
    "Scene label_1931"
    menu:
        "Pick up item":
            jump label_1938
        "Go back":
            $ intelligence += 1
            jump label_1939
        "Open door":
            $ intelligence += 1
            jump label_1940
        "Go forward":
            $ intelligence += 1
            jump label_1941

label label_1938:
    "Scene label_1938"
    jump end_1942

label label_1939:
    "Scene label_1939"
    jump end_1942

label label_1940:
    "Scene label_1940"
    jump end_1942

label label_1941:
    "Scene label_1941"
    jump end_1942

label label_1932:
    "Scene label_1932"
    menu:
        "Open door":
            jump label_1942
        "Talk":
            $ luck += 1
            jump label_1943

label label_1942:
    "Scene label_1942"
    jump end_1944

label label_1943:
    "Scene label_1943"
    jump end_1944

label label_1933:
    "Scene label_1933"
    if strength >= 10:
        jump label_1944

label label_1944:
    $ strength += 2
    jump end_1945

    jump label_1945

label label_1945:
    "Ветка false для label_1944"
    jump end_1946

label label_1831:
    "Scene label_1831"
    if charisma >= 7:
        jump label_1946

label label_1946:
    $ charisma += 3
    menu:
        "Pick up item":
            $ charisma += 2
            jump label_1947
        "Explore":
            jump label_1948

label label_1947:
    "Scene label_1947"
    menu:
        "Explore":
            jump label_1949
        "Explore":
            jump label_1950
        "Go back":
            jump label_1951

label label_1949:
    "Scene label_1949"
    jump end_1952

label label_1950:
    "Scene label_1950"
    jump end_1952

label label_1951:
    "Scene label_1951"
    jump end_1952

label label_1948:
    "Scene label_1948"
    menu:
        "Use item":
            jump label_1952
        "Open door":
            $ luck += 3
            jump label_1953

label label_1952:
    "Scene label_1952"
    jump end_1954

label label_1953:
    "Scene label_1953"
    jump end_1954

    jump label_1954

label label_1954:
    "Ветка false для label_1946"
    menu:
        "Open door":
            $ luck += 2
            jump label_1955
        "Look around":
            jump label_1956
        "Use item":
            jump label_1957
        "Use item":
            jump label_1958

label label_1955:
    "Scene label_1955"
    if intelligence >= 8:
        jump label_1959

label label_1959:
    $ intelligence += 4
    jump end_1960

    jump label_1960

label label_1960:
    "Ветка false для label_1959"
    jump end_1961

label label_1956:
    "Scene label_1956"
    menu:
        "Open door":
            jump label_1961
        "Go back":
            $ intelligence += 3
            jump label_1962
        "Pick up item":
            jump label_1963

label label_1961:
    "Scene label_1961"
    jump end_1964

label label_1962:
    "Scene label_1962"
    jump end_1964

label label_1963:
    "Scene label_1963"
    jump end_1964

label label_1957:
    "Scene label_1957"
    menu:
        "Go forward":
            $ charisma += 1
            jump label_1964
        "Open door":
            $ strength += 2
            jump label_1965
        "Explore":
            $ intelligence += 2
            jump label_1966

label label_1964:
    "Scene label_1964"
    jump end_1967

label label_1965:
    "Scene label_1965"
    jump end_1967

label label_1966:
    "Scene label_1966"
    jump end_1967

label label_1958:
    "Scene label_1958"
    menu:
        "Open door":
            jump label_1967
        "Open door":
            $ intelligence += 2
            jump label_1968
        "Use item":
            jump label_1969

label label_1967:
    "Scene label_1967"
    jump end_1970

label label_1968:
    "Scene label_1968"
    jump end_1970

label label_1969:
    "Scene label_1969"
    jump end_1970

label label_17:
    "Scene label_17"
    if intelligence >= 15:
        jump label_1970

label label_1970:
    $ intelligence += 5
    menu:
        "Look around":
            $ strength += 1
            jump label_1971
        "Open door":
            $ strength += 3
            jump label_1972

label label_1971:
    "Scene label_1971"
    menu:
        "Go forward":
            $ strength += 1
            jump label_1973
        "Go back":
            jump label_1974

label label_1973:
    "Scene label_1973"
    menu:
        "Explore":
            jump label_1975
        "Look around":
            $ luck += 2
            jump label_1976
        "Look around":
            $ strength += 1
            jump label_1977
        "Go forward":
            jump label_1978

label label_1975:
    "Scene label_1975"
    if intelligence >= 17:
        jump label_1979

label label_1979:
    $ intelligence += 5
    if luck >= 7:
        jump label_1980

label label_1980:
    $ luck += 4
    if charisma >= 13:
        jump label_1981

label label_1981:
    $ charisma += 3
    jump end_1982

    jump label_1982

label label_1982:
    "Ветка false для label_1981"
    jump end_1983

    jump label_1983

label label_1983:
    "Ветка false для label_1980"
    menu:
        "Look around":
            $ intelligence += 3
            jump label_1984
        "Go back":
            $ luck += 3
            jump label_1985
        "Talk":
            jump label_1986
        "Pick up item":
            $ luck += 2
            jump label_1987

label label_1984:
    "Scene label_1984"
    jump end_1988

label label_1985:
    "Scene label_1985"
    jump end_1988

label label_1986:
    "Scene label_1986"
    jump end_1988

label label_1987:
    "Scene label_1987"
    jump end_1988

    jump label_1988

label label_1988:
    "Ветка false для label_1979"
    menu:
        "Open door":
            jump label_1989
        "Use item":
            jump label_1990
        "Go back":
            jump label_1991

label label_1989:
    "Scene label_1989"
    if charisma >= 9:
        jump label_1992

label label_1992:
    $ charisma += 3
    jump end_1993

    jump label_1993

label label_1993:
    "Ветка false для label_1992"
    jump end_1994

label label_1990:
    "Scene label_1990"
    if strength >= 8:
        jump label_1994

label label_1994:
    $ strength += 3
    jump end_1995

    jump label_1995

label label_1995:
    "Ветка false для label_1994"
    jump end_1996

label label_1991:
    "Scene label_1991"
    if charisma >= 9:
        jump label_1996

label label_1996:
    $ charisma += 3
    jump end_1997

    jump label_1997

label label_1997:
    "Ветка false для label_1996"
    jump end_1998

label label_1976:
    "Scene label_1976"
    menu:
        "Explore":
            jump label_1998
        "Use item":
            jump label_1999
        "Open door":
            $ luck += 3
            jump label_2000

label label_1998:
    "Scene label_1998"
    if charisma >= 6:
        jump label_2001

label label_2001:
    $ charisma += 4
    if intelligence >= 16:
        jump label_2002

label label_2002:
    $ intelligence += 2
    jump end_2003

    jump label_2003

label label_2003:
    "Ветка false для label_2002"
    jump end_2004

    jump label_2004

label label_2004:
    "Ветка false для label_2001"
    if luck >= 17:
        jump label_2005

label label_2005:
    $ luck += 3
    jump end_2006

    jump label_2006

label label_2006:
    "Ветка false для label_2005"
    jump end_2007

label label_1999:
    "Scene label_1999"
    menu:
        "Open door":
            jump label_2007
        "Explore":
            $ luck += 3
            jump label_2008
        "Open door":
            jump label_2009

label label_2007:
    "Scene label_2007"
    menu:
        "Talk":
            $ intelligence += 2
            jump label_2010
        "Open door":
            $ luck += 1
            jump label_2011
        "Go forward":
            jump label_2012
        "Use item":
            jump label_2013

label label_2010:
    "Scene label_2010"
    jump end_2014

label label_2011:
    "Scene label_2011"
    jump end_2014

label label_2012:
    "Scene label_2012"
    jump end_2014

label label_2013:
    "Scene label_2013"
    jump end_2014

label label_2008:
    "Scene label_2008"
    menu:
        "Use item":
            jump label_2014
        "Open door":
            $ strength += 3
            jump label_2015
        "Explore":
            jump label_2016

label label_2014:
    "Scene label_2014"
    jump end_2017

label label_2015:
    "Scene label_2015"
    jump end_2017

label label_2016:
    "Scene label_2016"
    jump end_2017

label label_2009:
    "Scene label_2009"
    menu:
        "Explore":
            $ charisma += 3
            jump label_2017
        "Use item":
            $ luck += 3
            jump label_2018
        "Go back":
            jump label_2019

label label_2017:
    "Scene label_2017"
    jump end_2020

label label_2018:
    "Scene label_2018"
    jump end_2020

label label_2019:
    "Scene label_2019"
    jump end_2020

label label_2000:
    "Scene label_2000"
    menu:
        "Use item":
            $ strength += 2
            jump label_2020
        "Go back":
            jump label_2021
        "Pick up item":
            $ luck += 1
            jump label_2022
        "Open door":
            jump label_2023

label label_2020:
    "Scene label_2020"
    menu:
        "Pick up item":
            jump label_2024
        "Open door":
            jump label_2025

label label_2024:
    "Scene label_2024"
    jump end_2026

label label_2025:
    "Scene label_2025"
    jump end_2026

label label_2021:
    "Scene label_2021"
    menu:
        "Use item":
            jump label_2026
        "Use item":
            $ luck += 3
            jump label_2027
        "Go forward":
            jump label_2028
        "Go back":
            $ strength += 3
            jump label_2029

label label_2026:
    "Scene label_2026"
    jump end_2030

label label_2027:
    "Scene label_2027"
    jump end_2030

label label_2028:
    "Scene label_2028"
    jump end_2030

label label_2029:
    "Scene label_2029"
    jump end_2030

label label_2022:
    "Scene label_2022"
    if intelligence >= 19:
        jump label_2030

label label_2030:
    $ intelligence += 3
    jump end_2031

    jump label_2031

label label_2031:
    "Ветка false для label_2030"
    jump end_2032

label label_2023:
    "Scene label_2023"
    menu:
        "Go forward":
            jump label_2032
        "Go back":
            jump label_2033
        "Open door":
            $ luck += 3
            jump label_2034

label label_2032:
    "Scene label_2032"
    jump end_2035

label label_2033:
    "Scene label_2033"
    jump end_2035

label label_2034:
    "Scene label_2034"
    jump end_2035

label label_1977:
    "Scene label_1977"
    menu:
        "Use item":
            jump label_2035
        "Go back":
            jump label_2036
        "Use item":
            jump label_2037

label label_2035:
    "Scene label_2035"
    menu:
        "Explore":
            $ intelligence += 1
            jump label_2038
        "Open door":
            $ intelligence += 2
            jump label_2039
        "Go forward":
            $ luck += 1
            jump label_2040
        "Go back":
            jump label_2041

label label_2038:
    "Scene label_2038"
    menu:
        "Use item":
            jump label_2042
        "Explore":
            $ luck += 2
            jump label_2043
        "Look around":
            $ intelligence += 1
            jump label_2044

label label_2042:
    "Scene label_2042"
    jump end_2045

label label_2043:
    "Scene label_2043"
    jump end_2045

label label_2044:
    "Scene label_2044"
    jump end_2045

label label_2039:
    "Scene label_2039"
    menu:
        "Use item":
            $ luck += 1
            jump label_2045
        "Look around":
            jump label_2046

label label_2045:
    "Scene label_2045"
    jump end_2047

label label_2046:
    "Scene label_2046"
    jump end_2047

label label_2040:
    "Scene label_2040"
    menu:
        "Pick up item":
            jump label_2047
        "Pick up item":
            jump label_2048
        "Go back":
            jump label_2049
        "Explore":
            jump label_2050

label label_2047:
    "Scene label_2047"
    jump end_2051

label label_2048:
    "Scene label_2048"
    jump end_2051

label label_2049:
    "Scene label_2049"
    jump end_2051

label label_2050:
    "Scene label_2050"
    jump end_2051

label label_2041:
    "Scene label_2041"
    menu:
        "Use item":
            jump label_2051
        "Go back":
            jump label_2052
        "Look around":
            jump label_2053

label label_2051:
    "Scene label_2051"
    jump end_2054

label label_2052:
    "Scene label_2052"
    jump end_2054

label label_2053:
    "Scene label_2053"
    jump end_2054

label label_2036:
    "Scene label_2036"
    if luck >= 10:
        jump label_2054

label label_2054:
    $ luck += 3
    menu:
        "Explore":
            $ charisma += 2
            jump label_2055
        "Look around":
            jump label_2056
        "Open door":
            $ intelligence += 3
            jump label_2057
        "Pick up item":
            jump label_2058

label label_2055:
    "Scene label_2055"
    jump end_2059

label label_2056:
    "Scene label_2056"
    jump end_2059

label label_2057:
    "Scene label_2057"
    jump end_2059

label label_2058:
    "Scene label_2058"
    jump end_2059

    jump label_2059

label label_2059:
    "Ветка false для label_2054"
    menu:
        "Use item":
            jump label_2060
        "Pick up item":
            jump label_2061

label label_2060:
    "Scene label_2060"
    jump end_2062

label label_2061:
    "Scene label_2061"
    jump end_2062

label label_2037:
    "Scene label_2037"
    menu:
        "Explore":
            $ strength += 1
            jump label_2062
        "Pick up item":
            $ luck += 1
            jump label_2063
        "Explore":
            jump label_2064

label label_2062:
    "Scene label_2062"
    menu:
        "Explore":
            jump label_2065
        "Look around":
            $ strength += 3
            jump label_2066

label label_2065:
    "Scene label_2065"
    jump end_2067

label label_2066:
    "Scene label_2066"
    jump end_2067

label label_2063:
    "Scene label_2063"
    menu:
        "Talk":
            $ luck += 1
            jump label_2067
        "Go forward":
            jump label_2068

label label_2067:
    "Scene label_2067"
    jump end_2069

label label_2068:
    "Scene label_2068"
    jump end_2069

label label_2064:
    "Scene label_2064"
    menu:
        "Go back":
            jump label_2069
        "Open door":
            $ strength += 1
            jump label_2070

label label_2069:
    "Scene label_2069"
    jump end_2071

label label_2070:
    "Scene label_2070"
    jump end_2071

label label_1978:
    "Scene label_1978"
    menu:
        "Talk":
            jump label_2071
        "Open door":
            jump label_2072
        "Go back":
            $ charisma += 1
            jump label_2073
        "Explore":
            $ luck += 3
            jump label_2074

label label_2071:
    "Scene label_2071"
    if strength >= 5:
        jump label_2075

label label_2075:
    $ strength += 4
    menu:
        "Look around":
            jump label_2076
        "Look around":
            $ strength += 2
            jump label_2077
        "Explore":
            $ strength += 1
            jump label_2078
        "Use item":
            jump label_2079

label label_2076:
    "Scene label_2076"
    jump end_2080

label label_2077:
    "Scene label_2077"
    jump end_2080

label label_2078:
    "Scene label_2078"
    jump end_2080

label label_2079:
    "Scene label_2079"
    jump end_2080

    jump label_2080

label label_2080:
    "Ветка false для label_2075"
    if strength >= 13:
        jump label_2081

label label_2081:
    $ strength += 4
    jump end_2082

    jump label_2082

label label_2082:
    "Ветка false для label_2081"
    jump end_2083

label label_2072:
    "Scene label_2072"
    menu:
        "Look around":
            jump label_2083
        "Go back":
            jump label_2084
        "Go back":
            $ charisma += 1
            jump label_2085
        "Go back":
            jump label_2086

label label_2083:
    "Scene label_2083"
    menu:
        "Explore":
            $ strength += 1
            jump label_2087
        "Look around":
            $ strength += 1
            jump label_2088
        "Pick up item":
            $ luck += 2
            jump label_2089
        "Look around":
            $ intelligence += 1
            jump label_2090

label label_2087:
    "Scene label_2087"
    jump end_2091

label label_2088:
    "Scene label_2088"
    jump end_2091

label label_2089:
    "Scene label_2089"
    jump end_2091

label label_2090:
    "Scene label_2090"
    jump end_2091

label label_2084:
    "Scene label_2084"
    menu:
        "Look around":
            jump label_2091
        "Go forward":
            $ intelligence += 1
            jump label_2092

label label_2091:
    "Scene label_2091"
    jump end_2093

label label_2092:
    "Scene label_2092"
    jump end_2093

label label_2085:
    "Scene label_2085"
    menu:
        "Use item":
            jump label_2093
        "Go forward":
            jump label_2094
        "Go back":
            jump label_2095
        "Use item":
            $ intelligence += 1
            jump label_2096

label label_2093:
    "Scene label_2093"
    jump end_2097

label label_2094:
    "Scene label_2094"
    jump end_2097

label label_2095:
    "Scene label_2095"
    jump end_2097

label label_2096:
    "Scene label_2096"
    jump end_2097

label label_2086:
    "Scene label_2086"
    menu:
        "Open door":
            $ luck += 2
            jump label_2097
        "Talk":
            $ charisma += 3
            jump label_2098
        "Go back":
            $ strength += 3
            jump label_2099
        "Open door":
            $ charisma += 1
            jump label_2100

label label_2097:
    "Scene label_2097"
    jump end_2101

label label_2098:
    "Scene label_2098"
    jump end_2101

label label_2099:
    "Scene label_2099"
    jump end_2101

label label_2100:
    "Scene label_2100"
    jump end_2101

label label_2073:
    "Scene label_2073"
    menu:
        "Use item":
            jump label_2101
        "Talk":
            jump label_2102
        "Look around":
            jump label_2103

label label_2101:
    "Scene label_2101"
    if strength >= 12:
        jump label_2104

label label_2104:
    $ strength += 3
    jump end_2105

    jump label_2105

label label_2105:
    "Ветка false для label_2104"
    jump end_2106

label label_2102:
    "Scene label_2102"
    menu:
        "Look around":
            jump label_2106
        "Talk":
            jump label_2107
        "Go back":
            jump label_2108
        "Go forward":
            jump label_2109

label label_2106:
    "Scene label_2106"
    jump end_2110

label label_2107:
    "Scene label_2107"
    jump end_2110

label label_2108:
    "Scene label_2108"
    jump end_2110

label label_2109:
    "Scene label_2109"
    jump end_2110

label label_2103:
    "Scene label_2103"
    menu:
        "Go forward":
            $ luck += 1
            jump label_2110
        "Pick up item":
            $ strength += 2
            jump label_2111
        "Explore":
            jump label_2112
        "Open door":
            jump label_2113

label label_2110:
    "Scene label_2110"
    jump end_2114

label label_2111:
    "Scene label_2111"
    jump end_2114

label label_2112:
    "Scene label_2112"
    jump end_2114

label label_2113:
    "Scene label_2113"
    jump end_2114

label label_2074:
    "Scene label_2074"
    menu:
        "Use item":
            jump label_2114
        "Talk":
            $ luck += 1
            jump label_2115
        "Use item":
            $ luck += 2
            jump label_2116

label label_2114:
    "Scene label_2114"
    if strength >= 18:
        jump label_2117

label label_2117:
    $ strength += 5
    jump end_2118

    jump label_2118

label label_2118:
    "Ветка false для label_2117"
    jump end_2119

label label_2115:
    "Scene label_2115"
    if strength >= 19:
        jump label_2119

label label_2119:
    $ strength += 4
    jump end_2120

    jump label_2120

label label_2120:
    "Ветка false для label_2119"
    jump end_2121

label label_2116:
    "Scene label_2116"
    if strength >= 14:
        jump label_2121

label label_2121:
    $ strength += 3
    jump end_2122

    jump label_2122

label label_2122:
    "Ветка false для label_2121"
    jump end_2123

label label_1974:
    "Scene label_1974"
    if intelligence >= 18:
        jump label_2123

label label_2123:
    $ intelligence += 2
    menu:
        "Look around":
            jump label_2124
        "Explore":
            $ intelligence += 2
            jump label_2125
        "Use item":
            jump label_2126
        "Go back":
            jump label_2127

label label_2124:
    "Scene label_2124"
    menu:
        "Talk":
            $ charisma += 1
            jump label_2128
        "Go forward":
            jump label_2129
        "Pick up item":
            $ intelligence += 1
            jump label_2130

label label_2128:
    "Scene label_2128"
    if luck >= 13:
        jump label_2131

label label_2131:
    $ luck += 2
    jump end_2132

    jump label_2132

label label_2132:
    "Ветка false для label_2131"
    jump end_2133

label label_2129:
    "Scene label_2129"
    if luck >= 17:
        jump label_2133

label label_2133:
    $ luck += 2
    jump end_2134

    jump label_2134

label label_2134:
    "Ветка false для label_2133"
    jump end_2135

label label_2130:
    "Scene label_2130"
    if strength >= 12:
        jump label_2135

label label_2135:
    $ strength += 4
    jump end_2136

    jump label_2136

label label_2136:
    "Ветка false для label_2135"
    jump end_2137

label label_2125:
    "Scene label_2125"
    if intelligence >= 10:
        jump label_2137

label label_2137:
    $ intelligence += 5
    menu:
        "Talk":
            jump label_2138
        "Explore":
            jump label_2139

label label_2138:
    "Scene label_2138"
    jump end_2140

label label_2139:
    "Scene label_2139"
    jump end_2140

    jump label_2140

label label_2140:
    "Ветка false для label_2137"
    menu:
        "Explore":
            $ intelligence += 1
            jump label_2141
        "Look around":
            jump label_2142
        "Open door":
            $ luck += 3
            jump label_2143

label label_2141:
    "Scene label_2141"
    jump end_2144

label label_2142:
    "Scene label_2142"
    jump end_2144

label label_2143:
    "Scene label_2143"
    jump end_2144

label label_2126:
    "Scene label_2126"
    if charisma >= 16:
        jump label_2144

label label_2144:
    $ charisma += 2
    menu:
        "Use item":
            jump label_2145
        "Explore":
            $ luck += 2
            jump label_2146
        "Pick up item":
            jump label_2147
        "Explore":
            $ charisma += 3
            jump label_2148

label label_2145:
    "Scene label_2145"
    jump end_2149

label label_2146:
    "Scene label_2146"
    jump end_2149

label label_2147:
    "Scene label_2147"
    jump end_2149

label label_2148:
    "Scene label_2148"
    jump end_2149

    jump label_2149

label label_2149:
    "Ветка false для label_2144"
    if strength >= 8:
        jump label_2150

label label_2150:
    $ strength += 3
    jump end_2151

    jump label_2151

label label_2151:
    "Ветка false для label_2150"
    jump end_2152

label label_2127:
    "Scene label_2127"
    if strength >= 11:
        jump label_2152

label label_2152:
    $ strength += 5
    menu:
        "Look around":
            $ charisma += 3
            jump label_2153
        "Talk":
            $ intelligence += 1
            jump label_2154
        "Explore":
            $ luck += 1
            jump label_2155
        "Open door":
            $ luck += 3
            jump label_2156

label label_2153:
    "Scene label_2153"
    jump end_2157

label label_2154:
    "Scene label_2154"
    jump end_2157

label label_2155:
    "Scene label_2155"
    jump end_2157

label label_2156:
    "Scene label_2156"
    jump end_2157

    jump label_2157

label label_2157:
    "Ветка false для label_2152"
    menu:
        "Use item":
            $ intelligence += 3
            jump label_2158
        "Look around":
            $ luck += 3
            jump label_2159
        "Use item":
            $ luck += 3
            jump label_2160

label label_2158:
    "Scene label_2158"
    jump end_2161

label label_2159:
    "Scene label_2159"
    jump end_2161

label label_2160:
    "Scene label_2160"
    jump end_2161

    jump label_2161

label label_2161:
    "Ветка false для label_2123"
    if strength >= 20:
        jump label_2162

label label_2162:
    $ strength += 3
    menu:
        "Look around":
            $ intelligence += 3
            jump label_2163
        "Go back":
            $ luck += 2
            jump label_2164
        "Pick up item":
            jump label_2165

label label_2163:
    "Scene label_2163"
    if strength >= 5:
        jump label_2166

label label_2166:
    $ strength += 4
    jump end_2167

    jump label_2167

label label_2167:
    "Ветка false для label_2166"
    jump end_2168

label label_2164:
    "Scene label_2164"
    if intelligence >= 12:
        jump label_2168

label label_2168:
    $ intelligence += 2
    jump end_2169

    jump label_2169

label label_2169:
    "Ветка false для label_2168"
    jump end_2170

label label_2165:
    "Scene label_2165"
    menu:
        "Use item":
            $ luck += 2
            jump label_2170
        "Go forward":
            jump label_2171

label label_2170:
    "Scene label_2170"
    jump end_2172

label label_2171:
    "Scene label_2171"
    jump end_2172

    jump label_2172

label label_2172:
    "Ветка false для label_2162"
    if intelligence >= 6:
        jump label_2173

label label_2173:
    $ intelligence += 2
    menu:
        "Use item":
            $ luck += 3
            jump label_2174
        "Open door":
            $ strength += 1
            jump label_2175
        "Pick up item":
            $ intelligence += 2
            jump label_2176
        "Go forward":
            jump label_2177

label label_2174:
    "Scene label_2174"
    jump end_2178

label label_2175:
    "Scene label_2175"
    jump end_2178

label label_2176:
    "Scene label_2176"
    jump end_2178

label label_2177:
    "Scene label_2177"
    jump end_2178

    jump label_2178

label label_2178:
    "Ветка false для label_2173"
    menu:
        "Look around":
            $ intelligence += 1
            jump label_2179
        "Look around":
            $ strength += 2
            jump label_2180
        "Use item":
            jump label_2181

label label_2179:
    "Scene label_2179"
    jump end_2182

label label_2180:
    "Scene label_2180"
    jump end_2182

label label_2181:
    "Scene label_2181"
    jump end_2182

label label_1972:
    "Scene label_1972"
    if luck >= 19:
        jump label_2182

label label_2182:
    $ luck += 3
    menu:
        "Use item":
            jump label_2183
        "Open door":
            $ charisma += 2
            jump label_2184
        "Explore":
            $ intelligence += 3
            jump label_2185
        "Go forward":
            $ luck += 2
            jump label_2186

label label_2183:
    "Scene label_2183"
    menu:
        "Look around":
            jump label_2187
        "Look around":
            jump label_2188
        "Talk":
            jump label_2189

label label_2187:
    "Scene label_2187"
    if strength >= 20:
        jump label_2190

label label_2190:
    $ strength += 5
    menu:
        "Talk":
            $ intelligence += 3
            jump label_2191
        "Use item":
            jump label_2192
        "Use item":
            jump label_2193
        "Look around":
            $ strength += 2
            jump label_2194

label label_2191:
    "Scene label_2191"
    jump end_2195

label label_2192:
    "Scene label_2192"
    jump end_2195

label label_2193:
    "Scene label_2193"
    jump end_2195

label label_2194:
    "Scene label_2194"
    jump end_2195

    jump label_2195

label label_2195:
    "Ветка false для label_2190"
    menu:
        "Go back":
            $ intelligence += 1
            jump label_2196
        "Go forward":
            $ intelligence += 1
            jump label_2197

label label_2196:
    "Scene label_2196"
    jump end_2198

label label_2197:
    "Scene label_2197"
    jump end_2198

label label_2188:
    "Scene label_2188"
    menu:
        "Look around":
            jump label_2198
        "Pick up item":
            $ strength += 3
            jump label_2199

label label_2198:
    "Scene label_2198"
    menu:
        "Talk":
            jump label_2200
        "Explore":
            $ strength += 1
            jump label_2201
        "Go forward":
            jump label_2202

label label_2200:
    "Scene label_2200"
    jump end_2203

label label_2201:
    "Scene label_2201"
    jump end_2203

label label_2202:
    "Scene label_2202"
    jump end_2203

label label_2199:
    "Scene label_2199"
    menu:
        "Explore":
            $ strength += 1
            jump label_2203
        "Use item":
            $ strength += 2
            jump label_2204

label label_2203:
    "Scene label_2203"
    jump end_2205

label label_2204:
    "Scene label_2204"
    jump end_2205

label label_2189:
    "Scene label_2189"
    menu:
        "Explore":
            $ strength += 3
            jump label_2205
        "Talk":
            jump label_2206
        "Explore":
            $ strength += 3
            jump label_2207
        "Go back":
            jump label_2208

label label_2205:
    "Scene label_2205"
    if strength >= 9:
        jump label_2209

label label_2209:
    $ strength += 5
    jump end_2210

    jump label_2210

label label_2210:
    "Ветка false для label_2209"
    jump end_2211

label label_2206:
    "Scene label_2206"
    if strength >= 9:
        jump label_2211

label label_2211:
    $ strength += 3
    jump end_2212

    jump label_2212

label label_2212:
    "Ветка false для label_2211"
    jump end_2213

label label_2207:
    "Scene label_2207"
    menu:
        "Go forward":
            $ charisma += 1
            jump label_2213
        "Open door":
            $ strength += 3
            jump label_2214
        "Go forward":
            $ luck += 1
            jump label_2215

label label_2213:
    "Scene label_2213"
    jump end_2216

label label_2214:
    "Scene label_2214"
    jump end_2216

label label_2215:
    "Scene label_2215"
    jump end_2216

label label_2208:
    "Scene label_2208"
    menu:
        "Explore":
            $ luck += 3
            jump label_2216
        "Talk":
            $ strength += 1
            jump label_2217
        "Open door":
            $ luck += 3
            jump label_2218
        "Use item":
            jump label_2219

label label_2216:
    "Scene label_2216"
    jump end_2220

label label_2217:
    "Scene label_2217"
    jump end_2220

label label_2218:
    "Scene label_2218"
    jump end_2220

label label_2219:
    "Scene label_2219"
    jump end_2220

label label_2184:
    "Scene label_2184"
    menu:
        "Explore":
            $ intelligence += 3
            jump label_2220
        "Open door":
            jump label_2221

label label_2220:
    "Scene label_2220"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_2222
        "Open door":
            jump label_2223

label label_2222:
    "Scene label_2222"
    menu:
        "Explore":
            jump label_2224
        "Go forward":
            jump label_2225
        "Talk":
            $ strength += 2
            jump label_2226

label label_2224:
    "Scene label_2224"
    jump end_2227

label label_2225:
    "Scene label_2225"
    jump end_2227

label label_2226:
    "Scene label_2226"
    jump end_2227

label label_2223:
    "Scene label_2223"
    menu:
        "Open door":
            $ strength += 3
            jump label_2227
        "Go forward":
            $ luck += 3
            jump label_2228

label label_2227:
    "Scene label_2227"
    jump end_2229

label label_2228:
    "Scene label_2228"
    jump end_2229

label label_2221:
    "Scene label_2221"
    if charisma >= 20:
        jump label_2229

label label_2229:
    $ charisma += 3
    menu:
        "Use item":
            jump label_2230
        "Look around":
            $ intelligence += 1
            jump label_2231
        "Look around":
            $ charisma += 3
            jump label_2232

label label_2230:
    "Scene label_2230"
    jump end_2233

label label_2231:
    "Scene label_2231"
    jump end_2233

label label_2232:
    "Scene label_2232"
    jump end_2233

    jump label_2233

label label_2233:
    "Ветка false для label_2229"
    menu:
        "Talk":
            jump label_2234
        "Go back":
            $ intelligence += 1
            jump label_2235
        "Use item":
            jump label_2236
        "Talk":
            $ charisma += 1
            jump label_2237

label label_2234:
    "Scene label_2234"
    jump end_2238

label label_2235:
    "Scene label_2235"
    jump end_2238

label label_2236:
    "Scene label_2236"
    jump end_2238

label label_2237:
    "Scene label_2237"
    jump end_2238

label label_2185:
    "Scene label_2185"
    if luck >= 7:
        jump label_2238

label label_2238:
    $ luck += 5
    menu:
        "Go back":
            jump label_2239
        "Open door":
            $ luck += 2
            jump label_2240
        "Go forward":
            $ intelligence += 3
            jump label_2241

label label_2239:
    "Scene label_2239"
    menu:
        "Talk":
            $ strength += 3
            jump label_2242
        "Look around":
            $ luck += 2
            jump label_2243
        "Go back":
            jump label_2244

label label_2242:
    "Scene label_2242"
    jump end_2245

label label_2243:
    "Scene label_2243"
    jump end_2245

label label_2244:
    "Scene label_2244"
    jump end_2245

label label_2240:
    "Scene label_2240"
    menu:
        "Go forward":
            jump label_2245
        "Look around":
            $ intelligence += 2
            jump label_2246
        "Explore":
            jump label_2247
        "Talk":
            $ strength += 3
            jump label_2248

label label_2245:
    "Scene label_2245"
    jump end_2249

label label_2246:
    "Scene label_2246"
    jump end_2249

label label_2247:
    "Scene label_2247"
    jump end_2249

label label_2248:
    "Scene label_2248"
    jump end_2249

label label_2241:
    "Scene label_2241"
    menu:
        "Go back":
            jump label_2249
        "Go forward":
            jump label_2250

label label_2249:
    "Scene label_2249"
    jump end_2251

label label_2250:
    "Scene label_2250"
    jump end_2251

    jump label_2251

label label_2251:
    "Ветка false для label_2238"
    if intelligence >= 11:
        jump label_2252

label label_2252:
    $ intelligence += 3
    menu:
        "Use item":
            jump label_2253
        "Go back":
            jump label_2254
        "Look around":
            $ intelligence += 1
            jump label_2255

label label_2253:
    "Scene label_2253"
    jump end_2256

label label_2254:
    "Scene label_2254"
    jump end_2256

label label_2255:
    "Scene label_2255"
    jump end_2256

    jump label_2256

label label_2256:
    "Ветка false для label_2252"
    menu:
        "Look around":
            jump label_2257
        "Pick up item":
            jump label_2258

label label_2257:
    "Scene label_2257"
    jump end_2259

label label_2258:
    "Scene label_2258"
    jump end_2259

label label_2186:
    "Scene label_2186"
    menu:
        "Go forward":
            jump label_2259
        "Use item":
            $ strength += 3
            jump label_2260

label label_2259:
    "Scene label_2259"
    menu:
        "Use item":
            $ luck += 1
            jump label_2261
        "Go forward":
            jump label_2262
        "Go forward":
            jump label_2263

label label_2261:
    "Scene label_2261"
    menu:
        "Pick up item":
            jump label_2264
        "Explore":
            jump label_2265
        "Look around":
            $ charisma += 3
            jump label_2266
        "Go forward":
            $ intelligence += 1
            jump label_2267

label label_2264:
    "Scene label_2264"
    jump end_2268

label label_2265:
    "Scene label_2265"
    jump end_2268

label label_2266:
    "Scene label_2266"
    jump end_2268

label label_2267:
    "Scene label_2267"
    jump end_2268

label label_2262:
    "Scene label_2262"
    menu:
        "Look around":
            $ charisma += 1
            jump label_2268
        "Talk":
            jump label_2269

label label_2268:
    "Scene label_2268"
    jump end_2270

label label_2269:
    "Scene label_2269"
    jump end_2270

label label_2263:
    "Scene label_2263"
    menu:
        "Use item":
            jump label_2270
        "Explore":
            $ charisma += 2
            jump label_2271

label label_2270:
    "Scene label_2270"
    jump end_2272

label label_2271:
    "Scene label_2271"
    jump end_2272

label label_2260:
    "Scene label_2260"
    menu:
        "Look around":
            jump label_2272
        "Open door":
            jump label_2273
        "Use item":
            $ luck += 1
            jump label_2274
        "Go forward":
            $ strength += 1
            jump label_2275

label label_2272:
    "Scene label_2272"
    menu:
        "Go back":
            $ luck += 1
            jump label_2276
        "Use item":
            $ charisma += 2
            jump label_2277
        "Go forward":
            jump label_2278
        "Open door":
            $ intelligence += 1
            jump label_2279

label label_2276:
    "Scene label_2276"
    jump end_2280

label label_2277:
    "Scene label_2277"
    jump end_2280

label label_2278:
    "Scene label_2278"
    jump end_2280

label label_2279:
    "Scene label_2279"
    jump end_2280

label label_2273:
    "Scene label_2273"
    menu:
        "Talk":
            $ charisma += 2
            jump label_2280
        "Explore":
            $ strength += 1
            jump label_2281
        "Go back":
            jump label_2282
        "Go back":
            $ charisma += 3
            jump label_2283

label label_2280:
    "Scene label_2280"
    jump end_2284

label label_2281:
    "Scene label_2281"
    jump end_2284

label label_2282:
    "Scene label_2282"
    jump end_2284

label label_2283:
    "Scene label_2283"
    jump end_2284

label label_2274:
    "Scene label_2274"
    if luck >= 5:
        jump label_2284

label label_2284:
    $ luck += 4
    jump end_2285

    jump label_2285

label label_2285:
    "Ветка false для label_2284"
    jump end_2286

label label_2275:
    "Scene label_2275"
    if charisma >= 18:
        jump label_2286

label label_2286:
    $ charisma += 5
    jump end_2287

    jump label_2287

label label_2287:
    "Ветка false для label_2286"
    jump end_2288

    jump label_2288

label label_2288:
    "Ветка false для label_2182"
    menu:
        "Go forward":
            jump label_2289
        "Look around":
            $ intelligence += 2
            jump label_2290
        "Go forward":
            jump label_2291
        "Use item":
            jump label_2292

label label_2289:
    "Scene label_2289"
    if intelligence >= 16:
        jump label_2293

label label_2293:
    $ intelligence += 5
    menu:
        "Look around":
            jump label_2294
        "Go forward":
            $ charisma += 1
            jump label_2295
        "Explore":
            jump label_2296
        "Use item":
            $ intelligence += 1
            jump label_2297

label label_2294:
    "Scene label_2294"
    if luck >= 16:
        jump label_2298

label label_2298:
    $ luck += 2
    jump end_2299

    jump label_2299

label label_2299:
    "Ветка false для label_2298"
    jump end_2300

label label_2295:
    "Scene label_2295"
    menu:
        "Talk":
            $ strength += 2
            jump label_2300
        "Pick up item":
            $ intelligence += 3
            jump label_2301
        "Use item":
            jump label_2302
        "Go back":
            $ strength += 1
            jump label_2303

label label_2300:
    "Scene label_2300"
    jump end_2304

label label_2301:
    "Scene label_2301"
    jump end_2304

label label_2302:
    "Scene label_2302"
    jump end_2304

label label_2303:
    "Scene label_2303"
    jump end_2304

label label_2296:
    "Scene label_2296"
    if strength >= 19:
        jump label_2304

label label_2304:
    $ strength += 3
    jump end_2305

    jump label_2305

label label_2305:
    "Ветка false для label_2304"
    jump end_2306

label label_2297:
    "Scene label_2297"
    menu:
        "Pick up item":
            jump label_2306
        "Talk":
            $ intelligence += 1
            jump label_2307

label label_2306:
    "Scene label_2306"
    jump end_2308

label label_2307:
    "Scene label_2307"
    jump end_2308

    jump label_2308

label label_2308:
    "Ветка false для label_2293"
    menu:
        "Look around":
            $ luck += 2
            jump label_2309
        "Go forward":
            jump label_2310
        "Go forward":
            jump label_2311
        "Look around":
            jump label_2312

label label_2309:
    "Scene label_2309"
    if intelligence >= 5:
        jump label_2313

label label_2313:
    $ intelligence += 5
    jump end_2314

    jump label_2314

label label_2314:
    "Ветка false для label_2313"
    jump end_2315

label label_2310:
    "Scene label_2310"
    menu:
        "Talk":
            $ charisma += 3
            jump label_2315
        "Open door":
            jump label_2316
        "Go back":
            jump label_2317
        "Pick up item":
            $ luck += 1
            jump label_2318

label label_2315:
    "Scene label_2315"
    jump end_2319

label label_2316:
    "Scene label_2316"
    jump end_2319

label label_2317:
    "Scene label_2317"
    jump end_2319

label label_2318:
    "Scene label_2318"
    jump end_2319

label label_2311:
    "Scene label_2311"
    menu:
        "Open door":
            jump label_2319
        "Use item":
            $ strength += 2
            jump label_2320
        "Go forward":
            jump label_2321

label label_2319:
    "Scene label_2319"
    jump end_2322

label label_2320:
    "Scene label_2320"
    jump end_2322

label label_2321:
    "Scene label_2321"
    jump end_2322

label label_2312:
    "Scene label_2312"
    menu:
        "Use item":
            jump label_2322
        "Use item":
            $ intelligence += 2
            jump label_2323
        "Talk":
            jump label_2324
        "Open door":
            $ strength += 2
            jump label_2325

label label_2322:
    "Scene label_2322"
    jump end_2326

label label_2323:
    "Scene label_2323"
    jump end_2326

label label_2324:
    "Scene label_2324"
    jump end_2326

label label_2325:
    "Scene label_2325"
    jump end_2326

label label_2290:
    "Scene label_2290"
    menu:
        "Pick up item":
            $ strength += 2
            jump label_2326
        "Open door":
            jump label_2327

label label_2326:
    "Scene label_2326"
    if charisma >= 10:
        jump label_2328

label label_2328:
    $ charisma += 3
    menu:
        "Use item":
            jump label_2329
        "Use item":
            $ luck += 3
            jump label_2330
        "Use item":
            jump label_2331
        "Talk":
            jump label_2332

label label_2329:
    "Scene label_2329"
    jump end_2333

label label_2330:
    "Scene label_2330"
    jump end_2333

label label_2331:
    "Scene label_2331"
    jump end_2333

label label_2332:
    "Scene label_2332"
    jump end_2333

    jump label_2333

label label_2333:
    "Ветка false для label_2328"
    menu:
        "Go back":
            jump label_2334
        "Explore":
            jump label_2335

label label_2334:
    "Scene label_2334"
    jump end_2336

label label_2335:
    "Scene label_2335"
    jump end_2336

label label_2327:
    "Scene label_2327"
    menu:
        "Talk":
            jump label_2336
        "Open door":
            $ intelligence += 2
            jump label_2337

label label_2336:
    "Scene label_2336"
    menu:
        "Talk":
            $ luck += 1
            jump label_2338
        "Open door":
            jump label_2339
        "Explore":
            $ strength += 1
            jump label_2340

label label_2338:
    "Scene label_2338"
    jump end_2341

label label_2339:
    "Scene label_2339"
    jump end_2341

label label_2340:
    "Scene label_2340"
    jump end_2341

label label_2337:
    "Scene label_2337"
    if charisma >= 18:
        jump label_2341

label label_2341:
    $ charisma += 2
    jump end_2342

    jump label_2342

label label_2342:
    "Ветка false для label_2341"
    jump end_2343

label label_2291:
    "Scene label_2291"
    menu:
        "Talk":
            jump label_2343
        "Explore":
            jump label_2344
        "Look around":
            $ intelligence += 2
            jump label_2345
        "Open door":
            jump label_2346

label label_2343:
    "Scene label_2343"
    if luck >= 13:
        jump label_2347

label label_2347:
    $ luck += 2
    menu:
        "Pick up item":
            jump label_2348
        "Go forward":
            $ charisma += 3
            jump label_2349

label label_2348:
    "Scene label_2348"
    jump end_2350

label label_2349:
    "Scene label_2349"
    jump end_2350

    jump label_2350

label label_2350:
    "Ветка false для label_2347"
    menu:
        "Look around":
            jump label_2351
        "Look around":
            jump label_2352
        "Open door":
            jump label_2353

label label_2351:
    "Scene label_2351"
    jump end_2354

label label_2352:
    "Scene label_2352"
    jump end_2354

label label_2353:
    "Scene label_2353"
    jump end_2354

label label_2344:
    "Scene label_2344"
    if intelligence >= 15:
        jump label_2354

label label_2354:
    $ intelligence += 2
    if strength >= 17:
        jump label_2355

label label_2355:
    $ strength += 2
    jump end_2356

    jump label_2356

label label_2356:
    "Ветка false для label_2355"
    jump end_2357

    jump label_2357

label label_2357:
    "Ветка false для label_2354"
    menu:
        "Look around":
            $ strength += 3
            jump label_2358
        "Explore":
            $ charisma += 1
            jump label_2359
        "Use item":
            jump label_2360

label label_2358:
    "Scene label_2358"
    jump end_2361

label label_2359:
    "Scene label_2359"
    jump end_2361

label label_2360:
    "Scene label_2360"
    jump end_2361

label label_2345:
    "Scene label_2345"
    menu:
        "Open door":
            jump label_2361
        "Go forward":
            jump label_2362
        "Use item":
            jump label_2363
        "Go back":
            $ charisma += 2
            jump label_2364

label label_2361:
    "Scene label_2361"
    menu:
        "Open door":
            $ charisma += 1
            jump label_2365
        "Open door":
            jump label_2366
        "Open door":
            jump label_2367

label label_2365:
    "Scene label_2365"
    jump end_2368

label label_2366:
    "Scene label_2366"
    jump end_2368

label label_2367:
    "Scene label_2367"
    jump end_2368

label label_2362:
    "Scene label_2362"
    menu:
        "Go forward":
            jump label_2368
        "Look around":
            jump label_2369
        "Pick up item":
            jump label_2370

label label_2368:
    "Scene label_2368"
    jump end_2371

label label_2369:
    "Scene label_2369"
    jump end_2371

label label_2370:
    "Scene label_2370"
    jump end_2371

label label_2363:
    "Scene label_2363"
    menu:
        "Go forward":
            jump label_2371
        "Look around":
            jump label_2372
        "Go back":
            $ luck += 1
            jump label_2373

label label_2371:
    "Scene label_2371"
    jump end_2374

label label_2372:
    "Scene label_2372"
    jump end_2374

label label_2373:
    "Scene label_2373"
    jump end_2374

label label_2364:
    "Scene label_2364"
    menu:
        "Use item":
            $ strength += 1
            jump label_2374
        "Explore":
            $ intelligence += 1
            jump label_2375

label label_2374:
    "Scene label_2374"
    jump end_2376

label label_2375:
    "Scene label_2375"
    jump end_2376

label label_2346:
    "Scene label_2346"
    menu:
        "Look around":
            $ strength += 2
            jump label_2376
        "Go forward":
            $ intelligence += 3
            jump label_2377
        "Look around":
            $ intelligence += 1
            jump label_2378

label label_2376:
    "Scene label_2376"
    menu:
        "Open door":
            $ luck += 1
            jump label_2379
        "Pick up item":
            $ luck += 2
            jump label_2380

label label_2379:
    "Scene label_2379"
    jump end_2381

label label_2380:
    "Scene label_2380"
    jump end_2381

label label_2377:
    "Scene label_2377"
    if intelligence >= 19:
        jump label_2381

label label_2381:
    $ intelligence += 2
    jump end_2382

    jump label_2382

label label_2382:
    "Ветка false для label_2381"
    jump end_2383

label label_2378:
    "Scene label_2378"
    menu:
        "Go back":
            $ strength += 3
            jump label_2383
        "Talk":
            jump label_2384
        "Explore":
            $ charisma += 2
            jump label_2385
        "Go forward":
            jump label_2386

label label_2383:
    "Scene label_2383"
    jump end_2387

label label_2384:
    "Scene label_2384"
    jump end_2387

label label_2385:
    "Scene label_2385"
    jump end_2387

label label_2386:
    "Scene label_2386"
    jump end_2387

label label_2292:
    "Scene label_2292"
    if luck >= 14:
        jump label_2387

label label_2387:
    $ luck += 2
    if intelligence >= 13:
        jump label_2388

label label_2388:
    $ intelligence += 2
    menu:
        "Look around":
            jump label_2389
        "Pick up item":
            jump label_2390
        "Pick up item":
            jump label_2391
        "Talk":
            jump label_2392

label label_2389:
    "Scene label_2389"
    jump end_2393

label label_2390:
    "Scene label_2390"
    jump end_2393

label label_2391:
    "Scene label_2391"
    jump end_2393

label label_2392:
    "Scene label_2392"
    jump end_2393

    jump label_2393

label label_2393:
    "Ветка false для label_2388"
    if intelligence >= 7:
        jump label_2394

label label_2394:
    $ intelligence += 5
    jump end_2395

    jump label_2395

label label_2395:
    "Ветка false для label_2394"
    jump end_2396

    jump label_2396

label label_2396:
    "Ветка false для label_2387"
    menu:
        "Talk":
            $ intelligence += 2
            jump label_2397
        "Open door":
            $ luck += 3
            jump label_2398
        "Pick up item":
            jump label_2399
        "Pick up item":
            $ charisma += 1
            jump label_2400

label label_2397:
    "Scene label_2397"
    menu:
        "Use item":
            jump label_2401
        "Talk":
            jump label_2402
        "Explore":
            $ luck += 1
            jump label_2403
        "Pick up item":
            jump label_2404

label label_2401:
    "Scene label_2401"
    jump end_2405

label label_2402:
    "Scene label_2402"
    jump end_2405

label label_2403:
    "Scene label_2403"
    jump end_2405

label label_2404:
    "Scene label_2404"
    jump end_2405

label label_2398:
    "Scene label_2398"
    if charisma >= 17:
        jump label_2405

label label_2405:
    $ charisma += 2
    jump end_2406

    jump label_2406

label label_2406:
    "Ветка false для label_2405"
    jump end_2407

label label_2399:
    "Scene label_2399"
    menu:
        "Go forward":
            $ charisma += 1
            jump label_2407
        "Open door":
            jump label_2408
        "Talk":
            jump label_2409
        "Go forward":
            $ strength += 2
            jump label_2410

label label_2407:
    "Scene label_2407"
    jump end_2411

label label_2408:
    "Scene label_2408"
    jump end_2411

label label_2409:
    "Scene label_2409"
    jump end_2411

label label_2410:
    "Scene label_2410"
    jump end_2411

label label_2400:
    "Scene label_2400"
    menu:
        "Talk":
            $ luck += 2
            jump label_2411
        "Talk":
            $ charisma += 3
            jump label_2412

label label_2411:
    "Scene label_2411"
    jump end_2413

label label_2412:
    "Scene label_2412"
    jump end_2413

    jump label_2413

label label_2413:
    "Ветка false для label_1970"
    menu:
        "Go forward":
            jump label_2414
        "Pick up item":
            jump label_2415
        "Go back":
            $ intelligence += 3
            jump label_2416

label label_2414:
    "Scene label_2414"
    if intelligence >= 7:
        jump label_2417

label label_2417:
    $ intelligence += 3
    menu:
        "Pick up item":
            jump label_2418
        "Go forward":
            jump label_2419
        "Go back":
            $ luck += 3
            jump label_2420

label label_2418:
    "Scene label_2418"
    menu:
        "Talk":
            jump label_2421
        "Go forward":
            jump label_2422

label label_2421:
    "Scene label_2421"
    menu:
        "Use item":
            jump label_2423
        "Open door":
            jump label_2424
        "Go back":
            jump label_2425
        "Go back":
            jump label_2426

label label_2423:
    "Scene label_2423"
    if luck >= 7:
        jump label_2427

label label_2427:
    $ luck += 2
    jump end_2428

    jump label_2428

label label_2428:
    "Ветка false для label_2427"
    jump end_2429

label label_2424:
    "Scene label_2424"
    if charisma >= 19:
        jump label_2429

label label_2429:
    $ charisma += 2
    jump end_2430

    jump label_2430

label label_2430:
    "Ветка false для label_2429"
    jump end_2431

label label_2425:
    "Scene label_2425"
    menu:
        "Look around":
            $ intelligence += 1
            jump label_2431
        "Open door":
            $ charisma += 1
            jump label_2432
        "Talk":
            $ charisma += 2
            jump label_2433

label label_2431:
    "Scene label_2431"
    jump end_2434

label label_2432:
    "Scene label_2432"
    jump end_2434

label label_2433:
    "Scene label_2433"
    jump end_2434

label label_2426:
    "Scene label_2426"
    menu:
        "Look around":
            jump label_2434
        "Pick up item":
            $ charisma += 2
            jump label_2435

label label_2434:
    "Scene label_2434"
    jump end_2436

label label_2435:
    "Scene label_2435"
    jump end_2436

label label_2422:
    "Scene label_2422"
    menu:
        "Open door":
            jump label_2436
        "Talk":
            jump label_2437
        "Talk":
            $ intelligence += 2
            jump label_2438
        "Go forward":
            jump label_2439

label label_2436:
    "Scene label_2436"
    menu:
        "Go forward":
            $ intelligence += 3
            jump label_2440
        "Use item":
            $ luck += 1
            jump label_2441
        "Explore":
            jump label_2442
        "Open door":
            $ luck += 3
            jump label_2443

label label_2440:
    "Scene label_2440"
    jump end_2444

label label_2441:
    "Scene label_2441"
    jump end_2444

label label_2442:
    "Scene label_2442"
    jump end_2444

label label_2443:
    "Scene label_2443"
    jump end_2444

label label_2437:
    "Scene label_2437"
    menu:
        "Go forward":
            jump label_2444
        "Talk":
            $ intelligence += 3
            jump label_2445

label label_2444:
    "Scene label_2444"
    jump end_2446

label label_2445:
    "Scene label_2445"
    jump end_2446

label label_2438:
    "Scene label_2438"
    menu:
        "Go back":
            $ charisma += 2
            jump label_2446
        "Open door":
            $ luck += 3
            jump label_2447
        "Go back":
            $ intelligence += 3
            jump label_2448

label label_2446:
    "Scene label_2446"
    jump end_2449

label label_2447:
    "Scene label_2447"
    jump end_2449

label label_2448:
    "Scene label_2448"
    jump end_2449

label label_2439:
    "Scene label_2439"
    menu:
        "Go back":
            jump label_2449
        "Use item":
            jump label_2450
        "Use item":
            jump label_2451
        "Look around":
            $ intelligence += 2
            jump label_2452

label label_2449:
    "Scene label_2449"
    jump end_2453

label label_2450:
    "Scene label_2450"
    jump end_2453

label label_2451:
    "Scene label_2451"
    jump end_2453

label label_2452:
    "Scene label_2452"
    jump end_2453

label label_2419:
    "Scene label_2419"
    if luck >= 10:
        jump label_2453

label label_2453:
    $ luck += 4
    menu:
        "Talk":
            jump label_2454
        "Explore":
            $ intelligence += 2
            jump label_2455
        "Use item":
            jump label_2456

label label_2454:
    "Scene label_2454"
    if luck >= 8:
        jump label_2457

label label_2457:
    $ luck += 3
    jump end_2458

    jump label_2458

label label_2458:
    "Ветка false для label_2457"
    jump end_2459

label label_2455:
    "Scene label_2455"
    menu:
        "Look around":
            jump label_2459
        "Open door":
            $ strength += 3
            jump label_2460
        "Pick up item":
            jump label_2461
        "Open door":
            jump label_2462

label label_2459:
    "Scene label_2459"
    jump end_2463

label label_2460:
    "Scene label_2460"
    jump end_2463

label label_2461:
    "Scene label_2461"
    jump end_2463

label label_2462:
    "Scene label_2462"
    jump end_2463

label label_2456:
    "Scene label_2456"
    menu:
        "Explore":
            jump label_2463
        "Go back":
            jump label_2464

label label_2463:
    "Scene label_2463"
    jump end_2465

label label_2464:
    "Scene label_2464"
    jump end_2465

    jump label_2465

label label_2465:
    "Ветка false для label_2453"
    if intelligence >= 14:
        jump label_2466

label label_2466:
    $ intelligence += 2
    menu:
        "Look around":
            jump label_2467
        "Look around":
            jump label_2468
        "Pick up item":
            $ intelligence += 3
            jump label_2469
        "Explore":
            jump label_2470

label label_2467:
    "Scene label_2467"
    jump end_2471

label label_2468:
    "Scene label_2468"
    jump end_2471

label label_2469:
    "Scene label_2469"
    jump end_2471

label label_2470:
    "Scene label_2470"
    jump end_2471

    jump label_2471

label label_2471:
    "Ветка false для label_2466"
    if strength >= 7:
        jump label_2472

label label_2472:
    $ strength += 4
    jump end_2473

    jump label_2473

label label_2473:
    "Ветка false для label_2472"
    jump end_2474

label label_2420:
    "Scene label_2420"
    if luck >= 7:
        jump label_2474

label label_2474:
    $ luck += 4
    if strength >= 15:
        jump label_2475

label label_2475:
    $ strength += 4
    if intelligence >= 10:
        jump label_2476

label label_2476:
    $ intelligence += 4
    jump end_2477

    jump label_2477

label label_2477:
    "Ветка false для label_2476"
    jump end_2478

    jump label_2478

label label_2478:
    "Ветка false для label_2475"
    menu:
        "Open door":
            $ strength += 1
            jump label_2479
        "Open door":
            $ luck += 1
            jump label_2480

label label_2479:
    "Scene label_2479"
    jump end_2481

label label_2480:
    "Scene label_2480"
    jump end_2481

    jump label_2481

label label_2481:
    "Ветка false для label_2474"
    if luck >= 9:
        jump label_2482

label label_2482:
    $ luck += 2
    if strength >= 6:
        jump label_2483

label label_2483:
    $ strength += 4
    jump end_2484

    jump label_2484

label label_2484:
    "Ветка false для label_2483"
    jump end_2485

    jump label_2485

label label_2485:
    "Ветка false для label_2482"
    if charisma >= 8:
        jump label_2486

label label_2486:
    $ charisma += 5
    jump end_2487

    jump label_2487

label label_2487:
    "Ветка false для label_2486"
    jump end_2488

    jump label_2488

label label_2488:
    "Ветка false для label_2417"
    menu:
        "Talk":
            jump label_2489
        "Go forward":
            $ intelligence += 1
            jump label_2490
        "Explore":
            $ intelligence += 2
            jump label_2491
        "Open door":
            $ luck += 3
            jump label_2492

label label_2489:
    "Scene label_2489"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_2493
        "Pick up item":
            jump label_2494
        "Explore":
            jump label_2495

label label_2493:
    "Scene label_2493"
    menu:
        "Explore":
            jump label_2496
        "Open door":
            jump label_2497
        "Explore":
            jump label_2498

label label_2496:
    "Scene label_2496"
    menu:
        "Talk":
            jump label_2499
        "Go back":
            jump label_2500
        "Look around":
            jump label_2501

label label_2499:
    "Scene label_2499"
    jump end_2502

label label_2500:
    "Scene label_2500"
    jump end_2502

label label_2501:
    "Scene label_2501"
    jump end_2502

label label_2497:
    "Scene label_2497"
    menu:
        "Explore":
            $ strength += 1
            jump label_2502
        "Go forward":
            $ luck += 2
            jump label_2503
        "Use item":
            jump label_2504

label label_2502:
    "Scene label_2502"
    jump end_2505

label label_2503:
    "Scene label_2503"
    jump end_2505

label label_2504:
    "Scene label_2504"
    jump end_2505

label label_2498:
    "Scene label_2498"
    menu:
        "Use item":
            $ strength += 2
            jump label_2505
        "Explore":
            $ strength += 2
            jump label_2506

label label_2505:
    "Scene label_2505"
    jump end_2507

label label_2506:
    "Scene label_2506"
    jump end_2507

label label_2494:
    "Scene label_2494"
    menu:
        "Use item":
            jump label_2507
        "Open door":
            jump label_2508

label label_2507:
    "Scene label_2507"
    if strength >= 14:
        jump label_2509

label label_2509:
    $ strength += 4
    jump end_2510

    jump label_2510

label label_2510:
    "Ветка false для label_2509"
    jump end_2511

label label_2508:
    "Scene label_2508"
    if charisma >= 17:
        jump label_2511

label label_2511:
    $ charisma += 5
    jump end_2512

    jump label_2512

label label_2512:
    "Ветка false для label_2511"
    jump end_2513

label label_2495:
    "Scene label_2495"
    if intelligence >= 18:
        jump label_2513

label label_2513:
    $ intelligence += 5
    menu:
        "Go back":
            jump label_2514
        "Talk":
            jump label_2515
        "Talk":
            $ intelligence += 2
            jump label_2516

label label_2514:
    "Scene label_2514"
    jump end_2517

label label_2515:
    "Scene label_2515"
    jump end_2517

label label_2516:
    "Scene label_2516"
    jump end_2517

    jump label_2517

label label_2517:
    "Ветка false для label_2513"
    if strength >= 11:
        jump label_2518

label label_2518:
    $ strength += 3
    jump end_2519

    jump label_2519

label label_2519:
    "Ветка false для label_2518"
    jump end_2520

label label_2490:
    "Scene label_2490"
    menu:
        "Talk":
            $ strength += 1
            jump label_2520
        "Use item":
            jump label_2521

label label_2520:
    "Scene label_2520"
    menu:
        "Go forward":
            jump label_2522
        "Look around":
            $ strength += 1
            jump label_2523
        "Use item":
            $ charisma += 1
            jump label_2524
        "Use item":
            jump label_2525

label label_2522:
    "Scene label_2522"
    menu:
        "Talk":
            jump label_2526
        "Open door":
            jump label_2527

label label_2526:
    "Scene label_2526"
    jump end_2528

label label_2527:
    "Scene label_2527"
    jump end_2528

label label_2523:
    "Scene label_2523"
    if charisma >= 10:
        jump label_2528

label label_2528:
    $ charisma += 3
    jump end_2529

    jump label_2529

label label_2529:
    "Ветка false для label_2528"
    jump end_2530

label label_2524:
    "Scene label_2524"
    menu:
        "Pick up item":
            $ luck += 3
            jump label_2530
        "Go back":
            $ charisma += 1
            jump label_2531
        "Go forward":
            $ strength += 3
            jump label_2532

label label_2530:
    "Scene label_2530"
    jump end_2533

label label_2531:
    "Scene label_2531"
    jump end_2533

label label_2532:
    "Scene label_2532"
    jump end_2533

label label_2525:
    "Scene label_2525"
    menu:
        "Pick up item":
            $ intelligence += 3
            jump label_2533
        "Look around":
            $ intelligence += 3
            jump label_2534
        "Pick up item":
            jump label_2535
        "Pick up item":
            $ charisma += 3
            jump label_2536

label label_2533:
    "Scene label_2533"
    jump end_2537

label label_2534:
    "Scene label_2534"
    jump end_2537

label label_2535:
    "Scene label_2535"
    jump end_2537

label label_2536:
    "Scene label_2536"
    jump end_2537

label label_2521:
    "Scene label_2521"
    if charisma >= 11:
        jump label_2537

label label_2537:
    $ charisma += 3
    menu:
        "Explore":
            $ intelligence += 3
            jump label_2538
        "Use item":
            jump label_2539

label label_2538:
    "Scene label_2538"
    jump end_2540

label label_2539:
    "Scene label_2539"
    jump end_2540

    jump label_2540

label label_2540:
    "Ветка false для label_2537"
    menu:
        "Open door":
            jump label_2541
        "Look around":
            jump label_2542

label label_2541:
    "Scene label_2541"
    jump end_2543

label label_2542:
    "Scene label_2542"
    jump end_2543

label label_2491:
    "Scene label_2491"
    if intelligence >= 12:
        jump label_2543

label label_2543:
    $ intelligence += 3
    menu:
        "Use item":
            jump label_2544
        "Use item":
            $ luck += 2
            jump label_2545
        "Open door":
            $ charisma += 3
            jump label_2546

label label_2544:
    "Scene label_2544"
    menu:
        "Use item":
            $ charisma += 2
            jump label_2547
        "Use item":
            jump label_2548
        "Explore":
            $ luck += 3
            jump label_2549

label label_2547:
    "Scene label_2547"
    jump end_2550

label label_2548:
    "Scene label_2548"
    jump end_2550

label label_2549:
    "Scene label_2549"
    jump end_2550

label label_2545:
    "Scene label_2545"
    menu:
        "Look around":
            $ charisma += 3
            jump label_2550
        "Pick up item":
            $ intelligence += 2
            jump label_2551
        "Look around":
            $ luck += 1
            jump label_2552

label label_2550:
    "Scene label_2550"
    jump end_2553

label label_2551:
    "Scene label_2551"
    jump end_2553

label label_2552:
    "Scene label_2552"
    jump end_2553

label label_2546:
    "Scene label_2546"
    menu:
        "Pick up item":
            jump label_2553
        "Pick up item":
            jump label_2554
        "Use item":
            $ luck += 1
            jump label_2555
        "Use item":
            $ strength += 3
            jump label_2556

label label_2553:
    "Scene label_2553"
    jump end_2557

label label_2554:
    "Scene label_2554"
    jump end_2557

label label_2555:
    "Scene label_2555"
    jump end_2557

label label_2556:
    "Scene label_2556"
    jump end_2557

    jump label_2557

label label_2557:
    "Ветка false для label_2543"
    menu:
        "Talk":
            jump label_2558
        "Open door":
            jump label_2559

label label_2558:
    "Scene label_2558"
    menu:
        "Use item":
            $ strength += 2
            jump label_2560
        "Pick up item":
            jump label_2561

label label_2560:
    "Scene label_2560"
    jump end_2562

label label_2561:
    "Scene label_2561"
    jump end_2562

label label_2559:
    "Scene label_2559"
    menu:
        "Pick up item":
            $ intelligence += 3
            jump label_2562
        "Explore":
            jump label_2563
        "Explore":
            $ charisma += 1
            jump label_2564

label label_2562:
    "Scene label_2562"
    jump end_2565

label label_2563:
    "Scene label_2563"
    jump end_2565

label label_2564:
    "Scene label_2564"
    jump end_2565

label label_2492:
    "Scene label_2492"
    menu:
        "Use item":
            $ luck += 1
            jump label_2565
        "Open door":
            jump label_2566

label label_2565:
    "Scene label_2565"
    menu:
        "Explore":
            $ strength += 2
            jump label_2567
        "Talk":
            jump label_2568
        "Look around":
            $ intelligence += 3
            jump label_2569
        "Talk":
            jump label_2570

label label_2567:
    "Scene label_2567"
    menu:
        "Explore":
            jump label_2571
        "Look around":
            $ charisma += 2
            jump label_2572
        "Use item":
            $ intelligence += 1
            jump label_2573
        "Open door":
            jump label_2574

label label_2571:
    "Scene label_2571"
    jump end_2575

label label_2572:
    "Scene label_2572"
    jump end_2575

label label_2573:
    "Scene label_2573"
    jump end_2575

label label_2574:
    "Scene label_2574"
    jump end_2575

label label_2568:
    "Scene label_2568"
    if charisma >= 7:
        jump label_2575

label label_2575:
    $ charisma += 2
    jump end_2576

    jump label_2576

label label_2576:
    "Ветка false для label_2575"
    jump end_2577

label label_2569:
    "Scene label_2569"
    if strength >= 9:
        jump label_2577

label label_2577:
    $ strength += 3
    jump end_2578

    jump label_2578

label label_2578:
    "Ветка false для label_2577"
    jump end_2579

label label_2570:
    "Scene label_2570"
    if intelligence >= 8:
        jump label_2579

label label_2579:
    $ intelligence += 5
    jump end_2580

    jump label_2580

label label_2580:
    "Ветка false для label_2579"
    jump end_2581

label label_2566:
    "Scene label_2566"
    menu:
        "Talk":
            $ strength += 1
            jump label_2581
        "Look around":
            $ strength += 1
            jump label_2582
        "Talk":
            $ strength += 2
            jump label_2583
        "Talk":
            jump label_2584

label label_2581:
    "Scene label_2581"
    menu:
        "Pick up item":
            jump label_2585
        "Use item":
            jump label_2586
        "Use item":
            $ intelligence += 2
            jump label_2587
        "Open door":
            $ strength += 3
            jump label_2588

label label_2585:
    "Scene label_2585"
    jump end_2589

label label_2586:
    "Scene label_2586"
    jump end_2589

label label_2587:
    "Scene label_2587"
    jump end_2589

label label_2588:
    "Scene label_2588"
    jump end_2589

label label_2582:
    "Scene label_2582"
    if luck >= 8:
        jump label_2589

label label_2589:
    $ luck += 3
    jump end_2590

    jump label_2590

label label_2590:
    "Ветка false для label_2589"
    jump end_2591

label label_2583:
    "Scene label_2583"
    menu:
        "Talk":
            $ luck += 1
            jump label_2591
        "Open door":
            jump label_2592
        "Talk":
            jump label_2593

label label_2591:
    "Scene label_2591"
    jump end_2594

label label_2592:
    "Scene label_2592"
    jump end_2594

label label_2593:
    "Scene label_2593"
    jump end_2594

label label_2584:
    "Scene label_2584"
    menu:
        "Explore":
            jump label_2594
        "Talk":
            jump label_2595
        "Open door":
            $ intelligence += 3
            jump label_2596
        "Explore":
            jump label_2597

label label_2594:
    "Scene label_2594"
    jump end_2598

label label_2595:
    "Scene label_2595"
    jump end_2598

label label_2596:
    "Scene label_2596"
    jump end_2598

label label_2597:
    "Scene label_2597"
    jump end_2598

label label_2415:
    "Scene label_2415"
    menu:
        "Look around":
            jump label_2598
        "Go forward":
            jump label_2599
        "Use item":
            jump label_2600

label label_2598:
    "Scene label_2598"
    menu:
        "Talk":
            jump label_2601
        "Pick up item":
            jump label_2602
        "Look around":
            $ charisma += 1
            jump label_2603

label label_2601:
    "Scene label_2601"
    if intelligence >= 18:
        jump label_2604

label label_2604:
    $ intelligence += 4
    menu:
        "Explore":
            $ intelligence += 1
            jump label_2605
        "Go forward":
            $ strength += 3
            jump label_2606
        "Talk":
            $ charisma += 1
            jump label_2607
        "Open door":
            $ intelligence += 2
            jump label_2608

label label_2605:
    "Scene label_2605"
    if charisma >= 13:
        jump label_2609

label label_2609:
    $ charisma += 2
    jump end_2610

    jump label_2610

label label_2610:
    "Ветка false для label_2609"
    jump end_2611

label label_2606:
    "Scene label_2606"
    if strength >= 19:
        jump label_2611

label label_2611:
    $ strength += 2
    jump end_2612

    jump label_2612

label label_2612:
    "Ветка false для label_2611"
    jump end_2613

label label_2607:
    "Scene label_2607"
    menu:
        "Go forward":
            $ intelligence += 1
            jump label_2613
        "Go back":
            jump label_2614
        "Look around":
            $ luck += 1
            jump label_2615
        "Go forward":
            $ luck += 1
            jump label_2616

label label_2613:
    "Scene label_2613"
    jump end_2617

label label_2614:
    "Scene label_2614"
    jump end_2617

label label_2615:
    "Scene label_2615"
    jump end_2617

label label_2616:
    "Scene label_2616"
    jump end_2617

label label_2608:
    "Scene label_2608"
    if strength >= 5:
        jump label_2617

label label_2617:
    $ strength += 4
    jump end_2618

    jump label_2618

label label_2618:
    "Ветка false для label_2617"
    jump end_2619

    jump label_2619

label label_2619:
    "Ветка false для label_2604"
    menu:
        "Pick up item":
            jump label_2620
        "Pick up item":
            $ luck += 3
            jump label_2621
        "Look around":
            $ luck += 2
            jump label_2622

label label_2620:
    "Scene label_2620"
    if intelligence >= 12:
        jump label_2623

label label_2623:
    $ intelligence += 4
    jump end_2624

    jump label_2624

label label_2624:
    "Ветка false для label_2623"
    jump end_2625

label label_2621:
    "Scene label_2621"
    menu:
        "Talk":
            jump label_2625
        "Go back":
            $ strength += 1
            jump label_2626

label label_2625:
    "Scene label_2625"
    jump end_2627

label label_2626:
    "Scene label_2626"
    jump end_2627

label label_2622:
    "Scene label_2622"
    if strength >= 8:
        jump label_2627

label label_2627:
    $ strength += 2
    jump end_2628

    jump label_2628

label label_2628:
    "Ветка false для label_2627"
    jump end_2629

label label_2602:
    "Scene label_2602"
    if strength >= 18:
        jump label_2629

label label_2629:
    $ strength += 3
    if charisma >= 13:
        jump label_2630

label label_2630:
    $ charisma += 2
    menu:
        "Go forward":
            jump label_2631
        "Look around":
            jump label_2632
        "Explore":
            $ intelligence += 3
            jump label_2633

label label_2631:
    "Scene label_2631"
    jump end_2634

label label_2632:
    "Scene label_2632"
    jump end_2634

label label_2633:
    "Scene label_2633"
    jump end_2634

    jump label_2634

label label_2634:
    "Ветка false для label_2630"
    if strength >= 15:
        jump label_2635

label label_2635:
    $ strength += 2
    jump end_2636

    jump label_2636

label label_2636:
    "Ветка false для label_2635"
    jump end_2637

    jump label_2637

label label_2637:
    "Ветка false для label_2629"
    menu:
        "Go forward":
            $ strength += 1
            jump label_2638
        "Go forward":
            $ intelligence += 2
            jump label_2639

label label_2638:
    "Scene label_2638"
    if strength >= 14:
        jump label_2640

label label_2640:
    $ strength += 4
    jump end_2641

    jump label_2641

label label_2641:
    "Ветка false для label_2640"
    jump end_2642

label label_2639:
    "Scene label_2639"
    menu:
        "Pick up item":
            $ charisma += 1
            jump label_2642
        "Look around":
            jump label_2643
        "Go forward":
            $ charisma += 1
            jump label_2644

label label_2642:
    "Scene label_2642"
    jump end_2645

label label_2643:
    "Scene label_2643"
    jump end_2645

label label_2644:
    "Scene label_2644"
    jump end_2645

label label_2603:
    "Scene label_2603"
    menu:
        "Explore":
            $ charisma += 3
            jump label_2645
        "Go back":
            $ intelligence += 1
            jump label_2646
        "Go forward":
            $ intelligence += 3
            jump label_2647
        "Open door":
            $ charisma += 2
            jump label_2648

label label_2645:
    "Scene label_2645"
    menu:
        "Open door":
            jump label_2649
        "Look around":
            $ strength += 3
            jump label_2650
        "Use item":
            jump label_2651

label label_2649:
    "Scene label_2649"
    menu:
        "Go forward":
            $ luck += 2
            jump label_2652
        "Open door":
            $ luck += 2
            jump label_2653
        "Go forward":
            jump label_2654

label label_2652:
    "Scene label_2652"
    jump end_2655

label label_2653:
    "Scene label_2653"
    jump end_2655

label label_2654:
    "Scene label_2654"
    jump end_2655

label label_2650:
    "Scene label_2650"
    menu:
        "Pick up item":
            jump label_2655
        "Pick up item":
            $ luck += 1
            jump label_2656

label label_2655:
    "Scene label_2655"
    jump end_2657

label label_2656:
    "Scene label_2656"
    jump end_2657

label label_2651:
    "Scene label_2651"
    if luck >= 12:
        jump label_2657

label label_2657:
    $ luck += 2
    jump end_2658

    jump label_2658

label label_2658:
    "Ветка false для label_2657"
    jump end_2659

label label_2646:
    "Scene label_2646"
    menu:
        "Go back":
            jump label_2659
        "Explore":
            $ strength += 2
            jump label_2660
        "Talk":
            $ strength += 3
            jump label_2661
        "Go back":
            jump label_2662

label label_2659:
    "Scene label_2659"
    menu:
        "Open door":
            jump label_2663
        "Pick up item":
            jump label_2664
        "Look around":
            $ charisma += 3
            jump label_2665

label label_2663:
    "Scene label_2663"
    jump end_2666

label label_2664:
    "Scene label_2664"
    jump end_2666

label label_2665:
    "Scene label_2665"
    jump end_2666

label label_2660:
    "Scene label_2660"
    if charisma >= 17:
        jump label_2666

label label_2666:
    $ charisma += 4
    jump end_2667

    jump label_2667

label label_2667:
    "Ветка false для label_2666"
    jump end_2668

label label_2661:
    "Scene label_2661"
    if charisma >= 8:
        jump label_2668

label label_2668:
    $ charisma += 3
    jump end_2669

    jump label_2669

label label_2669:
    "Ветка false для label_2668"
    jump end_2670

label label_2662:
    "Scene label_2662"
    if luck >= 6:
        jump label_2670

label label_2670:
    $ luck += 5
    jump end_2671

    jump label_2671

label label_2671:
    "Ветка false для label_2670"
    jump end_2672

label label_2647:
    "Scene label_2647"
    menu:
        "Use item":
            $ intelligence += 2
            jump label_2672
        "Open door":
            $ luck += 3
            jump label_2673
        "Look around":
            jump label_2674

label label_2672:
    "Scene label_2672"
    menu:
        "Look around":
            jump label_2675
        "Go back":
            $ charisma += 3
            jump label_2676

label label_2675:
    "Scene label_2675"
    jump end_2677

label label_2676:
    "Scene label_2676"
    jump end_2677

label label_2673:
    "Scene label_2673"
    if intelligence >= 19:
        jump label_2677

label label_2677:
    $ intelligence += 2
    jump end_2678

    jump label_2678

label label_2678:
    "Ветка false для label_2677"
    jump end_2679

label label_2674:
    "Scene label_2674"
    menu:
        "Talk":
            $ charisma += 1
            jump label_2679
        "Talk":
            jump label_2680
        "Go forward":
            jump label_2681
        "Go back":
            $ strength += 1
            jump label_2682

label label_2679:
    "Scene label_2679"
    jump end_2683

label label_2680:
    "Scene label_2680"
    jump end_2683

label label_2681:
    "Scene label_2681"
    jump end_2683

label label_2682:
    "Scene label_2682"
    jump end_2683

label label_2648:
    "Scene label_2648"
    menu:
        "Pick up item":
            jump label_2683
        "Look around":
            $ charisma += 1
            jump label_2684
        "Go back":
            jump label_2685
        "Go forward":
            jump label_2686

label label_2683:
    "Scene label_2683"
    menu:
        "Open door":
            jump label_2687
        "Go back":
            jump label_2688
        "Talk":
            jump label_2689
        "Pick up item":
            jump label_2690

label label_2687:
    "Scene label_2687"
    jump end_2691

label label_2688:
    "Scene label_2688"
    jump end_2691

label label_2689:
    "Scene label_2689"
    jump end_2691

label label_2690:
    "Scene label_2690"
    jump end_2691

label label_2684:
    "Scene label_2684"
    menu:
        "Use item":
            jump label_2691
        "Pick up item":
            jump label_2692
        "Explore":
            $ strength += 3
            jump label_2693
        "Talk":
            $ strength += 2
            jump label_2694

label label_2691:
    "Scene label_2691"
    jump end_2695

label label_2692:
    "Scene label_2692"
    jump end_2695

label label_2693:
    "Scene label_2693"
    jump end_2695

label label_2694:
    "Scene label_2694"
    jump end_2695

label label_2685:
    "Scene label_2685"
    menu:
        "Pick up item":
            $ strength += 1
            jump label_2695
        "Use item":
            $ strength += 2
            jump label_2696
        "Open door":
            $ strength += 1
            jump label_2697

label label_2695:
    "Scene label_2695"
    jump end_2698

label label_2696:
    "Scene label_2696"
    jump end_2698

label label_2697:
    "Scene label_2697"
    jump end_2698

label label_2686:
    "Scene label_2686"
    menu:
        "Go back":
            jump label_2698
        "Open door":
            jump label_2699
        "Talk":
            $ charisma += 3
            jump label_2700

label label_2698:
    "Scene label_2698"
    jump end_2701

label label_2699:
    "Scene label_2699"
    jump end_2701

label label_2700:
    "Scene label_2700"
    jump end_2701

label label_2599:
    "Scene label_2599"
    menu:
        "Pick up item":
            jump label_2701
        "Go forward":
            $ luck += 1
            jump label_2702
        "Look around":
            $ strength += 3
            jump label_2703
        "Open door":
            $ charisma += 1
            jump label_2704

label label_2701:
    "Scene label_2701"
    menu:
        "Use item":
            $ luck += 3
            jump label_2705
        "Use item":
            $ charisma += 2
            jump label_2706
        "Look around":
            jump label_2707
        "Pick up item":
            jump label_2708

label label_2705:
    "Scene label_2705"
    menu:
        "Open door":
            $ strength += 3
            jump label_2709
        "Open door":
            jump label_2710
        "Go back":
            jump label_2711
        "Open door":
            $ intelligence += 3
            jump label_2712

label label_2709:
    "Scene label_2709"
    if charisma >= 5:
        jump label_2713

label label_2713:
    $ charisma += 4
    jump end_2714

    jump label_2714

label label_2714:
    "Ветка false для label_2713"
    jump end_2715

label label_2710:
    "Scene label_2710"
    menu:
        "Talk":
            $ strength += 1
            jump label_2715
        "Explore":
            $ intelligence += 1
            jump label_2716
        "Explore":
            jump label_2717

label label_2715:
    "Scene label_2715"
    jump end_2718

label label_2716:
    "Scene label_2716"
    jump end_2718

label label_2717:
    "Scene label_2717"
    jump end_2718

label label_2711:
    "Scene label_2711"
    if charisma >= 13:
        jump label_2718

label label_2718:
    $ charisma += 3
    jump end_2719

    jump label_2719

label label_2719:
    "Ветка false для label_2718"
    jump end_2720

label label_2712:
    "Scene label_2712"
    if intelligence >= 13:
        jump label_2720

label label_2720:
    $ intelligence += 5
    jump end_2721

    jump label_2721

label label_2721:
    "Ветка false для label_2720"
    jump end_2722

label label_2706:
    "Scene label_2706"
    menu:
        "Use item":
            jump label_2722
        "Open door":
            $ luck += 2
            jump label_2723
        "Pick up item":
            $ charisma += 3
            jump label_2724
        "Look around":
            $ strength += 1
            jump label_2725

label label_2722:
    "Scene label_2722"
    if intelligence >= 8:
        jump label_2726

label label_2726:
    $ intelligence += 3
    jump end_2727

    jump label_2727

label label_2727:
    "Ветка false для label_2726"
    jump end_2728

label label_2723:
    "Scene label_2723"
    menu:
        "Talk":
            jump label_2728
        "Use item":
            jump label_2729
        "Look around":
            $ charisma += 3
            jump label_2730
        "Open door":
            jump label_2731

label label_2728:
    "Scene label_2728"
    jump end_2732

label label_2729:
    "Scene label_2729"
    jump end_2732

label label_2730:
    "Scene label_2730"
    jump end_2732

label label_2731:
    "Scene label_2731"
    jump end_2732

label label_2724:
    "Scene label_2724"
    menu:
        "Go forward":
            jump label_2732
        "Explore":
            jump label_2733

label label_2732:
    "Scene label_2732"
    jump end_2734

label label_2733:
    "Scene label_2733"
    jump end_2734

label label_2725:
    "Scene label_2725"
    if luck >= 5:
        jump label_2734

label label_2734:
    $ luck += 3
    jump end_2735

    jump label_2735

label label_2735:
    "Ветка false для label_2734"
    jump end_2736

label label_2707:
    "Scene label_2707"
    menu:
        "Go back":
            $ luck += 1
            jump label_2736
        "Look around":
            $ strength += 1
            jump label_2737
        "Go back":
            $ charisma += 2
            jump label_2738

label label_2736:
    "Scene label_2736"
    menu:
        "Pick up item":
            jump label_2739
        "Look around":
            jump label_2740
        "Talk":
            jump label_2741

label label_2739:
    "Scene label_2739"
    jump end_2742

label label_2740:
    "Scene label_2740"
    jump end_2742

label label_2741:
    "Scene label_2741"
    jump end_2742

label label_2737:
    "Scene label_2737"
    menu:
        "Go forward":
            jump label_2742
        "Go forward":
            jump label_2743
        "Pick up item":
            jump label_2744
        "Talk":
            $ strength += 2
            jump label_2745

label label_2742:
    "Scene label_2742"
    jump end_2746

label label_2743:
    "Scene label_2743"
    jump end_2746

label label_2744:
    "Scene label_2744"
    jump end_2746

label label_2745:
    "Scene label_2745"
    jump end_2746

label label_2738:
    "Scene label_2738"
    if strength >= 12:
        jump label_2746

label label_2746:
    $ strength += 4
    jump end_2747

    jump label_2747

label label_2747:
    "Ветка false для label_2746"
    jump end_2748

label label_2708:
    "Scene label_2708"
    menu:
        "Open door":
            jump label_2748
        "Open door":
            jump label_2749
        "Use item":
            jump label_2750

label label_2748:
    "Scene label_2748"
    menu:
        "Pick up item":
            $ charisma += 3
            jump label_2751
        "Go back":
            jump label_2752
        "Look around":
            $ luck += 2
            jump label_2753
        "Go forward":
            $ intelligence += 3
            jump label_2754

label label_2751:
    "Scene label_2751"
    jump end_2755

label label_2752:
    "Scene label_2752"
    jump end_2755

label label_2753:
    "Scene label_2753"
    jump end_2755

label label_2754:
    "Scene label_2754"
    jump end_2755

label label_2749:
    "Scene label_2749"
    menu:
        "Go forward":
            jump label_2755
        "Pick up item":
            jump label_2756

label label_2755:
    "Scene label_2755"
    jump end_2757

label label_2756:
    "Scene label_2756"
    jump end_2757

label label_2750:
    "Scene label_2750"
    if charisma >= 6:
        jump label_2757

label label_2757:
    $ charisma += 4
    jump end_2758

    jump label_2758

label label_2758:
    "Ветка false для label_2757"
    jump end_2759

label label_2702:
    "Scene label_2702"
    if charisma >= 7:
        jump label_2759

label label_2759:
    $ charisma += 5
    menu:
        "Use item":
            jump label_2760
        "Open door":
            $ luck += 1
            jump label_2761

label label_2760:
    "Scene label_2760"
    menu:
        "Talk":
            $ luck += 2
            jump label_2762
        "Explore":
            jump label_2763
        "Open door":
            $ strength += 1
            jump label_2764
        "Go back":
            jump label_2765

label label_2762:
    "Scene label_2762"
    jump end_2766

label label_2763:
    "Scene label_2763"
    jump end_2766

label label_2764:
    "Scene label_2764"
    jump end_2766

label label_2765:
    "Scene label_2765"
    jump end_2766

label label_2761:
    "Scene label_2761"
    if luck >= 10:
        jump label_2766

label label_2766:
    $ luck += 2
    jump end_2767

    jump label_2767

label label_2767:
    "Ветка false для label_2766"
    jump end_2768

    jump label_2768

label label_2768:
    "Ветка false для label_2759"
    if charisma >= 17:
        jump label_2769

label label_2769:
    $ charisma += 4
    menu:
        "Open door":
            $ charisma += 1
            jump label_2770
        "Explore":
            jump label_2771
        "Go back":
            $ luck += 2
            jump label_2772
        "Open door":
            jump label_2773

label label_2770:
    "Scene label_2770"
    jump end_2774

label label_2771:
    "Scene label_2771"
    jump end_2774

label label_2772:
    "Scene label_2772"
    jump end_2774

label label_2773:
    "Scene label_2773"
    jump end_2774

    jump label_2774

label label_2774:
    "Ветка false для label_2769"
    menu:
        "Explore":
            jump label_2775
        "Go forward":
            jump label_2776
        "Go back":
            jump label_2777

label label_2775:
    "Scene label_2775"
    jump end_2778

label label_2776:
    "Scene label_2776"
    jump end_2778

label label_2777:
    "Scene label_2777"
    jump end_2778

label label_2703:
    "Scene label_2703"
    menu:
        "Go forward":
            $ intelligence += 2
            jump label_2778
        "Go back":
            jump label_2779

label label_2778:
    "Scene label_2778"
    menu:
        "Talk":
            jump label_2780
        "Explore":
            jump label_2781

label label_2780:
    "Scene label_2780"
    if charisma >= 15:
        jump label_2782

label label_2782:
    $ charisma += 4
    jump end_2783

    jump label_2783

label label_2783:
    "Ветка false для label_2782"
    jump end_2784

label label_2781:
    "Scene label_2781"
    if strength >= 5:
        jump label_2784

label label_2784:
    $ strength += 5
    jump end_2785

    jump label_2785

label label_2785:
    "Ветка false для label_2784"
    jump end_2786

label label_2779:
    "Scene label_2779"
    if intelligence >= 8:
        jump label_2786

label label_2786:
    $ intelligence += 3
    if intelligence >= 19:
        jump label_2787

label label_2787:
    $ intelligence += 5
    jump end_2788

    jump label_2788

label label_2788:
    "Ветка false для label_2787"
    jump end_2789

    jump label_2789

label label_2789:
    "Ветка false для label_2786"
    menu:
        "Pick up item":
            $ intelligence += 2
            jump label_2790
        "Look around":
            $ strength += 1
            jump label_2791
        "Talk":
            $ strength += 1
            jump label_2792

label label_2790:
    "Scene label_2790"
    jump end_2793

label label_2791:
    "Scene label_2791"
    jump end_2793

label label_2792:
    "Scene label_2792"
    jump end_2793

label label_2704:
    "Scene label_2704"
    menu:
        "Go back":
            jump label_2793
        "Open door":
            jump label_2794
        "Go forward":
            jump label_2795
        "Go forward":
            $ charisma += 2
            jump label_2796

label label_2793:
    "Scene label_2793"
    menu:
        "Talk":
            $ strength += 1
            jump label_2797
        "Explore":
            $ strength += 2
            jump label_2798
        "Pick up item":
            $ charisma += 2
            jump label_2799
        "Talk":
            jump label_2800

label label_2797:
    "Scene label_2797"
    menu:
        "Look around":
            jump label_2801
        "Go forward":
            $ luck += 1
            jump label_2802

label label_2801:
    "Scene label_2801"
    jump end_2803

label label_2802:
    "Scene label_2802"
    jump end_2803

label label_2798:
    "Scene label_2798"
    menu:
        "Explore":
            $ luck += 3
            jump label_2803
        "Open door":
            jump label_2804
        "Go forward":
            $ luck += 3
            jump label_2805

label label_2803:
    "Scene label_2803"
    jump end_2806

label label_2804:
    "Scene label_2804"
    jump end_2806

label label_2805:
    "Scene label_2805"
    jump end_2806

label label_2799:
    "Scene label_2799"
    if luck >= 10:
        jump label_2806

label label_2806:
    $ luck += 4
    jump end_2807

    jump label_2807

label label_2807:
    "Ветка false для label_2806"
    jump end_2808

label label_2800:
    "Scene label_2800"
    if intelligence >= 15:
        jump label_2808

label label_2808:
    $ intelligence += 4
    jump end_2809

    jump label_2809

label label_2809:
    "Ветка false для label_2808"
    jump end_2810

label label_2794:
    "Scene label_2794"
    menu:
        "Go forward":
            $ charisma += 2
            jump label_2810
        "Go back":
            jump label_2811
        "Go back":
            jump label_2812

label label_2810:
    "Scene label_2810"
    menu:
        "Use item":
            jump label_2813
        "Look around":
            $ intelligence += 1
            jump label_2814

label label_2813:
    "Scene label_2813"
    jump end_2815

label label_2814:
    "Scene label_2814"
    jump end_2815

label label_2811:
    "Scene label_2811"
    menu:
        "Go back":
            jump label_2815
        "Pick up item":
            jump label_2816
        "Look around":
            $ charisma += 1
            jump label_2817

label label_2815:
    "Scene label_2815"
    jump end_2818

label label_2816:
    "Scene label_2816"
    jump end_2818

label label_2817:
    "Scene label_2817"
    jump end_2818

label label_2812:
    "Scene label_2812"
    if luck >= 10:
        jump label_2818

label label_2818:
    $ luck += 5
    jump end_2819

    jump label_2819

label label_2819:
    "Ветка false для label_2818"
    jump end_2820

label label_2795:
    "Scene label_2795"
    if intelligence >= 17:
        jump label_2820

label label_2820:
    $ intelligence += 3
    menu:
        "Explore":
            jump label_2821
        "Go forward":
            jump label_2822
        "Look around":
            jump label_2823

label label_2821:
    "Scene label_2821"
    jump end_2824

label label_2822:
    "Scene label_2822"
    jump end_2824

label label_2823:
    "Scene label_2823"
    jump end_2824

    jump label_2824

label label_2824:
    "Ветка false для label_2820"
    menu:
        "Go forward":
            $ intelligence += 1
            jump label_2825
        "Open door":
            jump label_2826

label label_2825:
    "Scene label_2825"
    jump end_2827

label label_2826:
    "Scene label_2826"
    jump end_2827

label label_2796:
    "Scene label_2796"
    menu:
        "Explore":
            jump label_2827
        "Talk":
            $ intelligence += 2
            jump label_2828

label label_2827:
    "Scene label_2827"
    menu:
        "Go forward":
            $ strength += 3
            jump label_2829
        "Look around":
            jump label_2830
        "Open door":
            $ luck += 3
            jump label_2831

label label_2829:
    "Scene label_2829"
    jump end_2832

label label_2830:
    "Scene label_2830"
    jump end_2832

label label_2831:
    "Scene label_2831"
    jump end_2832

label label_2828:
    "Scene label_2828"
    menu:
        "Explore":
            jump label_2832
        "Go back":
            $ luck += 2
            jump label_2833
        "Go back":
            $ intelligence += 3
            jump label_2834

label label_2832:
    "Scene label_2832"
    jump end_2835

label label_2833:
    "Scene label_2833"
    jump end_2835

label label_2834:
    "Scene label_2834"
    jump end_2835

label label_2600:
    "Scene label_2600"
    menu:
        "Look around":
            $ intelligence += 2
            jump label_2835
        "Look around":
            $ luck += 1
            jump label_2836
        "Look around":
            $ charisma += 3
            jump label_2837
        "Go back":
            jump label_2838

label label_2835:
    "Scene label_2835"
    menu:
        "Open door":
            jump label_2839
        "Talk":
            jump label_2840
        "Go forward":
            $ luck += 2
            jump label_2841
        "Talk":
            jump label_2842

label label_2839:
    "Scene label_2839"
    if charisma >= 9:
        jump label_2843

label label_2843:
    $ charisma += 4
    menu:
        "Look around":
            jump label_2844
        "Open door":
            jump label_2845

label label_2844:
    "Scene label_2844"
    jump end_2846

label label_2845:
    "Scene label_2845"
    jump end_2846

    jump label_2846

label label_2846:
    "Ветка false для label_2843"
    if intelligence >= 11:
        jump label_2847

label label_2847:
    $ intelligence += 3
    jump end_2848

    jump label_2848

label label_2848:
    "Ветка false для label_2847"
    jump end_2849

label label_2840:
    "Scene label_2840"
    menu:
        "Use item":
            $ strength += 1
            jump label_2849
        "Look around":
            jump label_2850

label label_2849:
    "Scene label_2849"
    menu:
        "Go forward":
            $ intelligence += 3
            jump label_2851
        "Use item":
            jump label_2852
        "Go forward":
            jump label_2853

label label_2851:
    "Scene label_2851"
    jump end_2854

label label_2852:
    "Scene label_2852"
    jump end_2854

label label_2853:
    "Scene label_2853"
    jump end_2854

label label_2850:
    "Scene label_2850"
    menu:
        "Talk":
            $ strength += 1
            jump label_2854
        "Go forward":
            $ intelligence += 1
            jump label_2855

label label_2854:
    "Scene label_2854"
    jump end_2856

label label_2855:
    "Scene label_2855"
    jump end_2856

label label_2841:
    "Scene label_2841"
    if charisma >= 19:
        jump label_2856

label label_2856:
    $ charisma += 5
    menu:
        "Go forward":
            jump label_2857
        "Pick up item":
            jump label_2858

label label_2857:
    "Scene label_2857"
    jump end_2859

label label_2858:
    "Scene label_2858"
    jump end_2859

    jump label_2859

label label_2859:
    "Ветка false для label_2856"
    if strength >= 14:
        jump label_2860

label label_2860:
    $ strength += 3
    jump end_2861

    jump label_2861

label label_2861:
    "Ветка false для label_2860"
    jump end_2862

label label_2842:
    "Scene label_2842"
    menu:
        "Go back":
            $ intelligence += 3
            jump label_2862
        "Go back":
            jump label_2863

label label_2862:
    "Scene label_2862"
    menu:
        "Look around":
            jump label_2864
        "Go forward":
            jump label_2865
        "Go back":
            $ intelligence += 1
            jump label_2866
        "Explore":
            $ luck += 3
            jump label_2867

label label_2864:
    "Scene label_2864"
    jump end_2868

label label_2865:
    "Scene label_2865"
    jump end_2868

label label_2866:
    "Scene label_2866"
    jump end_2868

label label_2867:
    "Scene label_2867"
    jump end_2868

label label_2863:
    "Scene label_2863"
    menu:
        "Go forward":
            $ strength += 2
            jump label_2868
        "Open door":
            jump label_2869

label label_2868:
    "Scene label_2868"
    jump end_2870

label label_2869:
    "Scene label_2869"
    jump end_2870

label label_2836:
    "Scene label_2836"
    if luck >= 15:
        jump label_2870

label label_2870:
    $ luck += 5
    menu:
        "Explore":
            $ strength += 2
            jump label_2871
        "Open door":
            jump label_2872

label label_2871:
    "Scene label_2871"
    menu:
        "Go back":
            $ strength += 3
            jump label_2873
        "Open door":
            jump label_2874
        "Go back":
            jump label_2875

label label_2873:
    "Scene label_2873"
    jump end_2876

label label_2874:
    "Scene label_2874"
    jump end_2876

label label_2875:
    "Scene label_2875"
    jump end_2876

label label_2872:
    "Scene label_2872"
    menu:
        "Use item":
            jump label_2876
        "Go forward":
            jump label_2877
        "Explore":
            $ luck += 3
            jump label_2878
        "Pick up item":
            $ strength += 2
            jump label_2879

label label_2876:
    "Scene label_2876"
    jump end_2880

label label_2877:
    "Scene label_2877"
    jump end_2880

label label_2878:
    "Scene label_2878"
    jump end_2880

label label_2879:
    "Scene label_2879"
    jump end_2880

    jump label_2880

label label_2880:
    "Ветка false для label_2870"
    menu:
        "Open door":
            $ intelligence += 2
            jump label_2881
        "Talk":
            $ charisma += 1
            jump label_2882

label label_2881:
    "Scene label_2881"
    menu:
        "Go forward":
            jump label_2883
        "Open door":
            jump label_2884
        "Look around":
            $ charisma += 3
            jump label_2885

label label_2883:
    "Scene label_2883"
    jump end_2886

label label_2884:
    "Scene label_2884"
    jump end_2886

label label_2885:
    "Scene label_2885"
    jump end_2886

label label_2882:
    "Scene label_2882"
    if strength >= 16:
        jump label_2886

label label_2886:
    $ strength += 5
    jump end_2887

    jump label_2887

label label_2887:
    "Ветка false для label_2886"
    jump end_2888

label label_2837:
    "Scene label_2837"
    if charisma >= 7:
        jump label_2888

label label_2888:
    $ charisma += 5
    menu:
        "Use item":
            $ strength += 1
            jump label_2889
        "Open door":
            jump label_2890

label label_2889:
    "Scene label_2889"
    menu:
        "Pick up item":
            jump label_2891
        "Talk":
            $ luck += 1
            jump label_2892
        "Go forward":
            jump label_2893

label label_2891:
    "Scene label_2891"
    jump end_2894

label label_2892:
    "Scene label_2892"
    jump end_2894

label label_2893:
    "Scene label_2893"
    jump end_2894

label label_2890:
    "Scene label_2890"
    menu:
        "Explore":
            jump label_2894
        "Look around":
            jump label_2895
        "Explore":
            $ luck += 1
            jump label_2896
        "Pick up item":
            $ luck += 3
            jump label_2897

label label_2894:
    "Scene label_2894"
    jump end_2898

label label_2895:
    "Scene label_2895"
    jump end_2898

label label_2896:
    "Scene label_2896"
    jump end_2898

label label_2897:
    "Scene label_2897"
    jump end_2898

    jump label_2898

label label_2898:
    "Ветка false для label_2888"
    if intelligence >= 20:
        jump label_2899

label label_2899:
    $ intelligence += 4
    menu:
        "Look around":
            $ intelligence += 2
            jump label_2900
        "Look around":
            jump label_2901

label label_2900:
    "Scene label_2900"
    jump end_2902

label label_2901:
    "Scene label_2901"
    jump end_2902

    jump label_2902

label label_2902:
    "Ветка false для label_2899"
    menu:
        "Open door":
            $ intelligence += 1
            jump label_2903
        "Pick up item":
            $ strength += 2
            jump label_2904

label label_2903:
    "Scene label_2903"
    jump end_2905

label label_2904:
    "Scene label_2904"
    jump end_2905

label label_2838:
    "Scene label_2838"
    if luck >= 16:
        jump label_2905

label label_2905:
    $ luck += 4
    menu:
        "Explore":
            jump label_2906
        "Explore":
            $ strength += 2
            jump label_2907

label label_2906:
    "Scene label_2906"
    menu:
        "Talk":
            $ intelligence += 1
            jump label_2908
        "Explore":
            $ strength += 3
            jump label_2909
        "Go forward":
            jump label_2910
        "Go forward":
            $ charisma += 1
            jump label_2911

label label_2908:
    "Scene label_2908"
    jump end_2912

label label_2909:
    "Scene label_2909"
    jump end_2912

label label_2910:
    "Scene label_2910"
    jump end_2912

label label_2911:
    "Scene label_2911"
    jump end_2912

label label_2907:
    "Scene label_2907"
    menu:
        "Open door":
            $ strength += 2
            jump label_2912
        "Talk":
            $ intelligence += 2
            jump label_2913
        "Pick up item":
            jump label_2914

label label_2912:
    "Scene label_2912"
    jump end_2915

label label_2913:
    "Scene label_2913"
    jump end_2915

label label_2914:
    "Scene label_2914"
    jump end_2915

    jump label_2915

label label_2915:
    "Ветка false для label_2905"
    menu:
        "Explore":
            jump label_2916
        "Go back":
            $ strength += 2
            jump label_2917
        "Talk":
            $ luck += 3
            jump label_2918
        "Pick up item":
            $ intelligence += 2
            jump label_2919

label label_2916:
    "Scene label_2916"
    if luck >= 5:
        jump label_2920

label label_2920:
    $ luck += 5
    jump end_2921

    jump label_2921

label label_2921:
    "Ветка false для label_2920"
    jump end_2922

label label_2917:
    "Scene label_2917"
    if luck >= 6:
        jump label_2922

label label_2922:
    $ luck += 2
    jump end_2923

    jump label_2923

label label_2923:
    "Ветка false для label_2922"
    jump end_2924

label label_2918:
    "Scene label_2918"
    if luck >= 5:
        jump label_2924

label label_2924:
    $ luck += 3
    jump end_2925

    jump label_2925

label label_2925:
    "Ветка false для label_2924"
    jump end_2926

label label_2919:
    "Scene label_2919"
    menu:
        "Look around":
            $ charisma += 1
            jump label_2926
        "Go forward":
            jump label_2927

label label_2926:
    "Scene label_2926"
    jump end_2928

label label_2927:
    "Scene label_2927"
    jump end_2928

label label_2416:
    "Scene label_2416"
    if charisma >= 6:
        jump label_2928

label label_2928:
    $ charisma += 3
    if strength >= 19:
        jump label_2929

label label_2929:
    $ strength += 2
    menu:
        "Explore":
            jump label_2930
        "Go forward":
            jump label_2931
        "Go back":
            jump label_2932
        "Look around":
            jump label_2933

label label_2930:
    "Scene label_2930"
    menu:
        "Explore":
            jump label_2934
        "Use item":
            jump label_2935
        "Talk":
            jump label_2936

label label_2934:
    "Scene label_2934"
    menu:
        "Use item":
            jump label_2937
        "Open door":
            $ luck += 2
            jump label_2938
        "Pick up item":
            jump label_2939

label label_2937:
    "Scene label_2937"
    jump end_2940

label label_2938:
    "Scene label_2938"
    jump end_2940

label label_2939:
    "Scene label_2939"
    jump end_2940

label label_2935:
    "Scene label_2935"
    menu:
        "Look around":
            jump label_2940
        "Talk":
            jump label_2941
        "Use item":
            jump label_2942
        "Look around":
            $ strength += 1
            jump label_2943

label label_2940:
    "Scene label_2940"
    jump end_2944

label label_2941:
    "Scene label_2941"
    jump end_2944

label label_2942:
    "Scene label_2942"
    jump end_2944

label label_2943:
    "Scene label_2943"
    jump end_2944

label label_2936:
    "Scene label_2936"
    if strength >= 9:
        jump label_2944

label label_2944:
    $ strength += 4
    jump end_2945

    jump label_2945

label label_2945:
    "Ветка false для label_2944"
    jump end_2946

label label_2931:
    "Scene label_2931"
    menu:
        "Open door":
            $ intelligence += 1
            jump label_2946
        "Pick up item":
            jump label_2947
        "Use item":
            jump label_2948
        "Explore":
            $ intelligence += 2
            jump label_2949

label label_2946:
    "Scene label_2946"
    menu:
        "Open door":
            jump label_2950
        "Open door":
            jump label_2951

label label_2950:
    "Scene label_2950"
    jump end_2952

label label_2951:
    "Scene label_2951"
    jump end_2952

label label_2947:
    "Scene label_2947"
    menu:
        "Go forward":
            jump label_2952
        "Pick up item":
            $ intelligence += 3
            jump label_2953
        "Go back":
            jump label_2954

label label_2952:
    "Scene label_2952"
    jump end_2955

label label_2953:
    "Scene label_2953"
    jump end_2955

label label_2954:
    "Scene label_2954"
    jump end_2955

label label_2948:
    "Scene label_2948"
    menu:
        "Use item":
            jump label_2955
        "Talk":
            $ intelligence += 2
            jump label_2956
        "Go back":
            $ intelligence += 3
            jump label_2957
        "Go forward":
            $ strength += 2
            jump label_2958

label label_2955:
    "Scene label_2955"
    jump end_2959

label label_2956:
    "Scene label_2956"
    jump end_2959

label label_2957:
    "Scene label_2957"
    jump end_2959

label label_2958:
    "Scene label_2958"
    jump end_2959

label label_2949:
    "Scene label_2949"
    menu:
        "Go forward":
            $ charisma += 3
            jump label_2959
        "Explore":
            $ luck += 2
            jump label_2960
        "Talk":
            $ intelligence += 3
            jump label_2961

label label_2959:
    "Scene label_2959"
    jump end_2962

label label_2960:
    "Scene label_2960"
    jump end_2962

label label_2961:
    "Scene label_2961"
    jump end_2962

label label_2932:
    "Scene label_2932"
    menu:
        "Go forward":
            jump label_2962
        "Explore":
            jump label_2963
        "Explore":
            $ charisma += 3
            jump label_2964
        "Go back":
            jump label_2965

label label_2962:
    "Scene label_2962"
    menu:
        "Look around":
            jump label_2966
        "Look around":
            jump label_2967
        "Look around":
            $ charisma += 1
            jump label_2968
        "Go forward":
            $ luck += 3
            jump label_2969

label label_2966:
    "Scene label_2966"
    jump end_2970

label label_2967:
    "Scene label_2967"
    jump end_2970

label label_2968:
    "Scene label_2968"
    jump end_2970

label label_2969:
    "Scene label_2969"
    jump end_2970

label label_2963:
    "Scene label_2963"
    menu:
        "Open door":
            $ intelligence += 1
            jump label_2970
        "Go forward":
            $ luck += 1
            jump label_2971
        "Explore":
            jump label_2972
        "Go back":
            jump label_2973

label label_2970:
    "Scene label_2970"
    jump end_2974

label label_2971:
    "Scene label_2971"
    jump end_2974

label label_2972:
    "Scene label_2972"
    jump end_2974

label label_2973:
    "Scene label_2973"
    jump end_2974

label label_2964:
    "Scene label_2964"
    if intelligence >= 5:
        jump label_2974

label label_2974:
    $ intelligence += 2
    jump end_2975

    jump label_2975

label label_2975:
    "Ветка false для label_2974"
    jump end_2976

label label_2965:
    "Scene label_2965"
    menu:
        "Pick up item":
            jump label_2976
        "Explore":
            jump label_2977

label label_2976:
    "Scene label_2976"
    jump end_2978

label label_2977:
    "Scene label_2977"
    jump end_2978

label label_2933:
    "Scene label_2933"
    if intelligence >= 18:
        jump label_2978

label label_2978:
    $ intelligence += 2
    if strength >= 15:
        jump label_2979

label label_2979:
    $ strength += 3
    jump end_2980

    jump label_2980

label label_2980:
    "Ветка false для label_2979"
    jump end_2981

    jump label_2981

label label_2981:
    "Ветка false для label_2978"
    menu:
        "Explore":
            jump label_2982
        "Go back":
            $ luck += 1
            jump label_2983

label label_2982:
    "Scene label_2982"
    jump end_2984

label label_2983:
    "Scene label_2983"
    jump end_2984

    jump label_2984

label label_2984:
    "Ветка false для label_2929"
    menu:
        "Pick up item":
            $ charisma += 3
            jump label_2985
        "Use item":
            jump label_2986

label label_2985:
    "Scene label_2985"
    menu:
        "Go forward":
            jump label_2987
        "Explore":
            jump label_2988
        "Use item":
            jump label_2989
        "Look around":
            $ charisma += 2
            jump label_2990

label label_2987:
    "Scene label_2987"
    menu:
        "Use item":
            jump label_2991
        "Go forward":
            $ strength += 1
            jump label_2992
        "Go back":
            $ strength += 1
            jump label_2993
        "Open door":
            $ luck += 1
            jump label_2994

label label_2991:
    "Scene label_2991"
    jump end_2995

label label_2992:
    "Scene label_2992"
    jump end_2995

label label_2993:
    "Scene label_2993"
    jump end_2995

label label_2994:
    "Scene label_2994"
    jump end_2995

label label_2988:
    "Scene label_2988"
    if luck >= 8:
        jump label_2995

label label_2995:
    $ luck += 3
    jump end_2996

    jump label_2996

label label_2996:
    "Ветка false для label_2995"
    jump end_2997

label label_2989:
    "Scene label_2989"
    menu:
        "Talk":
            jump label_2997
        "Explore":
            $ intelligence += 2
            jump label_2998
        "Explore":
            $ luck += 2
            jump label_2999

label label_2997:
    "Scene label_2997"
    jump end_3000

label label_2998:
    "Scene label_2998"
    jump end_3000

label label_2999:
    "Scene label_2999"
    jump end_3000

label label_2990:
    "Scene label_2990"
    if strength >= 18:
        jump label_3000

label label_3000:
    $ strength += 5
    jump end_3001

    jump label_3001

label label_3001:
    "Ветка false для label_3000"
    jump end_3002

label label_2986:
    "Scene label_2986"
    menu:
        "Go forward":
            jump label_3002
        "Open door":
            jump label_3003
        "Go forward":
            $ charisma += 3
            jump label_3004
        "Pick up item":
            $ strength += 3
            jump label_3005

label label_3002:
    "Scene label_3002"
    menu:
        "Go back":
            jump label_3006
        "Talk":
            jump label_3007
        "Use item":
            jump label_3008

label label_3006:
    "Scene label_3006"
    jump end_3009

label label_3007:
    "Scene label_3007"
    jump end_3009

label label_3008:
    "Scene label_3008"
    jump end_3009

label label_3003:
    "Scene label_3003"
    menu:
        "Go back":
            jump label_3009
        "Explore":
            jump label_3010
        "Go forward":
            $ charisma += 2
            jump label_3011

label label_3009:
    "Scene label_3009"
    jump end_3012

label label_3010:
    "Scene label_3010"
    jump end_3012

label label_3011:
    "Scene label_3011"
    jump end_3012

label label_3004:
    "Scene label_3004"
    menu:
        "Explore":
            $ intelligence += 1
            jump label_3012
        "Explore":
            jump label_3013

label label_3012:
    "Scene label_3012"
    jump end_3014

label label_3013:
    "Scene label_3013"
    jump end_3014

label label_3005:
    "Scene label_3005"
    if intelligence >= 17:
        jump label_3014

label label_3014:
    $ intelligence += 4
    jump end_3015

    jump label_3015

label label_3015:
    "Ветка false для label_3014"
    jump end_3016

    jump label_3016

label label_3016:
    "Ветка false для label_2928"
    if charisma >= 10:
        jump label_3017

label label_3017:
    $ charisma += 4
    if luck >= 10:
        jump label_3018

label label_3018:
    $ luck += 2
    menu:
        "Talk":
            $ intelligence += 2
            jump label_3019
        "Explore":
            jump label_3020
        "Look around":
            $ strength += 3
            jump label_3021
        "Go forward":
            jump label_3022

label label_3019:
    "Scene label_3019"
    menu:
        "Go forward":
            $ strength += 3
            jump label_3023
        "Open door":
            jump label_3024
        "Use item":
            $ strength += 1
            jump label_3025
        "Open door":
            $ intelligence += 1
            jump label_3026

label label_3023:
    "Scene label_3023"
    jump end_3027

label label_3024:
    "Scene label_3024"
    jump end_3027

label label_3025:
    "Scene label_3025"
    jump end_3027

label label_3026:
    "Scene label_3026"
    jump end_3027

label label_3020:
    "Scene label_3020"
    menu:
        "Go back":
            jump label_3027
        "Explore":
            jump label_3028

label label_3027:
    "Scene label_3027"
    jump end_3029

label label_3028:
    "Scene label_3028"
    jump end_3029

label label_3021:
    "Scene label_3021"
    menu:
        "Explore":
            jump label_3029
        "Pick up item":
            $ intelligence += 1
            jump label_3030
        "Talk":
            jump label_3031

label label_3029:
    "Scene label_3029"
    jump end_3032

label label_3030:
    "Scene label_3030"
    jump end_3032

label label_3031:
    "Scene label_3031"
    jump end_3032

label label_3022:
    "Scene label_3022"
    menu:
        "Go back":
            $ strength += 1
            jump label_3032
        "Use item":
            $ intelligence += 1
            jump label_3033
        "Talk":
            $ luck += 3
            jump label_3034

label label_3032:
    "Scene label_3032"
    jump end_3035

label label_3033:
    "Scene label_3033"
    jump end_3035

label label_3034:
    "Scene label_3034"
    jump end_3035

    jump label_3035

label label_3035:
    "Ветка false для label_3018"
    if luck >= 19:
        jump label_3036

label label_3036:
    $ luck += 5
    menu:
        "Talk":
            $ charisma += 1
            jump label_3037
        "Look around":
            jump label_3038
        "Talk":
            $ strength += 1
            jump label_3039
        "Use item":
            $ intelligence += 1
            jump label_3040

label label_3037:
    "Scene label_3037"
    jump end_3041

label label_3038:
    "Scene label_3038"
    jump end_3041

label label_3039:
    "Scene label_3039"
    jump end_3041

label label_3040:
    "Scene label_3040"
    jump end_3041

    jump label_3041

label label_3041:
    "Ветка false для label_3036"
    menu:
        "Talk":
            $ strength += 3
            jump label_3042
        "Pick up item":
            jump label_3043
        "Explore":
            jump label_3044
        "Open door":
            $ strength += 3
            jump label_3045

label label_3042:
    "Scene label_3042"
    jump end_3046

label label_3043:
    "Scene label_3043"
    jump end_3046

label label_3044:
    "Scene label_3044"
    jump end_3046

label label_3045:
    "Scene label_3045"
    jump end_3046

    jump label_3046

label label_3046:
    "Ветка false для label_3017"
    menu:
        "Explore":
            $ strength += 3
            jump label_3047
        "Explore":
            jump label_3048
        "Pick up item":
            jump label_3049
        "Pick up item":
            $ strength += 2
            jump label_3050

label label_3047:
    "Scene label_3047"
    menu:
        "Go forward":
            jump label_3051
        "Explore":
            jump label_3052

label label_3051:
    "Scene label_3051"
    menu:
        "Use item":
            $ charisma += 3
            jump label_3053
        "Talk":
            jump label_3054
        "Pick up item":
            jump label_3055
        "Go back":
            $ luck += 1
            jump label_3056

label label_3053:
    "Scene label_3053"
    jump end_3057

label label_3054:
    "Scene label_3054"
    jump end_3057

label label_3055:
    "Scene label_3055"
    jump end_3057

label label_3056:
    "Scene label_3056"
    jump end_3057

label label_3052:
    "Scene label_3052"
    menu:
        "Talk":
            $ charisma += 1
            jump label_3057
        "Go forward":
            $ intelligence += 3
            jump label_3058
        "Go back":
            jump label_3059
        "Use item":
            $ intelligence += 1
            jump label_3060

label label_3057:
    "Scene label_3057"
    jump end_3061

label label_3058:
    "Scene label_3058"
    jump end_3061

label label_3059:
    "Scene label_3059"
    jump end_3061

label label_3060:
    "Scene label_3060"
    jump end_3061

label label_3048:
    "Scene label_3048"
    if luck >= 13:
        jump label_3061

label label_3061:
    $ luck += 5
    menu:
        "Use item":
            jump label_3062
        "Look around":
            $ luck += 3
            jump label_3063
        "Use item":
            jump label_3064
        "Talk":
            jump label_3065

label label_3062:
    "Scene label_3062"
    jump end_3066

label label_3063:
    "Scene label_3063"
    jump end_3066

label label_3064:
    "Scene label_3064"
    jump end_3066

label label_3065:
    "Scene label_3065"
    jump end_3066

    jump label_3066

label label_3066:
    "Ветка false для label_3061"
    menu:
        "Go forward":
            jump label_3067
        "Go forward":
            $ intelligence += 1
            jump label_3068

label label_3067:
    "Scene label_3067"
    jump end_3069

label label_3068:
    "Scene label_3068"
    jump end_3069

label label_3049:
    "Scene label_3049"
    menu:
        "Pick up item":
            $ intelligence += 3
            jump label_3069
        "Look around":
            $ intelligence += 1
            jump label_3070

label label_3069:
    "Scene label_3069"
    menu:
        "Look around":
            $ strength += 2
            jump label_3071
        "Go back":
            $ strength += 3
            jump label_3072

label label_3071:
    "Scene label_3071"
    jump end_3073

label label_3072:
    "Scene label_3072"
    jump end_3073

label label_3070:
    "Scene label_3070"
    menu:
        "Explore":
            jump label_3073
        "Use item":
            jump label_3074

label label_3073:
    "Scene label_3073"
    jump end_3075

label label_3074:
    "Scene label_3074"
    jump end_3075

label label_3050:
    "Scene label_3050"
    menu:
        "Explore":
            $ strength += 3
            jump label_3075
        "Use item":
            $ strength += 3
            jump label_3076
        "Go forward":
            jump label_3077

label label_3075:
    "Scene label_3075"
label label_3076:
    "Scene label_3076"
label label_3077:
    "Scene label_3077"
label label_18:
    "Scene label_18"
label label_13:
    "Scene label_13"
label label_14:
    "Scene label_14"
label label_15:
    "Scene label_15"
label label_9:
    "Scene label_9"
label label_5:
    "Scene label_5"
label label_3:
    "Scene label_3"

label end_35:
    "Конец: end_35"

label end_35:
    "Конец: end_35"

label end_37:
    "Конец: end_37"

label end_38:
    "Конец: end_38"

label end_45:
    "Конец: end_45"

label end_45:
    "Конец: end_45"

label end_47:
    "Конец: end_47"

label end_47:
    "Конец: end_47"

label end_49:
    "Конец: end_49"

label end_49:
    "Конец: end_49"

label end_52:
    "Конец: end_52"

label end_52:
    "Конец: end_52"

label end_52:
    "Конец: end_52"

label end_61:
    "Конец: end_61"

label end_61:
    "Конец: end_61"

label end_61:
    "Конец: end_61"

label end_63:
    "Конец: end_63"

label end_63:
    "Конец: end_63"

label end_65:
    "Конец: end_65"

label end_65:
    "Конец: end_65"

label end_70:
    "Конец: end_70"

label end_70:
    "Конец: end_70"

label end_70:
    "Конец: end_70"

label end_70:
    "Конец: end_70"

label end_73:
    "Конец: end_73"

label end_73:
    "Конец: end_73"

label end_79:
    "Конец: end_79"

label end_79:
    "Конец: end_79"

label end_81:
    "Конец: end_81"

label end_81:
    "Конец: end_81"

label end_85:
    "Конец: end_85"

label end_85:
    "Конец: end_85"

label end_85:
    "Конец: end_85"

label end_85:
    "Конец: end_85"

label end_88:
    "Конец: end_88"

label end_88:
    "Конец: end_88"

label end_88:
    "Конец: end_88"

label end_96:
    "Конец: end_96"

label end_96:
    "Конец: end_96"

label end_96:
    "Конец: end_96"

label end_97:
    "Конец: end_97"

label end_98:
    "Конец: end_98"

label end_101:
    "Конец: end_101"

label end_101:
    "Конец: end_101"

label end_101:
    "Конец: end_101"

label end_103:
    "Конец: end_103"

label end_103:
    "Конец: end_103"

label end_109:
    "Конец: end_109"

label end_109:
    "Конец: end_109"

label end_112:
    "Конец: end_112"

label end_112:
    "Конец: end_112"

label end_112:
    "Конец: end_112"

label end_113:
    "Конец: end_113"

label end_114:
    "Конец: end_114"

label end_126:
    "Конец: end_126"

label end_126:
    "Конец: end_126"

label end_126:
    "Конец: end_126"

label end_126:
    "Конец: end_126"

label end_128:
    "Конец: end_128"

label end_128:
    "Конец: end_128"

label end_131:
    "Конец: end_131"

label end_131:
    "Конец: end_131"

label end_136:
    "Конец: end_136"

label end_136:
    "Конец: end_136"

label end_136:
    "Конец: end_136"

label end_136:
    "Конец: end_136"

label end_142:
    "Конец: end_142"

label end_142:
    "Конец: end_142"

label end_142:
    "Конец: end_142"

label end_142:
    "Конец: end_142"

label end_146:
    "Конец: end_146"

label end_146:
    "Конец: end_146"

label end_146:
    "Конец: end_146"

label end_149:
    "Конец: end_149"

label end_150:
    "Конец: end_150"

label end_152:
    "Конец: end_152"

label end_153:
    "Конец: end_153"

label end_160:
    "Конец: end_160"

label end_160:
    "Конец: end_160"

label end_160:
    "Конец: end_160"

label end_160:
    "Конец: end_160"

label end_163:
    "Конец: end_163"

label end_163:
    "Конец: end_163"

label end_163:
    "Конец: end_163"

label end_169:
    "Конец: end_169"

label end_169:
    "Конец: end_169"

label end_169:
    "Конец: end_169"

label end_169:
    "Конец: end_169"

label end_174:
    "Конец: end_174"

label end_174:
    "Конец: end_174"

label end_174:
    "Конец: end_174"

label end_174:
    "Конец: end_174"

label end_185:
    "Конец: end_185"

label end_185:
    "Конец: end_185"

label end_185:
    "Конец: end_185"

label end_185:
    "Конец: end_185"

label end_186:
    "Конец: end_186"

label end_187:
    "Конец: end_187"

label end_191:
    "Конец: end_191"

label end_191:
    "Конец: end_191"

label end_191:
    "Конец: end_191"

label end_191:
    "Конец: end_191"

label end_197:
    "Конец: end_197"

label end_197:
    "Конец: end_197"

label end_201:
    "Конец: end_201"

label end_201:
    "Конец: end_201"

label end_201:
    "Конец: end_201"

label end_201:
    "Конец: end_201"

label end_203:
    "Конец: end_203"

label end_203:
    "Конец: end_203"

label end_204:
    "Конец: end_204"

label end_205:
    "Конец: end_205"

label end_211:
    "Конец: end_211"

label end_211:
    "Конец: end_211"

label end_211:
    "Конец: end_211"

label end_215:
    "Конец: end_215"

label end_215:
    "Конец: end_215"

label end_215:
    "Конец: end_215"

label end_215:
    "Конец: end_215"

label end_216:
    "Конец: end_216"

label end_217:
    "Конец: end_217"

label end_221:
    "Конец: end_221"

label end_221:
    "Конец: end_221"

label end_221:
    "Конец: end_221"

label end_224:
    "Конец: end_224"

label end_224:
    "Конец: end_224"

label end_232:
    "Конец: end_232"

label end_232:
    "Конец: end_232"

label end_232:
    "Конец: end_232"

label end_233:
    "Конец: end_233"

label end_234:
    "Конец: end_234"

label end_237:
    "Конец: end_237"

label end_237:
    "Конец: end_237"

label end_242:
    "Конец: end_242"

label end_242:
    "Конец: end_242"

label end_242:
    "Конец: end_242"

label end_242:
    "Конец: end_242"

label end_250:
    "Конец: end_250"

label end_250:
    "Конец: end_250"

label end_250:
    "Конец: end_250"

label end_250:
    "Конец: end_250"

label end_254:
    "Конец: end_254"

label end_254:
    "Конец: end_254"

label end_254:
    "Конец: end_254"

label end_254:
    "Конец: end_254"

label end_259:
    "Конец: end_259"

label end_260:
    "Конец: end_260"

label end_263:
    "Конец: end_263"

label end_263:
    "Конец: end_263"

label end_263:
    "Конец: end_263"

label end_266:
    "Конец: end_266"

label end_266:
    "Конец: end_266"

label end_266:
    "Конец: end_266"

label end_276:
    "Конец: end_276"

label end_276:
    "Конец: end_276"

label end_276:
    "Конец: end_276"

label end_276:
    "Конец: end_276"

label end_280:
    "Конец: end_280"

label end_280:
    "Конец: end_280"

label end_280:
    "Конец: end_280"

label end_283:
    "Конец: end_283"

label end_284:
    "Конец: end_284"

label end_286:
    "Конец: end_286"

label end_286:
    "Конец: end_286"

label end_290:
    "Конец: end_290"

label end_290:
    "Конец: end_290"

label end_291:
    "Конец: end_291"

label end_292:
    "Конец: end_292"

label end_299:
    "Конец: end_299"

label end_299:
    "Конец: end_299"

label end_301:
    "Конец: end_301"

label end_302:
    "Конец: end_302"

label end_306:
    "Конец: end_306"

label end_307:
    "Конец: end_307"

label end_309:
    "Конец: end_309"

label end_309:
    "Конец: end_309"

label end_311:
    "Конец: end_311"

label end_311:
    "Конец: end_311"

label end_315:
    "Конец: end_315"

label end_315:
    "Конец: end_315"

label end_315:
    "Конец: end_315"

label end_318:
    "Конец: end_318"

label end_318:
    "Конец: end_318"

label end_327:
    "Конец: end_327"

label end_327:
    "Конец: end_327"

label end_327:
    "Конец: end_327"

label end_330:
    "Конец: end_330"

label end_330:
    "Конец: end_330"

label end_330:
    "Конец: end_330"

label end_332:
    "Конец: end_332"

label end_332:
    "Конец: end_332"

label end_336:
    "Конец: end_336"

label end_336:
    "Конец: end_336"

label end_338:
    "Конец: end_338"

label end_339:
    "Конец: end_339"

label end_345:
    "Конец: end_345"

label end_345:
    "Конец: end_345"

label end_348:
    "Конец: end_348"

label end_348:
    "Конец: end_348"

label end_348:
    "Конец: end_348"

label end_353:
    "Конец: end_353"

label end_353:
    "Конец: end_353"

label end_353:
    "Конец: end_353"

label end_355:
    "Конец: end_355"

label end_356:
    "Конец: end_356"

label end_369:
    "Конец: end_369"

label end_369:
    "Конец: end_369"

label end_370:
    "Конец: end_370"

label end_371:
    "Конец: end_371"

label end_375:
    "Конец: end_375"

label end_375:
    "Конец: end_375"

label end_375:
    "Конец: end_375"

label end_375:
    "Конец: end_375"

label end_379:
    "Конец: end_379"

label end_380:
    "Конец: end_380"

label end_383:
    "Конец: end_383"

label end_383:
    "Конец: end_383"

label end_383:
    "Конец: end_383"

label end_387:
    "Конец: end_387"

label end_387:
    "Конец: end_387"

label end_387:
    "Конец: end_387"

label end_387:
    "Конец: end_387"

label end_390:
    "Конец: end_390"

label end_391:
    "Конец: end_391"

label end_396:
    "Конец: end_396"

label end_396:
    "Конец: end_396"

label end_396:
    "Конец: end_396"

label end_396:
    "Конец: end_396"

label end_404:
    "Конец: end_404"

label end_404:
    "Конец: end_404"

label end_404:
    "Конец: end_404"

label end_408:
    "Конец: end_408"

label end_408:
    "Конец: end_408"

label end_408:
    "Конец: end_408"

label end_408:
    "Конец: end_408"

label end_412:
    "Конец: end_412"

label end_412:
    "Конец: end_412"

label end_412:
    "Конец: end_412"

label end_412:
    "Конец: end_412"

label end_416:
    "Конец: end_416"

label end_416:
    "Конец: end_416"

label end_416:
    "Конец: end_416"

label end_416:
    "Конец: end_416"

label end_424:
    "Конец: end_424"

label end_424:
    "Конец: end_424"

label end_424:
    "Конец: end_424"

label end_426:
    "Конец: end_426"

label end_426:
    "Конец: end_426"

label end_434:
    "Конец: end_434"

label end_434:
    "Конец: end_434"

label end_434:
    "Конец: end_434"

label end_434:
    "Конец: end_434"

label end_437:
    "Конец: end_437"

label end_437:
    "Конец: end_437"

label end_437:
    "Конец: end_437"

label end_438:
    "Конец: end_438"

label end_439:
    "Конец: end_439"

label end_440:
    "Конец: end_440"

label end_441:
    "Конец: end_441"

label end_445:
    "Конец: end_445"

label end_446:
    "Конец: end_446"

label end_451:
    "Конец: end_451"

label end_451:
    "Конец: end_451"

label end_451:
    "Конец: end_451"

label end_451:
    "Конец: end_451"

label end_454:
    "Конец: end_454"

label end_455:
    "Конец: end_455"

label end_457:
    "Конец: end_457"

label end_458:
    "Конец: end_458"

label end_465:
    "Конец: end_465"

label end_466:
    "Конец: end_466"

label end_467:
    "Конец: end_467"

label end_468:
    "Конец: end_468"

label end_469:
    "Конец: end_469"

label end_470:
    "Конец: end_470"

label end_479:
    "Конец: end_479"

label end_479:
    "Конец: end_479"

label end_479:
    "Конец: end_479"

label end_479:
    "Конец: end_479"

label end_483:
    "Конец: end_483"

label end_483:
    "Конец: end_483"

label end_483:
    "Конец: end_483"

label end_483:
    "Конец: end_483"

label end_486:
    "Конец: end_486"

label end_486:
    "Конец: end_486"

label end_486:
    "Конец: end_486"

label end_487:
    "Конец: end_487"

label end_488:
    "Конец: end_488"

label end_499:
    "Конец: end_499"

label end_499:
    "Конец: end_499"

label end_499:
    "Конец: end_499"

label end_499:
    "Конец: end_499"

label end_500:
    "Конец: end_500"

label end_501:
    "Конец: end_501"

label end_502:
    "Конец: end_502"

label end_503:
    "Конец: end_503"

label end_507:
    "Конец: end_507"

label end_507:
    "Конец: end_507"

label end_507:
    "Конец: end_507"

label end_507:
    "Конец: end_507"

label end_514:
    "Конец: end_514"

label end_514:
    "Конец: end_514"

label end_514:
    "Конец: end_514"

label end_514:
    "Конец: end_514"

label end_518:
    "Конец: end_518"

label end_518:
    "Конец: end_518"

label end_518:
    "Конец: end_518"

label end_518:
    "Конец: end_518"

label end_522:
    "Конец: end_522"

label end_522:
    "Конец: end_522"

label end_522:
    "Конец: end_522"

label end_522:
    "Конец: end_522"

label end_527:
    "Конец: end_527"

label end_527:
    "Конец: end_527"

label end_527:
    "Конец: end_527"

label end_529:
    "Конец: end_529"

label end_529:
    "Конец: end_529"

label end_543:
    "Конец: end_543"

label end_543:
    "Конец: end_543"

label end_543:
    "Конец: end_543"

label end_546:
    "Конец: end_546"

label end_546:
    "Конец: end_546"

label end_546:
    "Конец: end_546"

label end_550:
    "Конец: end_550"

label end_551:
    "Конец: end_551"

label end_552:
    "Конец: end_552"

label end_553:
    "Конец: end_553"

label end_556:
    "Конец: end_556"

label end_557:
    "Конец: end_557"

label end_559:
    "Конец: end_559"

label end_560:
    "Конец: end_560"

label end_565:
    "Конец: end_565"

label end_566:
    "Конец: end_566"

label end_567:
    "Конец: end_567"

label end_568:
    "Конец: end_568"

label end_569:
    "Конец: end_569"

label end_570:
    "Конец: end_570"

label end_575:
    "Конец: end_575"

label end_576:
    "Конец: end_576"

label end_579:
    "Конец: end_579"

label end_579:
    "Конец: end_579"

label end_579:
    "Конец: end_579"

label end_583:
    "Конец: end_583"

label end_583:
    "Конец: end_583"

label end_583:
    "Конец: end_583"

label end_583:
    "Конец: end_583"

label end_587:
    "Конец: end_587"

label end_588:
    "Конец: end_588"

label end_591:
    "Конец: end_591"

label end_591:
    "Конец: end_591"

label end_591:
    "Конец: end_591"

label end_602:
    "Конец: end_602"

label end_602:
    "Конец: end_602"

label end_602:
    "Конец: end_602"

label end_605:
    "Конец: end_605"

label end_605:
    "Конец: end_605"

label end_605:
    "Конец: end_605"

label end_609:
    "Конец: end_609"

label end_609:
    "Конец: end_609"

label end_609:
    "Конец: end_609"

label end_609:
    "Конец: end_609"

label end_614:
    "Конец: end_614"

label end_614:
    "Конец: end_614"

label end_614:
    "Конец: end_614"

label end_615:
    "Конец: end_615"

label end_616:
    "Конец: end_616"

label end_619:
    "Конец: end_619"

label end_620:
    "Конец: end_620"

label end_624:
    "Конец: end_624"

label end_624:
    "Конец: end_624"

label end_624:
    "Конец: end_624"

label end_624:
    "Конец: end_624"

label end_632:
    "Конец: end_632"

label end_632:
    "Конец: end_632"

label end_632:
    "Конец: end_632"

label end_632:
    "Конец: end_632"

label end_634:
    "Конец: end_634"

label end_634:
    "Конец: end_634"

label end_636:
    "Конец: end_636"

label end_636:
    "Конец: end_636"

label end_641:
    "Конец: end_641"

label end_641:
    "Конец: end_641"

label end_643:
    "Конец: end_643"

label end_643:
    "Конец: end_643"

label end_652:
    "Конец: end_652"

label end_653:
    "Конец: end_653"

label end_655:
    "Конец: end_655"

label end_656:
    "Конец: end_656"

label end_660:
    "Конец: end_660"

label end_660:
    "Конец: end_660"

label end_660:
    "Конец: end_660"

label end_665:
    "Конец: end_665"

label end_665:
    "Конец: end_665"

label end_665:
    "Конец: end_665"

label end_665:
    "Конец: end_665"

label end_672:
    "Конец: end_672"

label end_672:
    "Конец: end_672"

label end_672:
    "Конец: end_672"

label end_674:
    "Конец: end_674"

label end_674:
    "Конец: end_674"

label end_678:
    "Конец: end_678"

label end_678:
    "Конец: end_678"

label end_678:
    "Конец: end_678"

label end_678:
    "Конец: end_678"

label end_680:
    "Конец: end_680"

label end_680:
    "Конец: end_680"

label end_689:
    "Конец: end_689"

label end_689:
    "Конец: end_689"

label end_689:
    "Конец: end_689"

label end_689:
    "Конец: end_689"

label end_691:
    "Конец: end_691"

label end_691:
    "Конец: end_691"

label end_692:
    "Конец: end_692"

label end_693:
    "Конец: end_693"

label end_697:
    "Конец: end_697"

label end_697:
    "Конец: end_697"

label end_698:
    "Конец: end_698"

label end_699:
    "Конец: end_699"

label end_706:
    "Конец: end_706"

label end_707:
    "Конец: end_707"

label end_710:
    "Конец: end_710"

label end_710:
    "Конец: end_710"

label end_710:
    "Конец: end_710"

label end_714:
    "Конец: end_714"

label end_714:
    "Конец: end_714"

label end_714:
    "Конец: end_714"

label end_714:
    "Конец: end_714"

label end_716:
    "Конец: end_716"

label end_716:
    "Конец: end_716"

label end_721:
    "Конец: end_721"

label end_722:
    "Конец: end_722"

label end_724:
    "Конец: end_724"

label end_724:
    "Конец: end_724"

label end_727:
    "Конец: end_727"

label end_727:
    "Конец: end_727"

label end_727:
    "Конец: end_727"

label end_728:
    "Конец: end_728"

label end_729:
    "Конец: end_729"

label end_737:
    "Конец: end_737"

label end_738:
    "Конец: end_738"

label end_739:
    "Конец: end_739"

label end_740:
    "Конец: end_740"

label end_741:
    "Конец: end_741"

label end_742:
    "Конец: end_742"

label end_750:
    "Конец: end_750"

label end_750:
    "Конец: end_750"

label end_750:
    "Конец: end_750"

label end_750:
    "Конец: end_750"

label end_754:
    "Конец: end_754"

label end_754:
    "Конец: end_754"

label end_754:
    "Конец: end_754"

label end_754:
    "Конец: end_754"

label end_758:
    "Конец: end_758"

label end_758:
    "Конец: end_758"

label end_758:
    "Конец: end_758"

label end_758:
    "Конец: end_758"

label end_759:
    "Конец: end_759"

label end_760:
    "Конец: end_760"

label end_768:
    "Конец: end_768"

label end_768:
    "Конец: end_768"

label end_768:
    "Конец: end_768"

label end_768:
    "Конец: end_768"

label end_769:
    "Конец: end_769"

label end_770:
    "Конец: end_770"

label end_772:
    "Конец: end_772"

label end_772:
    "Конец: end_772"

label end_776:
    "Конец: end_776"

label end_776:
    "Конец: end_776"

label end_776:
    "Конец: end_776"

label end_776:
    "Конец: end_776"

label end_781:
    "Конец: end_781"

label end_781:
    "Конец: end_781"

label end_781:
    "Конец: end_781"

label end_781:
    "Конец: end_781"

label end_783:
    "Конец: end_783"

label end_784:
    "Конец: end_784"

label end_796:
    "Конец: end_796"

label end_796:
    "Конец: end_796"

label end_796:
    "Конец: end_796"

label end_796:
    "Конец: end_796"

label end_800:
    "Конец: end_800"

label end_800:
    "Конец: end_800"

label end_800:
    "Конец: end_800"

label end_800:
    "Конец: end_800"

label end_802:
    "Конец: end_802"

label end_802:
    "Конец: end_802"

label end_810:
    "Конец: end_810"

label end_810:
    "Конец: end_810"

label end_810:
    "Конец: end_810"

label end_812:
    "Конец: end_812"

label end_812:
    "Конец: end_812"

label end_815:
    "Конец: end_815"

label end_815:
    "Конец: end_815"

label end_815:
    "Конец: end_815"

label end_819:
    "Конец: end_819"

label end_819:
    "Конец: end_819"

label end_819:
    "Конец: end_819"

label end_819:
    "Конец: end_819"

label end_828:
    "Конец: end_828"

label end_828:
    "Конец: end_828"

label end_830:
    "Конец: end_830"

label end_830:
    "Конец: end_830"

label end_832:
    "Конец: end_832"

label end_832:
    "Конец: end_832"

label end_835:
    "Конец: end_835"

label end_835:
    "Конец: end_835"

label end_840:
    "Конец: end_840"

label end_840:
    "Конец: end_840"

label end_840:
    "Конец: end_840"

label end_840:
    "Конец: end_840"

label end_843:
    "Конец: end_843"

label end_844:
    "Конец: end_844"

label end_847:
    "Конец: end_847"

label end_847:
    "Конец: end_847"

label end_847:
    "Конец: end_847"

label end_851:
    "Конец: end_851"

label end_851:
    "Конец: end_851"

label end_851:
    "Конец: end_851"

label end_855:
    "Конец: end_855"

label end_855:
    "Конец: end_855"

label end_855:
    "Конец: end_855"

label end_861:
    "Конец: end_861"

label end_862:
    "Конец: end_862"

label end_863:
    "Конец: end_863"

label end_864:
    "Конец: end_864"

label end_867:
    "Конец: end_867"

label end_867:
    "Конец: end_867"

label end_867:
    "Конец: end_867"

label end_868:
    "Конец: end_868"

label end_869:
    "Конец: end_869"

label end_875:
    "Конец: end_875"

label end_875:
    "Конец: end_875"

label end_875:
    "Конец: end_875"

label end_876:
    "Конец: end_876"

label end_877:
    "Конец: end_877"

label end_884:
    "Конец: end_884"

label end_884:
    "Конец: end_884"

label end_887:
    "Конец: end_887"

label end_887:
    "Конец: end_887"

label end_889:
    "Конец: end_889"

label end_890:
    "Конец: end_890"

label end_893:
    "Конец: end_893"

label end_893:
    "Конец: end_893"

label end_899:
    "Конец: end_899"

label end_899:
    "Конец: end_899"

label end_899:
    "Конец: end_899"

label end_903:
    "Конец: end_903"

label end_903:
    "Конец: end_903"

label end_903:
    "Конец: end_903"

label end_903:
    "Конец: end_903"

label end_907:
    "Конец: end_907"

label end_907:
    "Конец: end_907"

label end_907:
    "Конец: end_907"

label end_907:
    "Конец: end_907"

label end_913:
    "Конец: end_913"

label end_913:
    "Конец: end_913"

label end_917:
    "Конец: end_917"

label end_917:
    "Конец: end_917"

label end_917:
    "Конец: end_917"

label end_917:
    "Конец: end_917"

label end_918:
    "Конец: end_918"

label end_919:
    "Конец: end_919"

label end_922:
    "Конец: end_922"

label end_922:
    "Конец: end_922"

label end_922:
    "Конец: end_922"

label end_934:
    "Конец: end_934"

label end_934:
    "Конец: end_934"

label end_937:
    "Конец: end_937"

label end_937:
    "Конец: end_937"

label end_937:
    "Конец: end_937"

label end_940:
    "Конец: end_940"

label end_940:
    "Конец: end_940"

label end_940:
    "Конец: end_940"

label end_947:
    "Конец: end_947"

label end_947:
    "Конец: end_947"

label end_947:
    "Конец: end_947"

label end_950:
    "Конец: end_950"

label end_950:
    "Конец: end_950"

label end_950:
    "Конец: end_950"

label end_951:
    "Конец: end_951"

label end_952:
    "Конец: end_952"

label end_953:
    "Конец: end_953"

label end_954:
    "Конец: end_954"

label end_960:
    "Конец: end_960"

label end_960:
    "Конец: end_960"

label end_960:
    "Конец: end_960"

label end_960:
    "Конец: end_960"

label end_964:
    "Конец: end_964"

label end_964:
    "Конец: end_964"

label end_964:
    "Конец: end_964"

label end_964:
    "Конец: end_964"

label end_968:
    "Конец: end_968"

label end_969:
    "Конец: end_969"

label end_971:
    "Конец: end_971"

label end_971:
    "Конец: end_971"

label end_973:
    "Конец: end_973"

label end_973:
    "Конец: end_973"

label end_978:
    "Конец: end_978"

label end_978:
    "Конец: end_978"

label end_982:
    "Конец: end_982"

label end_982:
    "Конец: end_982"

label end_982:
    "Конец: end_982"

label end_985:
    "Конец: end_985"

label end_986:
    "Конец: end_986"

label end_991:
    "Конец: end_991"

label end_991:
    "Конец: end_991"

label end_991:
    "Конец: end_991"

label end_991:
    "Конец: end_991"

label end_1001:
    "Конец: end_1001"

label end_1001:
    "Конец: end_1001"

label end_1006:
    "Конец: end_1006"

label end_1006:
    "Конец: end_1006"

label end_1006:
    "Конец: end_1006"

label end_1006:
    "Конец: end_1006"

label end_1010:
    "Конец: end_1010"

label end_1011:
    "Конец: end_1011"

label end_1015:
    "Конец: end_1015"

label end_1015:
    "Конец: end_1015"

label end_1015:
    "Конец: end_1015"

label end_1015:
    "Конец: end_1015"

label end_1017:
    "Конец: end_1017"

label end_1017:
    "Конец: end_1017"

label end_1028:
    "Конец: end_1028"

label end_1028:
    "Конец: end_1028"

label end_1028:
    "Конец: end_1028"

label end_1028:
    "Конец: end_1028"

label end_1031:
    "Конец: end_1031"

label end_1031:
    "Конец: end_1031"

label end_1031:
    "Конец: end_1031"

label end_1034:
    "Конец: end_1034"

label end_1034:
    "Конец: end_1034"

label end_1034:
    "Конец: end_1034"

label end_1037:
    "Конец: end_1037"

label end_1037:
    "Конец: end_1037"

label end_1037:
    "Конец: end_1037"

label end_1045:
    "Конец: end_1045"

label end_1045:
    "Конец: end_1045"

label end_1045:
    "Конец: end_1045"

label end_1045:
    "Конец: end_1045"

label end_1047:
    "Конец: end_1047"

label end_1047:
    "Конец: end_1047"

label end_1051:
    "Конец: end_1051"

label end_1051:
    "Конец: end_1051"

label end_1051:
    "Конец: end_1051"

label end_1051:
    "Конец: end_1051"

label end_1054:
    "Конец: end_1054"

label end_1054:
    "Конец: end_1054"

label end_1054:
    "Конец: end_1054"

label end_1058:
    "Конец: end_1058"

label end_1058:
    "Конец: end_1058"

label end_1058:
    "Конец: end_1058"

label end_1060:
    "Конец: end_1060"

label end_1061:
    "Конец: end_1061"

label end_1071:
    "Конец: end_1071"

label end_1071:
    "Конец: end_1071"

label end_1072:
    "Конец: end_1072"

label end_1073:
    "Конец: end_1073"

label end_1074:
    "Конец: end_1074"

label end_1075:
    "Конец: end_1075"

label end_1076:
    "Конец: end_1076"

label end_1077:
    "Конец: end_1077"

label end_1083:
    "Конец: end_1083"

label end_1083:
    "Конец: end_1083"

label end_1086:
    "Конец: end_1086"

label end_1086:
    "Конец: end_1086"

label end_1086:
    "Конец: end_1086"

label end_1087:
    "Конец: end_1087"

label end_1088:
    "Конец: end_1088"

label end_1089:
    "Конец: end_1089"

label end_1090:
    "Конец: end_1090"

label end_1096:
    "Конец: end_1096"

label end_1096:
    "Конец: end_1096"

label end_1096:
    "Конец: end_1096"

label end_1096:
    "Конец: end_1096"

label end_1098:
    "Конец: end_1098"

label end_1098:
    "Конец: end_1098"

label end_1102:
    "Конец: end_1102"

label end_1102:
    "Конец: end_1102"

label end_1102:
    "Конец: end_1102"

label end_1107:
    "Конец: end_1107"

label end_1107:
    "Конец: end_1107"

label end_1107:
    "Конец: end_1107"

label end_1107:
    "Конец: end_1107"

label end_1112:
    "Конец: end_1112"

label end_1113:
    "Конец: end_1113"

label end_1117:
    "Конец: end_1117"

label end_1117:
    "Конец: end_1117"

label end_1117:
    "Конец: end_1117"

label end_1117:
    "Конец: end_1117"

label end_1124:
    "Конец: end_1124"

label end_1124:
    "Конец: end_1124"

label end_1124:
    "Конец: end_1124"

label end_1124:
    "Конец: end_1124"

label end_1128:
    "Конец: end_1128"

label end_1128:
    "Конец: end_1128"

label end_1128:
    "Конец: end_1128"

label end_1128:
    "Конец: end_1128"

label end_1130:
    "Конец: end_1130"

label end_1130:
    "Конец: end_1130"

label end_1143:
    "Конец: end_1143"

label end_1144:
    "Конец: end_1144"

label end_1146:
    "Конец: end_1146"

label end_1146:
    "Конец: end_1146"

label end_1150:
    "Конец: end_1150"

label end_1150:
    "Конец: end_1150"

label end_1150:
    "Конец: end_1150"

label end_1150:
    "Конец: end_1150"

label end_1152:
    "Конец: end_1152"

label end_1152:
    "Конец: end_1152"

label end_1157:
    "Конец: end_1157"

label end_1157:
    "Конец: end_1157"

label end_1157:
    "Конец: end_1157"

label end_1157:
    "Конец: end_1157"

label end_1159:
    "Конец: end_1159"

label end_1160:
    "Конец: end_1160"

label end_1167:
    "Конец: end_1167"

label end_1167:
    "Конец: end_1167"

label end_1167:
    "Конец: end_1167"

label end_1167:
    "Конец: end_1167"

label end_1170:
    "Конец: end_1170"

label end_1170:
    "Конец: end_1170"

label end_1177:
    "Конец: end_1177"

label end_1177:
    "Конец: end_1177"

label end_1177:
    "Конец: end_1177"

label end_1180:
    "Конец: end_1180"

label end_1180:
    "Конец: end_1180"

label end_1180:
    "Конец: end_1180"

label end_1181:
    "Конец: end_1181"

label end_1182:
    "Конец: end_1182"

label end_1183:
    "Конец: end_1183"

label end_1184:
    "Конец: end_1184"

label end_1192:
    "Конец: end_1192"

label end_1192:
    "Конец: end_1192"

label end_1193:
    "Конец: end_1193"

label end_1194:
    "Конец: end_1194"

label end_1197:
    "Конец: end_1197"

label end_1197:
    "Конец: end_1197"

label end_1197:
    "Конец: end_1197"

label end_1200:
    "Конец: end_1200"

label end_1200:
    "Конец: end_1200"

label end_1202:
    "Конец: end_1202"

label end_1203:
    "Конец: end_1203"

label end_1208:
    "Конец: end_1208"

label end_1208:
    "Конец: end_1208"

label end_1208:
    "Конец: end_1208"

label end_1208:
    "Конец: end_1208"

label end_1211:
    "Конец: end_1211"

label end_1211:
    "Конец: end_1211"

label end_1219:
    "Конец: end_1219"

label end_1219:
    "Конец: end_1219"

label end_1219:
    "Конец: end_1219"

label end_1219:
    "Конец: end_1219"

label end_1220:
    "Конец: end_1220"

label end_1221:
    "Конец: end_1221"

label end_1223:
    "Конец: end_1223"

label end_1223:
    "Конец: end_1223"

label end_1230:
    "Конец: end_1230"

label end_1230:
    "Конец: end_1230"

label end_1230:
    "Конец: end_1230"

label end_1230:
    "Конец: end_1230"

label end_1231:
    "Конец: end_1231"

label end_1232:
    "Конец: end_1232"

label end_1243:
    "Конец: end_1243"

label end_1244:
    "Конец: end_1244"

label end_1249:
    "Конец: end_1249"

label end_1249:
    "Конец: end_1249"

label end_1249:
    "Конец: end_1249"

label end_1249:
    "Конец: end_1249"

label end_1253:
    "Конец: end_1253"

label end_1253:
    "Конец: end_1253"

label end_1254:
    "Конец: end_1254"

label end_1255:
    "Конец: end_1255"

label end_1257:
    "Конец: end_1257"

label end_1258:
    "Конец: end_1258"

label end_1260:
    "Конец: end_1260"

label end_1261:
    "Конец: end_1261"

label end_1268:
    "Конец: end_1268"

label end_1268:
    "Конец: end_1268"

label end_1268:
    "Конец: end_1268"

label end_1268:
    "Конец: end_1268"

label end_1270:
    "Конец: end_1270"

label end_1270:
    "Конец: end_1270"

label end_1272:
    "Конец: end_1272"

label end_1272:
    "Конец: end_1272"

label end_1275:
    "Конец: end_1275"

label end_1276:
    "Конец: end_1276"

label end_1279:
    "Конец: end_1279"

label end_1279:
    "Конец: end_1279"

label end_1283:
    "Конец: end_1283"

label end_1284:
    "Конец: end_1284"

label end_1287:
    "Конец: end_1287"

label end_1287:
    "Конец: end_1287"

label end_1287:
    "Конец: end_1287"

label end_1295:
    "Конец: end_1295"

label end_1295:
    "Конец: end_1295"

label end_1295:
    "Конец: end_1295"

label end_1297:
    "Конец: end_1297"

label end_1297:
    "Конец: end_1297"

label end_1298:
    "Конец: end_1298"

label end_1299:
    "Конец: end_1299"

label end_1300:
    "Конец: end_1300"

label end_1301:
    "Конец: end_1301"

label end_1310:
    "Конец: end_1310"

label end_1310:
    "Конец: end_1310"

label end_1310:
    "Конец: end_1310"

label end_1310:
    "Конец: end_1310"

label end_1314:
    "Конец: end_1314"

label end_1314:
    "Конец: end_1314"

label end_1314:
    "Конец: end_1314"

label end_1314:
    "Конец: end_1314"

label end_1317:
    "Конец: end_1317"

label end_1317:
    "Конец: end_1317"

label end_1317:
    "Конец: end_1317"

label end_1321:
    "Конец: end_1321"

label end_1321:
    "Конец: end_1321"

label end_1321:
    "Конец: end_1321"

label end_1321:
    "Конец: end_1321"

label end_1326:
    "Конец: end_1326"

label end_1326:
    "Конец: end_1326"

label end_1327:
    "Конец: end_1327"

label end_1328:
    "Конец: end_1328"

label end_1333:
    "Конец: end_1333"

label end_1334:
    "Конец: end_1334"

label end_1335:
    "Конец: end_1335"

label end_1336:
    "Конец: end_1336"

label end_1338:
    "Конец: end_1338"

label end_1338:
    "Конец: end_1338"

label end_1355:
    "Конец: end_1355"

label end_1355:
    "Конец: end_1355"

label end_1355:
    "Конец: end_1355"

label end_1357:
    "Конец: end_1357"

label end_1358:
    "Конец: end_1358"

label end_1363:
    "Конец: end_1363"

label end_1363:
    "Конец: end_1363"

label end_1363:
    "Конец: end_1363"

label end_1364:
    "Конец: end_1364"

label end_1365:
    "Конец: end_1365"

label end_1372:
    "Конец: end_1372"

label end_1372:
    "Конец: end_1372"

label end_1372:
    "Конец: end_1372"

label end_1374:
    "Конец: end_1374"

label end_1374:
    "Конец: end_1374"

label end_1376:
    "Конец: end_1376"

label end_1376:
    "Конец: end_1376"

label end_1378:
    "Конец: end_1378"

label end_1378:
    "Конец: end_1378"

label end_1386:
    "Конец: end_1386"

label end_1386:
    "Конец: end_1386"

label end_1386:
    "Конец: end_1386"

label end_1387:
    "Конец: end_1387"

label end_1388:
    "Конец: end_1388"

label end_1392:
    "Конец: end_1392"

label end_1392:
    "Конец: end_1392"

label end_1392:
    "Конец: end_1392"

label end_1392:
    "Конец: end_1392"

label end_1395:
    "Конец: end_1395"

label end_1396:
    "Конец: end_1396"

label end_1399:
    "Конец: end_1399"

label end_1399:
    "Конец: end_1399"

label end_1399:
    "Конец: end_1399"

label end_1407:
    "Конец: end_1407"

label end_1407:
    "Конец: end_1407"

label end_1407:
    "Конец: end_1407"

label end_1407:
    "Конец: end_1407"

label end_1410:
    "Конец: end_1410"

label end_1410:
    "Конец: end_1410"

label end_1410:
    "Конец: end_1410"

label end_1414:
    "Конец: end_1414"

label end_1414:
    "Конец: end_1414"

label end_1414:
    "Конец: end_1414"

label end_1414:
    "Конец: end_1414"

label end_1420:
    "Конец: end_1420"

label end_1420:
    "Конец: end_1420"

label end_1422:
    "Конец: end_1422"

label end_1422:
    "Конец: end_1422"

label end_1424:
    "Конец: end_1424"

label end_1424:
    "Конец: end_1424"

label end_1430:
    "Конец: end_1430"

label end_1431:
    "Конец: end_1431"

label end_1432:
    "Конец: end_1432"

label end_1433:
    "Конец: end_1433"

label end_1439:
    "Конец: end_1439"

label end_1439:
    "Конец: end_1439"

label end_1439:
    "Конец: end_1439"

label end_1441:
    "Конец: end_1441"

label end_1441:
    "Конец: end_1441"

label end_1443:
    "Конец: end_1443"

label end_1443:
    "Конец: end_1443"

label end_1449:
    "Конец: end_1449"

label end_1449:
    "Конец: end_1449"

label end_1449:
    "Конец: end_1449"

label end_1449:
    "Конец: end_1449"

label end_1452:
    "Конец: end_1452"

label end_1452:
    "Конец: end_1452"

label end_1452:
    "Конец: end_1452"

label end_1464:
    "Конец: end_1464"

label end_1464:
    "Конец: end_1464"

label end_1464:
    "Конец: end_1464"

label end_1464:
    "Конец: end_1464"

label end_1467:
    "Конец: end_1467"

label end_1467:
    "Конец: end_1467"

label end_1469:
    "Конец: end_1469"

label end_1470:
    "Конец: end_1470"

label end_1475:
    "Конец: end_1475"

label end_1475:
    "Конец: end_1475"

label end_1475:
    "Конец: end_1475"

label end_1475:
    "Конец: end_1475"

label end_1478:
    "Конец: end_1478"

label end_1479:
    "Конец: end_1479"

label end_1480:
    "Конец: end_1480"

label end_1481:
    "Конец: end_1481"

label end_1487:
    "Конец: end_1487"

label end_1488:
    "Конец: end_1488"

label end_1492:
    "Конец: end_1492"

label end_1492:
    "Конец: end_1492"

label end_1492:
    "Конец: end_1492"

label end_1492:
    "Конец: end_1492"

label end_1496:
    "Конец: end_1496"

label end_1496:
    "Конец: end_1496"

label end_1498:
    "Конец: end_1498"

label end_1498:
    "Конец: end_1498"

label end_1504:
    "Конец: end_1504"

label end_1504:
    "Конец: end_1504"

label end_1504:
    "Конец: end_1504"

label end_1505:
    "Конец: end_1505"

label end_1506:
    "Конец: end_1506"

label end_1509:
    "Конец: end_1509"

label end_1509:
    "Конец: end_1509"

label end_1509:
    "Конец: end_1509"

label end_1515:
    "Конец: end_1515"

label end_1515:
    "Конец: end_1515"

label end_1518:
    "Конец: end_1518"

label end_1518:
    "Конец: end_1518"

label end_1518:
    "Конец: end_1518"

label end_1522:
    "Конец: end_1522"

label end_1522:
    "Конец: end_1522"

label end_1525:
    "Конец: end_1525"

label end_1525:
    "Конец: end_1525"

label end_1525:
    "Конец: end_1525"

label end_1533:
    "Конец: end_1533"

label end_1533:
    "Конец: end_1533"

label end_1533:
    "Конец: end_1533"

label end_1535:
    "Конец: end_1535"

label end_1536:
    "Конец: end_1536"

label end_1539:
    "Конец: end_1539"

label end_1539:
    "Конец: end_1539"

label end_1541:
    "Конец: end_1541"

label end_1542:
    "Конец: end_1542"

label end_1548:
    "Конец: end_1548"

label end_1548:
    "Конец: end_1548"

label end_1548:
    "Конец: end_1548"

label end_1552:
    "Конец: end_1552"

label end_1552:
    "Конец: end_1552"

label end_1552:
    "Конец: end_1552"

label end_1552:
    "Конец: end_1552"

label end_1553:
    "Конец: end_1553"

label end_1554:
    "Конец: end_1554"

label end_1561:
    "Конец: end_1561"

label end_1561:
    "Конец: end_1561"

label end_1561:
    "Конец: end_1561"

label end_1561:
    "Конец: end_1561"

label end_1562:
    "Конец: end_1562"

label end_1563:
    "Конец: end_1563"

label end_1565:
    "Конец: end_1565"

label end_1565:
    "Конец: end_1565"

label end_1572:
    "Конец: end_1572"

label end_1572:
    "Конец: end_1572"

label end_1575:
    "Конец: end_1575"

label end_1575:
    "Конец: end_1575"

label end_1582:
    "Конец: end_1582"

label end_1582:
    "Конец: end_1582"

label end_1582:
    "Конец: end_1582"

label end_1582:
    "Конец: end_1582"

label end_1583:
    "Конец: end_1583"

label end_1584:
    "Конец: end_1584"

label end_1588:
    "Конец: end_1588"

label end_1588:
    "Конец: end_1588"

label end_1590:
    "Конец: end_1590"

label end_1591:
    "Конец: end_1591"

label end_1595:
    "Конец: end_1595"

label end_1595:
    "Конец: end_1595"

label end_1597:
    "Конец: end_1597"

label end_1598:
    "Конец: end_1598"

label end_1603:
    "Конец: end_1603"

label end_1604:
    "Конец: end_1604"

label end_1605:
    "Конец: end_1605"

label end_1606:
    "Конец: end_1606"

label end_1610:
    "Конец: end_1610"

label end_1610:
    "Конец: end_1610"

label end_1610:
    "Конец: end_1610"

label end_1610:
    "Конец: end_1610"

label end_1619:
    "Конец: end_1619"

label end_1619:
    "Конец: end_1619"

label end_1619:
    "Конец: end_1619"

label end_1619:
    "Конец: end_1619"

label end_1621:
    "Конец: end_1621"

label end_1621:
    "Конец: end_1621"

label end_1623:
    "Конец: end_1623"

label end_1623:
    "Конец: end_1623"

label end_1625:
    "Конец: end_1625"

label end_1625:
    "Конец: end_1625"

label end_1636:
    "Конец: end_1636"

label end_1637:
    "Конец: end_1637"

label end_1640:
    "Конец: end_1640"

label end_1640:
    "Конец: end_1640"

label end_1640:
    "Конец: end_1640"

label end_1644:
    "Конец: end_1644"

label end_1644:
    "Конец: end_1644"

label end_1644:
    "Конец: end_1644"

label end_1644:
    "Конец: end_1644"

label end_1645:
    "Конец: end_1645"

label end_1646:
    "Конец: end_1646"

label end_1650:
    "Конец: end_1650"

label end_1651:
    "Конец: end_1651"

label end_1655:
    "Конец: end_1655"

label end_1655:
    "Конец: end_1655"

label end_1655:
    "Конец: end_1655"

label end_1655:
    "Конец: end_1655"

label end_1659:
    "Конец: end_1659"

label end_1659:
    "Конец: end_1659"

label end_1659:
    "Конец: end_1659"

label end_1659:
    "Конец: end_1659"

label end_1662:
    "Конец: end_1662"

label end_1662:
    "Конец: end_1662"

label end_1665:
    "Конец: end_1665"

label end_1665:
    "Конец: end_1665"

label end_1670:
    "Конец: end_1670"

label end_1671:
    "Конец: end_1671"

label end_1673:
    "Конец: end_1673"

label end_1673:
    "Конец: end_1673"

label end_1678:
    "Конец: end_1678"

label end_1678:
    "Конец: end_1678"

label end_1679:
    "Конец: end_1679"

label end_1680:
    "Конец: end_1680"

label end_1682:
    "Конец: end_1682"

label end_1682:
    "Конец: end_1682"

label end_1688:
    "Конец: end_1688"

label end_1689:
    "Конец: end_1689"

label end_1693:
    "Конец: end_1693"

label end_1693:
    "Конец: end_1693"

label end_1693:
    "Конец: end_1693"

label end_1693:
    "Конец: end_1693"

label end_1695:
    "Конец: end_1695"

label end_1695:
    "Конец: end_1695"

label end_1696:
    "Конец: end_1696"

label end_1697:
    "Конец: end_1697"

label end_1700:
    "Конец: end_1700"

label end_1701:
    "Конец: end_1701"

label end_1704:
    "Конец: end_1704"

label end_1704:
    "Конец: end_1704"

label end_1715:
    "Конец: end_1715"

label end_1715:
    "Конец: end_1715"

label end_1715:
    "Конец: end_1715"

label end_1716:
    "Конец: end_1716"

label end_1717:
    "Конец: end_1717"

label end_1723:
    "Конец: end_1723"

label end_1723:
    "Конец: end_1723"

label end_1723:
    "Конец: end_1723"

label end_1723:
    "Конец: end_1723"

label end_1728:
    "Конец: end_1728"

label end_1728:
    "Конец: end_1728"

label end_1728:
    "Конец: end_1728"

label end_1728:
    "Конец: end_1728"

label end_1734:
    "Конец: end_1734"

label end_1735:
    "Конец: end_1735"

label end_1739:
    "Конец: end_1739"

label end_1739:
    "Конец: end_1739"

label end_1739:
    "Конец: end_1739"

label end_1739:
    "Конец: end_1739"

label end_1743:
    "Конец: end_1743"

label end_1743:
    "Конец: end_1743"

label end_1743:
    "Конец: end_1743"

label end_1746:
    "Конец: end_1746"

label end_1746:
    "Конец: end_1746"

label end_1753:
    "Конец: end_1753"

label end_1753:
    "Конец: end_1753"

label end_1753:
    "Конец: end_1753"

label end_1754:
    "Конец: end_1754"

label end_1755:
    "Конец: end_1755"

label end_1758:
    "Конец: end_1758"

label end_1758:
    "Конец: end_1758"

label end_1758:
    "Конец: end_1758"

label end_1760:
    "Конец: end_1760"

label end_1760:
    "Конец: end_1760"

label end_1770:
    "Конец: end_1770"

label end_1770:
    "Конец: end_1770"

label end_1770:
    "Конец: end_1770"

label end_1770:
    "Конец: end_1770"

label end_1773:
    "Конец: end_1773"

label end_1773:
    "Конец: end_1773"

label end_1773:
    "Конец: end_1773"

label end_1776:
    "Конец: end_1776"

label end_1776:
    "Конец: end_1776"

label end_1776:
    "Конец: end_1776"

label end_1780:
    "Конец: end_1780"

label end_1780:
    "Конец: end_1780"

label end_1780:
    "Конец: end_1780"

label end_1780:
    "Конец: end_1780"

label end_1787:
    "Конец: end_1787"

label end_1787:
    "Конец: end_1787"

label end_1787:
    "Конец: end_1787"

label end_1787:
    "Конец: end_1787"

label end_1788:
    "Конец: end_1788"

label end_1789:
    "Конец: end_1789"

label end_1791:
    "Конец: end_1791"

label end_1791:
    "Конец: end_1791"

label end_1799:
    "Конец: end_1799"

label end_1800:
    "Конец: end_1800"

label end_1803:
    "Конец: end_1803"

label end_1803:
    "Конец: end_1803"

label end_1803:
    "Конец: end_1803"

label end_1804:
    "Конец: end_1804"

label end_1805:
    "Конец: end_1805"

label end_1809:
    "Конец: end_1809"

label end_1809:
    "Конец: end_1809"

label end_1809:
    "Конец: end_1809"

label end_1812:
    "Конец: end_1812"

label end_1812:
    "Конец: end_1812"

label end_1815:
    "Конец: end_1815"

label end_1815:
    "Конец: end_1815"

label end_1819:
    "Конец: end_1819"

label end_1819:
    "Конец: end_1819"

label end_1819:
    "Конец: end_1819"

label end_1824:
    "Конец: end_1824"

label end_1824:
    "Конец: end_1824"

label end_1824:
    "Конец: end_1824"

label end_1827:
    "Конец: end_1827"

label end_1827:
    "Конец: end_1827"

label end_1827:
    "Конец: end_1827"

label end_1838:
    "Конец: end_1838"

label end_1838:
    "Конец: end_1838"

label end_1840:
    "Конец: end_1840"

label end_1840:
    "Конец: end_1840"

label end_1843:
    "Конец: end_1843"

label end_1843:
    "Конец: end_1843"

label end_1843:
    "Конец: end_1843"

label end_1850:
    "Конец: end_1850"

label end_1850:
    "Конец: end_1850"

label end_1850:
    "Конец: end_1850"

label end_1853:
    "Конец: end_1853"

label end_1853:
    "Конец: end_1853"

label end_1853:
    "Конец: end_1853"

label end_1854:
    "Конец: end_1854"

label end_1855:
    "Конец: end_1855"

label end_1863:
    "Конец: end_1863"

label end_1863:
    "Конец: end_1863"

label end_1866:
    "Конец: end_1866"

label end_1866:
    "Конец: end_1866"

label end_1866:
    "Конец: end_1866"

label end_1873:
    "Конец: end_1873"

label end_1873:
    "Конец: end_1873"

label end_1873:
    "Конец: end_1873"

label end_1873:
    "Конец: end_1873"

label end_1877:
    "Конец: end_1877"

label end_1877:
    "Конец: end_1877"

label end_1877:
    "Конец: end_1877"

label end_1877:
    "Конец: end_1877"

label end_1881:
    "Конец: end_1881"

label end_1881:
    "Конец: end_1881"

label end_1881:
    "Конец: end_1881"

label end_1881:
    "Конец: end_1881"

label end_1884:
    "Конец: end_1884"

label end_1885:
    "Конец: end_1885"

label end_1889:
    "Конец: end_1889"

label end_1889:
    "Конец: end_1889"

label end_1889:
    "Конец: end_1889"

label end_1889:
    "Конец: end_1889"

label end_1893:
    "Конец: end_1893"

label end_1893:
    "Конец: end_1893"

label end_1893:
    "Конец: end_1893"

label end_1898:
    "Конец: end_1898"

label end_1898:
    "Конец: end_1898"

label end_1898:
    "Конец: end_1898"

label end_1898:
    "Конец: end_1898"

label end_1907:
    "Конец: end_1907"

label end_1907:
    "Конец: end_1907"

label end_1907:
    "Конец: end_1907"

label end_1909:
    "Конец: end_1909"

label end_1909:
    "Конец: end_1909"

label end_1916:
    "Конец: end_1916"

label end_1916:
    "Конец: end_1916"

label end_1916:
    "Конец: end_1916"

label end_1919:
    "Конец: end_1919"

label end_1919:
    "Конец: end_1919"

label end_1919:
    "Конец: end_1919"

label end_1920:
    "Конец: end_1920"

label end_1921:
    "Конец: end_1921"

label end_1924:
    "Конец: end_1924"

label end_1924:
    "Конец: end_1924"

label end_1924:
    "Конец: end_1924"

label end_1927:
    "Конец: end_1927"

label end_1927:
    "Конец: end_1927"

label end_1930:
    "Конец: end_1930"

label end_1930:
    "Конец: end_1930"

label end_1938:
    "Конец: end_1938"

label end_1938:
    "Конец: end_1938"

label end_1938:
    "Конец: end_1938"

label end_1938:
    "Конец: end_1938"

label end_1942:
    "Конец: end_1942"

label end_1942:
    "Конец: end_1942"

label end_1942:
    "Конец: end_1942"

label end_1942:
    "Конец: end_1942"

label end_1944:
    "Конец: end_1944"

label end_1944:
    "Конец: end_1944"

label end_1945:
    "Конец: end_1945"

label end_1946:
    "Конец: end_1946"

label end_1952:
    "Конец: end_1952"

label end_1952:
    "Конец: end_1952"

label end_1952:
    "Конец: end_1952"

label end_1954:
    "Конец: end_1954"

label end_1954:
    "Конец: end_1954"

label end_1960:
    "Конец: end_1960"

label end_1961:
    "Конец: end_1961"

label end_1964:
    "Конец: end_1964"

label end_1964:
    "Конец: end_1964"

label end_1964:
    "Конец: end_1964"

label end_1967:
    "Конец: end_1967"

label end_1967:
    "Конец: end_1967"

label end_1967:
    "Конец: end_1967"

label end_1970:
    "Конец: end_1970"

label end_1970:
    "Конец: end_1970"

label end_1970:
    "Конец: end_1970"

label end_1982:
    "Конец: end_1982"

label end_1983:
    "Конец: end_1983"

label end_1988:
    "Конец: end_1988"

label end_1988:
    "Конец: end_1988"

label end_1988:
    "Конец: end_1988"

label end_1988:
    "Конец: end_1988"

label end_1993:
    "Конец: end_1993"

label end_1994:
    "Конец: end_1994"

label end_1995:
    "Конец: end_1995"

label end_1996:
    "Конец: end_1996"

label end_1997:
    "Конец: end_1997"

label end_1998:
    "Конец: end_1998"

label end_2003:
    "Конец: end_2003"

label end_2004:
    "Конец: end_2004"

label end_2006:
    "Конец: end_2006"

label end_2007:
    "Конец: end_2007"

label end_2014:
    "Конец: end_2014"

label end_2014:
    "Конец: end_2014"

label end_2014:
    "Конец: end_2014"

label end_2014:
    "Конец: end_2014"

label end_2017:
    "Конец: end_2017"

label end_2017:
    "Конец: end_2017"

label end_2017:
    "Конец: end_2017"

label end_2020:
    "Конец: end_2020"

label end_2020:
    "Конец: end_2020"

label end_2020:
    "Конец: end_2020"

label end_2026:
    "Конец: end_2026"

label end_2026:
    "Конец: end_2026"

label end_2030:
    "Конец: end_2030"

label end_2030:
    "Конец: end_2030"

label end_2030:
    "Конец: end_2030"

label end_2030:
    "Конец: end_2030"

label end_2031:
    "Конец: end_2031"

label end_2032:
    "Конец: end_2032"

label end_2035:
    "Конец: end_2035"

label end_2035:
    "Конец: end_2035"

label end_2035:
    "Конец: end_2035"

label end_2045:
    "Конец: end_2045"

label end_2045:
    "Конец: end_2045"

label end_2045:
    "Конец: end_2045"

label end_2047:
    "Конец: end_2047"

label end_2047:
    "Конец: end_2047"

label end_2051:
    "Конец: end_2051"

label end_2051:
    "Конец: end_2051"

label end_2051:
    "Конец: end_2051"

label end_2051:
    "Конец: end_2051"

label end_2054:
    "Конец: end_2054"

label end_2054:
    "Конец: end_2054"

label end_2054:
    "Конец: end_2054"

label end_2059:
    "Конец: end_2059"

label end_2059:
    "Конец: end_2059"

label end_2059:
    "Конец: end_2059"

label end_2059:
    "Конец: end_2059"

label end_2062:
    "Конец: end_2062"

label end_2062:
    "Конец: end_2062"

label end_2067:
    "Конец: end_2067"

label end_2067:
    "Конец: end_2067"

label end_2069:
    "Конец: end_2069"

label end_2069:
    "Конец: end_2069"

label end_2071:
    "Конец: end_2071"

label end_2071:
    "Конец: end_2071"

label end_2080:
    "Конец: end_2080"

label end_2080:
    "Конец: end_2080"

label end_2080:
    "Конец: end_2080"

label end_2080:
    "Конец: end_2080"

label end_2082:
    "Конец: end_2082"

label end_2083:
    "Конец: end_2083"

label end_2091:
    "Конец: end_2091"

label end_2091:
    "Конец: end_2091"

label end_2091:
    "Конец: end_2091"

label end_2091:
    "Конец: end_2091"

label end_2093:
    "Конец: end_2093"

label end_2093:
    "Конец: end_2093"

label end_2097:
    "Конец: end_2097"

label end_2097:
    "Конец: end_2097"

label end_2097:
    "Конец: end_2097"

label end_2097:
    "Конец: end_2097"

label end_2101:
    "Конец: end_2101"

label end_2101:
    "Конец: end_2101"

label end_2101:
    "Конец: end_2101"

label end_2101:
    "Конец: end_2101"

label end_2105:
    "Конец: end_2105"

label end_2106:
    "Конец: end_2106"

label end_2110:
    "Конец: end_2110"

label end_2110:
    "Конец: end_2110"

label end_2110:
    "Конец: end_2110"

label end_2110:
    "Конец: end_2110"

label end_2114:
    "Конец: end_2114"

label end_2114:
    "Конец: end_2114"

label end_2114:
    "Конец: end_2114"

label end_2114:
    "Конец: end_2114"

label end_2118:
    "Конец: end_2118"

label end_2119:
    "Конец: end_2119"

label end_2120:
    "Конец: end_2120"

label end_2121:
    "Конец: end_2121"

label end_2122:
    "Конец: end_2122"

label end_2123:
    "Конец: end_2123"

label end_2132:
    "Конец: end_2132"

label end_2133:
    "Конец: end_2133"

label end_2134:
    "Конец: end_2134"

label end_2135:
    "Конец: end_2135"

label end_2136:
    "Конец: end_2136"

label end_2137:
    "Конец: end_2137"

label end_2140:
    "Конец: end_2140"

label end_2140:
    "Конец: end_2140"

label end_2144:
    "Конец: end_2144"

label end_2144:
    "Конец: end_2144"

label end_2144:
    "Конец: end_2144"

label end_2149:
    "Конец: end_2149"

label end_2149:
    "Конец: end_2149"

label end_2149:
    "Конец: end_2149"

label end_2149:
    "Конец: end_2149"

label end_2151:
    "Конец: end_2151"

label end_2152:
    "Конец: end_2152"

label end_2157:
    "Конец: end_2157"

label end_2157:
    "Конец: end_2157"

label end_2157:
    "Конец: end_2157"

label end_2157:
    "Конец: end_2157"

label end_2161:
    "Конец: end_2161"

label end_2161:
    "Конец: end_2161"

label end_2161:
    "Конец: end_2161"

label end_2167:
    "Конец: end_2167"

label end_2168:
    "Конец: end_2168"

label end_2169:
    "Конец: end_2169"

label end_2170:
    "Конец: end_2170"

label end_2172:
    "Конец: end_2172"

label end_2172:
    "Конец: end_2172"

label end_2178:
    "Конец: end_2178"

label end_2178:
    "Конец: end_2178"

label end_2178:
    "Конец: end_2178"

label end_2178:
    "Конец: end_2178"

label end_2182:
    "Конец: end_2182"

label end_2182:
    "Конец: end_2182"

label end_2182:
    "Конец: end_2182"

label end_2195:
    "Конец: end_2195"

label end_2195:
    "Конец: end_2195"

label end_2195:
    "Конец: end_2195"

label end_2195:
    "Конец: end_2195"

label end_2198:
    "Конец: end_2198"

label end_2198:
    "Конец: end_2198"

label end_2203:
    "Конец: end_2203"

label end_2203:
    "Конец: end_2203"

label end_2203:
    "Конец: end_2203"

label end_2205:
    "Конец: end_2205"

label end_2205:
    "Конец: end_2205"

label end_2210:
    "Конец: end_2210"

label end_2211:
    "Конец: end_2211"

label end_2212:
    "Конец: end_2212"

label end_2213:
    "Конец: end_2213"

label end_2216:
    "Конец: end_2216"

label end_2216:
    "Конец: end_2216"

label end_2216:
    "Конец: end_2216"

label end_2220:
    "Конец: end_2220"

label end_2220:
    "Конец: end_2220"

label end_2220:
    "Конец: end_2220"

label end_2220:
    "Конец: end_2220"

label end_2227:
    "Конец: end_2227"

label end_2227:
    "Конец: end_2227"

label end_2227:
    "Конец: end_2227"

label end_2229:
    "Конец: end_2229"

label end_2229:
    "Конец: end_2229"

label end_2233:
    "Конец: end_2233"

label end_2233:
    "Конец: end_2233"

label end_2233:
    "Конец: end_2233"

label end_2238:
    "Конец: end_2238"

label end_2238:
    "Конец: end_2238"

label end_2238:
    "Конец: end_2238"

label end_2238:
    "Конец: end_2238"

label end_2245:
    "Конец: end_2245"

label end_2245:
    "Конец: end_2245"

label end_2245:
    "Конец: end_2245"

label end_2249:
    "Конец: end_2249"

label end_2249:
    "Конец: end_2249"

label end_2249:
    "Конец: end_2249"

label end_2249:
    "Конец: end_2249"

label end_2251:
    "Конец: end_2251"

label end_2251:
    "Конец: end_2251"

label end_2256:
    "Конец: end_2256"

label end_2256:
    "Конец: end_2256"

label end_2256:
    "Конец: end_2256"

label end_2259:
    "Конец: end_2259"

label end_2259:
    "Конец: end_2259"

label end_2268:
    "Конец: end_2268"

label end_2268:
    "Конец: end_2268"

label end_2268:
    "Конец: end_2268"

label end_2268:
    "Конец: end_2268"

label end_2270:
    "Конец: end_2270"

label end_2270:
    "Конец: end_2270"

label end_2272:
    "Конец: end_2272"

label end_2272:
    "Конец: end_2272"

label end_2280:
    "Конец: end_2280"

label end_2280:
    "Конец: end_2280"

label end_2280:
    "Конец: end_2280"

label end_2280:
    "Конец: end_2280"

label end_2284:
    "Конец: end_2284"

label end_2284:
    "Конец: end_2284"

label end_2284:
    "Конец: end_2284"

label end_2284:
    "Конец: end_2284"

label end_2285:
    "Конец: end_2285"

label end_2286:
    "Конец: end_2286"

label end_2287:
    "Конец: end_2287"

label end_2288:
    "Конец: end_2288"

label end_2299:
    "Конец: end_2299"

label end_2300:
    "Конец: end_2300"

label end_2304:
    "Конец: end_2304"

label end_2304:
    "Конец: end_2304"

label end_2304:
    "Конец: end_2304"

label end_2304:
    "Конец: end_2304"

label end_2305:
    "Конец: end_2305"

label end_2306:
    "Конец: end_2306"

label end_2308:
    "Конец: end_2308"

label end_2308:
    "Конец: end_2308"

label end_2314:
    "Конец: end_2314"

label end_2315:
    "Конец: end_2315"

label end_2319:
    "Конец: end_2319"

label end_2319:
    "Конец: end_2319"

label end_2319:
    "Конец: end_2319"

label end_2319:
    "Конец: end_2319"

label end_2322:
    "Конец: end_2322"

label end_2322:
    "Конец: end_2322"

label end_2322:
    "Конец: end_2322"

label end_2326:
    "Конец: end_2326"

label end_2326:
    "Конец: end_2326"

label end_2326:
    "Конец: end_2326"

label end_2326:
    "Конец: end_2326"

label end_2333:
    "Конец: end_2333"

label end_2333:
    "Конец: end_2333"

label end_2333:
    "Конец: end_2333"

label end_2333:
    "Конец: end_2333"

label end_2336:
    "Конец: end_2336"

label end_2336:
    "Конец: end_2336"

label end_2341:
    "Конец: end_2341"

label end_2341:
    "Конец: end_2341"

label end_2341:
    "Конец: end_2341"

label end_2342:
    "Конец: end_2342"

label end_2343:
    "Конец: end_2343"

label end_2350:
    "Конец: end_2350"

label end_2350:
    "Конец: end_2350"

label end_2354:
    "Конец: end_2354"

label end_2354:
    "Конец: end_2354"

label end_2354:
    "Конец: end_2354"

label end_2356:
    "Конец: end_2356"

label end_2357:
    "Конец: end_2357"

label end_2361:
    "Конец: end_2361"

label end_2361:
    "Конец: end_2361"

label end_2361:
    "Конец: end_2361"

label end_2368:
    "Конец: end_2368"

label end_2368:
    "Конец: end_2368"

label end_2368:
    "Конец: end_2368"

label end_2371:
    "Конец: end_2371"

label end_2371:
    "Конец: end_2371"

label end_2371:
    "Конец: end_2371"

label end_2374:
    "Конец: end_2374"

label end_2374:
    "Конец: end_2374"

label end_2374:
    "Конец: end_2374"

label end_2376:
    "Конец: end_2376"

label end_2376:
    "Конец: end_2376"

label end_2381:
    "Конец: end_2381"

label end_2381:
    "Конец: end_2381"

label end_2382:
    "Конец: end_2382"

label end_2383:
    "Конец: end_2383"

label end_2387:
    "Конец: end_2387"

label end_2387:
    "Конец: end_2387"

label end_2387:
    "Конец: end_2387"

label end_2387:
    "Конец: end_2387"

label end_2393:
    "Конец: end_2393"

label end_2393:
    "Конец: end_2393"

label end_2393:
    "Конец: end_2393"

label end_2393:
    "Конец: end_2393"

label end_2395:
    "Конец: end_2395"

label end_2396:
    "Конец: end_2396"

label end_2405:
    "Конец: end_2405"

label end_2405:
    "Конец: end_2405"

label end_2405:
    "Конец: end_2405"

label end_2405:
    "Конец: end_2405"

label end_2406:
    "Конец: end_2406"

label end_2407:
    "Конец: end_2407"

label end_2411:
    "Конец: end_2411"

label end_2411:
    "Конец: end_2411"

label end_2411:
    "Конец: end_2411"

label end_2411:
    "Конец: end_2411"

label end_2413:
    "Конец: end_2413"

label end_2413:
    "Конец: end_2413"

label end_2428:
    "Конец: end_2428"

label end_2429:
    "Конец: end_2429"

label end_2430:
    "Конец: end_2430"

label end_2431:
    "Конец: end_2431"

label end_2434:
    "Конец: end_2434"

label end_2434:
    "Конец: end_2434"

label end_2434:
    "Конец: end_2434"

label end_2436:
    "Конец: end_2436"

label end_2436:
    "Конец: end_2436"

label end_2444:
    "Конец: end_2444"

label end_2444:
    "Конец: end_2444"

label end_2444:
    "Конец: end_2444"

label end_2444:
    "Конец: end_2444"

label end_2446:
    "Конец: end_2446"

label end_2446:
    "Конец: end_2446"

label end_2449:
    "Конец: end_2449"

label end_2449:
    "Конец: end_2449"

label end_2449:
    "Конец: end_2449"

label end_2453:
    "Конец: end_2453"

label end_2453:
    "Конец: end_2453"

label end_2453:
    "Конец: end_2453"

label end_2453:
    "Конец: end_2453"

label end_2458:
    "Конец: end_2458"

label end_2459:
    "Конец: end_2459"

label end_2463:
    "Конец: end_2463"

label end_2463:
    "Конец: end_2463"

label end_2463:
    "Конец: end_2463"

label end_2463:
    "Конец: end_2463"

label end_2465:
    "Конец: end_2465"

label end_2465:
    "Конец: end_2465"

label end_2471:
    "Конец: end_2471"

label end_2471:
    "Конец: end_2471"

label end_2471:
    "Конец: end_2471"

label end_2471:
    "Конец: end_2471"

label end_2473:
    "Конец: end_2473"

label end_2474:
    "Конец: end_2474"

label end_2477:
    "Конец: end_2477"

label end_2478:
    "Конец: end_2478"

label end_2481:
    "Конец: end_2481"

label end_2481:
    "Конец: end_2481"

label end_2484:
    "Конец: end_2484"

label end_2485:
    "Конец: end_2485"

label end_2487:
    "Конец: end_2487"

label end_2488:
    "Конец: end_2488"

label end_2502:
    "Конец: end_2502"

label end_2502:
    "Конец: end_2502"

label end_2502:
    "Конец: end_2502"

label end_2505:
    "Конец: end_2505"

label end_2505:
    "Конец: end_2505"

label end_2505:
    "Конец: end_2505"

label end_2507:
    "Конец: end_2507"

label end_2507:
    "Конец: end_2507"

label end_2510:
    "Конец: end_2510"

label end_2511:
    "Конец: end_2511"

label end_2512:
    "Конец: end_2512"

label end_2513:
    "Конец: end_2513"

label end_2517:
    "Конец: end_2517"

label end_2517:
    "Конец: end_2517"

label end_2517:
    "Конец: end_2517"

label end_2519:
    "Конец: end_2519"

label end_2520:
    "Конец: end_2520"

label end_2528:
    "Конец: end_2528"

label end_2528:
    "Конец: end_2528"

label end_2529:
    "Конец: end_2529"

label end_2530:
    "Конец: end_2530"

label end_2533:
    "Конец: end_2533"

label end_2533:
    "Конец: end_2533"

label end_2533:
    "Конец: end_2533"

label end_2537:
    "Конец: end_2537"

label end_2537:
    "Конец: end_2537"

label end_2537:
    "Конец: end_2537"

label end_2537:
    "Конец: end_2537"

label end_2540:
    "Конец: end_2540"

label end_2540:
    "Конец: end_2540"

label end_2543:
    "Конец: end_2543"

label end_2543:
    "Конец: end_2543"

label end_2550:
    "Конец: end_2550"

label end_2550:
    "Конец: end_2550"

label end_2550:
    "Конец: end_2550"

label end_2553:
    "Конец: end_2553"

label end_2553:
    "Конец: end_2553"

label end_2553:
    "Конец: end_2553"

label end_2557:
    "Конец: end_2557"

label end_2557:
    "Конец: end_2557"

label end_2557:
    "Конец: end_2557"

label end_2557:
    "Конец: end_2557"

label end_2562:
    "Конец: end_2562"

label end_2562:
    "Конец: end_2562"

label end_2565:
    "Конец: end_2565"

label end_2565:
    "Конец: end_2565"

label end_2565:
    "Конец: end_2565"

label end_2575:
    "Конец: end_2575"

label end_2575:
    "Конец: end_2575"

label end_2575:
    "Конец: end_2575"

label end_2575:
    "Конец: end_2575"

label end_2576:
    "Конец: end_2576"

label end_2577:
    "Конец: end_2577"

label end_2578:
    "Конец: end_2578"

label end_2579:
    "Конец: end_2579"

label end_2580:
    "Конец: end_2580"

label end_2581:
    "Конец: end_2581"

label end_2589:
    "Конец: end_2589"

label end_2589:
    "Конец: end_2589"

label end_2589:
    "Конец: end_2589"

label end_2589:
    "Конец: end_2589"

label end_2590:
    "Конец: end_2590"

label end_2591:
    "Конец: end_2591"

label end_2594:
    "Конец: end_2594"

label end_2594:
    "Конец: end_2594"

label end_2594:
    "Конец: end_2594"

label end_2598:
    "Конец: end_2598"

label end_2598:
    "Конец: end_2598"

label end_2598:
    "Конец: end_2598"

label end_2598:
    "Конец: end_2598"

label end_2610:
    "Конец: end_2610"

label end_2611:
    "Конец: end_2611"

label end_2612:
    "Конец: end_2612"

label end_2613:
    "Конец: end_2613"

label end_2617:
    "Конец: end_2617"

label end_2617:
    "Конец: end_2617"

label end_2617:
    "Конец: end_2617"

label end_2617:
    "Конец: end_2617"

label end_2618:
    "Конец: end_2618"

label end_2619:
    "Конец: end_2619"

label end_2624:
    "Конец: end_2624"

label end_2625:
    "Конец: end_2625"

label end_2627:
    "Конец: end_2627"

label end_2627:
    "Конец: end_2627"

label end_2628:
    "Конец: end_2628"

label end_2629:
    "Конец: end_2629"

label end_2634:
    "Конец: end_2634"

label end_2634:
    "Конец: end_2634"

label end_2634:
    "Конец: end_2634"

label end_2636:
    "Конец: end_2636"

label end_2637:
    "Конец: end_2637"

label end_2641:
    "Конец: end_2641"

label end_2642:
    "Конец: end_2642"

label end_2645:
    "Конец: end_2645"

label end_2645:
    "Конец: end_2645"

label end_2645:
    "Конец: end_2645"

label end_2655:
    "Конец: end_2655"

label end_2655:
    "Конец: end_2655"

label end_2655:
    "Конец: end_2655"

label end_2657:
    "Конец: end_2657"

label end_2657:
    "Конец: end_2657"

label end_2658:
    "Конец: end_2658"

label end_2659:
    "Конец: end_2659"

label end_2666:
    "Конец: end_2666"

label end_2666:
    "Конец: end_2666"

label end_2666:
    "Конец: end_2666"

label end_2667:
    "Конец: end_2667"

label end_2668:
    "Конец: end_2668"

label end_2669:
    "Конец: end_2669"

label end_2670:
    "Конец: end_2670"

label end_2671:
    "Конец: end_2671"

label end_2672:
    "Конец: end_2672"

label end_2677:
    "Конец: end_2677"

label end_2677:
    "Конец: end_2677"

label end_2678:
    "Конец: end_2678"

label end_2679:
    "Конец: end_2679"

label end_2683:
    "Конец: end_2683"

label end_2683:
    "Конец: end_2683"

label end_2683:
    "Конец: end_2683"

label end_2683:
    "Конец: end_2683"

label end_2691:
    "Конец: end_2691"

label end_2691:
    "Конец: end_2691"

label end_2691:
    "Конец: end_2691"

label end_2691:
    "Конец: end_2691"

label end_2695:
    "Конец: end_2695"

label end_2695:
    "Конец: end_2695"

label end_2695:
    "Конец: end_2695"

label end_2695:
    "Конец: end_2695"

label end_2698:
    "Конец: end_2698"

label end_2698:
    "Конец: end_2698"

label end_2698:
    "Конец: end_2698"

label end_2701:
    "Конец: end_2701"

label end_2701:
    "Конец: end_2701"

label end_2701:
    "Конец: end_2701"

label end_2714:
    "Конец: end_2714"

label end_2715:
    "Конец: end_2715"

label end_2718:
    "Конец: end_2718"

label end_2718:
    "Конец: end_2718"

label end_2718:
    "Конец: end_2718"

label end_2719:
    "Конец: end_2719"

label end_2720:
    "Конец: end_2720"

label end_2721:
    "Конец: end_2721"

label end_2722:
    "Конец: end_2722"

label end_2727:
    "Конец: end_2727"

label end_2728:
    "Конец: end_2728"

label end_2732:
    "Конец: end_2732"

label end_2732:
    "Конец: end_2732"

label end_2732:
    "Конец: end_2732"

label end_2732:
    "Конец: end_2732"

label end_2734:
    "Конец: end_2734"

label end_2734:
    "Конец: end_2734"

label end_2735:
    "Конец: end_2735"

label end_2736:
    "Конец: end_2736"

label end_2742:
    "Конец: end_2742"

label end_2742:
    "Конец: end_2742"

label end_2742:
    "Конец: end_2742"

label end_2746:
    "Конец: end_2746"

label end_2746:
    "Конец: end_2746"

label end_2746:
    "Конец: end_2746"

label end_2746:
    "Конец: end_2746"

label end_2747:
    "Конец: end_2747"

label end_2748:
    "Конец: end_2748"

label end_2755:
    "Конец: end_2755"

label end_2755:
    "Конец: end_2755"

label end_2755:
    "Конец: end_2755"

label end_2755:
    "Конец: end_2755"

label end_2757:
    "Конец: end_2757"

label end_2757:
    "Конец: end_2757"

label end_2758:
    "Конец: end_2758"

label end_2759:
    "Конец: end_2759"

label end_2766:
    "Конец: end_2766"

label end_2766:
    "Конец: end_2766"

label end_2766:
    "Конец: end_2766"

label end_2766:
    "Конец: end_2766"

label end_2767:
    "Конец: end_2767"

label end_2768:
    "Конец: end_2768"

label end_2774:
    "Конец: end_2774"

label end_2774:
    "Конец: end_2774"

label end_2774:
    "Конец: end_2774"

label end_2774:
    "Конец: end_2774"

label end_2778:
    "Конец: end_2778"

label end_2778:
    "Конец: end_2778"

label end_2778:
    "Конец: end_2778"

label end_2783:
    "Конец: end_2783"

label end_2784:
    "Конец: end_2784"

label end_2785:
    "Конец: end_2785"

label end_2786:
    "Конец: end_2786"

label end_2788:
    "Конец: end_2788"

label end_2789:
    "Конец: end_2789"

label end_2793:
    "Конец: end_2793"

label end_2793:
    "Конец: end_2793"

label end_2793:
    "Конец: end_2793"

label end_2803:
    "Конец: end_2803"

label end_2803:
    "Конец: end_2803"

label end_2806:
    "Конец: end_2806"

label end_2806:
    "Конец: end_2806"

label end_2806:
    "Конец: end_2806"

label end_2807:
    "Конец: end_2807"

label end_2808:
    "Конец: end_2808"

label end_2809:
    "Конец: end_2809"

label end_2810:
    "Конец: end_2810"

label end_2815:
    "Конец: end_2815"

label end_2815:
    "Конец: end_2815"

label end_2818:
    "Конец: end_2818"

label end_2818:
    "Конец: end_2818"

label end_2818:
    "Конец: end_2818"

label end_2819:
    "Конец: end_2819"

label end_2820:
    "Конец: end_2820"

label end_2824:
    "Конец: end_2824"

label end_2824:
    "Конец: end_2824"

label end_2824:
    "Конец: end_2824"

label end_2827:
    "Конец: end_2827"

label end_2827:
    "Конец: end_2827"

label end_2832:
    "Конец: end_2832"

label end_2832:
    "Конец: end_2832"

label end_2832:
    "Конец: end_2832"

label end_2835:
    "Конец: end_2835"

label end_2835:
    "Конец: end_2835"

label end_2835:
    "Конец: end_2835"

label end_2846:
    "Конец: end_2846"

label end_2846:
    "Конец: end_2846"

label end_2848:
    "Конец: end_2848"

label end_2849:
    "Конец: end_2849"

label end_2854:
    "Конец: end_2854"

label end_2854:
    "Конец: end_2854"

label end_2854:
    "Конец: end_2854"

label end_2856:
    "Конец: end_2856"

label end_2856:
    "Конец: end_2856"

label end_2859:
    "Конец: end_2859"

label end_2859:
    "Конец: end_2859"

label end_2861:
    "Конец: end_2861"

label end_2862:
    "Конец: end_2862"

label end_2868:
    "Конец: end_2868"

label end_2868:
    "Конец: end_2868"

label end_2868:
    "Конец: end_2868"

label end_2868:
    "Конец: end_2868"

label end_2870:
    "Конец: end_2870"

label end_2870:
    "Конец: end_2870"

label end_2876:
    "Конец: end_2876"

label end_2876:
    "Конец: end_2876"

label end_2876:
    "Конец: end_2876"

label end_2880:
    "Конец: end_2880"

label end_2880:
    "Конец: end_2880"

label end_2880:
    "Конец: end_2880"

label end_2880:
    "Конец: end_2880"

label end_2886:
    "Конец: end_2886"

label end_2886:
    "Конец: end_2886"

label end_2886:
    "Конец: end_2886"

label end_2887:
    "Конец: end_2887"

label end_2888:
    "Конец: end_2888"

label end_2894:
    "Конец: end_2894"

label end_2894:
    "Конец: end_2894"

label end_2894:
    "Конец: end_2894"

label end_2898:
    "Конец: end_2898"

label end_2898:
    "Конец: end_2898"

label end_2898:
    "Конец: end_2898"

label end_2898:
    "Конец: end_2898"

label end_2902:
    "Конец: end_2902"

label end_2902:
    "Конец: end_2902"

label end_2905:
    "Конец: end_2905"

label end_2905:
    "Конец: end_2905"

label end_2912:
    "Конец: end_2912"

label end_2912:
    "Конец: end_2912"

label end_2912:
    "Конец: end_2912"

label end_2912:
    "Конец: end_2912"

label end_2915:
    "Конец: end_2915"

label end_2915:
    "Конец: end_2915"

label end_2915:
    "Конец: end_2915"

label end_2921:
    "Конец: end_2921"

label end_2922:
    "Конец: end_2922"

label end_2923:
    "Конец: end_2923"

label end_2924:
    "Конец: end_2924"

label end_2925:
    "Конец: end_2925"

label end_2926:
    "Конец: end_2926"

label end_2928:
    "Конец: end_2928"

label end_2928:
    "Конец: end_2928"

label end_2940:
    "Конец: end_2940"

label end_2940:
    "Конец: end_2940"

label end_2940:
    "Конец: end_2940"

label end_2944:
    "Конец: end_2944"

label end_2944:
    "Конец: end_2944"

label end_2944:
    "Конец: end_2944"

label end_2944:
    "Конец: end_2944"

label end_2945:
    "Конец: end_2945"

label end_2946:
    "Конец: end_2946"

label end_2952:
    "Конец: end_2952"

label end_2952:
    "Конец: end_2952"

label end_2955:
    "Конец: end_2955"

label end_2955:
    "Конец: end_2955"

label end_2955:
    "Конец: end_2955"

label end_2959:
    "Конец: end_2959"

label end_2959:
    "Конец: end_2959"

label end_2959:
    "Конец: end_2959"

label end_2959:
    "Конец: end_2959"

label end_2962:
    "Конец: end_2962"

label end_2962:
    "Конец: end_2962"

label end_2962:
    "Конец: end_2962"

label end_2970:
    "Конец: end_2970"

label end_2970:
    "Конец: end_2970"

label end_2970:
    "Конец: end_2970"

label end_2970:
    "Конец: end_2970"

label end_2974:
    "Конец: end_2974"

label end_2974:
    "Конец: end_2974"

label end_2974:
    "Конец: end_2974"

label end_2974:
    "Конец: end_2974"

label end_2975:
    "Конец: end_2975"

label end_2976:
    "Конец: end_2976"

label end_2978:
    "Конец: end_2978"

label end_2978:
    "Конец: end_2978"

label end_2980:
    "Конец: end_2980"

label end_2981:
    "Конец: end_2981"

label end_2984:
    "Конец: end_2984"

label end_2984:
    "Конец: end_2984"

label end_2995:
    "Конец: end_2995"

label end_2995:
    "Конец: end_2995"

label end_2995:
    "Конец: end_2995"

label end_2995:
    "Конец: end_2995"

label end_2996:
    "Конец: end_2996"

label end_2997:
    "Конец: end_2997"

label end_3000:
    "Конец: end_3000"

label end_3000:
    "Конец: end_3000"

label end_3000:
    "Конец: end_3000"

label end_3001:
    "Конец: end_3001"

label end_3002:
    "Конец: end_3002"

label end_3009:
    "Конец: end_3009"

label end_3009:
    "Конец: end_3009"

label end_3009:
    "Конец: end_3009"

label end_3012:
    "Конец: end_3012"

label end_3012:
    "Конец: end_3012"

label end_3012:
    "Конец: end_3012"

label end_3014:
    "Конец: end_3014"

label end_3014:
    "Конец: end_3014"

label end_3015:
    "Конец: end_3015"

label end_3016:
    "Конец: end_3016"

label end_3027:
    "Конец: end_3027"

label end_3027:
    "Конец: end_3027"

label end_3027:
    "Конец: end_3027"

label end_3027:
    "Конец: end_3027"

label end_3029:
    "Конец: end_3029"

label end_3029:
    "Конец: end_3029"

label end_3032:
    "Конец: end_3032"

label end_3032:
    "Конец: end_3032"

label end_3032:
    "Конец: end_3032"

label end_3035:
    "Конец: end_3035"

label end_3035:
    "Конец: end_3035"

label end_3035:
    "Конец: end_3035"

label end_3041:
    "Конец: end_3041"

label end_3041:
    "Конец: end_3041"

label end_3041:
    "Конец: end_3041"

label end_3041:
    "Конец: end_3041"

label end_3046:
    "Конец: end_3046"

label end_3046:
    "Конец: end_3046"

label end_3046:
    "Конец: end_3046"

label end_3046:
    "Конец: end_3046"

label end_3057:
    "Конец: end_3057"

label end_3057:
    "Конец: end_3057"

label end_3057:
    "Конец: end_3057"

label end_3057:
    "Конец: end_3057"

label end_3061:
    "Конец: end_3061"

label end_3061:
    "Конец: end_3061"

label end_3061:
    "Конец: end_3061"

label end_3061:
    "Конец: end_3061"

label end_3066:
    "Конец: end_3066"

label end_3066:
    "Конец: end_3066"

label end_3066:
    "Конец: end_3066"

label end_3066:
    "Конец: end_3066"

label end_3069:
    "Конец: end_3069"

label end_3069:
    "Конец: end_3069"

label end_3073:
    "Конец: end_3073"

label end_3073:
    "Конец: end_3073"

label end_3075:
    "Конец: end_3075"

label end_3075:
    "Конец: end_3075"
