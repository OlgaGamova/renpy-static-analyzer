label start:
    $ strength = 0
    $ intelligence = 0
    $ luck = 0
    $ charisma = 0

    menu:
        "Open door":
            jump label_0
        "Look around":
            $ luck += 1
            jump label_1

label label_0:
    "Scene label_0"
    if strength >= 14:
        jump label_2

label label_2:
    $ strength += 4
    menu:
        "Use item":
            jump label_3
        "Talk":
            $ strength += 3
            jump label_4

label label_3:
    "Scene label_3"
    menu:
        "Pick up item":
            jump label_5
        "Talk":
            $ luck += 2
            jump label_6

label label_5:
    "Scene label_5"
    if strength >= 19:
        jump label_7

label label_7:
    $ strength += 4
    menu:
        "Look around":
            $ luck += 3
            jump label_8
        "Go back":
            jump label_9

label label_8:
    "Scene label_8"
    menu:
        "Pick up item":
            jump label_10
        "Use item":
            jump label_11
        "Pick up item":
            $ charisma += 3
            jump label_12

label label_10:
    "Scene label_10"
    menu:
        "Go back":
            $ charisma += 2
            jump label_13
        "Go forward":
            jump label_14
        "Go forward":
            jump label_15

label label_13:
    "Scene label_13"
    menu:
        "Use item":
            jump label_16
        "Explore":
            $ intelligence += 3
            jump label_17
        "Go back":
            jump label_18

label label_16:
    "Scene label_16"
    menu:
        "Look around":
            jump label_19
        "Go forward":
            $ charisma += 1
            jump label_20

label label_19:
    "Scene label_19"
    jump end_21

label label_20:
    "Scene label_20"
    jump end_21

label label_17:
    "Scene label_17"
    menu:
        "Look around":
            jump label_21
        "Explore":
            jump label_22

label label_21:
    "Scene label_21"
    jump end_23

label label_22:
    "Scene label_22"
    jump end_23

label label_18:
    "Scene label_18"
    if intelligence >= 16:
        jump label_23

label label_23:
    $ intelligence += 4
    jump end_24

    jump label_24

label label_24:
    "Ветка false для label_23"
    jump end_25

label label_14:
    "Scene label_14"
    menu:
        "Pick up item":
            jump label_25
        "Go back":
            jump label_26
        "Explore":
            jump label_27

label label_25:
    "Scene label_25"
    menu:
        "Talk":
            jump label_28
        "Use item":
            jump label_29

label label_28:
    "Scene label_28"
    jump end_30

label label_29:
    "Scene label_29"
    jump end_30

label label_26:
    "Scene label_26"
    menu:
        "Explore":
            $ charisma += 1
            jump label_30
        "Go back":
            jump label_31
        "Pick up item":
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

label label_27:
    "Scene label_27"
    menu:
        "Look around":
            jump label_33
        "Pick up item":
            $ luck += 3
            jump label_34
        "Use item":
            jump label_35

label label_33:
    "Scene label_33"
    jump end_36

label label_34:
    "Scene label_34"
    jump end_36

label label_35:
    "Scene label_35"
    jump end_36

label label_15:
    "Scene label_15"
    menu:
        "Go back":
            jump label_36
        "Look around":
            $ strength += 2
            jump label_37
        "Pick up item":
            $ intelligence += 3
            jump label_38

label label_36:
    "Scene label_36"
    if charisma >= 16:
        jump label_39

label label_39:
    $ charisma += 5
    jump end_40

    jump label_40

label label_40:
    "Ветка false для label_39"
    jump end_41

label label_37:
    "Scene label_37"
    menu:
        "Open door":
            jump label_41
        "Pick up item":
            jump label_42

label label_41:
    "Scene label_41"
    jump end_43

label label_42:
    "Scene label_42"
    jump end_43

label label_38:
    "Scene label_38"
    menu:
        "Go forward":
            jump label_43
        "Use item":
            $ intelligence += 2
            jump label_44
        "Look around":
            jump label_45

label label_43:
    "Scene label_43"
    jump end_46

label label_44:
    "Scene label_44"
    jump end_46

label label_45:
    "Scene label_45"
    jump end_46

label label_11:
    "Scene label_11"
    menu:
        "Go forward":
            $ intelligence += 1
            jump label_46
        "Pick up item":
            $ intelligence += 3
            jump label_47
        "Go forward":
            $ luck += 1
            jump label_48

label label_46:
    "Scene label_46"
    menu:
        "Look around":
            jump label_49
        "Use item":
            jump label_50

label label_49:
    "Scene label_49"
    menu:
        "Explore":
            jump label_51
        "Go forward":
            $ intelligence += 1
            jump label_52

label label_51:
    "Scene label_51"
    jump end_53

label label_52:
    "Scene label_52"
    jump end_53

label label_50:
    "Scene label_50"
    menu:
        "Look around":
            jump label_53
        "Go forward":
            $ luck += 1
            jump label_54

label label_53:
    "Scene label_53"
    jump end_55

label label_54:
    "Scene label_54"
    jump end_55

label label_47:
    "Scene label_47"
    menu:
        "Talk":
            $ intelligence += 3
            jump label_55
        "Open door":
            jump label_56

label label_55:
    "Scene label_55"
    menu:
        "Pick up item":
            jump label_57
        "Look around":
            $ intelligence += 3
            jump label_58
        "Go forward":
            jump label_59

label label_57:
    "Scene label_57"
    jump end_60

label label_58:
    "Scene label_58"
    jump end_60

label label_59:
    "Scene label_59"
    jump end_60

label label_56:
    "Scene label_56"
    menu:
        "Pick up item":
            jump label_60
        "Go forward":
            $ charisma += 2
            jump label_61
        "Open door":
            jump label_62

label label_60:
    "Scene label_60"
    jump end_63

label label_61:
    "Scene label_61"
    jump end_63

label label_62:
    "Scene label_62"
    jump end_63

label label_48:
    "Scene label_48"
    menu:
        "Look around":
            jump label_63
        "Explore":
            jump label_64
        "Look around":
            $ luck += 2
            jump label_65

label label_63:
    "Scene label_63"
    menu:
        "Pick up item":
            jump label_66
        "Open door":
            $ strength += 3
            jump label_67
        "Use item":
            $ intelligence += 2
            jump label_68

label label_66:
    "Scene label_66"
    jump end_69

label label_67:
    "Scene label_67"
    jump end_69

label label_68:
    "Scene label_68"
    jump end_69

label label_64:
    "Scene label_64"
    menu:
        "Open door":
            $ strength += 2
            jump label_69
        "Open door":
            $ luck += 2
            jump label_70
        "Talk":
            jump label_71

label label_69:
    "Scene label_69"
    jump end_72

label label_70:
    "Scene label_70"
    jump end_72

label label_71:
    "Scene label_71"
    jump end_72

label label_65:
    "Scene label_65"
    menu:
        "Look around":
            $ strength += 3
            jump label_72
        "Explore":
            jump label_73

label label_72:
    "Scene label_72"
    jump end_74

label label_73:
    "Scene label_73"
    jump end_74

label label_12:
    "Scene label_12"
    menu:
        "Look around":
            $ charisma += 3
            jump label_74
        "Go forward":
            jump label_75
        "Go back":
            $ intelligence += 1
            jump label_76

label label_74:
    "Scene label_74"
    menu:
        "Look around":
            $ luck += 1
            jump label_77
        "Go back":
            jump label_78

label label_77:
    "Scene label_77"
    menu:
        "Go back":
            $ luck += 3
            jump label_79
        "Go back":
            jump label_80

label label_79:
    "Scene label_79"
    jump end_81

label label_80:
    "Scene label_80"
    jump end_81

label label_78:
    "Scene label_78"
    menu:
        "Talk":
            jump label_81
        "Open door":
            $ strength += 1
            jump label_82

label label_81:
    "Scene label_81"
    jump end_83

label label_82:
    "Scene label_82"
    jump end_83

label label_75:
    "Scene label_75"
    menu:
        "Open door":
            $ luck += 1
            jump label_83
        "Explore":
            $ luck += 3
            jump label_84

label label_83:
    "Scene label_83"
    menu:
        "Talk":
            $ strength += 3
            jump label_85
        "Look around":
            $ charisma += 2
            jump label_86

label label_85:
    "Scene label_85"
    jump end_87

label label_86:
    "Scene label_86"
    jump end_87

label label_84:
    "Scene label_84"
    menu:
        "Go back":
            $ strength += 2
            jump label_87
        "Open door":
            $ charisma += 3
            jump label_88
        "Go back":
            $ charisma += 3
            jump label_89

label label_87:
    "Scene label_87"
    jump end_90

label label_88:
    "Scene label_88"
    jump end_90

label label_89:
    "Scene label_89"
    jump end_90

label label_76:
    "Scene label_76"
    if intelligence >= 14:
        jump label_90

label label_90:
    $ intelligence += 3
    menu:
        "Go back":
            $ strength += 2
            jump label_91
        "Open door":
            $ charisma += 3
            jump label_92
        "Use item":
            jump label_93

label label_91:
    "Scene label_91"
    jump end_94

label label_92:
    "Scene label_92"
    jump end_94

label label_93:
    "Scene label_93"
    jump end_94

    jump label_94

label label_94:
    "Ветка false для label_90"
    menu:
        "Look around":
            $ strength += 2
            jump label_95
        "Go forward":
            $ strength += 2
            jump label_96
        "Open door":
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

label label_9:
    "Scene label_9"
    menu:
        "Go back":
            $ strength += 2
            jump label_98
        "Talk":
            jump label_99
        "Pick up item":
            jump label_100

label label_98:
    "Scene label_98"
    menu:
        "Open door":
            jump label_101
        "Use item":
            $ charisma += 3
            jump label_102

label label_101:
    "Scene label_101"
    if luck >= 15:
        jump label_103

label label_103:
    $ luck += 3
    menu:
        "Look around":
            jump label_104
        "Look around":
            jump label_105

label label_104:
    "Scene label_104"
    jump end_106

label label_105:
    "Scene label_105"
    jump end_106

    jump label_106

label label_106:
    "Ветка false для label_103"
    if luck >= 16:
        jump label_107

label label_107:
    $ luck += 3
    jump end_108

    jump label_108

label label_108:
    "Ветка false для label_107"
    jump end_109

label label_102:
    "Scene label_102"
    if intelligence >= 13:
        jump label_109

label label_109:
    $ intelligence += 3
    if intelligence >= 7:
        jump label_110

label label_110:
    $ intelligence += 3
    jump end_111

    jump label_111

label label_111:
    "Ветка false для label_110"
    jump end_112

    jump label_112

label label_112:
    "Ветка false для label_109"
    menu:
        "Pick up item":
            jump label_113
        "Pick up item":
            jump label_114
        "Explore":
            jump label_115

label label_113:
    "Scene label_113"
    jump end_116

label label_114:
    "Scene label_114"
    jump end_116

label label_115:
    "Scene label_115"
    jump end_116

label label_99:
    "Scene label_99"
    menu:
        "Pick up item":
            $ charisma += 3
            jump label_116
        "Go back":
            jump label_117

label label_116:
    "Scene label_116"
    menu:
        "Look around":
            $ charisma += 1
            jump label_118
        "Go forward":
            $ luck += 1
            jump label_119
        "Look around":
            jump label_120

label label_118:
    "Scene label_118"
    menu:
        "Go forward":
            $ intelligence += 2
            jump label_121
        "Pick up item":
            jump label_122
        "Go forward":
            $ luck += 3
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
    if intelligence >= 6:
        jump label_124

label label_124:
    $ intelligence += 3
    jump end_125

    jump label_125

label label_125:
    "Ветка false для label_124"
    jump end_126

label label_120:
    "Scene label_120"
    menu:
        "Talk":
            $ luck += 2
            jump label_126
        "Open door":
            jump label_127
        "Go forward":
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
        "Explore":
            $ charisma += 2
            jump label_129
        "Go back":
            jump label_130

label label_129:
    "Scene label_129"
    menu:
        "Explore":
            $ intelligence += 2
            jump label_131
        "Go back":
            jump label_132

label label_131:
    "Scene label_131"
    jump end_133

label label_132:
    "Scene label_132"
    jump end_133

label label_130:
    "Scene label_130"
    menu:
        "Talk":
            jump label_133
        "Look around":
            $ charisma += 3
            jump label_134
        "Explore":
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

label label_100:
    "Scene label_100"
    menu:
        "Open door":
            jump label_136
        "Go forward":
            $ intelligence += 1
            jump label_137

label label_136:
    "Scene label_136"
    menu:
        "Use item":
            $ intelligence += 1
            jump label_138
        "Look around":
            $ strength += 3
            jump label_139
        "Go forward":
            jump label_140

label label_138:
    "Scene label_138"
    menu:
        "Open door":
            $ intelligence += 3
            jump label_141
        "Talk":
            jump label_142

label label_141:
    "Scene label_141"
    jump end_143

label label_142:
    "Scene label_142"
    jump end_143

label label_139:
    "Scene label_139"
    if luck >= 12:
        jump label_143

label label_143:
    $ luck += 5
    jump end_144

    jump label_144

label label_144:
    "Ветка false для label_143"
    jump end_145

label label_140:
    "Scene label_140"
    menu:
        "Use item":
            jump label_145
        "Go back":
            jump label_146
        "Pick up item":
            jump label_147

label label_145:
    "Scene label_145"
    jump end_148

label label_146:
    "Scene label_146"
    jump end_148

label label_147:
    "Scene label_147"
    jump end_148

label label_137:
    "Scene label_137"
    if charisma >= 19:
        jump label_148

label label_148:
    $ charisma += 4
    menu:
        "Talk":
            jump label_149
        "Talk":
            jump label_150
        "Go forward":
            jump label_151

label label_149:
    "Scene label_149"
    jump end_152

label label_150:
    "Scene label_150"
    jump end_152

label label_151:
    "Scene label_151"
    jump end_152

    jump label_152

label label_152:
    "Ветка false для label_148"
    menu:
        "Look around":
            $ intelligence += 2
            jump label_153
        "Pick up item":
            jump label_154

label label_153:
    "Scene label_153"
    jump end_155

label label_154:
    "Scene label_154"
    jump end_155

    jump label_155

label label_155:
    "Ветка false для label_7"
    if charisma >= 7:
        jump label_156

label label_156:
    $ charisma += 3
    menu:
        "Go forward":
            $ charisma += 3
            jump label_157
        "Explore":
            $ strength += 2
            jump label_158
        "Use item":
            $ strength += 3
            jump label_159

label label_157:
    "Scene label_157"
    menu:
        "Talk":
            $ charisma += 3
            jump label_160
        "Talk":
            jump label_161

label label_160:
    "Scene label_160"
    menu:
        "Look around":
            $ intelligence += 1
            jump label_162
        "Open door":
            $ luck += 1
            jump label_163

label label_162:
    "Scene label_162"
    menu:
        "Use item":
            $ charisma += 1
            jump label_164
        "Look around":
            jump label_165

label label_164:
    "Scene label_164"
    jump end_166

label label_165:
    "Scene label_165"
    jump end_166

label label_163:
    "Scene label_163"
    menu:
        "Use item":
            jump label_166
        "Go back":
            $ luck += 1
            jump label_167

label label_166:
    "Scene label_166"
    jump end_168

label label_167:
    "Scene label_167"
    jump end_168

label label_161:
    "Scene label_161"
    menu:
        "Look around":
            jump label_168
        "Explore":
            $ strength += 2
            jump label_169

label label_168:
    "Scene label_168"
    menu:
        "Open door":
            jump label_170
        "Go back":
            jump label_171

label label_170:
    "Scene label_170"
    jump end_172

label label_171:
    "Scene label_171"
    jump end_172

label label_169:
    "Scene label_169"
    menu:
        "Explore":
            $ strength += 3
            jump label_172
        "Explore":
            $ luck += 3
            jump label_173

label label_172:
    "Scene label_172"
    jump end_174

label label_173:
    "Scene label_173"
    jump end_174

label label_158:
    "Scene label_158"
    menu:
        "Pick up item":
            jump label_174
        "Pick up item":
            jump label_175

label label_174:
    "Scene label_174"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_176
        "Use item":
            jump label_177

label label_176:
    "Scene label_176"
    menu:
        "Open door":
            jump label_178
        "Pick up item":
            $ intelligence += 2
            jump label_179
        "Explore":
            jump label_180

label label_178:
    "Scene label_178"
    jump end_181

label label_179:
    "Scene label_179"
    jump end_181

label label_180:
    "Scene label_180"
    jump end_181

label label_177:
    "Scene label_177"
    if luck >= 13:
        jump label_181

label label_181:
    $ luck += 2
    jump end_182

    jump label_182

label label_182:
    "Ветка false для label_181"
    jump end_183

label label_175:
    "Scene label_175"
    menu:
        "Open door":
            jump label_183
        "Open door":
            $ intelligence += 2
            jump label_184
        "Pick up item":
            $ luck += 1
            jump label_185

label label_183:
    "Scene label_183"
    menu:
        "Open door":
            jump label_186
        "Talk":
            jump label_187

label label_186:
    "Scene label_186"
    jump end_188

label label_187:
    "Scene label_187"
    jump end_188

label label_184:
    "Scene label_184"
    menu:
        "Explore":
            jump label_188
        "Go back":
            $ charisma += 1
            jump label_189

label label_188:
    "Scene label_188"
    jump end_190

label label_189:
    "Scene label_189"
    jump end_190

label label_185:
    "Scene label_185"
    menu:
        "Pick up item":
            $ luck += 3
            jump label_190
        "Open door":
            $ strength += 1
            jump label_191
        "Open door":
            $ intelligence += 1
            jump label_192

label label_190:
    "Scene label_190"
    jump end_193

label label_191:
    "Scene label_191"
    jump end_193

label label_192:
    "Scene label_192"
    jump end_193

label label_159:
    "Scene label_159"
    if charisma >= 6:
        jump label_193

label label_193:
    $ charisma += 3
    if luck >= 16:
        jump label_194

label label_194:
    $ luck += 5
    menu:
        "Talk":
            jump label_195
        "Explore":
            $ strength += 3
            jump label_196

label label_195:
    "Scene label_195"
    jump end_197

label label_196:
    "Scene label_196"
    jump end_197

    jump label_197

label label_197:
    "Ветка false для label_194"
    if luck >= 17:
        jump label_198

label label_198:
    $ luck += 4
    jump end_199

    jump label_199

label label_199:
    "Ветка false для label_198"
    jump end_200

    jump label_200

label label_200:
    "Ветка false для label_193"
    menu:
        "Look around":
            $ intelligence += 2
            jump label_201
        "Open door":
            jump label_202

label label_201:
    "Scene label_201"
    if luck >= 19:
        jump label_203

label label_203:
    $ luck += 3
    jump end_204

    jump label_204

label label_204:
    "Ветка false для label_203"
    jump end_205

label label_202:
    "Scene label_202"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_205
        "Pick up item":
            $ charisma += 1
            jump label_206
        "Explore":
            jump label_207

label label_205:
    "Scene label_205"
    jump end_208

label label_206:
    "Scene label_206"
    jump end_208

label label_207:
    "Scene label_207"
    jump end_208

    jump label_208

label label_208:
    "Ветка false для label_156"
    menu:
        "Go back":
            jump label_209
        "Talk":
            jump label_210
        "Use item":
            $ intelligence += 1
            jump label_211

label label_209:
    "Scene label_209"
    if charisma >= 5:
        jump label_212

label label_212:
    $ charisma += 4
    menu:
        "Pick up item":
            jump label_213
        "Talk":
            jump label_214
        "Look around":
            $ charisma += 3
            jump label_215

label label_213:
    "Scene label_213"
    menu:
        "Open door":
            jump label_216
        "Look around":
            $ luck += 3
            jump label_217
        "Look around":
            $ luck += 1
            jump label_218

label label_216:
    "Scene label_216"
    jump end_219

label label_217:
    "Scene label_217"
    jump end_219

label label_218:
    "Scene label_218"
    jump end_219

label label_214:
    "Scene label_214"
    menu:
        "Talk":
            $ strength += 1
            jump label_219
        "Talk":
            $ intelligence += 2
            jump label_220

label label_219:
    "Scene label_219"
    jump end_221

label label_220:
    "Scene label_220"
    jump end_221

label label_215:
    "Scene label_215"
    menu:
        "Explore":
            jump label_221
        "Go back":
            jump label_222

label label_221:
    "Scene label_221"
    jump end_223

label label_222:
    "Scene label_222"
    jump end_223

    jump label_223

label label_223:
    "Ветка false для label_212"
    if luck >= 9:
        jump label_224

label label_224:
    $ luck += 4
    menu:
        "Talk":
            jump label_225
        "Talk":
            $ luck += 3
            jump label_226

label label_225:
    "Scene label_225"
    jump end_227

label label_226:
    "Scene label_226"
    jump end_227

    jump label_227

label label_227:
    "Ветка false для label_224"
    if strength >= 7:
        jump label_228

label label_228:
    $ strength += 2
    jump end_229

    jump label_229

label label_229:
    "Ветка false для label_228"
    jump end_230

label label_210:
    "Scene label_210"
    menu:
        "Use item":
            jump label_230
        "Open door":
            jump label_231
        "Go forward":
            $ luck += 3
            jump label_232

label label_230:
    "Scene label_230"
    menu:
        "Use item":
            jump label_233
        "Open door":
            $ strength += 3
            jump label_234
        "Go forward":
            $ charisma += 2
            jump label_235

label label_233:
    "Scene label_233"
    menu:
        "Talk":
            $ luck += 3
            jump label_236
        "Explore":
            jump label_237
        "Talk":
            jump label_238

label label_236:
    "Scene label_236"
    jump end_239

label label_237:
    "Scene label_237"
    jump end_239

label label_238:
    "Scene label_238"
    jump end_239

label label_234:
    "Scene label_234"
    menu:
        "Explore":
            $ strength += 2
            jump label_239
        "Pick up item":
            $ strength += 1
            jump label_240

label label_239:
    "Scene label_239"
    jump end_241

label label_240:
    "Scene label_240"
    jump end_241

label label_235:
    "Scene label_235"
    if charisma >= 18:
        jump label_241

label label_241:
    $ charisma += 3
    jump end_242

    jump label_242

label label_242:
    "Ветка false для label_241"
    jump end_243

label label_231:
    "Scene label_231"
    menu:
        "Explore":
            jump label_243
        "Explore":
            $ intelligence += 2
            jump label_244

label label_243:
    "Scene label_243"
    menu:
        "Pick up item":
            jump label_245
        "Pick up item":
            $ charisma += 3
            jump label_246
        "Pick up item":
            jump label_247

label label_245:
    "Scene label_245"
    jump end_248

label label_246:
    "Scene label_246"
    jump end_248

label label_247:
    "Scene label_247"
    jump end_248

label label_244:
    "Scene label_244"
    if luck >= 6:
        jump label_248

label label_248:
    $ luck += 2
    jump end_249

    jump label_249

label label_249:
    "Ветка false для label_248"
    jump end_250

label label_232:
    "Scene label_232"
    if charisma >= 14:
        jump label_250

label label_250:
    $ charisma += 2
    menu:
        "Talk":
            jump label_251
        "Explore":
            jump label_252
        "Explore":
            $ strength += 3
            jump label_253

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
    "Ветка false для label_250"
    menu:
        "Go back":
            $ charisma += 3
            jump label_255
        "Go back":
            jump label_256
        "Look around":
            $ strength += 2
            jump label_257

label label_255:
    "Scene label_255"
    jump end_258

label label_256:
    "Scene label_256"
    jump end_258

label label_257:
    "Scene label_257"
    jump end_258

label label_211:
    "Scene label_211"
    menu:
        "Explore":
            jump label_258
        "Use item":
            jump label_259
        "Open door":
            jump label_260

label label_258:
    "Scene label_258"
    if intelligence >= 15:
        jump label_261

label label_261:
    $ intelligence += 5
    menu:
        "Talk":
            $ luck += 1
            jump label_262
        "Open door":
            jump label_263

label label_262:
    "Scene label_262"
    jump end_264

label label_263:
    "Scene label_263"
    jump end_264

    jump label_264

label label_264:
    "Ветка false для label_261"
    menu:
        "Explore":
            jump label_265
        "Pick up item":
            jump label_266
        "Go back":
            $ strength += 2
            jump label_267

label label_265:
    "Scene label_265"
    jump end_268

label label_266:
    "Scene label_266"
    jump end_268

label label_267:
    "Scene label_267"
    jump end_268

label label_259:
    "Scene label_259"
    menu:
        "Open door":
            jump label_268
        "Go forward":
            jump label_269

label label_268:
    "Scene label_268"
    if intelligence >= 6:
        jump label_270

label label_270:
    $ intelligence += 5
    jump end_271

    jump label_271

label label_271:
    "Ветка false для label_270"
    jump end_272

label label_269:
    "Scene label_269"
    if charisma >= 9:
        jump label_272

label label_272:
    $ charisma += 3
    jump end_273

    jump label_273

label label_273:
    "Ветка false для label_272"
    jump end_274

label label_260:
    "Scene label_260"
    if strength >= 11:
        jump label_274

label label_274:
    $ strength += 2
    menu:
        "Talk":
            $ intelligence += 2
            jump label_275
        "Pick up item":
            jump label_276
        "Go forward":
            jump label_277

label label_275:
    "Scene label_275"
    jump end_278

label label_276:
    "Scene label_276"
    jump end_278

label label_277:
    "Scene label_277"
    jump end_278

    jump label_278

label label_278:
    "Ветка false для label_274"
    menu:
        "Pick up item":
            jump label_279
        "Explore":
            jump label_280
        "Pick up item":
            jump label_281

label label_279:
    "Scene label_279"
    jump end_282

label label_280:
    "Scene label_280"
    jump end_282

label label_281:
    "Scene label_281"
    jump end_282

label label_6:
    "Scene label_6"
    menu:
        "Go back":
            jump label_282
        "Use item":
            jump label_283
        "Go back":
            jump label_284

label label_282:
    "Scene label_282"
    if luck >= 14:
        jump label_285

label label_285:
    $ luck += 3
    menu:
        "Explore":
            $ luck += 2
            jump label_286
        "Look around":
            jump label_287
        "Open door":
            jump label_288

label label_286:
    "Scene label_286"
    menu:
        "Talk":
            $ luck += 3
            jump label_289
        "Look around":
            $ charisma += 3
            jump label_290
        "Go back":
            jump label_291

label label_289:
    "Scene label_289"
    if luck >= 13:
        jump label_292

label label_292:
    $ luck += 3
    if intelligence >= 12:
        jump label_293

label label_293:
    $ intelligence += 2
    jump end_294

    jump label_294

label label_294:
    "Ветка false для label_293"
    jump end_295

    jump label_295

label label_295:
    "Ветка false для label_292"
    menu:
        "Use item":
            $ charisma += 2
            jump label_296
        "Pick up item":
            $ intelligence += 1
            jump label_297

label label_296:
    "Scene label_296"
    jump end_298

label label_297:
    "Scene label_297"
    jump end_298

label label_290:
    "Scene label_290"
    menu:
        "Open door":
            jump label_298
        "Pick up item":
            $ intelligence += 2
            jump label_299

label label_298:
    "Scene label_298"
    menu:
        "Look around":
            jump label_300
        "Use item":
            jump label_301

label label_300:
    "Scene label_300"
    jump end_302

label label_301:
    "Scene label_301"
    jump end_302

label label_299:
    "Scene label_299"
    menu:
        "Talk":
            $ intelligence += 1
            jump label_302
        "Open door":
            jump label_303

label label_302:
    "Scene label_302"
    jump end_304

label label_303:
    "Scene label_303"
    jump end_304

label label_291:
    "Scene label_291"
    if luck >= 6:
        jump label_304

label label_304:
    $ luck += 2
    if strength >= 15:
        jump label_305

label label_305:
    $ strength += 4
    jump end_306

    jump label_306

label label_306:
    "Ветка false для label_305"
    jump end_307

    jump label_307

label label_307:
    "Ветка false для label_304"
    menu:
        "Talk":
            jump label_308
        "Pick up item":
            $ strength += 2
            jump label_309
        "Talk":
            jump label_310

label label_308:
    "Scene label_308"
    jump end_311

label label_309:
    "Scene label_309"
    jump end_311

label label_310:
    "Scene label_310"
    jump end_311

label label_287:
    "Scene label_287"
    menu:
        "Go forward":
            jump label_311
        "Go back":
            jump label_312

label label_311:
    "Scene label_311"
    menu:
        "Open door":
            jump label_313
        "Explore":
            $ strength += 1
            jump label_314

label label_313:
    "Scene label_313"
    menu:
        "Explore":
            jump label_315
        "Go forward":
            $ intelligence += 2
            jump label_316
        "Go back":
            jump label_317

label label_315:
    "Scene label_315"
    jump end_318

label label_316:
    "Scene label_316"
    jump end_318

label label_317:
    "Scene label_317"
    jump end_318

label label_314:
    "Scene label_314"
    menu:
        "Go back":
            jump label_318
        "Use item":
            $ strength += 2
            jump label_319

label label_318:
    "Scene label_318"
    jump end_320

label label_319:
    "Scene label_319"
    jump end_320

label label_312:
    "Scene label_312"
label label_288:
    "Scene label_288"
label label_283:
    "Scene label_283"
label label_284:
    "Scene label_284"
label label_4:
    "Scene label_4"
label label_1:
    "Scene label_1"

label end_21:
    "Конец: end_21"

label end_21:
    "Конец: end_21"

label end_23:
    "Конец: end_23"

label end_23:
    "Конец: end_23"

label end_24:
    "Конец: end_24"

label end_25:
    "Конец: end_25"

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

label end_36:
    "Конец: end_36"

label end_36:
    "Конец: end_36"

label end_36:
    "Конец: end_36"

label end_40:
    "Конец: end_40"

label end_41:
    "Конец: end_41"

label end_43:
    "Конец: end_43"

label end_43:
    "Конец: end_43"

label end_46:
    "Конец: end_46"

label end_46:
    "Конец: end_46"

label end_46:
    "Конец: end_46"

label end_53:
    "Конец: end_53"

label end_53:
    "Конец: end_53"

label end_55:
    "Конец: end_55"

label end_55:
    "Конец: end_55"

label end_60:
    "Конец: end_60"

label end_60:
    "Конец: end_60"

label end_60:
    "Конец: end_60"

label end_63:
    "Конец: end_63"

label end_63:
    "Конец: end_63"

label end_63:
    "Конец: end_63"

label end_69:
    "Конец: end_69"

label end_69:
    "Конец: end_69"

label end_69:
    "Конец: end_69"

label end_72:
    "Конец: end_72"

label end_72:
    "Конец: end_72"

label end_72:
    "Конец: end_72"

label end_74:
    "Конец: end_74"

label end_74:
    "Конец: end_74"

label end_81:
    "Конец: end_81"

label end_81:
    "Конец: end_81"

label end_83:
    "Конец: end_83"

label end_83:
    "Конец: end_83"

label end_87:
    "Конец: end_87"

label end_87:
    "Конец: end_87"

label end_90:
    "Конец: end_90"

label end_90:
    "Конец: end_90"

label end_90:
    "Конец: end_90"

label end_94:
    "Конец: end_94"

label end_94:
    "Конец: end_94"

label end_94:
    "Конец: end_94"

label end_98:
    "Конец: end_98"

label end_98:
    "Конец: end_98"

label end_98:
    "Конец: end_98"

label end_106:
    "Конец: end_106"

label end_106:
    "Конец: end_106"

label end_108:
    "Конец: end_108"

label end_109:
    "Конец: end_109"

label end_111:
    "Конец: end_111"

label end_112:
    "Конец: end_112"

label end_116:
    "Конец: end_116"

label end_116:
    "Конец: end_116"

label end_116:
    "Конец: end_116"

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

label end_133:
    "Конец: end_133"

label end_133:
    "Конец: end_133"

label end_136:
    "Конец: end_136"

label end_136:
    "Конец: end_136"

label end_136:
    "Конец: end_136"

label end_143:
    "Конец: end_143"

label end_143:
    "Конец: end_143"

label end_144:
    "Конец: end_144"

label end_145:
    "Конец: end_145"

label end_148:
    "Конец: end_148"

label end_148:
    "Конец: end_148"

label end_148:
    "Конец: end_148"

label end_152:
    "Конец: end_152"

label end_152:
    "Конец: end_152"

label end_152:
    "Конец: end_152"

label end_155:
    "Конец: end_155"

label end_155:
    "Конец: end_155"

label end_166:
    "Конец: end_166"

label end_166:
    "Конец: end_166"

label end_168:
    "Конец: end_168"

label end_168:
    "Конец: end_168"

label end_172:
    "Конец: end_172"

label end_172:
    "Конец: end_172"

label end_174:
    "Конец: end_174"

label end_174:
    "Конец: end_174"

label end_181:
    "Конец: end_181"

label end_181:
    "Конец: end_181"

label end_181:
    "Конец: end_181"

label end_182:
    "Конец: end_182"

label end_183:
    "Конец: end_183"

label end_188:
    "Конец: end_188"

label end_188:
    "Конец: end_188"

label end_190:
    "Конец: end_190"

label end_190:
    "Конец: end_190"

label end_193:
    "Конец: end_193"

label end_193:
    "Конец: end_193"

label end_193:
    "Конец: end_193"

label end_197:
    "Конец: end_197"

label end_197:
    "Конец: end_197"

label end_199:
    "Конец: end_199"

label end_200:
    "Конец: end_200"

label end_204:
    "Конец: end_204"

label end_205:
    "Конец: end_205"

label end_208:
    "Конец: end_208"

label end_208:
    "Конец: end_208"

label end_208:
    "Конец: end_208"

label end_219:
    "Конец: end_219"

label end_219:
    "Конец: end_219"

label end_219:
    "Конец: end_219"

label end_221:
    "Конец: end_221"

label end_221:
    "Конец: end_221"

label end_223:
    "Конец: end_223"

label end_223:
    "Конец: end_223"

label end_227:
    "Конец: end_227"

label end_227:
    "Конец: end_227"

label end_229:
    "Конец: end_229"

label end_230:
    "Конец: end_230"

label end_239:
    "Конец: end_239"

label end_239:
    "Конец: end_239"

label end_239:
    "Конец: end_239"

label end_241:
    "Конец: end_241"

label end_241:
    "Конец: end_241"

label end_242:
    "Конец: end_242"

label end_243:
    "Конец: end_243"

label end_248:
    "Конец: end_248"

label end_248:
    "Конец: end_248"

label end_248:
    "Конец: end_248"

label end_249:
    "Конец: end_249"

label end_250:
    "Конец: end_250"

label end_254:
    "Конец: end_254"

label end_254:
    "Конец: end_254"

label end_254:
    "Конец: end_254"

label end_258:
    "Конец: end_258"

label end_258:
    "Конец: end_258"

label end_258:
    "Конец: end_258"

label end_264:
    "Конец: end_264"

label end_264:
    "Конец: end_264"

label end_268:
    "Конец: end_268"

label end_268:
    "Конец: end_268"

label end_268:
    "Конец: end_268"

label end_271:
    "Конец: end_271"

label end_272:
    "Конец: end_272"

label end_273:
    "Конец: end_273"

label end_274:
    "Конец: end_274"

label end_278:
    "Конец: end_278"

label end_278:
    "Конец: end_278"

label end_278:
    "Конец: end_278"

label end_282:
    "Конец: end_282"

label end_282:
    "Конец: end_282"

label end_282:
    "Конец: end_282"

label end_294:
    "Конец: end_294"

label end_295:
    "Конец: end_295"

label end_298:
    "Конец: end_298"

label end_298:
    "Конец: end_298"

label end_302:
    "Конец: end_302"

label end_302:
    "Конец: end_302"

label end_304:
    "Конец: end_304"

label end_304:
    "Конец: end_304"

label end_306:
    "Конец: end_306"

label end_307:
    "Конец: end_307"

label end_311:
    "Конец: end_311"

label end_311:
    "Конец: end_311"

label end_311:
    "Конец: end_311"

label end_318:
    "Конец: end_318"

label end_318:
    "Конец: end_318"

label end_318:
    "Конец: end_318"

label end_320:
    "Конец: end_320"

label end_320:
    "Конец: end_320"
