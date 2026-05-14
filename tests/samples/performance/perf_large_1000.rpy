label start:
    $ strength = 0
    $ intelligence = 0
    $ luck = 0
    $ charisma = 0

    menu:
        "Go back":
            jump label_0
        "Go back":
            $ intelligence += 1
            jump label_1
        "Talk":
            $ charisma += 3
            jump label_2

label label_0:
    "Scene label_0"
    menu:
        "Open door":
            jump label_3
        "Pick up item":
            jump label_4
        "Use item":
            jump label_5

label label_3:
    "Scene label_3"
    menu:
        "Pick up item":
            jump label_6
        "Explore":
            $ strength += 1
            jump label_7

label label_6:
    "Scene label_6"
    menu:
        "Talk":
            $ charisma += 1
            jump label_8
        "Use item":
            jump label_9

label label_8:
    "Scene label_8"
    menu:
        "Go forward":
            $ charisma += 2
            jump label_10
        "Go forward":
            jump label_11
        "Go back":
            jump label_12

label label_10:
    "Scene label_10"
    menu:
        "Use item":
            jump label_13
        "Go forward":
            $ strength += 3
            jump label_14

label label_13:
    "Scene label_13"
    menu:
        "Pick up item":
            $ charisma += 1
            jump label_15
        "Talk":
            jump label_16

label label_15:
    "Scene label_15"
    menu:
        "Explore":
            jump label_17
        "Open door":
            $ charisma += 2
            jump label_18
        "Look around":
            jump label_19

label label_17:
    "Scene label_17"
    menu:
        "Explore":
            $ charisma += 3
            jump label_20
        "Talk":
            jump label_21

label label_20:
    "Scene label_20"
    if strength >= 5:
        jump label_22

label label_22:
    $ strength += 4
    menu:
        "Open door":
            jump label_23
        "Use item":
            $ intelligence += 2
            jump label_24
        "Use item":
            jump label_25

label label_23:
    "Scene label_23"
    menu:
        "Go forward":
            jump label_26
        "Open door":
            jump label_27

label label_26:
    "Scene label_26"
    jump end_28

label label_27:
    "Scene label_27"
    jump end_28

label label_24:
    "Scene label_24"
    menu:
        "Use item":
            $ strength += 3
            jump label_28
        "Go forward":
            $ strength += 1
            jump label_29

label label_28:
    "Scene label_28"
    jump end_30

label label_29:
    "Scene label_29"
    jump end_30

label label_25:
    "Scene label_25"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_30
        "Talk":
            jump label_31
        "Go back":
            $ luck += 3
            jump label_32

label label_30:
    "Scene label_30"
    jump end_33

label label_31:
    "Scene label_31"
    jump end_33

label label_32:
    "Scene label_32"
    jump end_33

    jump label_33

label label_33:
    "Ветка false для label_22"
    menu:
        "Use item":
            $ intelligence += 3
            jump label_34
        "Use item":
            $ luck += 1
            jump label_35
        "Talk":
            jump label_36

label label_34:
    "Scene label_34"
    menu:
        "Go forward":
            jump label_37
        "Open door":
            jump label_38
        "Explore":
            jump label_39

label label_37:
    "Scene label_37"
    jump end_40

label label_38:
    "Scene label_38"
    jump end_40

label label_39:
    "Scene label_39"
    jump end_40

label label_35:
    "Scene label_35"
    menu:
        "Open door":
            $ charisma += 1
            jump label_40
        "Use item":
            $ intelligence += 2
            jump label_41
        "Go forward":
            jump label_42

label label_40:
    "Scene label_40"
    jump end_43

label label_41:
    "Scene label_41"
    jump end_43

label label_42:
    "Scene label_42"
    jump end_43

label label_36:
    "Scene label_36"
    menu:
        "Open door":
            $ intelligence += 2
            jump label_43
        "Look around":
            jump label_44

label label_43:
    "Scene label_43"
    jump end_45

label label_44:
    "Scene label_44"
    jump end_45

label label_21:
    "Scene label_21"
    menu:
        "Use item":
            $ charisma += 3
            jump label_45
        "Go forward":
            jump label_46

label label_45:
    "Scene label_45"
    if intelligence >= 20:
        jump label_47

label label_47:
    $ intelligence += 3
    menu:
        "Go back":
            jump label_48
        "Go forward":
            $ intelligence += 3
            jump label_49
        "Look around":
            jump label_50

label label_48:
    "Scene label_48"
    jump end_51

label label_49:
    "Scene label_49"
    jump end_51

label label_50:
    "Scene label_50"
    jump end_51

    jump label_51

label label_51:
    "Ветка false для label_47"
    menu:
        "Use item":
            $ intelligence += 3
            jump label_52
        "Explore":
            jump label_53

label label_52:
    "Scene label_52"
    jump end_54

label label_53:
    "Scene label_53"
    jump end_54

label label_46:
    "Scene label_46"
    menu:
        "Go back":
            $ charisma += 2
            jump label_54
        "Look around":
            jump label_55
        "Pick up item":
            jump label_56

label label_54:
    "Scene label_54"
    menu:
        "Explore":
            $ strength += 3
            jump label_57
        "Use item":
            jump label_58

label label_57:
    "Scene label_57"
    jump end_59

label label_58:
    "Scene label_58"
    jump end_59

label label_55:
    "Scene label_55"
    if charisma >= 14:
        jump label_59

label label_59:
    $ charisma += 3
    jump end_60

    jump label_60

label label_60:
    "Ветка false для label_59"
    jump end_61

label label_56:
    "Scene label_56"
    if intelligence >= 17:
        jump label_61

label label_61:
    $ intelligence += 3
    jump end_62

    jump label_62

label label_62:
    "Ветка false для label_61"
    jump end_63

label label_18:
    "Scene label_18"
    menu:
        "Go back":
            jump label_63
        "Pick up item":
            jump label_64
        "Pick up item":
            $ luck += 1
            jump label_65

label label_63:
    "Scene label_63"
    if charisma >= 10:
        jump label_66

label label_66:
    $ charisma += 2
    menu:
        "Go forward":
            jump label_67
        "Open door":
            $ intelligence += 1
            jump label_68

label label_67:
    "Scene label_67"
    menu:
        "Use item":
            jump label_69
        "Explore":
            $ charisma += 3
            jump label_70

label label_69:
    "Scene label_69"
    jump end_71

label label_70:
    "Scene label_70"
    jump end_71

label label_68:
    "Scene label_68"
    menu:
        "Open door":
            $ luck += 3
            jump label_71
        "Go back":
            $ charisma += 1
            jump label_72

label label_71:
    "Scene label_71"
    jump end_73

label label_72:
    "Scene label_72"
    jump end_73

    jump label_73

label label_73:
    "Ветка false для label_66"
    if strength >= 9:
        jump label_74

label label_74:
    $ strength += 3
    if luck >= 16:
        jump label_75

label label_75:
    $ luck += 4
    jump end_76

    jump label_76

label label_76:
    "Ветка false для label_75"
    jump end_77

    jump label_77

label label_77:
    "Ветка false для label_74"
    menu:
        "Explore":
            jump label_78
        "Pick up item":
            jump label_79

label label_78:
    "Scene label_78"
    jump end_80

label label_79:
    "Scene label_79"
    jump end_80

label label_64:
    "Scene label_64"
    menu:
        "Go back":
            jump label_80
        "Look around":
            jump label_81

label label_80:
    "Scene label_80"
    menu:
        "Look around":
            $ charisma += 3
            jump label_82
        "Pick up item":
            $ strength += 3
            jump label_83

label label_82:
    "Scene label_82"
    if charisma >= 18:
        jump label_84

label label_84:
    $ charisma += 4
    jump end_85

    jump label_85

label label_85:
    "Ветка false для label_84"
    jump end_86

label label_83:
    "Scene label_83"
    menu:
        "Go forward":
            $ charisma += 2
            jump label_86
        "Go forward":
            jump label_87

label label_86:
    "Scene label_86"
    jump end_88

label label_87:
    "Scene label_87"
    jump end_88

label label_81:
    "Scene label_81"
    menu:
        "Go forward":
            $ luck += 1
            jump label_88
        "Use item":
            jump label_89
        "Open door":
            jump label_90

label label_88:
    "Scene label_88"
    if intelligence >= 17:
        jump label_91

label label_91:
    $ intelligence += 4
    jump end_92

    jump label_92

label label_92:
    "Ветка false для label_91"
    jump end_93

label label_89:
    "Scene label_89"
    menu:
        "Look around":
            jump label_93
        "Explore":
            $ charisma += 1
            jump label_94

label label_93:
    "Scene label_93"
    jump end_95

label label_94:
    "Scene label_94"
    jump end_95

label label_90:
    "Scene label_90"
    menu:
        "Open door":
            jump label_95
        "Explore":
            $ luck += 2
            jump label_96
        "Pick up item":
            $ charisma += 2
            jump label_97

label label_95:
    "Scene label_95"
    jump end_98

label label_96:
    "Scene label_96"
    jump end_98

label label_97:
    "Scene label_97"
    jump end_98

label label_65:
    "Scene label_65"
    if charisma >= 7:
        jump label_98

label label_98:
    $ charisma += 4
    menu:
        "Look around":
            $ charisma += 3
            jump label_99
        "Talk":
            jump label_100

label label_99:
    "Scene label_99"
    menu:
        "Look around":
            $ luck += 2
            jump label_101
        "Explore":
            jump label_102

label label_101:
    "Scene label_101"
    jump end_103

label label_102:
    "Scene label_102"
    jump end_103

label label_100:
    "Scene label_100"
    if strength >= 10:
        jump label_103

label label_103:
    $ strength += 5
    jump end_104

    jump label_104

label label_104:
    "Ветка false для label_103"
    jump end_105

    jump label_105

label label_105:
    "Ветка false для label_98"
    menu:
        "Look around":
            $ luck += 3
            jump label_106
        "Look around":
            jump label_107
        "Explore":
            jump label_108

label label_106:
    "Scene label_106"
    if charisma >= 17:
        jump label_109

label label_109:
    $ charisma += 2
    jump end_110

    jump label_110

label label_110:
    "Ветка false для label_109"
    jump end_111

label label_107:
    "Scene label_107"
    menu:
        "Talk":
            jump label_111
        "Talk":
            $ luck += 2
            jump label_112

label label_111:
    "Scene label_111"
    jump end_113

label label_112:
    "Scene label_112"
    jump end_113

label label_108:
    "Scene label_108"
    menu:
        "Talk":
            $ charisma += 2
            jump label_113
        "Pick up item":
            jump label_114

label label_113:
    "Scene label_113"
    jump end_115

label label_114:
    "Scene label_114"
    jump end_115

label label_19:
    "Scene label_19"
    menu:
        "Pick up item":
            jump label_115
        "Use item":
            $ intelligence += 2
            jump label_116

label label_115:
    "Scene label_115"
    if charisma >= 15:
        jump label_117

label label_117:
    $ charisma += 5
    menu:
        "Pick up item":
            $ intelligence += 2
            jump label_118
        "Explore":
            jump label_119
        "Use item":
            $ intelligence += 2
            jump label_120

label label_118:
    "Scene label_118"
    menu:
        "Pick up item":
            jump label_121
        "Use item":
            $ luck += 2
            jump label_122
        "Explore":
            $ intelligence += 3
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
    menu:
        "Go forward":
            jump label_124
        "Pick up item":
            jump label_125

label label_124:
    "Scene label_124"
    jump end_126

label label_125:
    "Scene label_125"
    jump end_126

label label_120:
    "Scene label_120"
    if luck >= 7:
        jump label_126

label label_126:
    $ luck += 5
    jump end_127

    jump label_127

label label_127:
    "Ветка false для label_126"
    jump end_128

    jump label_128

label label_128:
    "Ветка false для label_117"
    menu:
        "Go back":
            $ intelligence += 3
            jump label_129
        "Open door":
            jump label_130

label label_129:
    "Scene label_129"
    if charisma >= 17:
        jump label_131

label label_131:
    $ charisma += 5
    jump end_132

    jump label_132

label label_132:
    "Ветка false для label_131"
    jump end_133

label label_130:
    "Scene label_130"
    menu:
        "Look around":
            $ intelligence += 3
            jump label_133
        "Explore":
            $ strength += 3
            jump label_134
        "Open door":
            jump label_135

label label_133:
    "Scene label_133"
    jump end_136

label label_134:
    "Scene label_134"
    jump end_136

label label_135:
    "Scene label_135"
    jump end_136

label label_116:
    "Scene label_116"
    menu:
        "Look around":
            $ luck += 1
            jump label_136
        "Use item":
            $ charisma += 2
            jump label_137
        "Talk":
            $ strength += 2
            jump label_138

label label_136:
    "Scene label_136"
    if charisma >= 7:
        jump label_139

label label_139:
    $ charisma += 2
    menu:
        "Explore":
            $ charisma += 1
            jump label_140
        "Pick up item":
            $ strength += 2
            jump label_141

label label_140:
    "Scene label_140"
    jump end_142

label label_141:
    "Scene label_141"
    jump end_142

    jump label_142

label label_142:
    "Ветка false для label_139"
    menu:
        "Explore":
            $ strength += 3
            jump label_143
        "Look around":
            $ luck += 3
            jump label_144
        "Look around":
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

label label_137:
    "Scene label_137"
    if intelligence >= 10:
        jump label_146

label label_146:
    $ intelligence += 3
    menu:
        "Pick up item":
            $ charisma += 3
            jump label_147
        "Talk":
            $ charisma += 2
            jump label_148
        "Go forward":
            jump label_149

label label_147:
    "Scene label_147"
    jump end_150

label label_148:
    "Scene label_148"
    jump end_150

label label_149:
    "Scene label_149"
    jump end_150

    jump label_150

label label_150:
    "Ветка false для label_146"
    menu:
        "Open door":
            $ intelligence += 1
            jump label_151
        "Go back":
            jump label_152
        "Look around":
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

label label_138:
    "Scene label_138"
    menu:
        "Explore":
            $ charisma += 1
            jump label_154
        "Go back":
            jump label_155

label label_154:
    "Scene label_154"
    menu:
        "Open door":
            jump label_156
        "Look around":
            $ charisma += 3
            jump label_157
        "Talk":
            jump label_158

label label_156:
    "Scene label_156"
    jump end_159

label label_157:
    "Scene label_157"
    jump end_159

label label_158:
    "Scene label_158"
    jump end_159

label label_155:
    "Scene label_155"
    menu:
        "Look around":
            jump label_159
        "Explore":
            $ luck += 1
            jump label_160
        "Talk":
            $ intelligence += 3
            jump label_161

label label_159:
    "Scene label_159"
    jump end_162

label label_160:
    "Scene label_160"
    jump end_162

label label_161:
    "Scene label_161"
    jump end_162

label label_16:
    "Scene label_16"
    menu:
        "Open door":
            $ charisma += 3
            jump label_162
        "Talk":
            jump label_163

label label_162:
    "Scene label_162"
    menu:
        "Talk":
            $ charisma += 3
            jump label_164
        "Go forward":
            jump label_165

label label_164:
    "Scene label_164"
    menu:
        "Talk":
            $ charisma += 3
            jump label_166
        "Pick up item":
            $ charisma += 2
            jump label_167
        "Pick up item":
            $ strength += 3
            jump label_168

label label_166:
    "Scene label_166"
    if intelligence >= 14:
        jump label_169

label label_169:
    $ intelligence += 2
    if luck >= 10:
        jump label_170

label label_170:
    $ luck += 5
    jump end_171

    jump label_171

label label_171:
    "Ветка false для label_170"
    jump end_172

    jump label_172

label label_172:
    "Ветка false для label_169"
    menu:
        "Look around":
            jump label_173
        "Go back":
            jump label_174
        "Explore":
            jump label_175

label label_173:
    "Scene label_173"
    jump end_176

label label_174:
    "Scene label_174"
    jump end_176

label label_175:
    "Scene label_175"
    jump end_176

label label_167:
    "Scene label_167"
    menu:
        "Use item":
            jump label_176
        "Look around":
            jump label_177
        "Use item":
            $ strength += 2
            jump label_178

label label_176:
    "Scene label_176"
    if strength >= 19:
        jump label_179

label label_179:
    $ strength += 2
    jump end_180

    jump label_180

label label_180:
    "Ветка false для label_179"
    jump end_181

label label_177:
    "Scene label_177"
    menu:
        "Use item":
            jump label_181
        "Explore":
            jump label_182

label label_181:
    "Scene label_181"
    jump end_183

label label_182:
    "Scene label_182"
    jump end_183

label label_178:
    "Scene label_178"
    menu:
        "Talk":
            jump label_183
        "Use item":
            jump label_184
        "Go forward":
            jump label_185

label label_183:
    "Scene label_183"
    jump end_186

label label_184:
    "Scene label_184"
    jump end_186

label label_185:
    "Scene label_185"
    jump end_186

label label_168:
    "Scene label_168"
    menu:
        "Explore":
            jump label_186
        "Go back":
            $ luck += 3
            jump label_187

label label_186:
    "Scene label_186"
    menu:
        "Talk":
            jump label_188
        "Open door":
            jump label_189

label label_188:
    "Scene label_188"
    jump end_190

label label_189:
    "Scene label_189"
    jump end_190

label label_187:
    "Scene label_187"
    menu:
        "Talk":
            $ luck += 1
            jump label_190
        "Open door":
            $ luck += 3
            jump label_191

label label_190:
    "Scene label_190"
    jump end_192

label label_191:
    "Scene label_191"
    jump end_192

label label_165:
    "Scene label_165"
    menu:
        "Look around":
            jump label_192
        "Look around":
            $ luck += 3
            jump label_193
        "Explore":
            $ charisma += 2
            jump label_194

label label_192:
    "Scene label_192"
    menu:
        "Pick up item":
            jump label_195
        "Explore":
            jump label_196

label label_195:
    "Scene label_195"
    menu:
        "Use item":
            jump label_197
        "Use item":
            $ luck += 2
            jump label_198
        "Explore":
            jump label_199

label label_197:
    "Scene label_197"
    jump end_200

label label_198:
    "Scene label_198"
    jump end_200

label label_199:
    "Scene label_199"
    jump end_200

label label_196:
    "Scene label_196"
    if charisma >= 15:
        jump label_200

label label_200:
    $ charisma += 2
    jump end_201

    jump label_201

label label_201:
    "Ветка false для label_200"
    jump end_202

label label_193:
    "Scene label_193"
    if charisma >= 5:
        jump label_202

label label_202:
    $ charisma += 2
    menu:
        "Pick up item":
            $ charisma += 1
            jump label_203
        "Talk":
            jump label_204

label label_203:
    "Scene label_203"
    jump end_205

label label_204:
    "Scene label_204"
    jump end_205

    jump label_205

label label_205:
    "Ветка false для label_202"
    menu:
        "Look around":
            jump label_206
        "Go back":
            $ intelligence += 1
            jump label_207
        "Open door":
            jump label_208

label label_206:
    "Scene label_206"
    jump end_209

label label_207:
    "Scene label_207"
    jump end_209

label label_208:
    "Scene label_208"
    jump end_209

label label_194:
    "Scene label_194"
    menu:
        "Open door":
            jump label_209
        "Look around":
            $ charisma += 1
            jump label_210

label label_209:
    "Scene label_209"
    if intelligence >= 19:
        jump label_211

label label_211:
    $ intelligence += 2
    jump end_212

    jump label_212

label label_212:
    "Ветка false для label_211"
    jump end_213

label label_210:
    "Scene label_210"
    if luck >= 8:
        jump label_213

label label_213:
    $ luck += 5
    jump end_214

    jump label_214

label label_214:
    "Ветка false для label_213"
    jump end_215

label label_163:
    "Scene label_163"
    menu:
        "Look around":
            $ strength += 3
            jump label_215
        "Look around":
            $ luck += 2
            jump label_216
        "Talk":
            $ intelligence += 3
            jump label_217

label label_215:
    "Scene label_215"
    menu:
        "Look around":
            jump label_218
        "Go forward":
            jump label_219

label label_218:
    "Scene label_218"
    if luck >= 11:
        jump label_220

label label_220:
    $ luck += 3
    menu:
        "Use item":
            $ strength += 1
            jump label_221
        "Look around":
            jump label_222
        "Open door":
            $ charisma += 2
            jump label_223

label label_221:
    "Scene label_221"
    jump end_224

label label_222:
    "Scene label_222"
    jump end_224

label label_223:
    "Scene label_223"
    jump end_224

    jump label_224

label label_224:
    "Ветка false для label_220"
    menu:
        "Go back":
            jump label_225
        "Use item":
            jump label_226

label label_225:
    "Scene label_225"
    jump end_227

label label_226:
    "Scene label_226"
    jump end_227

label label_219:
    "Scene label_219"
    menu:
        "Go forward":
            jump label_227
        "Go back":
            $ intelligence += 3
            jump label_228
        "Open door":
            $ strength += 1
            jump label_229

label label_227:
    "Scene label_227"
    menu:
        "Use item":
            $ strength += 3
            jump label_230
        "Go forward":
            jump label_231

label label_230:
    "Scene label_230"
    jump end_232

label label_231:
    "Scene label_231"
    jump end_232

label label_228:
    "Scene label_228"
    menu:
        "Open door":
            jump label_232
        "Open door":
            $ intelligence += 2
            jump label_233

label label_232:
    "Scene label_232"
    jump end_234

label label_233:
    "Scene label_233"
    jump end_234

label label_229:
    "Scene label_229"
    menu:
        "Go forward":
            jump label_234
        "Go forward":
            $ strength += 1
            jump label_235

label label_234:
    "Scene label_234"
    jump end_236

label label_235:
    "Scene label_235"
    jump end_236

label label_216:
    "Scene label_216"
    menu:
        "Go back":
            jump label_236
        "Open door":
            $ charisma += 1
            jump label_237
        "Talk":
            $ luck += 1
            jump label_238

label label_236:
    "Scene label_236"
    menu:
        "Talk":
            jump label_239
        "Open door":
            jump label_240

label label_239:
    "Scene label_239"
    menu:
        "Go back":
            jump label_241
        "Use item":
            $ strength += 2
            jump label_242

label label_241:
    "Scene label_241"
    jump end_243

label label_242:
    "Scene label_242"
    jump end_243

label label_240:
    "Scene label_240"
    if strength >= 14:
        jump label_243

label label_243:
    $ strength += 3
    jump end_244

    jump label_244

label label_244:
    "Ветка false для label_243"
    jump end_245

label label_237:
    "Scene label_237"
    if intelligence >= 5:
        jump label_245

label label_245:
    $ intelligence += 3
    menu:
        "Go back":
            $ intelligence += 3
            jump label_246
        "Go back":
            jump label_247
        "Look around":
            jump label_248

label label_246:
    "Scene label_246"
    jump end_249

label label_247:
    "Scene label_247"
    jump end_249

label label_248:
    "Scene label_248"
    jump end_249

    jump label_249

label label_249:
    "Ветка false для label_245"
    if charisma >= 13:
        jump label_250

label label_250:
    $ charisma += 2
    jump end_251

    jump label_251

label label_251:
    "Ветка false для label_250"
    jump end_252

label label_238:
    "Scene label_238"
    if strength >= 20:
        jump label_252

label label_252:
    $ strength += 5
    menu:
        "Pick up item":
            jump label_253
        "Talk":
            $ luck += 1
            jump label_254

label label_253:
    "Scene label_253"
    jump end_255

label label_254:
    "Scene label_254"
    jump end_255

    jump label_255

label label_255:
    "Ветка false для label_252"
    menu:
        "Use item":
            jump label_256
        "Go forward":
            $ strength += 1
            jump label_257

label label_256:
    "Scene label_256"
    jump end_258

label label_257:
    "Scene label_257"
    jump end_258

label label_217:
    "Scene label_217"
    if luck >= 17:
        jump label_258

label label_258:
    $ luck += 3
    if strength >= 18:
        jump label_259

label label_259:
    $ strength += 3
    menu:
        "Explore":
            $ strength += 3
            jump label_260
        "Explore":
            $ strength += 1
            jump label_261
        "Use item":
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

    jump label_263

label label_263:
    "Ветка false для label_259"
    menu:
        "Look around":
            jump label_264
        "Go back":
            jump label_265
        "Go back":
            $ charisma += 1
            jump label_266

label label_264:
    "Scene label_264"
    jump end_267

label label_265:
    "Scene label_265"
    jump end_267

label label_266:
    "Scene label_266"
    jump end_267

    jump label_267

label label_267:
    "Ветка false для label_258"
    menu:
        "Go back":
            jump label_268
        "Use item":
            $ charisma += 1
            jump label_269
        "Use item":
            $ charisma += 1
            jump label_270

label label_268:
    "Scene label_268"
    if luck >= 5:
        jump label_271

label label_271:
    $ luck += 4
    jump end_272

    jump label_272

label label_272:
    "Ветка false для label_271"
    jump end_273

label label_269:
    "Scene label_269"
    if charisma >= 14:
        jump label_273

label label_273:
    $ charisma += 2
    jump end_274

    jump label_274

label label_274:
    "Ветка false для label_273"
    jump end_275

label label_270:
    "Scene label_270"
    if intelligence >= 18:
        jump label_275

label label_275:
    $ intelligence += 5
    jump end_276

    jump label_276

label label_276:
    "Ветка false для label_275"
    jump end_277

label label_14:
    "Scene label_14"
    menu:
        "Go back":
            $ intelligence += 3
            jump label_277
        "Open door":
            jump label_278

label label_277:
    "Scene label_277"
    menu:
        "Look around":
            jump label_279
        "Open door":
            $ strength += 2
            jump label_280

label label_279:
    "Scene label_279"
    menu:
        "Use item":
            $ luck += 2
            jump label_281
        "Explore":
            $ luck += 1
            jump label_282

label label_281:
    "Scene label_281"
    if intelligence >= 9:
        jump label_283

label label_283:
    $ intelligence += 2
    if intelligence >= 19:
        jump label_284

label label_284:
    $ intelligence += 5
    menu:
        "Explore":
            jump label_285
        "Use item":
            $ charisma += 2
            jump label_286

label label_285:
    "Scene label_285"
    jump end_287

label label_286:
    "Scene label_286"
    jump end_287

    jump label_287

label label_287:
    "Ветка false для label_284"
    menu:
        "Talk":
            jump label_288
        "Go back":
            jump label_289

label label_288:
    "Scene label_288"
    jump end_290

label label_289:
    "Scene label_289"
    jump end_290

    jump label_290

label label_290:
    "Ветка false для label_283"
    menu:
        "Use item":
            jump label_291
        "Explore":
            $ intelligence += 2
            jump label_292

label label_291:
    "Scene label_291"
    menu:
        "Go back":
            $ intelligence += 1
            jump label_293
        "Open door":
            jump label_294

label label_293:
    "Scene label_293"
    jump end_295

label label_294:
    "Scene label_294"
    jump end_295

label label_292:
    "Scene label_292"
    menu:
        "Look around":
            $ intelligence += 1
            jump label_295
        "Go forward":
            $ intelligence += 1
            jump label_296

label label_295:
    "Scene label_295"
    jump end_297

label label_296:
    "Scene label_296"
    jump end_297

label label_282:
    "Scene label_282"
    if charisma >= 16:
        jump label_297

label label_297:
    $ charisma += 2
    menu:
        "Look around":
            $ strength += 1
            jump label_298
        "Pick up item":
            jump label_299
        "Look around":
            jump label_300

label label_298:
    "Scene label_298"
    menu:
        "Look around":
            $ charisma += 1
            jump label_301
        "Talk":
            jump label_302
        "Open door":
            jump label_303

label label_301:
    "Scene label_301"
    jump end_304

label label_302:
    "Scene label_302"
    jump end_304

label label_303:
    "Scene label_303"
    jump end_304

label label_299:
    "Scene label_299"
    menu:
        "Open door":
            jump label_304
        "Talk":
            $ intelligence += 2
            jump label_305

label label_304:
    "Scene label_304"
    jump end_306

label label_305:
    "Scene label_305"
    jump end_306

label label_300:
    "Scene label_300"
    if intelligence >= 6:
        jump label_306

label label_306:
    $ intelligence += 3
    jump end_307

    jump label_307

label label_307:
    "Ветка false для label_306"
    jump end_308

    jump label_308

label label_308:
    "Ветка false для label_297"
    menu:
        "Open door":
            jump label_309
        "Pick up item":
            $ luck += 2
            jump label_310
        "Talk":
            $ intelligence += 3
            jump label_311

label label_309:
    "Scene label_309"
    menu:
        "Open door":
            jump label_312
        "Explore":
            $ charisma += 2
            jump label_313

label label_312:
    "Scene label_312"
    jump end_314

label label_313:
    "Scene label_313"
    jump end_314

label label_310:
    "Scene label_310"
    menu:
        "Open door":
            $ strength += 2
            jump label_314
        "Use item":
            $ luck += 1
            jump label_315
        "Pick up item":
            jump label_316

label label_314:
    "Scene label_314"
    jump end_317

label label_315:
    "Scene label_315"
    jump end_317

label label_316:
    "Scene label_316"
    jump end_317

label label_311:
    "Scene label_311"
    menu:
        "Talk":
            $ intelligence += 2
            jump label_317
        "Go forward":
            jump label_318

label label_317:
    "Scene label_317"
    jump end_319

label label_318:
    "Scene label_318"
    jump end_319

label label_280:
    "Scene label_280"
    menu:
        "Explore":
            jump label_319
        "Talk":
            $ luck += 3
            jump label_320
        "Explore":
            jump label_321

label label_319:
    "Scene label_319"
    if luck >= 9:
        jump label_322

label label_322:
    $ luck += 3
    menu:
        "Go back":
            $ strength += 1
            jump label_323
        "Go forward":
            $ intelligence += 1
            jump label_324
        "Pick up item":
            $ intelligence += 1
            jump label_325

label label_323:
    "Scene label_323"
    menu:
        "Explore":
            $ intelligence += 3
            jump label_326
        "Talk":
            jump label_327

label label_326:
    "Scene label_326"
    jump end_328

label label_327:
    "Scene label_327"
    jump end_328

label label_324:
    "Scene label_324"
    menu:
        "Look around":
            $ charisma += 3
            jump label_328
        "Look around":
            $ luck += 1
            jump label_329
        "Talk":
            jump label_330

label label_328:
    "Scene label_328"
    jump end_331

label label_329:
    "Scene label_329"
    jump end_331

label label_330:
    "Scene label_330"
    jump end_331

label label_325:
    "Scene label_325"
    menu:
        "Explore":
            $ luck += 1
            jump label_331
        "Talk":
            $ luck += 1
            jump label_332
        "Talk":
            jump label_333

label label_331:
    "Scene label_331"
    jump end_334

label label_332:
    "Scene label_332"
    jump end_334

label label_333:
    "Scene label_333"
    jump end_334

    jump label_334

label label_334:
    "Ветка false для label_322"
    menu:
        "Go forward":
            $ luck += 3
            jump label_335
        "Use item":
            jump label_336
        "Look around":
            jump label_337

label label_335:
    "Scene label_335"
    if strength >= 12:
        jump label_338

label label_338:
    $ strength += 4
    jump end_339

    jump label_339

label label_339:
    "Ветка false для label_338"
    jump end_340

label label_336:
    "Scene label_336"
    menu:
        "Look around":
            jump label_340
        "Explore":
            $ luck += 1
            jump label_341

label label_340:
    "Scene label_340"
    jump end_342

label label_341:
    "Scene label_341"
    jump end_342

label label_337:
    "Scene label_337"
    if strength >= 16:
        jump label_342

label label_342:
    $ strength += 4
    jump end_343

    jump label_343

label label_343:
    "Ветка false для label_342"
    jump end_344

label label_320:
    "Scene label_320"
    menu:
        "Go forward":
            $ charisma += 1
            jump label_344
        "Open door":
            $ charisma += 2
            jump label_345

label label_344:
    "Scene label_344"
    menu:
        "Pick up item":
            jump label_346
        "Use item":
            $ strength += 1
            jump label_347

label label_346:
    "Scene label_346"
    if luck >= 13:
        jump label_348

label label_348:
    $ luck += 2
    jump end_349

    jump label_349

label label_349:
    "Ветка false для label_348"
    jump end_350

label label_347:
    "Scene label_347"
    if intelligence >= 17:
        jump label_350

label label_350:
    $ intelligence += 3
    jump end_351

    jump label_351

label label_351:
    "Ветка false для label_350"
    jump end_352

label label_345:
    "Scene label_345"
    menu:
        "Explore":
            jump label_352
        "Pick up item":
            jump label_353

label label_352:
    "Scene label_352"
    menu:
        "Open door":
            $ strength += 2
            jump label_354
        "Use item":
            jump label_355

label label_354:
    "Scene label_354"
    jump end_356

label label_355:
    "Scene label_355"
    jump end_356

label label_353:
    "Scene label_353"
    menu:
        "Go back":
            $ strength += 1
            jump label_356
        "Open door":
            jump label_357
        "Pick up item":
            $ luck += 1
            jump label_358

label label_356:
    "Scene label_356"
    jump end_359

label label_357:
    "Scene label_357"
    jump end_359

label label_358:
    "Scene label_358"
    jump end_359

label label_321:
    "Scene label_321"
    menu:
        "Pick up item":
            $ strength += 1
            jump label_359
        "Talk":
            jump label_360
        "Look around":
            $ strength += 2
            jump label_361

label label_359:
    "Scene label_359"
    menu:
        "Pick up item":
            jump label_362
        "Go back":
            $ charisma += 1
            jump label_363
        "Explore":
            jump label_364

label label_362:
    "Scene label_362"
    menu:
        "Go forward":
            $ charisma += 2
            jump label_365
        "Use item":
            jump label_366
        "Go forward":
            $ strength += 1
            jump label_367

label label_365:
    "Scene label_365"
    jump end_368

label label_366:
    "Scene label_366"
    jump end_368

label label_367:
    "Scene label_367"
    jump end_368

label label_363:
    "Scene label_363"
    menu:
        "Use item":
            jump label_368
        "Open door":
            jump label_369
        "Open door":
            jump label_370

label label_368:
    "Scene label_368"
    jump end_371

label label_369:
    "Scene label_369"
    jump end_371

label label_370:
    "Scene label_370"
    jump end_371

label label_364:
    "Scene label_364"
    menu:
        "Use item":
            $ strength += 2
            jump label_371
        "Go forward":
            jump label_372
        "Talk":
            $ charisma += 1
            jump label_373

label label_371:
    "Scene label_371"
    jump end_374

label label_372:
    "Scene label_372"
    jump end_374

label label_373:
    "Scene label_373"
    jump end_374

label label_360:
    "Scene label_360"
    menu:
        "Use item":
            jump label_374
        "Talk":
            $ strength += 3
            jump label_375

label label_374:
    "Scene label_374"
    menu:
        "Go back":
            $ strength += 1
            jump label_376
        "Open door":
            jump label_377

label label_376:
    "Scene label_376"
    jump end_378

label label_377:
    "Scene label_377"
    jump end_378

label label_375:
    "Scene label_375"
    menu:
        "Pick up item":
            jump label_378
        "Go forward":
            jump label_379
        "Open door":
            $ intelligence += 1
            jump label_380

label label_378:
    "Scene label_378"
    jump end_381

label label_379:
    "Scene label_379"
    jump end_381

label label_380:
    "Scene label_380"
    jump end_381

label label_361:
    "Scene label_361"
    menu:
        "Look around":
            jump label_381
        "Look around":
            jump label_382

label label_381:
    "Scene label_381"
    menu:
        "Open door":
            $ charisma += 3
            jump label_383
        "Pick up item":
            $ luck += 2
            jump label_384
        "Talk":
            jump label_385

label label_383:
    "Scene label_383"
    jump end_386

label label_384:
    "Scene label_384"
    jump end_386

label label_385:
    "Scene label_385"
    jump end_386

label label_382:
    "Scene label_382"
    menu:
        "Go forward":
            $ luck += 3
            jump label_386
        "Use item":
            $ charisma += 2
            jump label_387
        "Explore":
            $ luck += 2
            jump label_388

label label_386:
    "Scene label_386"
    jump end_389

label label_387:
    "Scene label_387"
    jump end_389

label label_388:
    "Scene label_388"
    jump end_389

label label_278:
    "Scene label_278"
    if charisma >= 8:
        jump label_389

label label_389:
    $ charisma += 3
    if charisma >= 15:
        jump label_390

label label_390:
    $ charisma += 4
    menu:
        "Use item":
            $ charisma += 3
            jump label_391
        "Pick up item":
            jump label_392

label label_391:
    "Scene label_391"
    menu:
        "Talk":
            $ charisma += 1
            jump label_393
        "Go forward":
            $ intelligence += 1
            jump label_394

label label_393:
    "Scene label_393"
    if charisma >= 6:
        jump label_395

label label_395:
    $ charisma += 4
    jump end_396

    jump label_396

label label_396:
    "Ветка false для label_395"
    jump end_397

label label_394:
    "Scene label_394"
    menu:
        "Explore":
            jump label_397
        "Open door":
            jump label_398
        "Look around":
            jump label_399

label label_397:
    "Scene label_397"
    jump end_400

label label_398:
    "Scene label_398"
    jump end_400

label label_399:
    "Scene label_399"
    jump end_400

label label_392:
    "Scene label_392"
    if charisma >= 19:
        jump label_400

label label_400:
    $ charisma += 3
    menu:
        "Explore":
            $ luck += 3
            jump label_401
        "Look around":
            $ charisma += 1
            jump label_402
        "Talk":
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

    jump label_404

label label_404:
    "Ветка false для label_400"
    menu:
        "Use item":
            jump label_405
        "Use item":
            $ charisma += 3
            jump label_406

label label_405:
    "Scene label_405"
    jump end_407

label label_406:
    "Scene label_406"
    jump end_407

    jump label_407

label label_407:
    "Ветка false для label_390"
    if strength >= 20:
        jump label_408

label label_408:
    $ strength += 3
    menu:
        "Use item":
            $ luck += 3
            jump label_409
        "Go back":
            $ charisma += 2
            jump label_410

label label_409:
    "Scene label_409"
    menu:
        "Pick up item":
            $ charisma += 3
            jump label_411
        "Look around":
            $ luck += 3
            jump label_412

label label_411:
    "Scene label_411"
    jump end_413

label label_412:
    "Scene label_412"
    jump end_413

label label_410:
    "Scene label_410"
    menu:
        "Go back":
            jump label_413
        "Pick up item":
            $ luck += 3
            jump label_414
        "Explore":
            jump label_415

label label_413:
    "Scene label_413"
    jump end_416

label label_414:
    "Scene label_414"
    jump end_416

label label_415:
    "Scene label_415"
    jump end_416

    jump label_416

label label_416:
    "Ветка false для label_408"
    if luck >= 11:
        jump label_417

label label_417:
    $ luck += 3
    menu:
        "Go forward":
            jump label_418
        "Open door":
            jump label_419

label label_418:
    "Scene label_418"
    jump end_420

label label_419:
    "Scene label_419"
    jump end_420

    jump label_420

label label_420:
    "Ветка false для label_417"
    menu:
        "Pick up item":
            jump label_421
        "Go back":
            jump label_422

label label_421:
    "Scene label_421"
    jump end_423

label label_422:
    "Scene label_422"
    jump end_423

    jump label_423

label label_423:
    "Ветка false для label_389"
    menu:
        "Use item":
            $ intelligence += 3
            jump label_424
        "Pick up item":
            jump label_425

label label_424:
    "Scene label_424"
    menu:
        "Talk":
            jump label_426
        "Talk":
            $ charisma += 1
            jump label_427
        "Go back":
            jump label_428

label label_426:
    "Scene label_426"
    menu:
        "Explore":
            jump label_429
        "Use item":
            $ luck += 2
            jump label_430

label label_429:
    "Scene label_429"
    menu:
        "Explore":
            $ luck += 2
            jump label_431
        "Look around":
            $ strength += 2
            jump label_432
        "Use item":
            jump label_433

label label_431:
    "Scene label_431"
    jump end_434

label label_432:
    "Scene label_432"
    jump end_434

label label_433:
    "Scene label_433"
    jump end_434

label label_430:
    "Scene label_430"
    menu:
        "Go back":
            $ intelligence += 1
            jump label_434
        "Use item":
            $ charisma += 1
            jump label_435
        "Explore":
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

label label_427:
    "Scene label_427"
    if strength >= 20:
        jump label_437

label label_437:
    $ strength += 4
    menu:
        "Explore":
            jump label_438
        "Go forward":
            $ intelligence += 1
            jump label_439

label label_438:
    "Scene label_438"
    jump end_440

label label_439:
    "Scene label_439"
    jump end_440

    jump label_440

label label_440:
    "Ветка false для label_437"
    menu:
        "Pick up item":
            jump label_441
        "Look around":
            $ charisma += 3
            jump label_442

label label_441:
    "Scene label_441"
    jump end_443

label label_442:
    "Scene label_442"
    jump end_443

label label_428:
    "Scene label_428"
    menu:
        "Pick up item":
            $ strength += 3
            jump label_443
        "Use item":
            jump label_444
        "Go forward":
            jump label_445

label label_443:
    "Scene label_443"
    menu:
        "Go forward":
            jump label_446
        "Use item":
            $ luck += 2
            jump label_447

label label_446:
    "Scene label_446"
    jump end_448

label label_447:
    "Scene label_447"
    jump end_448

label label_444:
    "Scene label_444"
    if charisma >= 14:
        jump label_448

label label_448:
    $ charisma += 3
    jump end_449

    jump label_449

label label_449:
    "Ветка false для label_448"
    jump end_450

label label_445:
    "Scene label_445"
    if strength >= 14:
        jump label_450

label label_450:
    $ strength += 4
    jump end_451

    jump label_451

label label_451:
    "Ветка false для label_450"
    jump end_452

label label_425:
    "Scene label_425"
    menu:
        "Open door":
            jump label_452
        "Talk":
            $ charisma += 2
            jump label_453
        "Use item":
            $ charisma += 1
            jump label_454

label label_452:
    "Scene label_452"
    if intelligence >= 11:
        jump label_455

label label_455:
    $ intelligence += 2
    menu:
        "Look around":
            $ strength += 2
            jump label_456
        "Go back":
            jump label_457

label label_456:
    "Scene label_456"
    jump end_458

label label_457:
    "Scene label_457"
    jump end_458

    jump label_458

label label_458:
    "Ветка false для label_455"
    menu:
        "Look around":
            jump label_459
        "Go forward":
            $ strength += 2
            jump label_460

label label_459:
    "Scene label_459"
    jump end_461

label label_460:
    "Scene label_460"
    jump end_461

label label_453:
    "Scene label_453"
    menu:
        "Go back":
            $ intelligence += 1
            jump label_461
        "Go forward":
            $ strength += 3
            jump label_462

label label_461:
    "Scene label_461"
    menu:
        "Open door":
            jump label_463
        "Look around":
            jump label_464

label label_463:
    "Scene label_463"
    jump end_465

label label_464:
    "Scene label_464"
    jump end_465

label label_462:
    "Scene label_462"
    menu:
        "Look around":
            jump label_465
        "Pick up item":
            $ intelligence += 2
            jump label_466
        "Use item":
            $ charisma += 2
            jump label_467

label label_465:
    "Scene label_465"
    jump end_468

label label_466:
    "Scene label_466"
    jump end_468

label label_467:
    "Scene label_467"
    jump end_468

label label_454:
    "Scene label_454"
    if charisma >= 11:
        jump label_468

label label_468:
    $ charisma += 5
    menu:
        "Go forward":
            jump label_469
        "Look around":
            jump label_470

label label_469:
    "Scene label_469"
    jump end_471

label label_470:
    "Scene label_470"
    jump end_471

    jump label_471

label label_471:
    "Ветка false для label_468"
    menu:
        "Look around":
            jump label_472
        "Look around":
            jump label_473

label label_472:
    "Scene label_472"
    jump end_474

label label_473:
    "Scene label_473"
    jump end_474

label label_11:
    "Scene label_11"
    if luck >= 12:
        jump label_474

label label_474:
    $ luck += 5
    menu:
        "Go back":
            $ strength += 1
            jump label_475
        "Go forward":
            jump label_476
        "Explore":
            jump label_477

label label_475:
    "Scene label_475"
    menu:
        "Look around":
            jump label_478
        "Go forward":
            $ intelligence += 3
            jump label_479

label label_478:
    "Scene label_478"
    menu:
        "Explore":
            jump label_480
        "Go back":
            jump label_481
        "Look around":
            $ luck += 1
            jump label_482

label label_480:
    "Scene label_480"
    if charisma >= 19:
        jump label_483

label label_483:
    $ charisma += 4
    menu:
        "Open door":
            jump label_484
        "Talk":
            $ strength += 1
            jump label_485
        "Look around":
            $ charisma += 3
            jump label_486

label label_484:
    "Scene label_484"
    menu:
        "Open door":
            jump label_487
        "Go forward":
            jump label_488

label label_487:
    "Scene label_487"
    jump end_489

label label_488:
    "Scene label_488"
    jump end_489

label label_485:
    "Scene label_485"
    menu:
        "Pick up item":
            jump label_489
        "Look around":
            jump label_490

label label_489:
    "Scene label_489"
    jump end_491

label label_490:
    "Scene label_490"
    jump end_491

label label_486:
    "Scene label_486"
    menu:
        "Go back":
            jump label_491
        "Go forward":
            jump label_492

label label_491:
    "Scene label_491"
    jump end_493

label label_492:
    "Scene label_492"
    jump end_493

    jump label_493

label label_493:
    "Ветка false для label_483"
    menu:
        "Explore":
            jump label_494
        "Look around":
            $ intelligence += 2
            jump label_495

label label_494:
    "Scene label_494"
    menu:
        "Talk":
            jump label_496
        "Go forward":
            $ intelligence += 3
            jump label_497
        "Pick up item":
            jump label_498

label label_496:
    "Scene label_496"
    jump end_499

label label_497:
    "Scene label_497"
    jump end_499

label label_498:
    "Scene label_498"
    jump end_499

label label_495:
    "Scene label_495"
    menu:
        "Pick up item":
            $ luck += 2
            jump label_499
        "Go forward":
            jump label_500

label label_499:
    "Scene label_499"
    jump end_501

label label_500:
    "Scene label_500"
    jump end_501

label label_481:
    "Scene label_481"
    menu:
        "Open door":
            jump label_501
        "Look around":
            $ charisma += 1
            jump label_502
        "Pick up item":
            $ strength += 2
            jump label_503

label label_501:
    "Scene label_501"
    menu:
        "Look around":
            $ strength += 3
            jump label_504
        "Go forward":
            jump label_505

label label_504:
    "Scene label_504"
    menu:
        "Use item":
            jump label_506
        "Pick up item":
            jump label_507
        "Explore":
            jump label_508

label label_506:
    "Scene label_506"
    jump end_509

label label_507:
    "Scene label_507"
    jump end_509

label label_508:
    "Scene label_508"
    jump end_509

label label_505:
    "Scene label_505"
    menu:
        "Explore":
            jump label_509
        "Pick up item":
            jump label_510
        "Explore":
            jump label_511

label label_509:
    "Scene label_509"
    jump end_512

label label_510:
    "Scene label_510"
    jump end_512

label label_511:
    "Scene label_511"
    jump end_512

label label_502:
    "Scene label_502"
    if intelligence >= 5:
        jump label_512

label label_512:
    $ intelligence += 4
    menu:
        "Explore":
            jump label_513
        "Go forward":
            jump label_514
        "Pick up item":
            $ charisma += 1
            jump label_515

label label_513:
    "Scene label_513"
    jump end_516

label label_514:
    "Scene label_514"
    jump end_516

label label_515:
    "Scene label_515"
    jump end_516

    jump label_516

label label_516:
    "Ветка false для label_512"
    if intelligence >= 11:
        jump label_517

label label_517:
    $ intelligence += 2
    jump end_518

    jump label_518

label label_518:
    "Ветка false для label_517"
    jump end_519

label label_503:
    "Scene label_503"
    menu:
        "Use item":
            $ intelligence += 3
            jump label_519
        "Explore":
            $ charisma += 1
            jump label_520
        "Look around":
            jump label_521

label label_519:
    "Scene label_519"
    menu:
        "Pick up item":
            $ strength += 3
            jump label_522
        "Open door":
            jump label_523

label label_522:
    "Scene label_522"
    jump end_524

label label_523:
    "Scene label_523"
    jump end_524

label label_520:
    "Scene label_520"
    menu:
        "Talk":
            jump label_524
        "Talk":
            $ luck += 3
            jump label_525

label label_524:
    "Scene label_524"
    jump end_526

label label_525:
    "Scene label_525"
    jump end_526

label label_521:
    "Scene label_521"
    menu:
        "Use item":
            $ luck += 2
            jump label_526
        "Pick up item":
            jump label_527
        "Talk":
            $ luck += 3
            jump label_528

label label_526:
    "Scene label_526"
    jump end_529

label label_527:
    "Scene label_527"
    jump end_529

label label_528:
    "Scene label_528"
    jump end_529

label label_482:
    "Scene label_482"
    menu:
        "Use item":
            $ luck += 3
            jump label_529
        "Explore":
            jump label_530
        "Talk":
            jump label_531

label label_529:
    "Scene label_529"
    menu:
        "Explore":
            jump label_532
        "Explore":
            jump label_533

label label_532:
    "Scene label_532"
    menu:
        "Go back":
            jump label_534
        "Open door":
            jump label_535
        "Look around":
            $ intelligence += 1
            jump label_536

label label_534:
    "Scene label_534"
    jump end_537

label label_535:
    "Scene label_535"
    jump end_537

label label_536:
    "Scene label_536"
    jump end_537

label label_533:
    "Scene label_533"
    menu:
        "Go back":
            jump label_537
        "Talk":
            jump label_538

label label_537:
    "Scene label_537"
    jump end_539

label label_538:
    "Scene label_538"
    jump end_539

label label_530:
    "Scene label_530"
    menu:
        "Go forward":
            jump label_539
        "Go back":
            $ strength += 2
            jump label_540

label label_539:
    "Scene label_539"
    menu:
        "Use item":
            jump label_541
        "Open door":
            $ luck += 3
            jump label_542

label label_541:
    "Scene label_541"
    jump end_543

label label_542:
    "Scene label_542"
    jump end_543

label label_540:
    "Scene label_540"
    menu:
        "Open door":
            $ luck += 3
            jump label_543
        "Go forward":
            $ luck += 1
            jump label_544
        "Pick up item":
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

label label_531:
    "Scene label_531"
    menu:
        "Use item":
            jump label_546
        "Use item":
            $ intelligence += 3
            jump label_547
        "Look around":
            $ intelligence += 3
            jump label_548

label label_546:
    "Scene label_546"
    menu:
        "Go forward":
            $ luck += 1
            jump label_549
        "Talk":
            jump label_550
        "Go back":
            $ charisma += 3
            jump label_551

label label_549:
    "Scene label_549"
    jump end_552

label label_550:
    "Scene label_550"
    jump end_552

label label_551:
    "Scene label_551"
    jump end_552

label label_547:
    "Scene label_547"
    menu:
        "Talk":
            jump label_552
        "Go forward":
            jump label_553

label label_552:
    "Scene label_552"
    jump end_554

label label_553:
    "Scene label_553"
    jump end_554

label label_548:
    "Scene label_548"
    menu:
        "Pick up item":
            jump label_554
        "Explore":
            $ luck += 3
            jump label_555
        "Use item":
            jump label_556

label label_554:
    "Scene label_554"
    jump end_557

label label_555:
    "Scene label_555"
    jump end_557

label label_556:
    "Scene label_556"
    jump end_557

label label_479:
    "Scene label_479"
    menu:
        "Open door":
            jump label_557
        "Open door":
            $ intelligence += 1
            jump label_558

label label_557:
    "Scene label_557"
    menu:
        "Explore":
            $ charisma += 3
            jump label_559
        "Go forward":
            $ luck += 2
            jump label_560
        "Use item":
            jump label_561

label label_559:
    "Scene label_559"
    menu:
        "Go forward":
            jump label_562
        "Explore":
            $ strength += 2
            jump label_563

label label_562:
    "Scene label_562"
    if luck >= 5:
        jump label_564

label label_564:
    $ luck += 4
    jump end_565

    jump label_565

label label_565:
    "Ветка false для label_564"
    jump end_566

label label_563:
    "Scene label_563"
    menu:
        "Pick up item":
            $ intelligence += 2
            jump label_566
        "Look around":
            jump label_567
        "Talk":
            jump label_568

label label_566:
    "Scene label_566"
    jump end_569

label label_567:
    "Scene label_567"
    jump end_569

label label_568:
    "Scene label_568"
    jump end_569

label label_560:
    "Scene label_560"
    menu:
        "Look around":
            $ intelligence += 3
            jump label_569
        "Open door":
            jump label_570

label label_569:
    "Scene label_569"
    if charisma >= 7:
        jump label_571

label label_571:
    $ charisma += 3
    jump end_572

    jump label_572

label label_572:
    "Ветка false для label_571"
    jump end_573

label label_570:
    "Scene label_570"
    if luck >= 6:
        jump label_573

label label_573:
    $ luck += 2
    jump end_574

    jump label_574

label label_574:
    "Ветка false для label_573"
    jump end_575

label label_561:
    "Scene label_561"
    if intelligence >= 13:
        jump label_575

label label_575:
    $ intelligence += 2
    menu:
        "Go back":
            $ charisma += 3
            jump label_576
        "Open door":
            $ strength += 2
            jump label_577

label label_576:
    "Scene label_576"
    jump end_578

label label_577:
    "Scene label_577"
    jump end_578

    jump label_578

label label_578:
    "Ветка false для label_575"
    menu:
        "Look around":
            jump label_579
        "Go forward":
            jump label_580

label label_579:
    "Scene label_579"
    jump end_581

label label_580:
    "Scene label_580"
    jump end_581

label label_558:
    "Scene label_558"
    if strength >= 14:
        jump label_581

label label_581:
    $ strength += 4
    menu:
        "Pick up item":
            $ strength += 2
            jump label_582
        "Talk":
            jump label_583
        "Talk":
            jump label_584

label label_582:
    "Scene label_582"
    menu:
        "Talk":
            $ luck += 1
            jump label_585
        "Talk":
            $ strength += 3
            jump label_586
        "Open door":
            jump label_587

label label_585:
    "Scene label_585"
    jump end_588

label label_586:
    "Scene label_586"
    jump end_588

label label_587:
    "Scene label_587"
    jump end_588

label label_583:
    "Scene label_583"
    menu:
        "Use item":
            jump label_588
        "Explore":
            $ intelligence += 1
            jump label_589
        "Talk":
            $ luck += 1
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

label label_584:
    "Scene label_584"
    if strength >= 19:
        jump label_591

label label_591:
    $ strength += 2
    jump end_592

    jump label_592

label label_592:
    "Ветка false для label_591"
    jump end_593

    jump label_593

label label_593:
    "Ветка false для label_581"
    if strength >= 13:
        jump label_594

label label_594:
    $ strength += 2
    if charisma >= 15:
        jump label_595

label label_595:
    $ charisma += 4
    jump end_596

    jump label_596

label label_596:
    "Ветка false для label_595"
    jump end_597

    jump label_597

label label_597:
    "Ветка false для label_594"
    if intelligence >= 8:
        jump label_598

label label_598:
    $ intelligence += 4
    jump end_599

    jump label_599

label label_599:
    "Ветка false для label_598"
    jump end_600

label label_476:
    "Scene label_476"
    menu:
        "Explore":
            $ luck += 3
            jump label_600
        "Go back":
            jump label_601

label label_600:
    "Scene label_600"
    if luck >= 15:
        jump label_602

label label_602:
    $ luck += 5
    if luck >= 12:
        jump label_603

label label_603:
    $ luck += 3
    menu:
        "Go back":
            jump label_604
        "Talk":
            jump label_605
        "Explore":
            jump label_606

label label_604:
    "Scene label_604"
    menu:
        "Go back":
            $ strength += 1
            jump label_607
        "Look around":
            jump label_608
        "Talk":
            jump label_609

label label_607:
    "Scene label_607"
    jump end_610

label label_608:
    "Scene label_608"
    jump end_610

label label_609:
    "Scene label_609"
    jump end_610

label label_605:
    "Scene label_605"
    if strength >= 7:
        jump label_610

label label_610:
    $ strength += 2
    jump end_611

    jump label_611

label label_611:
    "Ветка false для label_610"
    jump end_612

label label_606:
    "Scene label_606"
    menu:
        "Open door":
            jump label_612
        "Use item":
            jump label_613

label label_612:
    "Scene label_612"
    jump end_614

label label_613:
    "Scene label_613"
    jump end_614

    jump label_614

label label_614:
    "Ветка false для label_603"
    menu:
        "Talk":
            $ intelligence += 3
            jump label_615
        "Go back":
            $ strength += 2
            jump label_616
        "Explore":
            jump label_617

label label_615:
    "Scene label_615"
    menu:
        "Talk":
            $ intelligence += 3
            jump label_618
        "Talk":
            jump label_619

label label_618:
    "Scene label_618"
    jump end_620

label label_619:
    "Scene label_619"
    jump end_620

label label_616:
    "Scene label_616"
    menu:
        "Go forward":
            $ charisma += 1
            jump label_620
        "Look around":
            $ intelligence += 1
            jump label_621
        "Use item":
            jump label_622

label label_620:
    "Scene label_620"
    jump end_623

label label_621:
    "Scene label_621"
    jump end_623

label label_622:
    "Scene label_622"
    jump end_623

label label_617:
    "Scene label_617"
    menu:
        "Pick up item":
            jump label_623
        "Go forward":
            $ luck += 1
            jump label_624
        "Go back":
            jump label_625

label label_623:
    "Scene label_623"
    jump end_626

label label_624:
    "Scene label_624"
    jump end_626

label label_625:
    "Scene label_625"
    jump end_626

    jump label_626

label label_626:
    "Ветка false для label_602"
    if intelligence >= 17:
        jump label_627

label label_627:
    $ intelligence += 5
    menu:
        "Go back":
            $ intelligence += 3
            jump label_628
        "Open door":
            $ luck += 2
            jump label_629

label label_628:
    "Scene label_628"
    menu:
        "Talk":
            $ intelligence += 1
            jump label_630
        "Go back":
            $ intelligence += 1
            jump label_631

label label_630:
    "Scene label_630"
    jump end_632

label label_631:
    "Scene label_631"
    jump end_632

label label_629:
    "Scene label_629"
    menu:
        "Use item":
            $ luck += 3
            jump label_632
        "Look around":
            $ charisma += 2
            jump label_633

label label_632:
    "Scene label_632"
    jump end_634

label label_633:
    "Scene label_633"
    jump end_634

    jump label_634

label label_634:
    "Ветка false для label_627"
    if intelligence >= 18:
        jump label_635

label label_635:
    $ intelligence += 2
    if intelligence >= 10:
        jump label_636

label label_636:
    $ intelligence += 3
    jump end_637

    jump label_637

label label_637:
    "Ветка false для label_636"
    jump end_638

    jump label_638

label label_638:
    "Ветка false для label_635"
    menu:
        "Talk":
            $ luck += 1
            jump label_639
        "Open door":
            jump label_640

label label_639:
    "Scene label_639"
    jump end_641

label label_640:
    "Scene label_640"
    jump end_641

label label_601:
    "Scene label_601"
label label_477:
    "Scene label_477"
label label_12:
    "Scene label_12"
label label_9:
    "Scene label_9"
label label_7:
    "Scene label_7"
label label_4:
    "Scene label_4"
label label_5:
    "Scene label_5"
label label_1:
    "Scene label_1"
label label_2:
    "Scene label_2"

label end_28:
    "Конец: end_28"

label end_28:
    "Конец: end_28"

label end_30:
    "Конец: end_30"

label end_30:
    "Конец: end_30"

label end_33:
    "Конец: end_33"

label end_33:
    "Конец: end_33"

label end_33:
    "Конец: end_33"

label end_40:
    "Конец: end_40"

label end_40:
    "Конец: end_40"

label end_40:
    "Конец: end_40"

label end_43:
    "Конец: end_43"

label end_43:
    "Конец: end_43"

label end_43:
    "Конец: end_43"

label end_45:
    "Конец: end_45"

label end_45:
    "Конец: end_45"

label end_51:
    "Конец: end_51"

label end_51:
    "Конец: end_51"

label end_51:
    "Конец: end_51"

label end_54:
    "Конец: end_54"

label end_54:
    "Конец: end_54"

label end_59:
    "Конец: end_59"

label end_59:
    "Конец: end_59"

label end_60:
    "Конец: end_60"

label end_61:
    "Конец: end_61"

label end_62:
    "Конец: end_62"

label end_63:
    "Конец: end_63"

label end_71:
    "Конец: end_71"

label end_71:
    "Конец: end_71"

label end_73:
    "Конец: end_73"

label end_73:
    "Конец: end_73"

label end_76:
    "Конец: end_76"

label end_77:
    "Конец: end_77"

label end_80:
    "Конец: end_80"

label end_80:
    "Конец: end_80"

label end_85:
    "Конец: end_85"

label end_86:
    "Конец: end_86"

label end_88:
    "Конец: end_88"

label end_88:
    "Конец: end_88"

label end_92:
    "Конец: end_92"

label end_93:
    "Конец: end_93"

label end_95:
    "Конец: end_95"

label end_95:
    "Конец: end_95"

label end_98:
    "Конец: end_98"

label end_98:
    "Конец: end_98"

label end_98:
    "Конец: end_98"

label end_103:
    "Конец: end_103"

label end_103:
    "Конец: end_103"

label end_104:
    "Конец: end_104"

label end_105:
    "Конец: end_105"

label end_110:
    "Конец: end_110"

label end_111:
    "Конец: end_111"

label end_113:
    "Конец: end_113"

label end_113:
    "Конец: end_113"

label end_115:
    "Конец: end_115"

label end_115:
    "Конец: end_115"

label end_124:
    "Конец: end_124"

label end_124:
    "Конец: end_124"

label end_124:
    "Конец: end_124"

label end_126:
    "Конец: end_126"

label end_126:
    "Конец: end_126"

label end_127:
    "Конец: end_127"

label end_128:
    "Конец: end_128"

label end_132:
    "Конец: end_132"

label end_133:
    "Конец: end_133"

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

label end_146:
    "Конец: end_146"

label end_146:
    "Конец: end_146"

label end_146:
    "Конец: end_146"

label end_150:
    "Конец: end_150"

label end_150:
    "Конец: end_150"

label end_150:
    "Конец: end_150"

label end_154:
    "Конец: end_154"

label end_154:
    "Конец: end_154"

label end_154:
    "Конец: end_154"

label end_159:
    "Конец: end_159"

label end_159:
    "Конец: end_159"

label end_159:
    "Конец: end_159"

label end_162:
    "Конец: end_162"

label end_162:
    "Конец: end_162"

label end_162:
    "Конец: end_162"

label end_171:
    "Конец: end_171"

label end_172:
    "Конец: end_172"

label end_176:
    "Конец: end_176"

label end_176:
    "Конец: end_176"

label end_176:
    "Конец: end_176"

label end_180:
    "Конец: end_180"

label end_181:
    "Конец: end_181"

label end_183:
    "Конец: end_183"

label end_183:
    "Конец: end_183"

label end_186:
    "Конец: end_186"

label end_186:
    "Конец: end_186"

label end_186:
    "Конец: end_186"

label end_190:
    "Конец: end_190"

label end_190:
    "Конец: end_190"

label end_192:
    "Конец: end_192"

label end_192:
    "Конец: end_192"

label end_200:
    "Конец: end_200"

label end_200:
    "Конец: end_200"

label end_200:
    "Конец: end_200"

label end_201:
    "Конец: end_201"

label end_202:
    "Конец: end_202"

label end_205:
    "Конец: end_205"

label end_205:
    "Конец: end_205"

label end_209:
    "Конец: end_209"

label end_209:
    "Конец: end_209"

label end_209:
    "Конец: end_209"

label end_212:
    "Конец: end_212"

label end_213:
    "Конец: end_213"

label end_214:
    "Конец: end_214"

label end_215:
    "Конец: end_215"

label end_224:
    "Конец: end_224"

label end_224:
    "Конец: end_224"

label end_224:
    "Конец: end_224"

label end_227:
    "Конец: end_227"

label end_227:
    "Конец: end_227"

label end_232:
    "Конец: end_232"

label end_232:
    "Конец: end_232"

label end_234:
    "Конец: end_234"

label end_234:
    "Конец: end_234"

label end_236:
    "Конец: end_236"

label end_236:
    "Конец: end_236"

label end_243:
    "Конец: end_243"

label end_243:
    "Конец: end_243"

label end_244:
    "Конец: end_244"

label end_245:
    "Конец: end_245"

label end_249:
    "Конец: end_249"

label end_249:
    "Конец: end_249"

label end_249:
    "Конец: end_249"

label end_251:
    "Конец: end_251"

label end_252:
    "Конец: end_252"

label end_255:
    "Конец: end_255"

label end_255:
    "Конец: end_255"

label end_258:
    "Конец: end_258"

label end_258:
    "Конец: end_258"

label end_263:
    "Конец: end_263"

label end_263:
    "Конец: end_263"

label end_263:
    "Конец: end_263"

label end_267:
    "Конец: end_267"

label end_267:
    "Конец: end_267"

label end_267:
    "Конец: end_267"

label end_272:
    "Конец: end_272"

label end_273:
    "Конец: end_273"

label end_274:
    "Конец: end_274"

label end_275:
    "Конец: end_275"

label end_276:
    "Конец: end_276"

label end_277:
    "Конец: end_277"

label end_287:
    "Конец: end_287"

label end_287:
    "Конец: end_287"

label end_290:
    "Конец: end_290"

label end_290:
    "Конец: end_290"

label end_295:
    "Конец: end_295"

label end_295:
    "Конец: end_295"

label end_297:
    "Конец: end_297"

label end_297:
    "Конец: end_297"

label end_304:
    "Конец: end_304"

label end_304:
    "Конец: end_304"

label end_304:
    "Конец: end_304"

label end_306:
    "Конец: end_306"

label end_306:
    "Конец: end_306"

label end_307:
    "Конец: end_307"

label end_308:
    "Конец: end_308"

label end_314:
    "Конец: end_314"

label end_314:
    "Конец: end_314"

label end_317:
    "Конец: end_317"

label end_317:
    "Конец: end_317"

label end_317:
    "Конец: end_317"

label end_319:
    "Конец: end_319"

label end_319:
    "Конец: end_319"

label end_328:
    "Конец: end_328"

label end_328:
    "Конец: end_328"

label end_331:
    "Конец: end_331"

label end_331:
    "Конец: end_331"

label end_331:
    "Конец: end_331"

label end_334:
    "Конец: end_334"

label end_334:
    "Конец: end_334"

label end_334:
    "Конец: end_334"

label end_339:
    "Конец: end_339"

label end_340:
    "Конец: end_340"

label end_342:
    "Конец: end_342"

label end_342:
    "Конец: end_342"

label end_343:
    "Конец: end_343"

label end_344:
    "Конец: end_344"

label end_349:
    "Конец: end_349"

label end_350:
    "Конец: end_350"

label end_351:
    "Конец: end_351"

label end_352:
    "Конец: end_352"

label end_356:
    "Конец: end_356"

label end_356:
    "Конец: end_356"

label end_359:
    "Конец: end_359"

label end_359:
    "Конец: end_359"

label end_359:
    "Конец: end_359"

label end_368:
    "Конец: end_368"

label end_368:
    "Конец: end_368"

label end_368:
    "Конец: end_368"

label end_371:
    "Конец: end_371"

label end_371:
    "Конец: end_371"

label end_371:
    "Конец: end_371"

label end_374:
    "Конец: end_374"

label end_374:
    "Конец: end_374"

label end_374:
    "Конец: end_374"

label end_378:
    "Конец: end_378"

label end_378:
    "Конец: end_378"

label end_381:
    "Конец: end_381"

label end_381:
    "Конец: end_381"

label end_381:
    "Конец: end_381"

label end_386:
    "Конец: end_386"

label end_386:
    "Конец: end_386"

label end_386:
    "Конец: end_386"

label end_389:
    "Конец: end_389"

label end_389:
    "Конец: end_389"

label end_389:
    "Конец: end_389"

label end_396:
    "Конец: end_396"

label end_397:
    "Конец: end_397"

label end_400:
    "Конец: end_400"

label end_400:
    "Конец: end_400"

label end_400:
    "Конец: end_400"

label end_404:
    "Конец: end_404"

label end_404:
    "Конец: end_404"

label end_404:
    "Конец: end_404"

label end_407:
    "Конец: end_407"

label end_407:
    "Конец: end_407"

label end_413:
    "Конец: end_413"

label end_413:
    "Конец: end_413"

label end_416:
    "Конец: end_416"

label end_416:
    "Конец: end_416"

label end_416:
    "Конец: end_416"

label end_420:
    "Конец: end_420"

label end_420:
    "Конец: end_420"

label end_423:
    "Конец: end_423"

label end_423:
    "Конец: end_423"

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

label end_440:
    "Конец: end_440"

label end_440:
    "Конец: end_440"

label end_443:
    "Конец: end_443"

label end_443:
    "Конец: end_443"

label end_448:
    "Конец: end_448"

label end_448:
    "Конец: end_448"

label end_449:
    "Конец: end_449"

label end_450:
    "Конец: end_450"

label end_451:
    "Конец: end_451"

label end_452:
    "Конец: end_452"

label end_458:
    "Конец: end_458"

label end_458:
    "Конец: end_458"

label end_461:
    "Конец: end_461"

label end_461:
    "Конец: end_461"

label end_465:
    "Конец: end_465"

label end_465:
    "Конец: end_465"

label end_468:
    "Конец: end_468"

label end_468:
    "Конец: end_468"

label end_468:
    "Конец: end_468"

label end_471:
    "Конец: end_471"

label end_471:
    "Конец: end_471"

label end_474:
    "Конец: end_474"

label end_474:
    "Конец: end_474"

label end_489:
    "Конец: end_489"

label end_489:
    "Конец: end_489"

label end_491:
    "Конец: end_491"

label end_491:
    "Конец: end_491"

label end_493:
    "Конец: end_493"

label end_493:
    "Конец: end_493"

label end_499:
    "Конец: end_499"

label end_499:
    "Конец: end_499"

label end_499:
    "Конец: end_499"

label end_501:
    "Конец: end_501"

label end_501:
    "Конец: end_501"

label end_509:
    "Конец: end_509"

label end_509:
    "Конец: end_509"

label end_509:
    "Конец: end_509"

label end_512:
    "Конец: end_512"

label end_512:
    "Конец: end_512"

label end_512:
    "Конец: end_512"

label end_516:
    "Конец: end_516"

label end_516:
    "Конец: end_516"

label end_516:
    "Конец: end_516"

label end_518:
    "Конец: end_518"

label end_519:
    "Конец: end_519"

label end_524:
    "Конец: end_524"

label end_524:
    "Конец: end_524"

label end_526:
    "Конец: end_526"

label end_526:
    "Конец: end_526"

label end_529:
    "Конец: end_529"

label end_529:
    "Конец: end_529"

label end_529:
    "Конец: end_529"

label end_537:
    "Конец: end_537"

label end_537:
    "Конец: end_537"

label end_537:
    "Конец: end_537"

label end_539:
    "Конец: end_539"

label end_539:
    "Конец: end_539"

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

label end_552:
    "Конец: end_552"

label end_552:
    "Конец: end_552"

label end_552:
    "Конец: end_552"

label end_554:
    "Конец: end_554"

label end_554:
    "Конец: end_554"

label end_557:
    "Конец: end_557"

label end_557:
    "Конец: end_557"

label end_557:
    "Конец: end_557"

label end_565:
    "Конец: end_565"

label end_566:
    "Конец: end_566"

label end_569:
    "Конец: end_569"

label end_569:
    "Конец: end_569"

label end_569:
    "Конец: end_569"

label end_572:
    "Конец: end_572"

label end_573:
    "Конец: end_573"

label end_574:
    "Конец: end_574"

label end_575:
    "Конец: end_575"

label end_578:
    "Конец: end_578"

label end_578:
    "Конец: end_578"

label end_581:
    "Конец: end_581"

label end_581:
    "Конец: end_581"

label end_588:
    "Конец: end_588"

label end_588:
    "Конец: end_588"

label end_588:
    "Конец: end_588"

label end_591:
    "Конец: end_591"

label end_591:
    "Конец: end_591"

label end_591:
    "Конец: end_591"

label end_592:
    "Конец: end_592"

label end_593:
    "Конец: end_593"

label end_596:
    "Конец: end_596"

label end_597:
    "Конец: end_597"

label end_599:
    "Конец: end_599"

label end_600:
    "Конец: end_600"

label end_610:
    "Конец: end_610"

label end_610:
    "Конец: end_610"

label end_610:
    "Конец: end_610"

label end_611:
    "Конец: end_611"

label end_612:
    "Конец: end_612"

label end_614:
    "Конец: end_614"

label end_614:
    "Конец: end_614"

label end_620:
    "Конец: end_620"

label end_620:
    "Конец: end_620"

label end_623:
    "Конец: end_623"

label end_623:
    "Конец: end_623"

label end_623:
    "Конец: end_623"

label end_626:
    "Конец: end_626"

label end_626:
    "Конец: end_626"

label end_626:
    "Конец: end_626"

label end_632:
    "Конец: end_632"

label end_632:
    "Конец: end_632"

label end_634:
    "Конец: end_634"

label end_634:
    "Конец: end_634"

label end_637:
    "Конец: end_637"

label end_638:
    "Конец: end_638"

label end_641:
    "Конец: end_641"

label end_641:
    "Конец: end_641"
