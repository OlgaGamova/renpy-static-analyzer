label start:
    $ strength = 0
    $ intelligence = 0
    $ luck = 0
    $ charisma = 0

    menu:
        "Go back":
            jump label_0
        "Use item":
            $ charisma += 2
            jump label_1

label label_0:
    "Scene label_0"
    if charisma >= 9:
        jump label_2

label label_2:
    $ charisma += 3
    menu:
        "Go back":
            $ luck += 2
            jump label_3
        "Look around":
            $ charisma += 1
            jump label_4
        "Look around":
            $ charisma += 1
            jump label_5
        "Look around":
            $ strength += 3
            jump label_6

label label_3:
    "Scene label_3"
    menu:
        "Look around":
            $ intelligence += 3
            jump label_7
        "Go forward":
            jump label_8

label label_7:
    "Scene label_7"
    menu:
        "Open door":
            jump label_9
        "Explore":
            jump label_10
        "Open door":
            $ charisma += 2
            jump label_11
        "Explore":
            jump label_12

label label_9:
    "Scene label_9"
    menu:
        "Look around":
            $ luck += 2
            jump label_13
        "Use item":
            jump label_14
        "Look around":
            $ charisma += 2
            jump label_15
        "Use item":
            $ strength += 3
            jump label_16

label label_13:
    "Scene label_13"
    menu:
        "Go forward":
            $ intelligence += 3
            jump label_17
        "Explore":
            $ strength += 1
            jump label_18
        "Open door":
            jump label_19
        "Go back":
            $ charisma += 3
            jump label_20

label label_17:
    "Scene label_17"
    menu:
        "Open door":
            jump label_21
        "Open door":
            jump label_22
        "Pick up item":
            $ charisma += 2
            jump label_23

label label_21:
    "Scene label_21"
    menu:
        "Explore":
            jump label_24
        "Open door":
            jump label_25
        "Look around":
            jump label_26
        "Pick up item":
            jump label_27

label label_24:
    "Scene label_24"
    menu:
        "Use item":
            jump label_28
        "Explore":
            jump label_29

label label_28:
    "Scene label_28"
    menu:
        "Go forward":
            $ strength += 1
            jump label_30
        "Talk":
            $ charisma += 1
            jump label_31
        "Look around":
            $ luck += 1
            jump label_32
        "Go forward":
            jump label_33

label label_30:
    "Scene label_30"
    menu:
        "Go back":
            jump label_34
        "Go forward":
            jump label_35
        "Talk":
            jump label_36

label label_34:
    "Scene label_34"
    menu:
        "Go back":
            $ intelligence += 3
            jump label_37
        "Talk":
            jump label_38

label label_37:
    "Scene label_37"
    menu:
        "Go forward":
            jump label_39
        "Look around":
            jump label_40
        "Open door":
            $ charisma += 2
            jump label_41
        "Use item":
            jump label_42

label label_39:
    "Scene label_39"
    menu:
        "Look around":
            jump label_43
        "Explore":
            $ luck += 1
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
        "Pick up item":
            jump label_45
        "Go forward":
            $ charisma += 3
            jump label_46

label label_45:
    "Scene label_45"
    jump end_47

label label_46:
    "Scene label_46"
    jump end_47

label label_41:
    "Scene label_41"
    if strength >= 14:
        jump label_47

label label_47:
    $ strength += 4
    jump end_48

    jump label_48

label label_48:
    "Ветка false для label_47"
    jump end_49

label label_42:
    "Scene label_42"
    menu:
        "Go back":
            jump label_49
        "Go back":
            jump label_50
        "Open door":
            jump label_51
        "Use item":
            jump label_52

label label_49:
    "Scene label_49"
    jump end_53

label label_50:
    "Scene label_50"
    jump end_53

label label_51:
    "Scene label_51"
    jump end_53

label label_52:
    "Scene label_52"
    jump end_53

label label_38:
    "Scene label_38"
    menu:
        "Pick up item":
            jump label_53
        "Go forward":
            $ luck += 1
            jump label_54
        "Open door":
            jump label_55

label label_53:
    "Scene label_53"
    menu:
        "Use item":
            jump label_56
        "Open door":
            jump label_57
        "Go forward":
            jump label_58
        "Go back":
            $ strength += 2
            jump label_59

label label_56:
    "Scene label_56"
    jump end_60

label label_57:
    "Scene label_57"
    jump end_60

label label_58:
    "Scene label_58"
    jump end_60

label label_59:
    "Scene label_59"
    jump end_60

label label_54:
    "Scene label_54"
    menu:
        "Look around":
            jump label_60
        "Talk":
            $ luck += 1
            jump label_61
        "Go back":
            $ intelligence += 2
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

label label_55:
    "Scene label_55"
    menu:
        "Use item":
            jump label_63
        "Use item":
            $ intelligence += 3
            jump label_64

label label_63:
    "Scene label_63"
    jump end_65

label label_64:
    "Scene label_64"
    jump end_65

label label_35:
    "Scene label_35"
    menu:
        "Look around":
            jump label_65
        "Pick up item":
            jump label_66

label label_65:
    "Scene label_65"
    menu:
        "Go forward":
            jump label_67
        "Explore":
            jump label_68
        "Pick up item":
            jump label_69
        "Go back":
            $ luck += 2
            jump label_70

label label_67:
    "Scene label_67"
    if intelligence >= 6:
        jump label_71

label label_71:
    $ intelligence += 5
    jump end_72

    jump label_72

label label_72:
    "Ветка false для label_71"
    jump end_73

label label_68:
    "Scene label_68"
    menu:
        "Go forward":
            jump label_73
        "Open door":
            jump label_74
        "Talk":
            $ strength += 3
            jump label_75
        "Pick up item":
            $ strength += 1
            jump label_76

label label_73:
    "Scene label_73"
    jump end_77

label label_74:
    "Scene label_74"
    jump end_77

label label_75:
    "Scene label_75"
    jump end_77

label label_76:
    "Scene label_76"
    jump end_77

label label_69:
    "Scene label_69"
    menu:
        "Look around":
            $ luck += 1
            jump label_77
        "Go back":
            $ charisma += 3
            jump label_78
        "Explore":
            $ charisma += 2
            jump label_79

label label_77:
    "Scene label_77"
    jump end_80

label label_78:
    "Scene label_78"
    jump end_80

label label_79:
    "Scene label_79"
    jump end_80

label label_70:
    "Scene label_70"
    if luck >= 16:
        jump label_80

label label_80:
    $ luck += 5
    jump end_81

    jump label_81

label label_81:
    "Ветка false для label_80"
    jump end_82

label label_66:
    "Scene label_66"
    if intelligence >= 9:
        jump label_82

label label_82:
    $ intelligence += 3
    menu:
        "Go back":
            jump label_83
        "Open door":
            jump label_84
        "Use item":
            $ intelligence += 2
            jump label_85
        "Go forward":
            $ charisma += 1
            jump label_86

label label_83:
    "Scene label_83"
    jump end_87

label label_84:
    "Scene label_84"
    jump end_87

label label_85:
    "Scene label_85"
    jump end_87

label label_86:
    "Scene label_86"
    jump end_87

    jump label_87

label label_87:
    "Ветка false для label_82"
    menu:
        "Explore":
            jump label_88
        "Go back":
            $ strength += 2
            jump label_89
        "Look around":
            jump label_90
        "Go forward":
            $ luck += 2
            jump label_91

label label_88:
    "Scene label_88"
    jump end_92

label label_89:
    "Scene label_89"
    jump end_92

label label_90:
    "Scene label_90"
    jump end_92

label label_91:
    "Scene label_91"
    jump end_92

label label_36:
    "Scene label_36"
    menu:
        "Pick up item":
            jump label_92
        "Go back":
            $ luck += 2
            jump label_93

label label_92:
    "Scene label_92"
    if strength >= 16:
        jump label_94

label label_94:
    $ strength += 3
    menu:
        "Talk":
            jump label_95
        "Go back":
            $ charisma += 3
            jump label_96
        "Pick up item":
            jump label_97
        "Open door":
            jump label_98

label label_95:
    "Scene label_95"
    jump end_99

label label_96:
    "Scene label_96"
    jump end_99

label label_97:
    "Scene label_97"
    jump end_99

label label_98:
    "Scene label_98"
    jump end_99

    jump label_99

label label_99:
    "Ветка false для label_94"
    menu:
        "Talk":
            jump label_100
        "Explore":
            $ charisma += 1
            jump label_101

label label_100:
    "Scene label_100"
    jump end_102

label label_101:
    "Scene label_101"
    jump end_102

label label_93:
    "Scene label_93"
    if luck >= 12:
        jump label_102

label label_102:
    $ luck += 4
    menu:
        "Go back":
            jump label_103
        "Open door":
            $ charisma += 2
            jump label_104
        "Pick up item":
            $ intelligence += 1
            jump label_105

label label_103:
    "Scene label_103"
    jump end_106

label label_104:
    "Scene label_104"
    jump end_106

label label_105:
    "Scene label_105"
    jump end_106

    jump label_106

label label_106:
    "Ветка false для label_102"
    if intelligence >= 13:
        jump label_107

label label_107:
    $ intelligence += 2
    jump end_108

    jump label_108

label label_108:
    "Ветка false для label_107"
    jump end_109

label label_31:
    "Scene label_31"
    if charisma >= 8:
        jump label_109

label label_109:
    $ charisma += 2
    if charisma >= 6:
        jump label_110

label label_110:
    $ charisma += 2
    menu:
        "Look around":
            $ intelligence += 1
            jump label_111
        "Open door":
            $ intelligence += 3
            jump label_112
        "Go back":
            $ intelligence += 1
            jump label_113
        "Talk":
            $ luck += 2
            jump label_114

label label_111:
    "Scene label_111"
    menu:
        "Go back":
            jump label_115
        "Talk":
            jump label_116
        "Talk":
            jump label_117

label label_115:
    "Scene label_115"
    jump end_118

label label_116:
    "Scene label_116"
    jump end_118

label label_117:
    "Scene label_117"
    jump end_118

label label_112:
    "Scene label_112"
    menu:
        "Open door":
            jump label_118
        "Go back":
            jump label_119
        "Pick up item":
            jump label_120
        "Look around":
            $ luck += 2
            jump label_121

label label_118:
    "Scene label_118"
    jump end_122

label label_119:
    "Scene label_119"
    jump end_122

label label_120:
    "Scene label_120"
    jump end_122

label label_121:
    "Scene label_121"
    jump end_122

label label_113:
    "Scene label_113"
    if luck >= 5:
        jump label_122

label label_122:
    $ luck += 2
    jump end_123

    jump label_123

label label_123:
    "Ветка false для label_122"
    jump end_124

label label_114:
    "Scene label_114"
    menu:
        "Explore":
            $ strength += 3
            jump label_124
        "Pick up item":
            jump label_125

label label_124:
    "Scene label_124"
    jump end_126

label label_125:
    "Scene label_125"
    jump end_126

    jump label_126

label label_126:
    "Ветка false для label_110"
    menu:
        "Open door":
            jump label_127
        "Use item":
            jump label_128

label label_127:
    "Scene label_127"
    menu:
        "Open door":
            jump label_129
        "Open door":
            $ intelligence += 3
            jump label_130

label label_129:
    "Scene label_129"
    jump end_131

label label_130:
    "Scene label_130"
    jump end_131

label label_128:
    "Scene label_128"
    menu:
        "Open door":
            $ strength += 2
            jump label_131
        "Use item":
            jump label_132
        "Go back":
            $ luck += 2
            jump label_133

label label_131:
    "Scene label_131"
    jump end_134

label label_132:
    "Scene label_132"
    jump end_134

label label_133:
    "Scene label_133"
    jump end_134

    jump label_134

label label_134:
    "Ветка false для label_109"
    if strength >= 10:
        jump label_135

label label_135:
    $ strength += 3
    if charisma >= 19:
        jump label_136

label label_136:
    $ charisma += 4
    menu:
        "Use item":
            $ intelligence += 1
            jump label_137
        "Go forward":
            $ strength += 2
            jump label_138
        "Go back":
            $ charisma += 3
            jump label_139

label label_137:
    "Scene label_137"
    jump end_140

label label_138:
    "Scene label_138"
    jump end_140

label label_139:
    "Scene label_139"
    jump end_140

    jump label_140

label label_140:
    "Ветка false для label_136"
    if strength >= 9:
        jump label_141

label label_141:
    $ strength += 2
    jump end_142

    jump label_142

label label_142:
    "Ветка false для label_141"
    jump end_143

    jump label_143

label label_143:
    "Ветка false для label_135"
    menu:
        "Open door":
            $ charisma += 2
            jump label_144
        "Pick up item":
            jump label_145
        "Go forward":
            $ intelligence += 1
            jump label_146

label label_144:
    "Scene label_144"
    if charisma >= 7:
        jump label_147

label label_147:
    $ charisma += 5
    jump end_148

    jump label_148

label label_148:
    "Ветка false для label_147"
    jump end_149

label label_145:
    "Scene label_145"
    if luck >= 17:
        jump label_149

label label_149:
    $ luck += 2
    jump end_150

    jump label_150

label label_150:
    "Ветка false для label_149"
    jump end_151

label label_146:
    "Scene label_146"
    if intelligence >= 17:
        jump label_151

label label_151:
    $ intelligence += 5
    jump end_152

    jump label_152

label label_152:
    "Ветка false для label_151"
    jump end_153

label label_32:
    "Scene label_32"
    if strength >= 11:
        jump label_153

label label_153:
    $ strength += 5
    menu:
        "Use item":
            $ luck += 2
            jump label_154
        "Talk":
            jump label_155

label label_154:
    "Scene label_154"
    if strength >= 13:
        jump label_156

label label_156:
    $ strength += 5
    menu:
        "Explore":
            jump label_157
        "Use item":
            jump label_158

label label_157:
    "Scene label_157"
    jump end_159

label label_158:
    "Scene label_158"
    jump end_159

    jump label_159

label label_159:
    "Ветка false для label_156"
    if charisma >= 15:
        jump label_160

label label_160:
    $ charisma += 2
    jump end_161

    jump label_161

label label_161:
    "Ветка false для label_160"
    jump end_162

label label_155:
    "Scene label_155"
    if luck >= 8:
        jump label_162

label label_162:
    $ luck += 5
    menu:
        "Go forward":
            jump label_163
        "Pick up item":
            jump label_164

label label_163:
    "Scene label_163"
    jump end_165

label label_164:
    "Scene label_164"
    jump end_165

    jump label_165

label label_165:
    "Ветка false для label_162"
    if strength >= 12:
        jump label_166

label label_166:
    $ strength += 3
    jump end_167

    jump label_167

label label_167:
    "Ветка false для label_166"
    jump end_168

    jump label_168

label label_168:
    "Ветка false для label_153"
    menu:
        "Explore":
            jump label_169
        "Go forward":
            $ intelligence += 3
            jump label_170
        "Look around":
            $ intelligence += 2
            jump label_171
        "Explore":
            jump label_172

label label_169:
    "Scene label_169"
    menu:
        "Go forward":
            jump label_173
        "Explore":
            jump label_174

label label_173:
    "Scene label_173"
    if strength >= 20:
        jump label_175

label label_175:
    $ strength += 5
    jump end_176

    jump label_176

label label_176:
    "Ветка false для label_175"
    jump end_177

label label_174:
    "Scene label_174"
    menu:
        "Pick up item":
            $ intelligence += 3
            jump label_177
        "Explore":
            $ charisma += 2
            jump label_178
        "Talk":
            $ intelligence += 2
            jump label_179
        "Go back":
            jump label_180

label label_177:
    "Scene label_177"
    jump end_181

label label_178:
    "Scene label_178"
    jump end_181

label label_179:
    "Scene label_179"
    jump end_181

label label_180:
    "Scene label_180"
    jump end_181

label label_170:
    "Scene label_170"
    menu:
        "Go forward":
            jump label_181
        "Open door":
            jump label_182
        "Go forward":
            jump label_183

label label_181:
    "Scene label_181"
    menu:
        "Use item":
            $ strength += 3
            jump label_184
        "Open door":
            $ charisma += 3
            jump label_185
        "Talk":
            jump label_186
        "Explore":
            $ luck += 1
            jump label_187

label label_184:
    "Scene label_184"
    jump end_188

label label_185:
    "Scene label_185"
    jump end_188

label label_186:
    "Scene label_186"
    jump end_188

label label_187:
    "Scene label_187"
    jump end_188

label label_182:
    "Scene label_182"
    if strength >= 6:
        jump label_188

label label_188:
    $ strength += 3
    jump end_189

    jump label_189

label label_189:
    "Ветка false для label_188"
    jump end_190

label label_183:
    "Scene label_183"
    if strength >= 11:
        jump label_190

label label_190:
    $ strength += 2
    jump end_191

    jump label_191

label label_191:
    "Ветка false для label_190"
    jump end_192

label label_171:
    "Scene label_171"
    menu:
        "Go forward":
            jump label_192
        "Open door":
            jump label_193

label label_192:
    "Scene label_192"
    menu:
        "Go back":
            $ intelligence += 3
            jump label_194
        "Look around":
            $ intelligence += 3
            jump label_195
        "Pick up item":
            jump label_196
        "Look around":
            $ strength += 2
            jump label_197

label label_194:
    "Scene label_194"
    jump end_198

label label_195:
    "Scene label_195"
    jump end_198

label label_196:
    "Scene label_196"
    jump end_198

label label_197:
    "Scene label_197"
    jump end_198

label label_193:
    "Scene label_193"
    menu:
        "Explore":
            jump label_198
        "Go forward":
            jump label_199
        "Go back":
            jump label_200

label label_198:
    "Scene label_198"
    jump end_201

label label_199:
    "Scene label_199"
    jump end_201

label label_200:
    "Scene label_200"
    jump end_201

label label_172:
    "Scene label_172"
    menu:
        "Look around":
            jump label_201
        "Look around":
            $ intelligence += 3
            jump label_202
        "Open door":
            $ intelligence += 3
            jump label_203

label label_201:
    "Scene label_201"
    menu:
        "Open door":
            jump label_204
        "Explore":
            jump label_205

label label_204:
    "Scene label_204"
    jump end_206

label label_205:
    "Scene label_205"
    jump end_206

label label_202:
    "Scene label_202"
    menu:
        "Look around":
            $ intelligence += 3
            jump label_206
        "Open door":
            jump label_207
        "Talk":
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

label label_203:
    "Scene label_203"
    menu:
        "Explore":
            jump label_209
        "Explore":
            jump label_210
        "Open door":
            jump label_211

label label_209:
    "Scene label_209"
    jump end_212

label label_210:
    "Scene label_210"
    jump end_212

label label_211:
    "Scene label_211"
    jump end_212

label label_33:
    "Scene label_33"
    menu:
        "Explore":
            jump label_212
        "Use item":
            $ luck += 2
            jump label_213
        "Pick up item":
            $ charisma += 1
            jump label_214
        "Go forward":
            jump label_215

label label_212:
    "Scene label_212"
    menu:
        "Talk":
            jump label_216
        "Go back":
            $ intelligence += 1
            jump label_217
        "Explore":
            $ luck += 3
            jump label_218
        "Talk":
            $ charisma += 2
            jump label_219

label label_216:
    "Scene label_216"
    if luck >= 16:
        jump label_220

label label_220:
    $ luck += 3
    if luck >= 7:
        jump label_221

label label_221:
    $ luck += 5
    jump end_222

    jump label_222

label label_222:
    "Ветка false для label_221"
    jump end_223

    jump label_223

label label_223:
    "Ветка false для label_220"
    menu:
        "Look around":
            jump label_224
        "Pick up item":
            $ strength += 3
            jump label_225

label label_224:
    "Scene label_224"
    jump end_226

label label_225:
    "Scene label_225"
    jump end_226

label label_217:
    "Scene label_217"
    menu:
        "Open door":
            $ strength += 2
            jump label_226
        "Explore":
            jump label_227

label label_226:
    "Scene label_226"
    menu:
        "Use item":
            jump label_228
        "Go forward":
            jump label_229

label label_228:
    "Scene label_228"
    jump end_230

label label_229:
    "Scene label_229"
    jump end_230

label label_227:
    "Scene label_227"
    menu:
        "Go back":
            jump label_230
        "Explore":
            jump label_231

label label_230:
    "Scene label_230"
    jump end_232

label label_231:
    "Scene label_231"
    jump end_232

label label_218:
    "Scene label_218"
    if intelligence >= 9:
        jump label_232

label label_232:
    $ intelligence += 2
    menu:
        "Pick up item":
            jump label_233
        "Look around":
            $ luck += 2
            jump label_234
        "Talk":
            $ strength += 2
            jump label_235

label label_233:
    "Scene label_233"
    jump end_236

label label_234:
    "Scene label_234"
    jump end_236

label label_235:
    "Scene label_235"
    jump end_236

    jump label_236

label label_236:
    "Ветка false для label_232"
    menu:
        "Open door":
            $ charisma += 3
            jump label_237
        "Open door":
            jump label_238

label label_237:
    "Scene label_237"
    jump end_239

label label_238:
    "Scene label_238"
    jump end_239

label label_219:
    "Scene label_219"
    if intelligence >= 20:
        jump label_239

label label_239:
    $ intelligence += 3
    menu:
        "Use item":
            jump label_240
        "Use item":
            $ luck += 2
            jump label_241
        "Explore":
            jump label_242
        "Look around":
            $ charisma += 2
            jump label_243

label label_240:
    "Scene label_240"
    jump end_244

label label_241:
    "Scene label_241"
    jump end_244

label label_242:
    "Scene label_242"
    jump end_244

label label_243:
    "Scene label_243"
    jump end_244

    jump label_244

label label_244:
    "Ветка false для label_239"
    menu:
        "Explore":
            $ strength += 2
            jump label_245
        "Talk":
            jump label_246

label label_245:
    "Scene label_245"
    jump end_247

label label_246:
    "Scene label_246"
    jump end_247

label label_213:
    "Scene label_213"
    menu:
        "Talk":
            $ intelligence += 1
            jump label_247
        "Explore":
            $ strength += 1
            jump label_248
        "Go forward":
            $ intelligence += 2
            jump label_249

label label_247:
    "Scene label_247"
    if strength >= 14:
        jump label_250

label label_250:
    $ strength += 5
    menu:
        "Use item":
            jump label_251
        "Use item":
            $ luck += 3
            jump label_252
        "Pick up item":
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
        "Go forward":
            $ strength += 2
            jump label_255
        "Talk":
            $ intelligence += 3
            jump label_256
        "Go back":
            $ strength += 1
            jump label_257
        "Open door":
            jump label_258

label label_255:
    "Scene label_255"
    jump end_259

label label_256:
    "Scene label_256"
    jump end_259

label label_257:
    "Scene label_257"
    jump end_259

label label_258:
    "Scene label_258"
    jump end_259

label label_248:
    "Scene label_248"
    menu:
        "Explore":
            jump label_259
        "Go forward":
            $ charisma += 1
            jump label_260
        "Open door":
            jump label_261
        "Look around":
            jump label_262

label label_259:
    "Scene label_259"
    menu:
        "Look around":
            $ charisma += 3
            jump label_263
        "Go forward":
            $ luck += 2
            jump label_264
        "Pick up item":
            $ intelligence += 1
            jump label_265
        "Explore":
            jump label_266

label label_263:
    "Scene label_263"
    jump end_267

label label_264:
    "Scene label_264"
    jump end_267

label label_265:
    "Scene label_265"
    jump end_267

label label_266:
    "Scene label_266"
    jump end_267

label label_260:
    "Scene label_260"
    menu:
        "Use item":
            jump label_267
        "Go back":
            jump label_268
        "Go back":
            jump label_269

label label_267:
    "Scene label_267"
    jump end_270

label label_268:
    "Scene label_268"
    jump end_270

label label_269:
    "Scene label_269"
    jump end_270

label label_261:
    "Scene label_261"
    menu:
        "Go back":
            $ luck += 2
            jump label_270
        "Talk":
            $ charisma += 3
            jump label_271

label label_270:
    "Scene label_270"
    jump end_272

label label_271:
    "Scene label_271"
    jump end_272

label label_262:
    "Scene label_262"
    menu:
        "Use item":
            $ intelligence += 2
            jump label_272
        "Go back":
            jump label_273
        "Explore":
            $ intelligence += 1
            jump label_274
        "Talk":
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

label label_249:
    "Scene label_249"
    menu:
        "Talk":
            $ intelligence += 2
            jump label_276
        "Talk":
            jump label_277

label label_276:
    "Scene label_276"
    menu:
        "Explore":
            $ strength += 1
            jump label_278
        "Explore":
            jump label_279

label label_278:
    "Scene label_278"
    jump end_280

label label_279:
    "Scene label_279"
    jump end_280

label label_277:
    "Scene label_277"
    if strength >= 15:
        jump label_280

label label_280:
    $ strength += 5
    jump end_281

    jump label_281

label label_281:
    "Ветка false для label_280"
    jump end_282

label label_214:
    "Scene label_214"
    menu:
        "Pick up item":
            jump label_282
        "Go back":
            $ intelligence += 1
            jump label_283
        "Talk":
            $ luck += 3
            jump label_284

label label_282:
    "Scene label_282"
    menu:
        "Use item":
            $ strength += 2
            jump label_285
        "Look around":
            jump label_286

label label_285:
    "Scene label_285"
    menu:
        "Pick up item":
            jump label_287
        "Explore":
            $ charisma += 2
            jump label_288
        "Pick up item":
            $ intelligence += 1
            jump label_289
        "Go forward":
            $ strength += 2
            jump label_290

label label_287:
    "Scene label_287"
    jump end_291

label label_288:
    "Scene label_288"
    jump end_291

label label_289:
    "Scene label_289"
    jump end_291

label label_290:
    "Scene label_290"
    jump end_291

label label_286:
    "Scene label_286"
    menu:
        "Use item":
            jump label_291
        "Look around":
            $ charisma += 3
            jump label_292

label label_291:
    "Scene label_291"
    jump end_293

label label_292:
    "Scene label_292"
    jump end_293

label label_283:
    "Scene label_283"
    menu:
        "Pick up item":
            jump label_293
        "Open door":
            $ strength += 3
            jump label_294
        "Open door":
            jump label_295

label label_293:
    "Scene label_293"
    menu:
        "Go forward":
            jump label_296
        "Pick up item":
            $ strength += 1
            jump label_297
        "Open door":
            jump label_298
        "Go forward":
            jump label_299

label label_296:
    "Scene label_296"
    jump end_300

label label_297:
    "Scene label_297"
    jump end_300

label label_298:
    "Scene label_298"
    jump end_300

label label_299:
    "Scene label_299"
    jump end_300

label label_294:
    "Scene label_294"
    menu:
        "Go forward":
            $ charisma += 2
            jump label_300
        "Go back":
            jump label_301
        "Go back":
            $ charisma += 2
            jump label_302
        "Go forward":
            jump label_303

label label_300:
    "Scene label_300"
    jump end_304

label label_301:
    "Scene label_301"
    jump end_304

label label_302:
    "Scene label_302"
    jump end_304

label label_303:
    "Scene label_303"
    jump end_304

label label_295:
    "Scene label_295"
    menu:
        "Pick up item":
            $ strength += 1
            jump label_304
        "Talk":
            $ luck += 2
            jump label_305
        "Go forward":
            $ intelligence += 2
            jump label_306

label label_304:
    "Scene label_304"
    jump end_307

label label_305:
    "Scene label_305"
    jump end_307

label label_306:
    "Scene label_306"
    jump end_307

label label_284:
    "Scene label_284"
    if luck >= 10:
        jump label_307

label label_307:
    $ luck += 2
    if charisma >= 16:
        jump label_308

label label_308:
    $ charisma += 2
    jump end_309

    jump label_309

label label_309:
    "Ветка false для label_308"
    jump end_310

    jump label_310

label label_310:
    "Ветка false для label_307"
    menu:
        "Talk":
            $ charisma += 1
            jump label_311
        "Talk":
            jump label_312
        "Talk":
            $ intelligence += 1
            jump label_313

label label_311:
    "Scene label_311"
    jump end_314

label label_312:
    "Scene label_312"
    jump end_314

label label_313:
    "Scene label_313"
    jump end_314

label label_215:
    "Scene label_215"
    menu:
        "Open door":
            $ charisma += 2
            jump label_314
        "Talk":
            $ intelligence += 1
            jump label_315

label label_314:
    "Scene label_314"
    if luck >= 5:
        jump label_316

label label_316:
    $ luck += 5
    menu:
        "Go forward":
            jump label_317
        "Pick up item":
            $ charisma += 2
            jump label_318
        "Open door":
            $ strength += 1
            jump label_319

label label_317:
    "Scene label_317"
    jump end_320

label label_318:
    "Scene label_318"
    jump end_320

label label_319:
    "Scene label_319"
    jump end_320

    jump label_320

label label_320:
    "Ветка false для label_316"
    menu:
        "Use item":
            $ intelligence += 1
            jump label_321
        "Explore":
            $ strength += 3
            jump label_322
        "Go back":
            $ strength += 1
            jump label_323

label label_321:
    "Scene label_321"
    jump end_324

label label_322:
    "Scene label_322"
    jump end_324

label label_323:
    "Scene label_323"
    jump end_324

label label_315:
    "Scene label_315"
    if intelligence >= 10:
        jump label_324

label label_324:
    $ intelligence += 4
    menu:
        "Talk":
            jump label_325
        "Explore":
            jump label_326
        "Look around":
            jump label_327
        "Explore":
            $ charisma += 1
            jump label_328

label label_325:
    "Scene label_325"
    jump end_329

label label_326:
    "Scene label_326"
    jump end_329

label label_327:
    "Scene label_327"
    jump end_329

label label_328:
    "Scene label_328"
    jump end_329

    jump label_329

label label_329:
    "Ветка false для label_324"
    menu:
        "Look around":
            $ intelligence += 1
            jump label_330
        "Go back":
            $ charisma += 3
            jump label_331
        "Use item":
            jump label_332
        "Go forward":
            $ strength += 2
            jump label_333

label label_330:
    "Scene label_330"
    jump end_334

label label_331:
    "Scene label_331"
    jump end_334

label label_332:
    "Scene label_332"
    jump end_334

label label_333:
    "Scene label_333"
    jump end_334

label label_29:
    "Scene label_29"
    menu:
        "Go back":
            $ luck += 2
            jump label_334
        "Explore":
            jump label_335
        "Pick up item":
            jump label_336
        "Pick up item":
            $ intelligence += 3
            jump label_337

label label_334:
    "Scene label_334"
    if luck >= 11:
        jump label_338

label label_338:
    $ luck += 2
    if charisma >= 8:
        jump label_339

label label_339:
    $ charisma += 3
    menu:
        "Open door":
            $ luck += 3
            jump label_340
        "Use item":
            $ intelligence += 3
            jump label_341
        "Go back":
            $ strength += 2
            jump label_342

label label_340:
    "Scene label_340"
    menu:
        "Explore":
            jump label_343
        "Look around":
            jump label_344
        "Explore":
            $ strength += 1
            jump label_345
        "Use item":
            $ luck += 3
            jump label_346

label label_343:
    "Scene label_343"
    jump end_347

label label_344:
    "Scene label_344"
    jump end_347

label label_345:
    "Scene label_345"
    jump end_347

label label_346:
    "Scene label_346"
    jump end_347

label label_341:
    "Scene label_341"
    menu:
        "Go forward":
            jump label_347
        "Pick up item":
            $ charisma += 3
            jump label_348
        "Explore":
            $ charisma += 3
            jump label_349

label label_347:
    "Scene label_347"
    jump end_350

label label_348:
    "Scene label_348"
    jump end_350

label label_349:
    "Scene label_349"
    jump end_350

label label_342:
    "Scene label_342"
    if luck >= 15:
        jump label_350

label label_350:
    $ luck += 2
    jump end_351

    jump label_351

label label_351:
    "Ветка false для label_350"
    jump end_352

    jump label_352

label label_352:
    "Ветка false для label_339"
    if luck >= 16:
        jump label_353

label label_353:
    $ luck += 2
    menu:
        "Go forward":
            $ charisma += 3
            jump label_354
        "Talk":
            jump label_355
        "Open door":
            $ strength += 2
            jump label_356

label label_354:
    "Scene label_354"
    jump end_357

label label_355:
    "Scene label_355"
    jump end_357

label label_356:
    "Scene label_356"
    jump end_357

    jump label_357

label label_357:
    "Ветка false для label_353"
    menu:
        "Go forward":
            $ strength += 2
            jump label_358
        "Use item":
            $ luck += 1
            jump label_359
        "Go back":
            $ luck += 1
            jump label_360

label label_358:
    "Scene label_358"
    jump end_361

label label_359:
    "Scene label_359"
    jump end_361

label label_360:
    "Scene label_360"
    jump end_361

    jump label_361

label label_361:
    "Ветка false для label_338"
    menu:
        "Pick up item":
            jump label_362
        "Pick up item":
            jump label_363

label label_362:
    "Scene label_362"
    if luck >= 20:
        jump label_364

label label_364:
    $ luck += 4
    menu:
        "Look around":
            jump label_365
        "Talk":
            $ strength += 2
            jump label_366

label label_365:
    "Scene label_365"
    jump end_367

label label_366:
    "Scene label_366"
    jump end_367

    jump label_367

label label_367:
    "Ветка false для label_364"
    menu:
        "Look around":
            $ strength += 3
            jump label_368
        "Look around":
            $ strength += 1
            jump label_369
        "Go back":
            $ luck += 3
            jump label_370
        "Use item":
            $ intelligence += 2
            jump label_371

label label_368:
    "Scene label_368"
    jump end_372

label label_369:
    "Scene label_369"
    jump end_372

label label_370:
    "Scene label_370"
    jump end_372

label label_371:
    "Scene label_371"
    jump end_372

label label_363:
    "Scene label_363"
    if luck >= 19:
        jump label_372

label label_372:
    $ luck += 2
    if intelligence >= 13:
        jump label_373

label label_373:
    $ intelligence += 2
    jump end_374

    jump label_374

label label_374:
    "Ветка false для label_373"
    jump end_375

    jump label_375

label label_375:
    "Ветка false для label_372"
    if strength >= 11:
        jump label_376

label label_376:
    $ strength += 4
    jump end_377

    jump label_377

label label_377:
    "Ветка false для label_376"
    jump end_378

label label_335:
    "Scene label_335"
    menu:
        "Talk":
            jump label_378
        "Go back":
            jump label_379
        "Talk":
            $ luck += 3
            jump label_380

label label_378:
    "Scene label_378"
    menu:
        "Go forward":
            $ strength += 1
            jump label_381
        "Open door":
            $ charisma += 2
            jump label_382

label label_381:
    "Scene label_381"
    if charisma >= 16:
        jump label_383

label label_383:
    $ charisma += 4
    menu:
        "Look around":
            jump label_384
        "Pick up item":
            jump label_385

label label_384:
    "Scene label_384"
    jump end_386

label label_385:
    "Scene label_385"
    jump end_386

    jump label_386

label label_386:
    "Ветка false для label_383"
    if charisma >= 8:
        jump label_387

label label_387:
    $ charisma += 5
    jump end_388

    jump label_388

label label_388:
    "Ветка false для label_387"
    jump end_389

label label_382:
    "Scene label_382"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_389
        "Go back":
            jump label_390
        "Open door":
            $ luck += 2
            jump label_391
        "Pick up item":
            $ strength += 2
            jump label_392

label label_389:
    "Scene label_389"
    if charisma >= 19:
        jump label_393

label label_393:
    $ charisma += 3
    jump end_394

    jump label_394

label label_394:
    "Ветка false для label_393"
    jump end_395

label label_390:
    "Scene label_390"
    if luck >= 9:
        jump label_395

label label_395:
    $ luck += 2
    jump end_396

    jump label_396

label label_396:
    "Ветка false для label_395"
    jump end_397

label label_391:
    "Scene label_391"
    menu:
        "Look around":
            $ strength += 2
            jump label_397
        "Pick up item":
            $ charisma += 1
            jump label_398
        "Use item":
            jump label_399
        "Pick up item":
            $ luck += 1
            jump label_400

label label_397:
    "Scene label_397"
    jump end_401

label label_398:
    "Scene label_398"
    jump end_401

label label_399:
    "Scene label_399"
    jump end_401

label label_400:
    "Scene label_400"
    jump end_401

label label_392:
    "Scene label_392"
    menu:
        "Open door":
            jump label_401
        "Open door":
            jump label_402
        "Explore":
            jump label_403
        "Use item":
            $ strength += 3
            jump label_404

label label_401:
    "Scene label_401"
    jump end_405

label label_402:
    "Scene label_402"
    jump end_405

label label_403:
    "Scene label_403"
    jump end_405

label label_404:
    "Scene label_404"
    jump end_405

label label_379:
    "Scene label_379"
    menu:
        "Pick up item":
            $ charisma += 2
            jump label_405
        "Look around":
            jump label_406
        "Talk":
            $ charisma += 1
            jump label_407
        "Look around":
            jump label_408

label label_405:
    "Scene label_405"
    menu:
        "Explore":
            $ strength += 1
            jump label_409
        "Use item":
            jump label_410
        "Go forward":
            jump label_411

label label_409:
    "Scene label_409"
    menu:
        "Go back":
            $ charisma += 1
            jump label_412
        "Use item":
            jump label_413
        "Explore":
            $ luck += 2
            jump label_414

label label_412:
    "Scene label_412"
    jump end_415

label label_413:
    "Scene label_413"
    jump end_415

label label_414:
    "Scene label_414"
    jump end_415

label label_410:
    "Scene label_410"
    menu:
        "Look around":
            jump label_415
        "Open door":
            jump label_416
        "Go back":
            $ strength += 1
            jump label_417

label label_415:
    "Scene label_415"
    jump end_418

label label_416:
    "Scene label_416"
    jump end_418

label label_417:
    "Scene label_417"
    jump end_418

label label_411:
    "Scene label_411"
    menu:
        "Look around":
            jump label_418
        "Go forward":
            $ charisma += 3
            jump label_419
        "Explore":
            jump label_420

label label_418:
    "Scene label_418"
    jump end_421

label label_419:
    "Scene label_419"
    jump end_421

label label_420:
    "Scene label_420"
    jump end_421

label label_406:
    "Scene label_406"
    menu:
        "Use item":
            jump label_421
        "Pick up item":
            $ charisma += 2
            jump label_422
        "Open door":
            $ intelligence += 1
            jump label_423

label label_421:
    "Scene label_421"
    if strength >= 9:
        jump label_424

label label_424:
    $ strength += 5
    jump end_425

    jump label_425

label label_425:
    "Ветка false для label_424"
    jump end_426

label label_422:
    "Scene label_422"
    menu:
        "Look around":
            $ charisma += 2
            jump label_426
        "Open door":
            jump label_427

label label_426:
    "Scene label_426"
    jump end_428

label label_427:
    "Scene label_427"
    jump end_428

label label_423:
    "Scene label_423"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_428
        "Open door":
            jump label_429
        "Pick up item":
            jump label_430

label label_428:
    "Scene label_428"
    jump end_431

label label_429:
    "Scene label_429"
    jump end_431

label label_430:
    "Scene label_430"
    jump end_431

label label_407:
    "Scene label_407"
    if luck >= 18:
        jump label_431

label label_431:
    $ luck += 4
    if strength >= 20:
        jump label_432

label label_432:
    $ strength += 4
    jump end_433

    jump label_433

label label_433:
    "Ветка false для label_432"
    jump end_434

    jump label_434

label label_434:
    "Ветка false для label_431"
    if charisma >= 7:
        jump label_435

label label_435:
    $ charisma += 3
    jump end_436

    jump label_436

label label_436:
    "Ветка false для label_435"
    jump end_437

label label_408:
    "Scene label_408"
    menu:
        "Go back":
            $ strength += 3
            jump label_437
        "Look around":
            $ strength += 3
            jump label_438
        "Go back":
            jump label_439
        "Explore":
            jump label_440

label label_437:
    "Scene label_437"
    if charisma >= 20:
        jump label_441

label label_441:
    $ charisma += 4
    jump end_442

    jump label_442

label label_442:
    "Ветка false для label_441"
    jump end_443

label label_438:
    "Scene label_438"
    menu:
        "Go back":
            $ luck += 3
            jump label_443
        "Go back":
            $ charisma += 3
            jump label_444
        "Talk":
            jump label_445

label label_443:
    "Scene label_443"
    jump end_446

label label_444:
    "Scene label_444"
    jump end_446

label label_445:
    "Scene label_445"
    jump end_446

label label_439:
    "Scene label_439"
    menu:
        "Go forward":
            $ strength += 1
            jump label_446
        "Look around":
            jump label_447
        "Go back":
            $ luck += 2
            jump label_448

label label_446:
    "Scene label_446"
    jump end_449

label label_447:
    "Scene label_447"
    jump end_449

label label_448:
    "Scene label_448"
    jump end_449

label label_440:
    "Scene label_440"
    menu:
        "Look around":
            jump label_449
        "Talk":
            jump label_450

label label_449:
    "Scene label_449"
    jump end_451

label label_450:
    "Scene label_450"
    jump end_451

label label_380:
    "Scene label_380"
    menu:
        "Go back":
            jump label_451
        "Use item":
            $ strength += 2
            jump label_452

label label_451:
    "Scene label_451"
    menu:
        "Talk":
            jump label_453
        "Open door":
            jump label_454

label label_453:
    "Scene label_453"
    if charisma >= 10:
        jump label_455

label label_455:
    $ charisma += 3
    jump end_456

    jump label_456

label label_456:
    "Ветка false для label_455"
    jump end_457

label label_454:
    "Scene label_454"
    menu:
        "Go forward":
            jump label_457
        "Look around":
            $ charisma += 2
            jump label_458
        "Pick up item":
            $ intelligence += 2
            jump label_459

label label_457:
    "Scene label_457"
    jump end_460

label label_458:
    "Scene label_458"
    jump end_460

label label_459:
    "Scene label_459"
    jump end_460

label label_452:
    "Scene label_452"
    menu:
        "Pick up item":
            $ charisma += 1
            jump label_460
        "Go back":
            jump label_461
        "Pick up item":
            $ luck += 3
            jump label_462

label label_460:
    "Scene label_460"
    menu:
        "Look around":
            jump label_463
        "Explore":
            jump label_464

label label_463:
    "Scene label_463"
    jump end_465

label label_464:
    "Scene label_464"
    jump end_465

label label_461:
    "Scene label_461"
    menu:
        "Go back":
            $ luck += 1
            jump label_465
        "Go back":
            jump label_466
        "Open door":
            $ intelligence += 3
            jump label_467
        "Use item":
            jump label_468

label label_465:
    "Scene label_465"
    jump end_469

label label_466:
    "Scene label_466"
    jump end_469

label label_467:
    "Scene label_467"
    jump end_469

label label_468:
    "Scene label_468"
    jump end_469

label label_462:
    "Scene label_462"
    menu:
        "Explore":
            jump label_469
        "Go forward":
            jump label_470

label label_469:
    "Scene label_469"
    jump end_471

label label_470:
    "Scene label_470"
    jump end_471

label label_336:
    "Scene label_336"
    if strength >= 8:
        jump label_471

label label_471:
    $ strength += 5
    menu:
        "Go back":
            $ strength += 1
            jump label_472
        "Look around":
            $ intelligence += 3
            jump label_473
        "Look around":
            jump label_474
        "Look around":
            $ intelligence += 2
            jump label_475

label label_472:
    "Scene label_472"
    menu:
        "Talk":
            jump label_476
        "Talk":
            $ charisma += 3
            jump label_477
        "Look around":
            jump label_478
        "Go back":
            jump label_479

label label_476:
    "Scene label_476"
    menu:
        "Explore":
            $ strength += 2
            jump label_480
        "Go forward":
            $ luck += 1
            jump label_481
        "Go back":
            jump label_482
        "Go back":
            $ strength += 2
            jump label_483

label label_480:
    "Scene label_480"
    jump end_484

label label_481:
    "Scene label_481"
    jump end_484

label label_482:
    "Scene label_482"
    jump end_484

label label_483:
    "Scene label_483"
    jump end_484

label label_477:
    "Scene label_477"
    menu:
        "Open door":
            $ charisma += 1
            jump label_484
        "Talk":
            jump label_485

label label_484:
    "Scene label_484"
    jump end_486

label label_485:
    "Scene label_485"
    jump end_486

label label_478:
    "Scene label_478"
    menu:
        "Look around":
            jump label_486
        "Go back":
            $ strength += 1
            jump label_487
        "Go back":
            jump label_488
        "Go forward":
            jump label_489

label label_486:
    "Scene label_486"
    jump end_490

label label_487:
    "Scene label_487"
    jump end_490

label label_488:
    "Scene label_488"
    jump end_490

label label_489:
    "Scene label_489"
    jump end_490

label label_479:
    "Scene label_479"
    if strength >= 6:
        jump label_490

label label_490:
    $ strength += 5
    jump end_491

    jump label_491

label label_491:
    "Ветка false для label_490"
    jump end_492

label label_473:
    "Scene label_473"
    if luck >= 17:
        jump label_492

label label_492:
    $ luck += 2
    menu:
        "Pick up item":
            $ strength += 3
            jump label_493
        "Use item":
            $ charisma += 1
            jump label_494
        "Explore":
            $ luck += 2
            jump label_495

label label_493:
    "Scene label_493"
    jump end_496

label label_494:
    "Scene label_494"
    jump end_496

label label_495:
    "Scene label_495"
    jump end_496

    jump label_496

label label_496:
    "Ветка false для label_492"
    if strength >= 16:
        jump label_497

label label_497:
    $ strength += 4
    jump end_498

    jump label_498

label label_498:
    "Ветка false для label_497"
    jump end_499

label label_474:
    "Scene label_474"
    if charisma >= 14:
        jump label_499

label label_499:
    $ charisma += 3
    if strength >= 17:
        jump label_500

label label_500:
    $ strength += 3
    jump end_501

    jump label_501

label label_501:
    "Ветка false для label_500"
    jump end_502

    jump label_502

label label_502:
    "Ветка false для label_499"
    if charisma >= 8:
        jump label_503

label label_503:
    $ charisma += 4
    jump end_504

    jump label_504

label label_504:
    "Ветка false для label_503"
    jump end_505

label label_475:
    "Scene label_475"
    menu:
        "Pick up item":
            jump label_505
        "Talk":
            $ strength += 3
            jump label_506
        "Use item":
            $ strength += 3
            jump label_507
        "Go back":
            $ charisma += 1
            jump label_508

label label_505:
    "Scene label_505"
    if strength >= 15:
        jump label_509

label label_509:
    $ strength += 2
    jump end_510

    jump label_510

label label_510:
    "Ветка false для label_509"
    jump end_511

label label_506:
    "Scene label_506"
    menu:
        "Pick up item":
            jump label_511
        "Talk":
            jump label_512

label label_511:
    "Scene label_511"
    jump end_513

label label_512:
    "Scene label_512"
    jump end_513

label label_507:
    "Scene label_507"
    if strength >= 6:
        jump label_513

label label_513:
    $ strength += 3
    jump end_514

    jump label_514

label label_514:
    "Ветка false для label_513"
    jump end_515

label label_508:
    "Scene label_508"
    menu:
        "Pick up item":
            jump label_515
        "Go forward":
            $ intelligence += 1
            jump label_516

label label_515:
    "Scene label_515"
    jump end_517

label label_516:
    "Scene label_516"
    jump end_517

    jump label_517

label label_517:
    "Ветка false для label_471"
    if strength >= 14:
        jump label_518

label label_518:
    $ strength += 2
    menu:
        "Look around":
            jump label_519
        "Look around":
            $ intelligence += 1
            jump label_520

label label_519:
    "Scene label_519"
    menu:
        "Explore":
            jump label_521
        "Open door":
            $ intelligence += 2
            jump label_522
        "Use item":
            jump label_523

label label_521:
    "Scene label_521"
    jump end_524

label label_522:
    "Scene label_522"
    jump end_524

label label_523:
    "Scene label_523"
    jump end_524

label label_520:
    "Scene label_520"
    menu:
        "Look around":
            $ intelligence += 2
            jump label_524
        "Talk":
            jump label_525
        "Talk":
            $ strength += 1
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

    jump label_527

label label_527:
    "Ветка false для label_518"
    if charisma >= 10:
        jump label_528

label label_528:
    $ charisma += 2
    menu:
        "Go forward":
            $ strength += 3
            jump label_529
        "Go back":
            $ charisma += 3
            jump label_530

label label_529:
    "Scene label_529"
    jump end_531

label label_530:
    "Scene label_530"
    jump end_531

    jump label_531

label label_531:
    "Ветка false для label_528"
    if intelligence >= 13:
        jump label_532

label label_532:
    $ intelligence += 5
    jump end_533

    jump label_533

label label_533:
    "Ветка false для label_532"
    jump end_534

label label_337:
    "Scene label_337"
    menu:
        "Go forward":
            jump label_534
        "Pick up item":
            jump label_535

label label_534:
    "Scene label_534"
    if luck >= 16:
        jump label_536

label label_536:
    $ luck += 5
    if intelligence >= 11:
        jump label_537

label label_537:
    $ intelligence += 2
    menu:
        "Explore":
            jump label_538
        "Use item":
            $ intelligence += 2
            jump label_539

label label_538:
    "Scene label_538"
    jump end_540

label label_539:
    "Scene label_539"
    jump end_540

    jump label_540

label label_540:
    "Ветка false для label_537"
    if strength >= 9:
        jump label_541

label label_541:
    $ strength += 5
    jump end_542

    jump label_542

label label_542:
    "Ветка false для label_541"
    jump end_543

    jump label_543

label label_543:
    "Ветка false для label_536"
    menu:
        "Go forward":
            $ luck += 2
            jump label_544
        "Use item":
            $ luck += 3
            jump label_545

label label_544:
    "Scene label_544"
    menu:
        "Go forward":
            $ strength += 3
            jump label_546
        "Talk":
            $ strength += 2
            jump label_547
        "Look around":
            $ intelligence += 3
            jump label_548

label label_546:
    "Scene label_546"
    jump end_549

label label_547:
    "Scene label_547"
    jump end_549

label label_548:
    "Scene label_548"
    jump end_549

label label_545:
    "Scene label_545"
    menu:
        "Explore":
            $ luck += 1
            jump label_549
        "Look around":
            $ strength += 1
            jump label_550
        "Open door":
            jump label_551
        "Open door":
            jump label_552

label label_549:
    "Scene label_549"
    jump end_553

label label_550:
    "Scene label_550"
    jump end_553

label label_551:
    "Scene label_551"
    jump end_553

label label_552:
    "Scene label_552"
    jump end_553

label label_535:
    "Scene label_535"
    if charisma >= 6:
        jump label_553

label label_553:
    $ charisma += 5
    if charisma >= 10:
        jump label_554

label label_554:
    $ charisma += 5
    menu:
        "Use item":
            jump label_555
        "Go back":
            $ intelligence += 1
            jump label_556
        "Go forward":
            $ strength += 2
            jump label_557

label label_555:
    "Scene label_555"
    jump end_558

label label_556:
    "Scene label_556"
    jump end_558

label label_557:
    "Scene label_557"
    jump end_558

    jump label_558

label label_558:
    "Ветка false для label_554"
    menu:
        "Explore":
            $ luck += 3
            jump label_559
        "Talk":
            jump label_560

label label_559:
    "Scene label_559"
    jump end_561

label label_560:
    "Scene label_560"
    jump end_561

    jump label_561

label label_561:
    "Ветка false для label_553"
    menu:
        "Talk":
            jump label_562
        "Use item":
            $ charisma += 1
            jump label_563
        "Pick up item":
            jump label_564
        "Go back":
            $ charisma += 3
            jump label_565

label label_562:
    "Scene label_562"
    menu:
        "Explore":
            $ intelligence += 3
            jump label_566
        "Talk":
            jump label_567

label label_566:
    "Scene label_566"
    jump end_568

label label_567:
    "Scene label_567"
    jump end_568

label label_563:
    "Scene label_563"
    menu:
        "Go forward":
            $ charisma += 3
            jump label_568
        "Go forward":
            $ charisma += 2
            jump label_569
        "Look around":
            $ intelligence += 1
            jump label_570

label label_568:
    "Scene label_568"
    jump end_571

label label_569:
    "Scene label_569"
    jump end_571

label label_570:
    "Scene label_570"
    jump end_571

label label_564:
    "Scene label_564"
    menu:
        "Open door":
            jump label_571
        "Talk":
            $ intelligence += 3
            jump label_572

label label_571:
    "Scene label_571"
    jump end_573

label label_572:
    "Scene label_572"
    jump end_573

label label_565:
    "Scene label_565"
    menu:
        "Pick up item":
            jump label_573
        "Talk":
            jump label_574

label label_573:
    "Scene label_573"
    jump end_575

label label_574:
    "Scene label_574"
    jump end_575

label label_25:
    "Scene label_25"
    menu:
        "Go forward":
            jump label_575
        "Pick up item":
            jump label_576
        "Open door":
            $ luck += 3
            jump label_577
        "Pick up item":
            jump label_578

label label_575:
    "Scene label_575"
    if strength >= 17:
        jump label_579

label label_579:
    $ strength += 4
    menu:
        "Open door":
            jump label_580
        "Use item":
            jump label_581
        "Look around":
            jump label_582

label label_580:
    "Scene label_580"
    menu:
        "Explore":
            jump label_583
        "Look around":
            $ charisma += 3
            jump label_584

label label_583:
    "Scene label_583"
    if luck >= 10:
        jump label_585

label label_585:
    $ luck += 2
    menu:
        "Talk":
            jump label_586
        "Use item":
            jump label_587

label label_586:
    "Scene label_586"
    jump end_588

label label_587:
    "Scene label_587"
    jump end_588

    jump label_588

label label_588:
    "Ветка false для label_585"
    menu:
        "Use item":
            jump label_589
        "Use item":
            $ luck += 3
            jump label_590
        "Open door":
            $ strength += 2
            jump label_591
        "Explore":
            $ strength += 2
            jump label_592

label label_589:
    "Scene label_589"
    jump end_593

label label_590:
    "Scene label_590"
    jump end_593

label label_591:
    "Scene label_591"
    jump end_593

label label_592:
    "Scene label_592"
    jump end_593

label label_584:
    "Scene label_584"
    menu:
        "Go back":
            $ luck += 3
            jump label_593
        "Look around":
            $ charisma += 1
            jump label_594
        "Look around":
            $ intelligence += 2
            jump label_595
        "Look around":
            $ luck += 1
            jump label_596

label label_593:
    "Scene label_593"
    menu:
        "Talk":
            jump label_597
        "Go forward":
            $ intelligence += 2
            jump label_598
        "Explore":
            $ strength += 2
            jump label_599

label label_597:
    "Scene label_597"
    jump end_600

label label_598:
    "Scene label_598"
    jump end_600

label label_599:
    "Scene label_599"
    jump end_600

label label_594:
    "Scene label_594"
    if strength >= 12:
        jump label_600

label label_600:
    $ strength += 4
    jump end_601

    jump label_601

label label_601:
    "Ветка false для label_600"
    jump end_602

label label_595:
    "Scene label_595"
    menu:
        "Explore":
            $ charisma += 2
            jump label_602
        "Go back":
            jump label_603
        "Go back":
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

label label_596:
    "Scene label_596"
    menu:
        "Go forward":
            $ luck += 2
            jump label_605
        "Talk":
            jump label_606
        "Talk":
            jump label_607

label label_605:
    "Scene label_605"
    jump end_608

label label_606:
    "Scene label_606"
    jump end_608

label label_607:
    "Scene label_607"
    jump end_608

label label_581:
    "Scene label_581"
    if intelligence >= 9:
        jump label_608

label label_608:
    $ intelligence += 3
    if strength >= 15:
        jump label_609

label label_609:
    $ strength += 3
    menu:
        "Talk":
            $ strength += 3
            jump label_610
        "Explore":
            jump label_611
        "Talk":
            $ intelligence += 3
            jump label_612

label label_610:
    "Scene label_610"
    jump end_613

label label_611:
    "Scene label_611"
    jump end_613

label label_612:
    "Scene label_612"
    jump end_613

    jump label_613

label label_613:
    "Ветка false для label_609"
    menu:
        "Open door":
            jump label_614
        "Talk":
            jump label_615

label label_614:
    "Scene label_614"
    jump end_616

label label_615:
    "Scene label_615"
    jump end_616

    jump label_616

label label_616:
    "Ветка false для label_608"
    menu:
        "Go forward":
            jump label_617
        "Explore":
            jump label_618

label label_617:
    "Scene label_617"
    if luck >= 9:
        jump label_619

label label_619:
    $ luck += 5
    jump end_620

    jump label_620

label label_620:
    "Ветка false для label_619"
    jump end_621

label label_618:
    "Scene label_618"
    menu:
        "Pick up item":
            jump label_621
        "Talk":
            jump label_622

label label_621:
    "Scene label_621"
    jump end_623

label label_622:
    "Scene label_622"
    jump end_623

label label_582:
    "Scene label_582"
    if strength >= 17:
        jump label_623

label label_623:
    $ strength += 3
    menu:
        "Explore":
            $ intelligence += 3
            jump label_624
        "Use item":
            jump label_625

label label_624:
    "Scene label_624"
    menu:
        "Go forward":
            $ charisma += 3
            jump label_626
        "Look around":
            jump label_627

label label_626:
    "Scene label_626"
    jump end_628

label label_627:
    "Scene label_627"
    jump end_628

label label_625:
    "Scene label_625"
    menu:
        "Explore":
            jump label_628
        "Go forward":
            jump label_629
        "Explore":
            $ charisma += 2
            jump label_630

label label_628:
    "Scene label_628"
    jump end_631

label label_629:
    "Scene label_629"
    jump end_631

label label_630:
    "Scene label_630"
    jump end_631

    jump label_631

label label_631:
    "Ветка false для label_623"
    menu:
        "Go back":
            $ luck += 2
            jump label_632
        "Look around":
            $ charisma += 3
            jump label_633

label label_632:
    "Scene label_632"
    menu:
        "Go back":
            $ charisma += 3
            jump label_634
        "Open door":
            $ strength += 1
            jump label_635
        "Use item":
            $ luck += 1
            jump label_636

label label_634:
    "Scene label_634"
    jump end_637

label label_635:
    "Scene label_635"
    jump end_637

label label_636:
    "Scene label_636"
    jump end_637

label label_633:
    "Scene label_633"
    menu:
        "Open door":
            $ charisma += 3
            jump label_637
        "Go back":
            $ charisma += 3
            jump label_638
        "Talk":
            $ charisma += 2
            jump label_639
        "Pick up item":
            $ luck += 3
            jump label_640

label label_637:
    "Scene label_637"
    jump end_641

label label_638:
    "Scene label_638"
    jump end_641

label label_639:
    "Scene label_639"
    jump end_641

label label_640:
    "Scene label_640"
    jump end_641

    jump label_641

label label_641:
    "Ветка false для label_579"
    menu:
        "Pick up item":
            $ strength += 1
            jump label_642
        "Go back":
            $ charisma += 1
            jump label_643
        "Go back":
            $ charisma += 3
            jump label_644
        "Use item":
            $ luck += 2
            jump label_645

label label_642:
    "Scene label_642"
    menu:
        "Explore":
            jump label_646
        "Open door":
            jump label_647

label label_646:
    "Scene label_646"
    menu:
        "Look around":
            $ strength += 2
            jump label_648
        "Talk":
            jump label_649
        "Talk":
            $ intelligence += 2
            jump label_650

label label_648:
    "Scene label_648"
    if luck >= 16:
        jump label_651

label label_651:
    $ luck += 5
    jump end_652

    jump label_652

label label_652:
    "Ветка false для label_651"
    jump end_653

label label_649:
    "Scene label_649"
    menu:
        "Go forward":
            $ strength += 3
            jump label_653
        "Use item":
            jump label_654
        "Talk":
            jump label_655

label label_653:
    "Scene label_653"
    jump end_656

label label_654:
    "Scene label_654"
    jump end_656

label label_655:
    "Scene label_655"
    jump end_656

label label_650:
    "Scene label_650"
    menu:
        "Explore":
            jump label_656
        "Go back":
            $ luck += 1
            jump label_657

label label_656:
    "Scene label_656"
    jump end_658

label label_657:
    "Scene label_657"
    jump end_658

label label_647:
    "Scene label_647"
    menu:
        "Talk":
            $ luck += 2
            jump label_658
        "Pick up item":
            $ intelligence += 1
            jump label_659
        "Use item":
            $ intelligence += 1
            jump label_660

label label_658:
    "Scene label_658"
    menu:
        "Look around":
            $ strength += 1
            jump label_661
        "Talk":
            jump label_662
        "Pick up item":
            $ luck += 1
            jump label_663
        "Pick up item":
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

label label_659:
    "Scene label_659"
    menu:
        "Talk":
            jump label_665
        "Go forward":
            jump label_666
        "Look around":
            $ intelligence += 3
            jump label_667

label label_665:
    "Scene label_665"
    jump end_668

label label_666:
    "Scene label_666"
    jump end_668

label label_667:
    "Scene label_667"
    jump end_668

label label_660:
    "Scene label_660"
    if intelligence >= 11:
        jump label_668

label label_668:
    $ intelligence += 3
    jump end_669

    jump label_669

label label_669:
    "Ветка false для label_668"
    jump end_670

label label_643:
    "Scene label_643"
    menu:
        "Look around":
            $ charisma += 2
            jump label_670
        "Go forward":
            $ strength += 3
            jump label_671
        "Go forward":
            $ luck += 1
            jump label_672

label label_670:
    "Scene label_670"
    if strength >= 8:
        jump label_673

label label_673:
    $ strength += 2
    menu:
        "Use item":
            $ luck += 1
            jump label_674
        "Look around":
            $ luck += 3
            jump label_675

label label_674:
    "Scene label_674"
    jump end_676

label label_675:
    "Scene label_675"
    jump end_676

    jump label_676

label label_676:
    "Ветка false для label_673"
    menu:
        "Use item":
            jump label_677
        "Look around":
            $ strength += 3
            jump label_678

label label_677:
    "Scene label_677"
    jump end_679

label label_678:
    "Scene label_678"
    jump end_679

label label_671:
    "Scene label_671"
    if intelligence >= 14:
        jump label_679

label label_679:
    $ intelligence += 3
    menu:
        "Go forward":
            jump label_680
        "Look around":
            jump label_681
        "Pick up item":
            $ intelligence += 2
            jump label_682
        "Look around":
            $ luck += 2
            jump label_683

label label_680:
    "Scene label_680"
    jump end_684

label label_681:
    "Scene label_681"
    jump end_684

label label_682:
    "Scene label_682"
    jump end_684

label label_683:
    "Scene label_683"
    jump end_684

    jump label_684

label label_684:
    "Ветка false для label_679"
    menu:
        "Use item":
            $ luck += 1
            jump label_685
        "Pick up item":
            $ intelligence += 2
            jump label_686
        "Explore":
            jump label_687
        "Go forward":
            $ charisma += 1
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

label label_672:
    "Scene label_672"
    menu:
        "Go back":
            jump label_689
        "Pick up item":
            $ charisma += 2
            jump label_690
        "Open door":
            $ strength += 2
            jump label_691

label label_689:
    "Scene label_689"
    menu:
        "Talk":
            $ charisma += 3
            jump label_692
        "Look around":
            $ strength += 1
            jump label_693
        "Talk":
            $ strength += 3
            jump label_694

label label_692:
    "Scene label_692"
    jump end_695

label label_693:
    "Scene label_693"
    jump end_695

label label_694:
    "Scene label_694"
    jump end_695

label label_690:
    "Scene label_690"
    menu:
        "Look around":
            $ intelligence += 2
            jump label_695
        "Use item":
            jump label_696

label label_695:
    "Scene label_695"
    jump end_697

label label_696:
    "Scene label_696"
    jump end_697

label label_691:
    "Scene label_691"
    menu:
        "Use item":
            jump label_697
        "Pick up item":
            $ luck += 3
            jump label_698

label label_697:
    "Scene label_697"
    jump end_699

label label_698:
    "Scene label_698"
    jump end_699

label label_644:
    "Scene label_644"
    menu:
        "Pick up item":
            jump label_699
        "Open door":
            jump label_700
        "Go back":
            $ charisma += 1
            jump label_701

label label_699:
    "Scene label_699"
    if charisma >= 20:
        jump label_702

label label_702:
    $ charisma += 3
    menu:
        "Go forward":
            $ strength += 1
            jump label_703
        "Pick up item":
            jump label_704

label label_703:
    "Scene label_703"
    jump end_705

label label_704:
    "Scene label_704"
    jump end_705

    jump label_705

label label_705:
    "Ветка false для label_702"
    menu:
        "Explore":
            $ strength += 1
            jump label_706
        "Pick up item":
            jump label_707
        "Use item":
            $ charisma += 2
            jump label_708

label label_706:
    "Scene label_706"
    jump end_709

label label_707:
    "Scene label_707"
    jump end_709

label label_708:
    "Scene label_708"
    jump end_709

label label_700:
    "Scene label_700"
    menu:
        "Explore":
            jump label_709
        "Go forward":
            jump label_710
        "Go forward":
            jump label_711
        "Look around":
            $ luck += 2
            jump label_712

label label_709:
    "Scene label_709"
    menu:
        "Go forward":
            $ luck += 3
            jump label_713
        "Talk":
            $ intelligence += 2
            jump label_714

label label_713:
    "Scene label_713"
    jump end_715

label label_714:
    "Scene label_714"
    jump end_715

label label_710:
    "Scene label_710"
    menu:
        "Look around":
            jump label_715
        "Pick up item":
            jump label_716
        "Pick up item":
            $ intelligence += 3
            jump label_717

label label_715:
    "Scene label_715"
    jump end_718

label label_716:
    "Scene label_716"
    jump end_718

label label_717:
    "Scene label_717"
    jump end_718

label label_711:
    "Scene label_711"
    if luck >= 20:
        jump label_718

label label_718:
    $ luck += 5
    jump end_719

    jump label_719

label label_719:
    "Ветка false для label_718"
    jump end_720

label label_712:
    "Scene label_712"
    menu:
        "Go back":
            $ strength += 3
            jump label_720
        "Go forward":
            $ luck += 2
            jump label_721
        "Go forward":
            jump label_722

label label_720:
    "Scene label_720"
    jump end_723

label label_721:
    "Scene label_721"
    jump end_723

label label_722:
    "Scene label_722"
    jump end_723

label label_701:
    "Scene label_701"
    menu:
        "Look around":
            $ luck += 2
            jump label_723
        "Explore":
            $ intelligence += 1
            jump label_724
        "Use item":
            jump label_725

label label_723:
    "Scene label_723"
    menu:
        "Look around":
            jump label_726
        "Look around":
            $ strength += 3
            jump label_727
        "Explore":
            $ charisma += 3
            jump label_728
        "Open door":
            $ charisma += 3
            jump label_729

label label_726:
    "Scene label_726"
    jump end_730

label label_727:
    "Scene label_727"
    jump end_730

label label_728:
    "Scene label_728"
    jump end_730

label label_729:
    "Scene label_729"
    jump end_730

label label_724:
    "Scene label_724"
    if luck >= 17:
        jump label_730

label label_730:
    $ luck += 5
    jump end_731

    jump label_731

label label_731:
    "Ветка false для label_730"
    jump end_732

label label_725:
    "Scene label_725"
    menu:
        "Pick up item":
            $ intelligence += 2
            jump label_732
        "Pick up item":
            jump label_733

label label_732:
    "Scene label_732"
    jump end_734

label label_733:
    "Scene label_733"
    jump end_734

label label_645:
    "Scene label_645"
    menu:
        "Talk":
            jump label_734
        "Explore":
            jump label_735
        "Use item":
            $ strength += 3
            jump label_736

label label_734:
    "Scene label_734"
    if luck >= 6:
        jump label_737

label label_737:
    $ luck += 4
    menu:
        "Use item":
            jump label_738
        "Look around":
            jump label_739
        "Look around":
            jump label_740

label label_738:
    "Scene label_738"
    jump end_741

label label_739:
    "Scene label_739"
    jump end_741

label label_740:
    "Scene label_740"
    jump end_741

    jump label_741

label label_741:
    "Ветка false для label_737"
    if charisma >= 18:
        jump label_742

label label_742:
    $ charisma += 3
    jump end_743

    jump label_743

label label_743:
    "Ветка false для label_742"
    jump end_744

label label_735:
    "Scene label_735"
    menu:
        "Go back":
            jump label_744
        "Go back":
            $ luck += 1
            jump label_745

label label_744:
    "Scene label_744"
    menu:
        "Pick up item":
            jump label_746
        "Talk":
            jump label_747
        "Talk":
            jump label_748

label label_746:
    "Scene label_746"
    jump end_749

label label_747:
    "Scene label_747"
    jump end_749

label label_748:
    "Scene label_748"
    jump end_749

label label_745:
    "Scene label_745"
    if charisma >= 13:
        jump label_749

label label_749:
    $ charisma += 5
    jump end_750

    jump label_750

label label_750:
    "Ветка false для label_749"
    jump end_751

label label_736:
    "Scene label_736"
    menu:
        "Go forward":
            jump label_751
        "Explore":
            $ intelligence += 1
            jump label_752
        "Go back":
            jump label_753
        "Open door":
            $ strength += 3
            jump label_754

label label_751:
    "Scene label_751"
    if charisma >= 13:
        jump label_755

label label_755:
    $ charisma += 4
    jump end_756

    jump label_756

label label_756:
    "Ветка false для label_755"
    jump end_757

label label_752:
    "Scene label_752"
    menu:
        "Use item":
            $ strength += 1
            jump label_757
        "Use item":
            $ luck += 2
            jump label_758
        "Pick up item":
            jump label_759

label label_757:
    "Scene label_757"
    jump end_760

label label_758:
    "Scene label_758"
    jump end_760

label label_759:
    "Scene label_759"
    jump end_760

label label_753:
    "Scene label_753"
    menu:
        "Go forward":
            $ luck += 1
            jump label_760
        "Go forward":
            $ luck += 3
            jump label_761
        "Talk":
            jump label_762
        "Go forward":
            jump label_763

label label_760:
    "Scene label_760"
    jump end_764

label label_761:
    "Scene label_761"
    jump end_764

label label_762:
    "Scene label_762"
    jump end_764

label label_763:
    "Scene label_763"
    jump end_764

label label_754:
    "Scene label_754"
    menu:
        "Go forward":
            jump label_764
        "Look around":
            $ luck += 1
            jump label_765

label label_764:
    "Scene label_764"
    jump end_766

label label_765:
    "Scene label_765"
    jump end_766

label label_576:
    "Scene label_576"
    menu:
        "Explore":
            jump label_766
        "Look around":
            $ intelligence += 1
            jump label_767
        "Look around":
            jump label_768

label label_766:
    "Scene label_766"
    menu:
        "Go back":
            $ strength += 1
            jump label_769
        "Look around":
            jump label_770

label label_769:
    "Scene label_769"
    menu:
        "Open door":
            jump label_771
        "Use item":
            jump label_772
        "Use item":
            $ intelligence += 1
            jump label_773
        "Go back":
            $ luck += 3
            jump label_774

label label_771:
    "Scene label_771"
    if luck >= 8:
        jump label_775

label label_775:
    $ luck += 4
    menu:
        "Use item":
            jump label_776
        "Talk":
            $ luck += 2
            jump label_777
        "Go forward":
            jump label_778

label label_776:
    "Scene label_776"
    jump end_779

label label_777:
    "Scene label_777"
    jump end_779

label label_778:
    "Scene label_778"
    jump end_779

    jump label_779

label label_779:
    "Ветка false для label_775"
    menu:
        "Go forward":
            jump label_780
        "Use item":
            $ charisma += 2
            jump label_781

label label_780:
    "Scene label_780"
    jump end_782

label label_781:
    "Scene label_781"
    jump end_782

label label_772:
    "Scene label_772"
    menu:
        "Explore":
            jump label_782
        "Look around":
            jump label_783
        "Use item":
            jump label_784
        "Open door":
            $ charisma += 2
            jump label_785

label label_782:
    "Scene label_782"
    menu:
        "Go back":
            $ intelligence += 2
            jump label_786
        "Explore":
            jump label_787

label label_786:
    "Scene label_786"
    jump end_788

label label_787:
    "Scene label_787"
    jump end_788

label label_783:
    "Scene label_783"
    menu:
        "Go forward":
            $ strength += 2
            jump label_788
        "Pick up item":
            jump label_789
        "Explore":
            jump label_790

label label_788:
    "Scene label_788"
    jump end_791

label label_789:
    "Scene label_789"
    jump end_791

label label_790:
    "Scene label_790"
    jump end_791

label label_784:
    "Scene label_784"
    menu:
        "Talk":
            jump label_791
        "Look around":
            $ luck += 2
            jump label_792

label label_791:
    "Scene label_791"
    jump end_793

label label_792:
    "Scene label_792"
    jump end_793

label label_785:
    "Scene label_785"
    menu:
        "Talk":
            jump label_793
        "Talk":
            $ intelligence += 3
            jump label_794

label label_793:
    "Scene label_793"
    jump end_795

label label_794:
    "Scene label_794"
    jump end_795

label label_773:
    "Scene label_773"
    menu:
        "Look around":
            $ intelligence += 3
            jump label_795
        "Talk":
            jump label_796
        "Open door":
            jump label_797
        "Explore":
            $ intelligence += 2
            jump label_798

label label_795:
    "Scene label_795"
    if luck >= 14:
        jump label_799

label label_799:
    $ luck += 3
    jump end_800

    jump label_800

label label_800:
    "Ветка false для label_799"
    jump end_801

label label_796:
    "Scene label_796"
    if luck >= 10:
        jump label_801

label label_801:
    $ luck += 5
    jump end_802

    jump label_802

label label_802:
    "Ветка false для label_801"
    jump end_803

label label_797:
    "Scene label_797"
    menu:
        "Use item":
            $ strength += 3
            jump label_803
        "Use item":
            jump label_804
        "Pick up item":
            $ intelligence += 1
            jump label_805
        "Open door":
            jump label_806

label label_803:
    "Scene label_803"
    jump end_807

label label_804:
    "Scene label_804"
    jump end_807

label label_805:
    "Scene label_805"
    jump end_807

label label_806:
    "Scene label_806"
    jump end_807

label label_798:
    "Scene label_798"
    menu:
        "Look around":
            jump label_807
        "Talk":
            jump label_808

label label_807:
    "Scene label_807"
    jump end_809

label label_808:
    "Scene label_808"
    jump end_809

label label_774:
    "Scene label_774"
    if charisma >= 19:
        jump label_809

label label_809:
    $ charisma += 5
    if intelligence >= 11:
        jump label_810

label label_810:
    $ intelligence += 4
    jump end_811

    jump label_811

label label_811:
    "Ветка false для label_810"
    jump end_812

    jump label_812

label label_812:
    "Ветка false для label_809"
    if charisma >= 17:
        jump label_813

label label_813:
    $ charisma += 3
    jump end_814

    jump label_814

label label_814:
    "Ветка false для label_813"
    jump end_815

label label_770:
    "Scene label_770"
    menu:
        "Use item":
            jump label_815
        "Go back":
            jump label_816

label label_815:
    "Scene label_815"
    if intelligence >= 18:
        jump label_817

label label_817:
    $ intelligence += 3
    if luck >= 12:
        jump label_818

label label_818:
    $ luck += 5
    jump end_819

    jump label_819

label label_819:
    "Ветка false для label_818"
    jump end_820

    jump label_820

label label_820:
    "Ветка false для label_817"
    menu:
        "Pick up item":
            $ charisma += 1
            jump label_821
        "Explore":
            jump label_822
        "Open door":
            jump label_823

label label_821:
    "Scene label_821"
    jump end_824

label label_822:
    "Scene label_822"
    jump end_824

label label_823:
    "Scene label_823"
    jump end_824

label label_816:
    "Scene label_816"
    menu:
        "Open door":
            jump label_824
        "Go back":
            $ strength += 1
            jump label_825
        "Explore":
            jump label_826
        "Pick up item":
            jump label_827

label label_824:
    "Scene label_824"
    menu:
        "Go forward":
            $ charisma += 2
            jump label_828
        "Open door":
            jump label_829
        "Talk":
            jump label_830
        "Go forward":
            jump label_831

label label_828:
    "Scene label_828"
    jump end_832

label label_829:
    "Scene label_829"
    jump end_832

label label_830:
    "Scene label_830"
    jump end_832

label label_831:
    "Scene label_831"
    jump end_832

label label_825:
    "Scene label_825"
    if charisma >= 15:
        jump label_832

label label_832:
    $ charisma += 5
    jump end_833

    jump label_833

label label_833:
    "Ветка false для label_832"
    jump end_834

label label_826:
    "Scene label_826"
    if luck >= 18:
        jump label_834

label label_834:
    $ luck += 3
    jump end_835

    jump label_835

label label_835:
    "Ветка false для label_834"
    jump end_836

label label_827:
    "Scene label_827"
    if luck >= 6:
        jump label_836

label label_836:
    $ luck += 3
    jump end_837

    jump label_837

label label_837:
    "Ветка false для label_836"
    jump end_838

label label_767:
    "Scene label_767"
    menu:
        "Explore":
            jump label_838
        "Go back":
            jump label_839
        "Go back":
            jump label_840

label label_838:
    "Scene label_838"
    menu:
        "Explore":
            $ intelligence += 2
            jump label_841
        "Pick up item":
            jump label_842
        "Talk":
            jump label_843

label label_841:
    "Scene label_841"
    menu:
        "Pick up item":
            $ intelligence += 1
            jump label_844
        "Use item":
            $ charisma += 2
            jump label_845
        "Talk":
            jump label_846
        "Open door":
            $ charisma += 1
            jump label_847

label label_844:
    "Scene label_844"
    menu:
        "Pick up item":
            $ strength += 3
            jump label_848
        "Talk":
            $ strength += 1
            jump label_849
        "Go back":
            $ intelligence += 3
            jump label_850
        "Go back":
            jump label_851

label label_848:
    "Scene label_848"
    jump end_852

label label_849:
    "Scene label_849"
    jump end_852

label label_850:
    "Scene label_850"
    jump end_852

label label_851:
    "Scene label_851"
    jump end_852

label label_845:
    "Scene label_845"
    menu:
        "Go forward":
            jump label_852
        "Talk":
            $ strength += 1
            jump label_853

label label_852:
    "Scene label_852"
    jump end_854

label label_853:
    "Scene label_853"
    jump end_854

label label_846:
    "Scene label_846"
    menu:
        "Look around":
            jump label_854
        "Go forward":
            $ strength += 2
            jump label_855
        "Explore":
            jump label_856
        "Look around":
            jump label_857

label label_854:
    "Scene label_854"
    jump end_858

label label_855:
    "Scene label_855"
    jump end_858

label label_856:
    "Scene label_856"
    jump end_858

label label_857:
    "Scene label_857"
    jump end_858

label label_847:
    "Scene label_847"
    if strength >= 19:
        jump label_858

label label_858:
    $ strength += 5
    jump end_859

    jump label_859

label label_859:
    "Ветка false для label_858"
    jump end_860

label label_842:
    "Scene label_842"
    menu:
        "Go forward":
            $ strength += 3
            jump label_860
        "Pick up item":
            $ intelligence += 1
            jump label_861
        "Go forward":
            jump label_862

label label_860:
    "Scene label_860"
    if strength >= 7:
        jump label_863

label label_863:
    $ strength += 5
    jump end_864

    jump label_864

label label_864:
    "Ветка false для label_863"
    jump end_865

label label_861:
    "Scene label_861"
    if luck >= 10:
        jump label_865

label label_865:
    $ luck += 3
    jump end_866

    jump label_866

label label_866:
    "Ветка false для label_865"
    jump end_867

label label_862:
    "Scene label_862"
    menu:
        "Look around":
            $ intelligence += 1
            jump label_867
        "Open door":
            jump label_868
        "Go back":
            jump label_869

label label_867:
    "Scene label_867"
    jump end_870

label label_868:
    "Scene label_868"
    jump end_870

label label_869:
    "Scene label_869"
    jump end_870

label label_843:
    "Scene label_843"
    menu:
        "Look around":
            $ charisma += 3
            jump label_870
        "Go back":
            jump label_871

label label_870:
    "Scene label_870"
    menu:
        "Look around":
            jump label_872
        "Use item":
            $ charisma += 2
            jump label_873
        "Go back":
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
    menu:
        "Explore":
            jump label_875
        "Open door":
            jump label_876
        "Look around":
            $ luck += 2
            jump label_877

label label_875:
    "Scene label_875"
    jump end_878

label label_876:
    "Scene label_876"
    jump end_878

label label_877:
    "Scene label_877"
    jump end_878

label label_839:
    "Scene label_839"
    menu:
        "Talk":
            jump label_878
        "Look around":
            $ charisma += 1
            jump label_879
        "Pick up item":
            $ intelligence += 3
            jump label_880
        "Go back":
            jump label_881

label label_878:
    "Scene label_878"
    menu:
        "Go forward":
            jump label_882
        "Go forward":
            jump label_883
        "Open door":
            $ charisma += 3
            jump label_884

label label_882:
    "Scene label_882"
    menu:
        "Explore":
            $ strength += 3
            jump label_885
        "Go forward":
            $ charisma += 1
            jump label_886
        "Talk":
            jump label_887

label label_885:
    "Scene label_885"
    jump end_888

label label_886:
    "Scene label_886"
    jump end_888

label label_887:
    "Scene label_887"
    jump end_888

label label_883:
    "Scene label_883"
    if charisma >= 14:
        jump label_888

label label_888:
    $ charisma += 4
    jump end_889

    jump label_889

label label_889:
    "Ветка false для label_888"
    jump end_890

label label_884:
    "Scene label_884"
    menu:
        "Pick up item":
            jump label_890
        "Go back":
            $ intelligence += 1
            jump label_891
        "Talk":
            $ luck += 3
            jump label_892

label label_890:
    "Scene label_890"
    jump end_893

label label_891:
    "Scene label_891"
    jump end_893

label label_892:
    "Scene label_892"
    jump end_893

label label_879:
    "Scene label_879"
    if strength >= 5:
        jump label_893

label label_893:
    $ strength += 5
    if intelligence >= 20:
        jump label_894

label label_894:
    $ intelligence += 5
    jump end_895

    jump label_895

label label_895:
    "Ветка false для label_894"
    jump end_896

    jump label_896

label label_896:
    "Ветка false для label_893"
    menu:
        "Pick up item":
            $ luck += 3
            jump label_897
        "Open door":
            jump label_898
        "Look around":
            $ strength += 1
            jump label_899
        "Look around":
            jump label_900

label label_897:
    "Scene label_897"
    jump end_901

label label_898:
    "Scene label_898"
    jump end_901

label label_899:
    "Scene label_899"
    jump end_901

label label_900:
    "Scene label_900"
    jump end_901

label label_880:
    "Scene label_880"
    menu:
        "Go forward":
            $ intelligence += 3
            jump label_901
        "Use item":
            $ intelligence += 1
            jump label_902

label label_901:
    "Scene label_901"
    menu:
        "Talk":
            $ strength += 1
            jump label_903
        "Talk":
            jump label_904
        "Pick up item":
            jump label_905

label label_903:
    "Scene label_903"
    jump end_906

label label_904:
    "Scene label_904"
    jump end_906

label label_905:
    "Scene label_905"
    jump end_906

label label_902:
    "Scene label_902"
    menu:
        "Use item":
            $ charisma += 1
            jump label_906
        "Explore":
            $ charisma += 2
            jump label_907
        "Pick up item":
            jump label_908

label label_906:
    "Scene label_906"
    jump end_909

label label_907:
    "Scene label_907"
    jump end_909

label label_908:
    "Scene label_908"
    jump end_909

label label_881:
    "Scene label_881"
    menu:
        "Go back":
            $ charisma += 2
            jump label_909
        "Pick up item":
            $ strength += 3
            jump label_910
        "Go forward":
            $ luck += 3
            jump label_911
        "Look around":
            $ charisma += 2
            jump label_912

label label_909:
    "Scene label_909"
    if luck >= 19:
        jump label_913

label label_913:
    $ luck += 5
    jump end_914

    jump label_914

label label_914:
    "Ветка false для label_913"
    jump end_915

label label_910:
    "Scene label_910"
    if luck >= 11:
        jump label_915

label label_915:
    $ luck += 5
    jump end_916

    jump label_916

label label_916:
    "Ветка false для label_915"
    jump end_917

label label_911:
    "Scene label_911"
    menu:
        "Use item":
            jump label_917
        "Explore":
            jump label_918

label label_917:
    "Scene label_917"
    jump end_919

label label_918:
    "Scene label_918"
    jump end_919

label label_912:
    "Scene label_912"
    menu:
        "Pick up item":
            $ luck += 3
            jump label_919
        "Open door":
            jump label_920
        "Explore":
            jump label_921
        "Talk":
            jump label_922

label label_919:
    "Scene label_919"
    jump end_923

label label_920:
    "Scene label_920"
    jump end_923

label label_921:
    "Scene label_921"
    jump end_923

label label_922:
    "Scene label_922"
    jump end_923

label label_840:
    "Scene label_840"
    if strength >= 20:
        jump label_923

label label_923:
    $ strength += 3
    if intelligence >= 20:
        jump label_924

label label_924:
    $ intelligence += 2
    menu:
        "Go back":
            $ strength += 1
            jump label_925
        "Explore":
            jump label_926
        "Explore":
            jump label_927

label label_925:
    "Scene label_925"
    jump end_928

label label_926:
    "Scene label_926"
    jump end_928

label label_927:
    "Scene label_927"
    jump end_928

    jump label_928

label label_928:
    "Ветка false для label_924"
    if strength >= 7:
        jump label_929

label label_929:
    $ strength += 4
    jump end_930

    jump label_930

label label_930:
    "Ветка false для label_929"
    jump end_931

    jump label_931

label label_931:
    "Ветка false для label_923"
    menu:
        "Use item":
            $ intelligence += 2
            jump label_932
        "Go back":
            jump label_933
        "Explore":
            jump label_934
        "Go back":
            jump label_935

label label_932:
    "Scene label_932"
    menu:
        "Look around":
            jump label_936
        "Pick up item":
            jump label_937
        "Look around":
            jump label_938
        "Look around":
            jump label_939

label label_936:
    "Scene label_936"
    jump end_940

label label_937:
    "Scene label_937"
    jump end_940

label label_938:
    "Scene label_938"
    jump end_940

label label_939:
    "Scene label_939"
    jump end_940

label label_933:
    "Scene label_933"
    if strength >= 10:
        jump label_940

label label_940:
    $ strength += 2
    jump end_941

    jump label_941

label label_941:
    "Ветка false для label_940"
    jump end_942

label label_934:
    "Scene label_934"
    menu:
        "Talk":
            jump label_942
        "Pick up item":
            jump label_943
        "Pick up item":
            jump label_944

label label_942:
    "Scene label_942"
    jump end_945

label label_943:
    "Scene label_943"
    jump end_945

label label_944:
    "Scene label_944"
    jump end_945

label label_935:
    "Scene label_935"
    if luck >= 15:
        jump label_945

label label_945:
    $ luck += 3
    jump end_946

    jump label_946

label label_946:
    "Ветка false для label_945"
    jump end_947

label label_768:
    "Scene label_768"
    if intelligence >= 19:
        jump label_947

label label_947:
    $ intelligence += 5
    menu:
        "Use item":
            jump label_948
        "Pick up item":
            $ intelligence += 1
            jump label_949

label label_948:
    "Scene label_948"
    if charisma >= 16:
        jump label_950

label label_950:
    $ charisma += 3
    if charisma >= 12:
        jump label_951

label label_951:
    $ charisma += 3
    jump end_952

    jump label_952

label label_952:
    "Ветка false для label_951"
    jump end_953

    jump label_953

label label_953:
    "Ветка false для label_950"
    menu:
        "Open door":
            jump label_954
        "Explore":
            jump label_955
        "Pick up item":
            $ strength += 3
            jump label_956

label label_954:
    "Scene label_954"
    jump end_957

label label_955:
    "Scene label_955"
    jump end_957

label label_956:
    "Scene label_956"
    jump end_957

label label_949:
    "Scene label_949"
    menu:
        "Look around":
            $ charisma += 1
            jump label_957
        "Open door":
            $ strength += 3
            jump label_958

label label_957:
    "Scene label_957"
    menu:
        "Go forward":
            jump label_959
        "Go back":
            $ luck += 3
            jump label_960

label label_959:
    "Scene label_959"
    jump end_961

label label_960:
    "Scene label_960"
    jump end_961

label label_958:
    "Scene label_958"
    menu:
        "Go forward":
            jump label_961
        "Talk":
            jump label_962
        "Pick up item":
            jump label_963

label label_961:
    "Scene label_961"
    jump end_964

label label_962:
    "Scene label_962"
    jump end_964

label label_963:
    "Scene label_963"
    jump end_964

    jump label_964

label label_964:
    "Ветка false для label_947"
    menu:
        "Pick up item":
            jump label_965
        "Open door":
            jump label_966
        "Go back":
            $ luck += 2
            jump label_967
        "Talk":
            jump label_968

label label_965:
    "Scene label_965"
    menu:
        "Look around":
            jump label_969
        "Go back":
            jump label_970

label label_969:
    "Scene label_969"
    menu:
        "Go forward":
            $ luck += 1
            jump label_971
        "Go back":
            jump label_972

label label_971:
    "Scene label_971"
    jump end_973

label label_972:
    "Scene label_972"
    jump end_973

label label_970:
    "Scene label_970"
    menu:
        "Go forward":
            jump label_973
        "Go back":
            jump label_974

label label_973:
    "Scene label_973"
    jump end_975

label label_974:
    "Scene label_974"
    jump end_975

label label_966:
    "Scene label_966"
    menu:
        "Look around":
            $ strength += 2
            jump label_975
        "Explore":
            jump label_976

label label_975:
    "Scene label_975"
    menu:
        "Use item":
            $ luck += 3
            jump label_977
        "Talk":
            jump label_978
        "Use item":
            $ intelligence += 2
            jump label_979
        "Pick up item":
            $ charisma += 2
            jump label_980

label label_977:
    "Scene label_977"
    jump end_981

label label_978:
    "Scene label_978"
    jump end_981

label label_979:
    "Scene label_979"
    jump end_981

label label_980:
    "Scene label_980"
    jump end_981

label label_976:
    "Scene label_976"
    if strength >= 18:
        jump label_981

label label_981:
    $ strength += 3
    jump end_982

    jump label_982

label label_982:
    "Ветка false для label_981"
    jump end_983

label label_967:
    "Scene label_967"
    menu:
        "Look around":
            $ charisma += 3
            jump label_983
        "Open door":
            jump label_984
        "Pick up item":
            jump label_985

label label_983:
    "Scene label_983"
    menu:
        "Pick up item":
            jump label_986
        "Open door":
            jump label_987
        "Talk":
            jump label_988
        "Pick up item":
            jump label_989

label label_986:
    "Scene label_986"
    jump end_990

label label_987:
    "Scene label_987"
    jump end_990

label label_988:
    "Scene label_988"
    jump end_990

label label_989:
    "Scene label_989"
    jump end_990

label label_984:
    "Scene label_984"
    if strength >= 11:
        jump label_990

label label_990:
    $ strength += 5
    jump end_991

    jump label_991

label label_991:
    "Ветка false для label_990"
    jump end_992

label label_985:
    "Scene label_985"
    menu:
        "Talk":
            jump label_992
        "Explore":
            jump label_993
        "Look around":
            jump label_994
        "Open door":
            $ luck += 3
            jump label_995

label label_992:
    "Scene label_992"
    jump end_996

label label_993:
    "Scene label_993"
    jump end_996

label label_994:
    "Scene label_994"
    jump end_996

label label_995:
    "Scene label_995"
    jump end_996

label label_968:
    "Scene label_968"
    if intelligence >= 8:
        jump label_996

label label_996:
    $ intelligence += 4
    menu:
        "Go back":
            $ strength += 1
            jump label_997
        "Talk":
            jump label_998
        "Open door":
            $ luck += 2
            jump label_999

label label_997:
    "Scene label_997"
    jump end_1000

label label_998:
    "Scene label_998"
    jump end_1000

label label_999:
    "Scene label_999"
    jump end_1000

    jump label_1000

label label_1000:
    "Ветка false для label_996"
    if charisma >= 5:
        jump label_1001

label label_1001:
    $ charisma += 2
    jump end_1002

    jump label_1002

label label_1002:
    "Ветка false для label_1001"
    jump end_1003

label label_577:
    "Scene label_577"
    menu:
        "Go forward":
            $ luck += 3
            jump label_1003
        "Pick up item":
            jump label_1004

label label_1003:
    "Scene label_1003"
    menu:
        "Talk":
            jump label_1005
        "Pick up item":
            jump label_1006
        "Pick up item":
            $ luck += 1
            jump label_1007

label label_1005:
    "Scene label_1005"
    menu:
        "Open door":
            $ charisma += 2
            jump label_1008
        "Go forward":
            jump label_1009
        "Pick up item":
            jump label_1010
        "Look around":
            jump label_1011

label label_1008:
    "Scene label_1008"
    menu:
        "Go back":
            jump label_1012
        "Look around":
            jump label_1013
        "Look around":
            $ strength += 3
            jump label_1014
        "Use item":
            jump label_1015

label label_1012:
    "Scene label_1012"
    menu:
        "Look around":
            jump label_1016
        "Talk":
            jump label_1017

label label_1016:
    "Scene label_1016"
    jump end_1018

label label_1017:
    "Scene label_1017"
    jump end_1018

label label_1013:
    "Scene label_1013"
    if intelligence >= 12:
        jump label_1018

label label_1018:
    $ intelligence += 5
    jump end_1019

    jump label_1019

label label_1019:
    "Ветка false для label_1018"
    jump end_1020

label label_1014:
    "Scene label_1014"
    if luck >= 17:
        jump label_1020

label label_1020:
    $ luck += 2
    jump end_1021

    jump label_1021

label label_1021:
    "Ветка false для label_1020"
    jump end_1022

label label_1015:
    "Scene label_1015"
    menu:
        "Explore":
            $ charisma += 1
            jump label_1022
        "Explore":
            $ strength += 1
            jump label_1023

label label_1022:
    "Scene label_1022"
    jump end_1024

label label_1023:
    "Scene label_1023"
    jump end_1024

label label_1009:
    "Scene label_1009"
    menu:
        "Talk":
            $ intelligence += 2
            jump label_1024
        "Look around":
            $ charisma += 3
            jump label_1025
        "Talk":
            $ luck += 1
            jump label_1026
        "Go forward":
            jump label_1027

label label_1024:
    "Scene label_1024"
    if strength >= 15:
        jump label_1028

label label_1028:
    $ strength += 3
    jump end_1029

    jump label_1029

label label_1029:
    "Ветка false для label_1028"
    jump end_1030

label label_1025:
    "Scene label_1025"
    menu:
        "Go back":
            $ strength += 1
            jump label_1030
        "Use item":
            $ intelligence += 2
            jump label_1031
        "Open door":
            jump label_1032

label label_1030:
    "Scene label_1030"
    jump end_1033

label label_1031:
    "Scene label_1031"
    jump end_1033

label label_1032:
    "Scene label_1032"
    jump end_1033

label label_1026:
    "Scene label_1026"
    if luck >= 19:
        jump label_1033

label label_1033:
    $ luck += 5
    jump end_1034

    jump label_1034

label label_1034:
    "Ветка false для label_1033"
    jump end_1035

label label_1027:
    "Scene label_1027"
    if strength >= 18:
        jump label_1035

label label_1035:
    $ strength += 3
    jump end_1036

    jump label_1036

label label_1036:
    "Ветка false для label_1035"
    jump end_1037

label label_1010:
    "Scene label_1010"
    menu:
        "Go back":
            jump label_1037
        "Look around":
            $ intelligence += 2
            jump label_1038

label label_1037:
    "Scene label_1037"
    menu:
        "Look around":
            jump label_1039
        "Use item":
            jump label_1040
        "Talk":
            $ intelligence += 1
            jump label_1041

label label_1039:
    "Scene label_1039"
    jump end_1042

label label_1040:
    "Scene label_1040"
    jump end_1042

label label_1041:
    "Scene label_1041"
    jump end_1042

label label_1038:
    "Scene label_1038"
    menu:
        "Pick up item":
            $ charisma += 3
            jump label_1042
        "Go back":
            jump label_1043
        "Talk":
            $ charisma += 2
            jump label_1044

label label_1042:
    "Scene label_1042"
    jump end_1045

label label_1043:
    "Scene label_1043"
    jump end_1045

label label_1044:
    "Scene label_1044"
    jump end_1045

label label_1011:
    "Scene label_1011"
    menu:
        "Open door":
            jump label_1045
        "Use item":
            jump label_1046
        "Go back":
            $ strength += 2
            jump label_1047
        "Look around":
            $ strength += 1
            jump label_1048

label label_1045:
    "Scene label_1045"
    menu:
        "Open door":
            $ luck += 3
            jump label_1049
        "Explore":
            jump label_1050
        "Pick up item":
            $ luck += 2
            jump label_1051

label label_1049:
    "Scene label_1049"
    jump end_1052

label label_1050:
    "Scene label_1050"
    jump end_1052

label label_1051:
    "Scene label_1051"
    jump end_1052

label label_1046:
    "Scene label_1046"
    if luck >= 5:
        jump label_1052

label label_1052:
    $ luck += 3
    jump end_1053

    jump label_1053

label label_1053:
    "Ветка false для label_1052"
    jump end_1054

label label_1047:
    "Scene label_1047"
    menu:
        "Pick up item":
            $ strength += 3
            jump label_1054
        "Talk":
            $ charisma += 2
            jump label_1055

label label_1054:
    "Scene label_1054"
    jump end_1056

label label_1055:
    "Scene label_1055"
    jump end_1056

label label_1048:
    "Scene label_1048"
    menu:
        "Look around":
            jump label_1056
        "Pick up item":
            jump label_1057
        "Explore":
            jump label_1058
        "Open door":
            jump label_1059

label label_1056:
    "Scene label_1056"
    jump end_1060

label label_1057:
    "Scene label_1057"
    jump end_1060

label label_1058:
    "Scene label_1058"
    jump end_1060

label label_1059:
    "Scene label_1059"
    jump end_1060

label label_1006:
    "Scene label_1006"
    menu:
        "Go forward":
            $ luck += 1
            jump label_1060
        "Pick up item":
            $ strength += 2
            jump label_1061

label label_1060:
    "Scene label_1060"
    menu:
        "Explore":
            $ luck += 3
            jump label_1062
        "Use item":
            $ charisma += 2
            jump label_1063
        "Go forward":
            $ intelligence += 1
            jump label_1064
        "Use item":
            jump label_1065

label label_1062:
    "Scene label_1062"
    menu:
        "Go back":
            jump label_1066
        "Pick up item":
            $ intelligence += 3
            jump label_1067

label label_1066:
    "Scene label_1066"
    jump end_1068

label label_1067:
    "Scene label_1067"
    jump end_1068

label label_1063:
    "Scene label_1063"
    menu:
        "Talk":
            $ intelligence += 3
            jump label_1068
        "Look around":
            $ intelligence += 3
            jump label_1069
        "Go back":
            $ strength += 3
            jump label_1070
        "Go back":
            jump label_1071

label label_1068:
    "Scene label_1068"
    jump end_1072

label label_1069:
    "Scene label_1069"
    jump end_1072

label label_1070:
    "Scene label_1070"
    jump end_1072

label label_1071:
    "Scene label_1071"
    jump end_1072

label label_1064:
    "Scene label_1064"
    menu:
        "Open door":
            jump label_1072
        "Go forward":
            jump label_1073

label label_1072:
    "Scene label_1072"
    jump end_1074

label label_1073:
    "Scene label_1073"
    jump end_1074

label label_1065:
    "Scene label_1065"
    menu:
        "Go back":
            $ charisma += 2
            jump label_1074
        "Explore":
            jump label_1075
        "Go forward":
            jump label_1076

label label_1074:
    "Scene label_1074"
    jump end_1077

label label_1075:
    "Scene label_1075"
    jump end_1077

label label_1076:
    "Scene label_1076"
    jump end_1077

label label_1061:
    "Scene label_1061"
    if luck >= 18:
        jump label_1077

label label_1077:
    $ luck += 5
    menu:
        "Use item":
            $ strength += 3
            jump label_1078
        "Use item":
            jump label_1079
        "Open door":
            jump label_1080

label label_1078:
    "Scene label_1078"
    jump end_1081

label label_1079:
    "Scene label_1079"
    jump end_1081

label label_1080:
    "Scene label_1080"
    jump end_1081

    jump label_1081

label label_1081:
    "Ветка false для label_1077"
    menu:
        "Talk":
            $ strength += 3
            jump label_1082
        "Look around":
            $ charisma += 1
            jump label_1083

label label_1082:
    "Scene label_1082"
    jump end_1084

label label_1083:
    "Scene label_1083"
    jump end_1084

label label_1007:
    "Scene label_1007"
    menu:
        "Explore":
            jump label_1084
        "Use item":
            $ intelligence += 2
            jump label_1085
        "Go forward":
            jump label_1086
        "Use item":
            jump label_1087

label label_1084:
    "Scene label_1084"
    menu:
        "Pick up item":
            jump label_1088
        "Pick up item":
            jump label_1089
        "Look around":
            jump label_1090
        "Go forward":
            $ strength += 1
            jump label_1091

label label_1088:
    "Scene label_1088"
    if charisma >= 6:
        jump label_1092

label label_1092:
    $ charisma += 4
    jump end_1093

    jump label_1093

label label_1093:
    "Ветка false для label_1092"
    jump end_1094

label label_1089:
    "Scene label_1089"
    menu:
        "Look around":
            $ strength += 3
            jump label_1094
        "Go forward":
            $ charisma += 2
            jump label_1095
        "Look around":
            jump label_1096

label label_1094:
    "Scene label_1094"
    jump end_1097

label label_1095:
    "Scene label_1095"
    jump end_1097

label label_1096:
    "Scene label_1096"
    jump end_1097

label label_1090:
    "Scene label_1090"
    menu:
        "Go forward":
            $ charisma += 2
            jump label_1097
        "Look around":
            $ strength += 2
            jump label_1098
        "Explore":
            jump label_1099
        "Look around":
            $ strength += 3
            jump label_1100

label label_1097:
    "Scene label_1097"
    jump end_1101

label label_1098:
    "Scene label_1098"
    jump end_1101

label label_1099:
    "Scene label_1099"
    jump end_1101

label label_1100:
    "Scene label_1100"
    jump end_1101

label label_1091:
    "Scene label_1091"
    menu:
        "Talk":
            jump label_1101
        "Go back":
            $ charisma += 3
            jump label_1102

label label_1101:
    "Scene label_1101"
    jump end_1103

label label_1102:
    "Scene label_1102"
    jump end_1103

label label_1085:
    "Scene label_1085"
    menu:
        "Use item":
            $ strength += 1
            jump label_1103
        "Talk":
            $ charisma += 3
            jump label_1104

label label_1103:
    "Scene label_1103"
    menu:
        "Go back":
            jump label_1105
        "Talk":
            $ luck += 3
            jump label_1106
        "Explore":
            $ strength += 3
            jump label_1107

label label_1105:
    "Scene label_1105"
    jump end_1108

label label_1106:
    "Scene label_1106"
    jump end_1108

label label_1107:
    "Scene label_1107"
    jump end_1108

label label_1104:
    "Scene label_1104"
    menu:
        "Talk":
            $ strength += 2
            jump label_1108
        "Explore":
            $ intelligence += 3
            jump label_1109
        "Use item":
            jump label_1110
        "Explore":
            $ charisma += 3
            jump label_1111

label label_1108:
    "Scene label_1108"
    jump end_1112

label label_1109:
    "Scene label_1109"
    jump end_1112

label label_1110:
    "Scene label_1110"
    jump end_1112

label label_1111:
    "Scene label_1111"
    jump end_1112

label label_1086:
    "Scene label_1086"
    menu:
        "Explore":
            jump label_1112
        "Explore":
            jump label_1113
        "Open door":
            $ strength += 2
            jump label_1114

label label_1112:
    "Scene label_1112"
    menu:
        "Pick up item":
            $ strength += 3
            jump label_1115
        "Use item":
            jump label_1116

label label_1115:
    "Scene label_1115"
    jump end_1117

label label_1116:
    "Scene label_1116"
    jump end_1117

label label_1113:
    "Scene label_1113"
    menu:
        "Use item":
            $ luck += 3
            jump label_1117
        "Open door":
            $ intelligence += 1
            jump label_1118

label label_1117:
    "Scene label_1117"
    jump end_1119

label label_1118:
    "Scene label_1118"
    jump end_1119

label label_1114:
    "Scene label_1114"
    menu:
        "Explore":
            $ strength += 1
            jump label_1119
        "Go back":
            $ luck += 1
            jump label_1120

label label_1119:
    "Scene label_1119"
    jump end_1121

label label_1120:
    "Scene label_1120"
    jump end_1121

label label_1087:
    "Scene label_1087"
    menu:
        "Use item":
            $ intelligence += 2
            jump label_1121
        "Talk":
            $ intelligence += 1
            jump label_1122

label label_1121:
    "Scene label_1121"
    if intelligence >= 13:
        jump label_1123

label label_1123:
    $ intelligence += 2
    jump end_1124

    jump label_1124

label label_1124:
    "Ветка false для label_1123"
    jump end_1125

label label_1122:
    "Scene label_1122"
    if intelligence >= 17:
        jump label_1125

label label_1125:
    $ intelligence += 2
    jump end_1126

    jump label_1126

label label_1126:
    "Ветка false для label_1125"
    jump end_1127

label label_1004:
    "Scene label_1004"
    menu:
        "Go back":
            $ luck += 2
            jump label_1127
        "Talk":
            jump label_1128

label label_1127:
    "Scene label_1127"
    menu:
        "Open door":
            jump label_1129
        "Look around":
            $ intelligence += 1
            jump label_1130
        "Use item":
            jump label_1131
        "Explore":
            $ charisma += 3
            jump label_1132

label label_1129:
    "Scene label_1129"
    if strength >= 11:
        jump label_1133

label label_1133:
    $ strength += 4
    menu:
        "Use item":
            $ luck += 1
            jump label_1134
        "Pick up item":
            $ strength += 2
            jump label_1135
        "Look around":
            $ charisma += 3
            jump label_1136

label label_1134:
    "Scene label_1134"
    jump end_1137

label label_1135:
    "Scene label_1135"
    jump end_1137

label label_1136:
    "Scene label_1136"
    jump end_1137

    jump label_1137

label label_1137:
    "Ветка false для label_1133"
    menu:
        "Pick up item":
            jump label_1138
        "Talk":
            $ luck += 3
            jump label_1139
        "Pick up item":
            jump label_1140

label label_1138:
    "Scene label_1138"
    jump end_1141

label label_1139:
    "Scene label_1139"
    jump end_1141

label label_1140:
    "Scene label_1140"
    jump end_1141

label label_1130:
    "Scene label_1130"
    menu:
        "Open door":
            jump label_1141
        "Go forward":
            $ intelligence += 2
            jump label_1142
        "Use item":
            $ luck += 2
            jump label_1143

label label_1141:
    "Scene label_1141"
    menu:
        "Talk":
            jump label_1144
        "Explore":
            $ strength += 1
            jump label_1145
        "Look around":
            $ luck += 1
            jump label_1146
        "Go forward":
            $ luck += 2
            jump label_1147

label label_1144:
    "Scene label_1144"
    jump end_1148

label label_1145:
    "Scene label_1145"
    jump end_1148

label label_1146:
    "Scene label_1146"
    jump end_1148

label label_1147:
    "Scene label_1147"
    jump end_1148

label label_1142:
    "Scene label_1142"
    menu:
        "Open door":
            $ charisma += 2
            jump label_1148
        "Go back":
            $ intelligence += 2
            jump label_1149
        "Use item":
            $ strength += 2
            jump label_1150

label label_1148:
    "Scene label_1148"
    jump end_1151

label label_1149:
    "Scene label_1149"
    jump end_1151

label label_1150:
    "Scene label_1150"
    jump end_1151

label label_1143:
    "Scene label_1143"
    menu:
        "Look around":
            jump label_1151
        "Use item":
            $ strength += 2
            jump label_1152
        "Go forward":
            jump label_1153

label label_1151:
    "Scene label_1151"
    jump end_1154

label label_1152:
    "Scene label_1152"
    jump end_1154

label label_1153:
    "Scene label_1153"
    jump end_1154

label label_1131:
    "Scene label_1131"
    menu:
        "Explore":
            $ luck += 1
            jump label_1154
        "Talk":
            jump label_1155
        "Go back":
            $ luck += 2
            jump label_1156
        "Explore":
            jump label_1157

label label_1154:
    "Scene label_1154"
    menu:
        "Go forward":
            $ intelligence += 2
            jump label_1158
        "Use item":
            $ intelligence += 2
            jump label_1159
        "Use item":
            jump label_1160

label label_1158:
    "Scene label_1158"
    jump end_1161

label label_1159:
    "Scene label_1159"
    jump end_1161

label label_1160:
    "Scene label_1160"
    jump end_1161

label label_1155:
    "Scene label_1155"
    menu:
        "Pick up item":
            $ strength += 2
            jump label_1161
        "Use item":
            $ charisma += 1
            jump label_1162
        "Pick up item":
            $ strength += 2
            jump label_1163

label label_1161:
    "Scene label_1161"
    jump end_1164

label label_1162:
    "Scene label_1162"
    jump end_1164

label label_1163:
    "Scene label_1163"
    jump end_1164

label label_1156:
    "Scene label_1156"
    if intelligence >= 14:
        jump label_1164

label label_1164:
    $ intelligence += 2
    jump end_1165

    jump label_1165

label label_1165:
    "Ветка false для label_1164"
    jump end_1166

label label_1157:
    "Scene label_1157"
    menu:
        "Explore":
            $ charisma += 2
            jump label_1166
        "Open door":
            jump label_1167
        "Go back":
            $ strength += 3
            jump label_1168
        "Go forward":
            jump label_1169

label label_1166:
    "Scene label_1166"
    jump end_1170

label label_1167:
    "Scene label_1167"
    jump end_1170

label label_1168:
    "Scene label_1168"
    jump end_1170

label label_1169:
    "Scene label_1169"
    jump end_1170

label label_1132:
    "Scene label_1132"
    if luck >= 17:
        jump label_1170

label label_1170:
    $ luck += 5
    if charisma >= 7:
        jump label_1171

label label_1171:
    $ charisma += 5
    jump end_1172

    jump label_1172

label label_1172:
    "Ветка false для label_1171"
    jump end_1173

    jump label_1173

label label_1173:
    "Ветка false для label_1170"
    if strength >= 15:
        jump label_1174

label label_1174:
    $ strength += 5
    jump end_1175

    jump label_1175

label label_1175:
    "Ветка false для label_1174"
    jump end_1176

label label_1128:
    "Scene label_1128"
    menu:
        "Look around":
            $ intelligence += 1
            jump label_1176
        "Pick up item":
            $ intelligence += 1
            jump label_1177
        "Open door":
            $ intelligence += 2
            jump label_1178

label label_1176:
    "Scene label_1176"
    menu:
        "Pick up item":
            $ strength += 1
            jump label_1179
        "Explore":
            jump label_1180

label label_1179:
    "Scene label_1179"
    menu:
        "Look around":
            $ charisma += 2
            jump label_1181
        "Look around":
            $ intelligence += 1
            jump label_1182

label label_1181:
    "Scene label_1181"
    jump end_1183

label label_1182:
    "Scene label_1182"
    jump end_1183

label label_1180:
    "Scene label_1180"
    menu:
        "Open door":
            jump label_1183
        "Pick up item":
            $ luck += 3
            jump label_1184
        "Use item":
            jump label_1185

label label_1183:
    "Scene label_1183"
    jump end_1186

label label_1184:
    "Scene label_1184"
    jump end_1186

label label_1185:
    "Scene label_1185"
    jump end_1186

label label_1177:
    "Scene label_1177"
    menu:
        "Use item":
            $ intelligence += 2
            jump label_1186
        "Look around":
            jump label_1187
        "Use item":
            jump label_1188

label label_1186:
    "Scene label_1186"
    menu:
        "Pick up item":
            $ strength += 3
            jump label_1189
        "Look around":
            $ charisma += 2
            jump label_1190
        "Go back":
            $ intelligence += 2
            jump label_1191

label label_1189:
    "Scene label_1189"
    jump end_1192

label label_1190:
    "Scene label_1190"
    jump end_1192

label label_1191:
    "Scene label_1191"
    jump end_1192

label label_1187:
    "Scene label_1187"
    if charisma >= 19:
        jump label_1192

label label_1192:
    $ charisma += 5
    jump end_1193

    jump label_1193

label label_1193:
    "Ветка false для label_1192"
    jump end_1194

label label_1188:
    "Scene label_1188"
    menu:
        "Look around":
            $ strength += 1
            jump label_1194
        "Talk":
            $ luck += 3
            jump label_1195

label label_1194:
    "Scene label_1194"
    jump end_1196

label label_1195:
    "Scene label_1195"
    jump end_1196

label label_1178:
    "Scene label_1178"
    menu:
        "Use item":
            jump label_1196
        "Open door":
            jump label_1197
        "Look around":
            jump label_1198
        "Look around":
            jump label_1199

label label_1196:
    "Scene label_1196"
    menu:
        "Open door":
            $ luck += 1
            jump label_1200
        "Go forward":
            $ strength += 3
            jump label_1201
        "Pick up item":
            $ charisma += 1
            jump label_1202

label label_1200:
    "Scene label_1200"
    jump end_1203

label label_1201:
    "Scene label_1201"
    jump end_1203

label label_1202:
    "Scene label_1202"
    jump end_1203

label label_1197:
    "Scene label_1197"
    menu:
        "Go back":
            $ intelligence += 2
            jump label_1203
        "Pick up item":
            $ strength += 1
            jump label_1204

label label_1203:
    "Scene label_1203"
    jump end_1205

label label_1204:
    "Scene label_1204"
    jump end_1205

label label_1198:
    "Scene label_1198"
    menu:
        "Pick up item":
            $ luck += 1
            jump label_1205
        "Talk":
            jump label_1206

label label_1205:
    "Scene label_1205"
    jump end_1207

label label_1206:
    "Scene label_1206"
    jump end_1207

label label_1199:
    "Scene label_1199"
    menu:
        "Go back":
            $ charisma += 1
            jump label_1207
        "Look around":
            jump label_1208

label label_1207:
    "Scene label_1207"
    jump end_1209

label label_1208:
    "Scene label_1208"
    jump end_1209

label label_578:
    "Scene label_578"
    if luck >= 9:
        jump label_1209

label label_1209:
    $ luck += 5
    menu:
        "Go forward":
            jump label_1210
        "Use item":
            $ strength += 3
            jump label_1211

label label_1210:
    "Scene label_1210"
    menu:
        "Look around":
            $ luck += 2
            jump label_1212
        "Go forward":
            jump label_1213
        "Go forward":
            jump label_1214
        "Use item":
            jump label_1215

label label_1212:
    "Scene label_1212"
    menu:
        "Use item":
            $ charisma += 1
            jump label_1216
        "Go forward":
            $ intelligence += 3
            jump label_1217

label label_1216:
    "Scene label_1216"
    menu:
        "Look around":
            jump label_1218
        "Talk":
            jump label_1219

label label_1218:
    "Scene label_1218"
    jump end_1220

label label_1219:
    "Scene label_1219"
    jump end_1220

label label_1217:
    "Scene label_1217"
    if strength >= 15:
        jump label_1220

label label_1220:
    $ strength += 4
    jump end_1221

    jump label_1221

label label_1221:
    "Ветка false для label_1220"
    jump end_1222

label label_1213:
    "Scene label_1213"
    menu:
        "Use item":
            jump label_1222
        "Open door":
            jump label_1223

label label_1222:
    "Scene label_1222"
    if intelligence >= 8:
        jump label_1224

label label_1224:
    $ intelligence += 4
    jump end_1225

    jump label_1225

label label_1225:
    "Ветка false для label_1224"
    jump end_1226

label label_1223:
    "Scene label_1223"
    menu:
        "Open door":
            jump label_1226
        "Go forward":
            $ charisma += 1
            jump label_1227

label label_1226:
    "Scene label_1226"
    jump end_1228

label label_1227:
    "Scene label_1227"
    jump end_1228

label label_1214:
    "Scene label_1214"
    if luck >= 16:
        jump label_1228

label label_1228:
    $ luck += 2
    if intelligence >= 18:
        jump label_1229

label label_1229:
    $ intelligence += 4
    jump end_1230

    jump label_1230

label label_1230:
    "Ветка false для label_1229"
    jump end_1231

    jump label_1231

label label_1231:
    "Ветка false для label_1228"
    menu:
        "Look around":
            jump label_1232
        "Talk":
            $ strength += 3
            jump label_1233
        "Explore":
            jump label_1234

label label_1232:
    "Scene label_1232"
    jump end_1235

label label_1233:
    "Scene label_1233"
    jump end_1235

label label_1234:
    "Scene label_1234"
    jump end_1235

label label_1215:
    "Scene label_1215"
    menu:
        "Talk":
            $ luck += 3
            jump label_1235
        "Pick up item":
            $ strength += 3
            jump label_1236
        "Pick up item":
            $ intelligence += 3
            jump label_1237
        "Go forward":
            $ strength += 2
            jump label_1238

label label_1235:
    "Scene label_1235"
    if charisma >= 12:
        jump label_1239

label label_1239:
    $ charisma += 2
    jump end_1240

    jump label_1240

label label_1240:
    "Ветка false для label_1239"
    jump end_1241

label label_1236:
    "Scene label_1236"
    if luck >= 20:
        jump label_1241

label label_1241:
    $ luck += 4
    jump end_1242

    jump label_1242

label label_1242:
    "Ветка false для label_1241"
    jump end_1243

label label_1237:
    "Scene label_1237"
    if charisma >= 11:
        jump label_1243

label label_1243:
    $ charisma += 2
    jump end_1244

label label_1238:
    "Scene label_1238"
label label_1211:
    "Scene label_1211"
label label_26:
    "Scene label_26"
label label_27:
    "Scene label_27"
label label_22:
    "Scene label_22"
label label_23:
    "Scene label_23"
label label_18:
    "Scene label_18"
label label_19:
    "Scene label_19"
label label_20:
    "Scene label_20"
label label_14:
    "Scene label_14"
label label_15:
    "Scene label_15"
label label_16:
    "Scene label_16"
label label_10:
    "Scene label_10"
label label_11:
    "Scene label_11"
label label_12:
    "Scene label_12"
label label_8:
    "Scene label_8"
label label_4:
    "Scene label_4"
label label_5:
    "Scene label_5"
label label_6:
    "Scene label_6"
label label_1:
    "Scene label_1"

label end_45:
    "Конец: end_45"

label end_45:
    "Конец: end_45"

label end_47:
    "Конец: end_47"

label end_47:
    "Конец: end_47"

label end_48:
    "Конец: end_48"

label end_49:
    "Конец: end_49"

label end_53:
    "Конец: end_53"

label end_53:
    "Конец: end_53"

label end_53:
    "Конец: end_53"

label end_53:
    "Конец: end_53"

label end_60:
    "Конец: end_60"

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

label end_65:
    "Конец: end_65"

label end_65:
    "Конец: end_65"

label end_72:
    "Конец: end_72"

label end_73:
    "Конец: end_73"

label end_77:
    "Конец: end_77"

label end_77:
    "Конец: end_77"

label end_77:
    "Конец: end_77"

label end_77:
    "Конец: end_77"

label end_80:
    "Конец: end_80"

label end_80:
    "Конец: end_80"

label end_80:
    "Конец: end_80"

label end_81:
    "Конец: end_81"

label end_82:
    "Конец: end_82"

label end_87:
    "Конец: end_87"

label end_87:
    "Конец: end_87"

label end_87:
    "Конец: end_87"

label end_87:
    "Конец: end_87"

label end_92:
    "Конец: end_92"

label end_92:
    "Конец: end_92"

label end_92:
    "Конец: end_92"

label end_92:
    "Конец: end_92"

label end_99:
    "Конец: end_99"

label end_99:
    "Конец: end_99"

label end_99:
    "Конец: end_99"

label end_99:
    "Конец: end_99"

label end_102:
    "Конец: end_102"

label end_102:
    "Конец: end_102"

label end_106:
    "Конец: end_106"

label end_106:
    "Конец: end_106"

label end_106:
    "Конец: end_106"

label end_108:
    "Конец: end_108"

label end_109:
    "Конец: end_109"

label end_118:
    "Конец: end_118"

label end_118:
    "Конец: end_118"

label end_118:
    "Конец: end_118"

label end_122:
    "Конец: end_122"

label end_122:
    "Конец: end_122"

label end_122:
    "Конец: end_122"

label end_122:
    "Конец: end_122"

label end_123:
    "Конец: end_123"

label end_124:
    "Конец: end_124"

label end_126:
    "Конец: end_126"

label end_126:
    "Конец: end_126"

label end_131:
    "Конец: end_131"

label end_131:
    "Конец: end_131"

label end_134:
    "Конец: end_134"

label end_134:
    "Конец: end_134"

label end_134:
    "Конец: end_134"

label end_140:
    "Конец: end_140"

label end_140:
    "Конец: end_140"

label end_140:
    "Конец: end_140"

label end_142:
    "Конец: end_142"

label end_143:
    "Конец: end_143"

label end_148:
    "Конец: end_148"

label end_149:
    "Конец: end_149"

label end_150:
    "Конец: end_150"

label end_151:
    "Конец: end_151"

label end_152:
    "Конец: end_152"

label end_153:
    "Конец: end_153"

label end_159:
    "Конец: end_159"

label end_159:
    "Конец: end_159"

label end_161:
    "Конец: end_161"

label end_162:
    "Конец: end_162"

label end_165:
    "Конец: end_165"

label end_165:
    "Конец: end_165"

label end_167:
    "Конец: end_167"

label end_168:
    "Конец: end_168"

label end_176:
    "Конец: end_176"

label end_177:
    "Конец: end_177"

label end_181:
    "Конец: end_181"

label end_181:
    "Конец: end_181"

label end_181:
    "Конец: end_181"

label end_181:
    "Конец: end_181"

label end_188:
    "Конец: end_188"

label end_188:
    "Конец: end_188"

label end_188:
    "Конец: end_188"

label end_188:
    "Конец: end_188"

label end_189:
    "Конец: end_189"

label end_190:
    "Конец: end_190"

label end_191:
    "Конец: end_191"

label end_192:
    "Конец: end_192"

label end_198:
    "Конец: end_198"

label end_198:
    "Конец: end_198"

label end_198:
    "Конец: end_198"

label end_198:
    "Конец: end_198"

label end_201:
    "Конец: end_201"

label end_201:
    "Конец: end_201"

label end_201:
    "Конец: end_201"

label end_206:
    "Конец: end_206"

label end_206:
    "Конец: end_206"

label end_209:
    "Конец: end_209"

label end_209:
    "Конец: end_209"

label end_209:
    "Конец: end_209"

label end_212:
    "Конец: end_212"

label end_212:
    "Конец: end_212"

label end_212:
    "Конец: end_212"

label end_222:
    "Конец: end_222"

label end_223:
    "Конец: end_223"

label end_226:
    "Конец: end_226"

label end_226:
    "Конец: end_226"

label end_230:
    "Конец: end_230"

label end_230:
    "Конец: end_230"

label end_232:
    "Конец: end_232"

label end_232:
    "Конец: end_232"

label end_236:
    "Конец: end_236"

label end_236:
    "Конец: end_236"

label end_236:
    "Конец: end_236"

label end_239:
    "Конец: end_239"

label end_239:
    "Конец: end_239"

label end_244:
    "Конец: end_244"

label end_244:
    "Конец: end_244"

label end_244:
    "Конец: end_244"

label end_244:
    "Конец: end_244"

label end_247:
    "Конец: end_247"

label end_247:
    "Конец: end_247"

label end_254:
    "Конец: end_254"

label end_254:
    "Конец: end_254"

label end_254:
    "Конец: end_254"

label end_259:
    "Конец: end_259"

label end_259:
    "Конец: end_259"

label end_259:
    "Конец: end_259"

label end_259:
    "Конец: end_259"

label end_267:
    "Конец: end_267"

label end_267:
    "Конец: end_267"

label end_267:
    "Конец: end_267"

label end_267:
    "Конец: end_267"

label end_270:
    "Конец: end_270"

label end_270:
    "Конец: end_270"

label end_270:
    "Конец: end_270"

label end_272:
    "Конец: end_272"

label end_272:
    "Конец: end_272"

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

label end_281:
    "Конец: end_281"

label end_282:
    "Конец: end_282"

label end_291:
    "Конец: end_291"

label end_291:
    "Конец: end_291"

label end_291:
    "Конец: end_291"

label end_291:
    "Конец: end_291"

label end_293:
    "Конец: end_293"

label end_293:
    "Конец: end_293"

label end_300:
    "Конец: end_300"

label end_300:
    "Конец: end_300"

label end_300:
    "Конец: end_300"

label end_300:
    "Конец: end_300"

label end_304:
    "Конец: end_304"

label end_304:
    "Конец: end_304"

label end_304:
    "Конец: end_304"

label end_304:
    "Конец: end_304"

label end_307:
    "Конец: end_307"

label end_307:
    "Конец: end_307"

label end_307:
    "Конец: end_307"

label end_309:
    "Конец: end_309"

label end_310:
    "Конец: end_310"

label end_314:
    "Конец: end_314"

label end_314:
    "Конец: end_314"

label end_314:
    "Конец: end_314"

label end_320:
    "Конец: end_320"

label end_320:
    "Конец: end_320"

label end_320:
    "Конец: end_320"

label end_324:
    "Конец: end_324"

label end_324:
    "Конец: end_324"

label end_324:
    "Конец: end_324"

label end_329:
    "Конец: end_329"

label end_329:
    "Конец: end_329"

label end_329:
    "Конец: end_329"

label end_329:
    "Конец: end_329"

label end_334:
    "Конец: end_334"

label end_334:
    "Конец: end_334"

label end_334:
    "Конец: end_334"

label end_334:
    "Конец: end_334"

label end_347:
    "Конец: end_347"

label end_347:
    "Конец: end_347"

label end_347:
    "Конец: end_347"

label end_347:
    "Конец: end_347"

label end_350:
    "Конец: end_350"

label end_350:
    "Конец: end_350"

label end_350:
    "Конец: end_350"

label end_351:
    "Конец: end_351"

label end_352:
    "Конец: end_352"

label end_357:
    "Конец: end_357"

label end_357:
    "Конец: end_357"

label end_357:
    "Конец: end_357"

label end_361:
    "Конец: end_361"

label end_361:
    "Конец: end_361"

label end_361:
    "Конец: end_361"

label end_367:
    "Конец: end_367"

label end_367:
    "Конец: end_367"

label end_372:
    "Конец: end_372"

label end_372:
    "Конец: end_372"

label end_372:
    "Конец: end_372"

label end_372:
    "Конец: end_372"

label end_374:
    "Конец: end_374"

label end_375:
    "Конец: end_375"

label end_377:
    "Конец: end_377"

label end_378:
    "Конец: end_378"

label end_386:
    "Конец: end_386"

label end_386:
    "Конец: end_386"

label end_388:
    "Конец: end_388"

label end_389:
    "Конец: end_389"

label end_394:
    "Конец: end_394"

label end_395:
    "Конец: end_395"

label end_396:
    "Конец: end_396"

label end_397:
    "Конец: end_397"

label end_401:
    "Конец: end_401"

label end_401:
    "Конец: end_401"

label end_401:
    "Конец: end_401"

label end_401:
    "Конец: end_401"

label end_405:
    "Конец: end_405"

label end_405:
    "Конец: end_405"

label end_405:
    "Конец: end_405"

label end_405:
    "Конец: end_405"

label end_415:
    "Конец: end_415"

label end_415:
    "Конец: end_415"

label end_415:
    "Конец: end_415"

label end_418:
    "Конец: end_418"

label end_418:
    "Конец: end_418"

label end_418:
    "Конец: end_418"

label end_421:
    "Конец: end_421"

label end_421:
    "Конец: end_421"

label end_421:
    "Конец: end_421"

label end_425:
    "Конец: end_425"

label end_426:
    "Конец: end_426"

label end_428:
    "Конец: end_428"

label end_428:
    "Конец: end_428"

label end_431:
    "Конец: end_431"

label end_431:
    "Конец: end_431"

label end_431:
    "Конец: end_431"

label end_433:
    "Конец: end_433"

label end_434:
    "Конец: end_434"

label end_436:
    "Конец: end_436"

label end_437:
    "Конец: end_437"

label end_442:
    "Конец: end_442"

label end_443:
    "Конец: end_443"

label end_446:
    "Конец: end_446"

label end_446:
    "Конец: end_446"

label end_446:
    "Конец: end_446"

label end_449:
    "Конец: end_449"

label end_449:
    "Конец: end_449"

label end_449:
    "Конец: end_449"

label end_451:
    "Конец: end_451"

label end_451:
    "Конец: end_451"

label end_456:
    "Конец: end_456"

label end_457:
    "Конец: end_457"

label end_460:
    "Конец: end_460"

label end_460:
    "Конец: end_460"

label end_460:
    "Конец: end_460"

label end_465:
    "Конец: end_465"

label end_465:
    "Конец: end_465"

label end_469:
    "Конец: end_469"

label end_469:
    "Конец: end_469"

label end_469:
    "Конец: end_469"

label end_469:
    "Конец: end_469"

label end_471:
    "Конец: end_471"

label end_471:
    "Конец: end_471"

label end_484:
    "Конец: end_484"

label end_484:
    "Конец: end_484"

label end_484:
    "Конец: end_484"

label end_484:
    "Конец: end_484"

label end_486:
    "Конец: end_486"

label end_486:
    "Конец: end_486"

label end_490:
    "Конец: end_490"

label end_490:
    "Конец: end_490"

label end_490:
    "Конец: end_490"

label end_490:
    "Конец: end_490"

label end_491:
    "Конец: end_491"

label end_492:
    "Конец: end_492"

label end_496:
    "Конец: end_496"

label end_496:
    "Конец: end_496"

label end_496:
    "Конец: end_496"

label end_498:
    "Конец: end_498"

label end_499:
    "Конец: end_499"

label end_501:
    "Конец: end_501"

label end_502:
    "Конец: end_502"

label end_504:
    "Конец: end_504"

label end_505:
    "Конец: end_505"

label end_510:
    "Конец: end_510"

label end_511:
    "Конец: end_511"

label end_513:
    "Конец: end_513"

label end_513:
    "Конец: end_513"

label end_514:
    "Конец: end_514"

label end_515:
    "Конец: end_515"

label end_517:
    "Конец: end_517"

label end_517:
    "Конец: end_517"

label end_524:
    "Конец: end_524"

label end_524:
    "Конец: end_524"

label end_524:
    "Конец: end_524"

label end_527:
    "Конец: end_527"

label end_527:
    "Конец: end_527"

label end_527:
    "Конец: end_527"

label end_531:
    "Конец: end_531"

label end_531:
    "Конец: end_531"

label end_533:
    "Конец: end_533"

label end_534:
    "Конец: end_534"

label end_540:
    "Конец: end_540"

label end_540:
    "Конец: end_540"

label end_542:
    "Конец: end_542"

label end_543:
    "Конец: end_543"

label end_549:
    "Конец: end_549"

label end_549:
    "Конец: end_549"

label end_549:
    "Конец: end_549"

label end_553:
    "Конец: end_553"

label end_553:
    "Конец: end_553"

label end_553:
    "Конец: end_553"

label end_553:
    "Конец: end_553"

label end_558:
    "Конец: end_558"

label end_558:
    "Конец: end_558"

label end_558:
    "Конец: end_558"

label end_561:
    "Конец: end_561"

label end_561:
    "Конец: end_561"

label end_568:
    "Конец: end_568"

label end_568:
    "Конец: end_568"

label end_571:
    "Конец: end_571"

label end_571:
    "Конец: end_571"

label end_571:
    "Конец: end_571"

label end_573:
    "Конец: end_573"

label end_573:
    "Конец: end_573"

label end_575:
    "Конец: end_575"

label end_575:
    "Конец: end_575"

label end_588:
    "Конец: end_588"

label end_588:
    "Конец: end_588"

label end_593:
    "Конец: end_593"

label end_593:
    "Конец: end_593"

label end_593:
    "Конец: end_593"

label end_593:
    "Конец: end_593"

label end_600:
    "Конец: end_600"

label end_600:
    "Конец: end_600"

label end_600:
    "Конец: end_600"

label end_601:
    "Конец: end_601"

label end_602:
    "Конец: end_602"

label end_605:
    "Конец: end_605"

label end_605:
    "Конец: end_605"

label end_605:
    "Конец: end_605"

label end_608:
    "Конец: end_608"

label end_608:
    "Конец: end_608"

label end_608:
    "Конец: end_608"

label end_613:
    "Конец: end_613"

label end_613:
    "Конец: end_613"

label end_613:
    "Конец: end_613"

label end_616:
    "Конец: end_616"

label end_616:
    "Конец: end_616"

label end_620:
    "Конец: end_620"

label end_621:
    "Конец: end_621"

label end_623:
    "Конец: end_623"

label end_623:
    "Конец: end_623"

label end_628:
    "Конец: end_628"

label end_628:
    "Конец: end_628"

label end_631:
    "Конец: end_631"

label end_631:
    "Конец: end_631"

label end_631:
    "Конец: end_631"

label end_637:
    "Конец: end_637"

label end_637:
    "Конец: end_637"

label end_637:
    "Конец: end_637"

label end_641:
    "Конец: end_641"

label end_641:
    "Конец: end_641"

label end_641:
    "Конец: end_641"

label end_641:
    "Конец: end_641"

label end_652:
    "Конец: end_652"

label end_653:
    "Конец: end_653"

label end_656:
    "Конец: end_656"

label end_656:
    "Конец: end_656"

label end_656:
    "Конец: end_656"

label end_658:
    "Конец: end_658"

label end_658:
    "Конец: end_658"

label end_665:
    "Конец: end_665"

label end_665:
    "Конец: end_665"

label end_665:
    "Конец: end_665"

label end_665:
    "Конец: end_665"

label end_668:
    "Конец: end_668"

label end_668:
    "Конец: end_668"

label end_668:
    "Конец: end_668"

label end_669:
    "Конец: end_669"

label end_670:
    "Конец: end_670"

label end_676:
    "Конец: end_676"

label end_676:
    "Конец: end_676"

label end_679:
    "Конец: end_679"

label end_679:
    "Конец: end_679"

label end_684:
    "Конец: end_684"

label end_684:
    "Конец: end_684"

label end_684:
    "Конец: end_684"

label end_684:
    "Конец: end_684"

label end_689:
    "Конец: end_689"

label end_689:
    "Конец: end_689"

label end_689:
    "Конец: end_689"

label end_689:
    "Конец: end_689"

label end_695:
    "Конец: end_695"

label end_695:
    "Конец: end_695"

label end_695:
    "Конец: end_695"

label end_697:
    "Конец: end_697"

label end_697:
    "Конец: end_697"

label end_699:
    "Конец: end_699"

label end_699:
    "Конец: end_699"

label end_705:
    "Конец: end_705"

label end_705:
    "Конец: end_705"

label end_709:
    "Конец: end_709"

label end_709:
    "Конец: end_709"

label end_709:
    "Конец: end_709"

label end_715:
    "Конец: end_715"

label end_715:
    "Конец: end_715"

label end_718:
    "Конец: end_718"

label end_718:
    "Конец: end_718"

label end_718:
    "Конец: end_718"

label end_719:
    "Конец: end_719"

label end_720:
    "Конец: end_720"

label end_723:
    "Конец: end_723"

label end_723:
    "Конец: end_723"

label end_723:
    "Конец: end_723"

label end_730:
    "Конец: end_730"

label end_730:
    "Конец: end_730"

label end_730:
    "Конец: end_730"

label end_730:
    "Конец: end_730"

label end_731:
    "Конец: end_731"

label end_732:
    "Конец: end_732"

label end_734:
    "Конец: end_734"

label end_734:
    "Конец: end_734"

label end_741:
    "Конец: end_741"

label end_741:
    "Конец: end_741"

label end_741:
    "Конец: end_741"

label end_743:
    "Конец: end_743"

label end_744:
    "Конец: end_744"

label end_749:
    "Конец: end_749"

label end_749:
    "Конец: end_749"

label end_749:
    "Конец: end_749"

label end_750:
    "Конец: end_750"

label end_751:
    "Конец: end_751"

label end_756:
    "Конец: end_756"

label end_757:
    "Конец: end_757"

label end_760:
    "Конец: end_760"

label end_760:
    "Конец: end_760"

label end_760:
    "Конец: end_760"

label end_764:
    "Конец: end_764"

label end_764:
    "Конец: end_764"

label end_764:
    "Конец: end_764"

label end_764:
    "Конец: end_764"

label end_766:
    "Конец: end_766"

label end_766:
    "Конец: end_766"

label end_779:
    "Конец: end_779"

label end_779:
    "Конец: end_779"

label end_779:
    "Конец: end_779"

label end_782:
    "Конец: end_782"

label end_782:
    "Конец: end_782"

label end_788:
    "Конец: end_788"

label end_788:
    "Конец: end_788"

label end_791:
    "Конец: end_791"

label end_791:
    "Конец: end_791"

label end_791:
    "Конец: end_791"

label end_793:
    "Конец: end_793"

label end_793:
    "Конец: end_793"

label end_795:
    "Конец: end_795"

label end_795:
    "Конец: end_795"

label end_800:
    "Конец: end_800"

label end_801:
    "Конец: end_801"

label end_802:
    "Конец: end_802"

label end_803:
    "Конец: end_803"

label end_807:
    "Конец: end_807"

label end_807:
    "Конец: end_807"

label end_807:
    "Конец: end_807"

label end_807:
    "Конец: end_807"

label end_809:
    "Конец: end_809"

label end_809:
    "Конец: end_809"

label end_811:
    "Конец: end_811"

label end_812:
    "Конец: end_812"

label end_814:
    "Конец: end_814"

label end_815:
    "Конец: end_815"

label end_819:
    "Конец: end_819"

label end_820:
    "Конец: end_820"

label end_824:
    "Конец: end_824"

label end_824:
    "Конец: end_824"

label end_824:
    "Конец: end_824"

label end_832:
    "Конец: end_832"

label end_832:
    "Конец: end_832"

label end_832:
    "Конец: end_832"

label end_832:
    "Конец: end_832"

label end_833:
    "Конец: end_833"

label end_834:
    "Конец: end_834"

label end_835:
    "Конец: end_835"

label end_836:
    "Конец: end_836"

label end_837:
    "Конец: end_837"

label end_838:
    "Конец: end_838"

label end_852:
    "Конец: end_852"

label end_852:
    "Конец: end_852"

label end_852:
    "Конец: end_852"

label end_852:
    "Конец: end_852"

label end_854:
    "Конец: end_854"

label end_854:
    "Конец: end_854"

label end_858:
    "Конец: end_858"

label end_858:
    "Конец: end_858"

label end_858:
    "Конец: end_858"

label end_858:
    "Конец: end_858"

label end_859:
    "Конец: end_859"

label end_860:
    "Конец: end_860"

label end_864:
    "Конец: end_864"

label end_865:
    "Конец: end_865"

label end_866:
    "Конец: end_866"

label end_867:
    "Конец: end_867"

label end_870:
    "Конец: end_870"

label end_870:
    "Конец: end_870"

label end_870:
    "Конец: end_870"

label end_875:
    "Конец: end_875"

label end_875:
    "Конец: end_875"

label end_875:
    "Конец: end_875"

label end_878:
    "Конец: end_878"

label end_878:
    "Конец: end_878"

label end_878:
    "Конец: end_878"

label end_888:
    "Конец: end_888"

label end_888:
    "Конец: end_888"

label end_888:
    "Конец: end_888"

label end_889:
    "Конец: end_889"

label end_890:
    "Конец: end_890"

label end_893:
    "Конец: end_893"

label end_893:
    "Конец: end_893"

label end_893:
    "Конец: end_893"

label end_895:
    "Конец: end_895"

label end_896:
    "Конец: end_896"

label end_901:
    "Конец: end_901"

label end_901:
    "Конец: end_901"

label end_901:
    "Конец: end_901"

label end_901:
    "Конец: end_901"

label end_906:
    "Конец: end_906"

label end_906:
    "Конец: end_906"

label end_906:
    "Конец: end_906"

label end_909:
    "Конец: end_909"

label end_909:
    "Конец: end_909"

label end_909:
    "Конец: end_909"

label end_914:
    "Конец: end_914"

label end_915:
    "Конец: end_915"

label end_916:
    "Конец: end_916"

label end_917:
    "Конец: end_917"

label end_919:
    "Конец: end_919"

label end_919:
    "Конец: end_919"

label end_923:
    "Конец: end_923"

label end_923:
    "Конец: end_923"

label end_923:
    "Конец: end_923"

label end_923:
    "Конец: end_923"

label end_928:
    "Конец: end_928"

label end_928:
    "Конец: end_928"

label end_928:
    "Конец: end_928"

label end_930:
    "Конец: end_930"

label end_931:
    "Конец: end_931"

label end_940:
    "Конец: end_940"

label end_940:
    "Конец: end_940"

label end_940:
    "Конец: end_940"

label end_940:
    "Конец: end_940"

label end_941:
    "Конец: end_941"

label end_942:
    "Конец: end_942"

label end_945:
    "Конец: end_945"

label end_945:
    "Конец: end_945"

label end_945:
    "Конец: end_945"

label end_946:
    "Конец: end_946"

label end_947:
    "Конец: end_947"

label end_952:
    "Конец: end_952"

label end_953:
    "Конец: end_953"

label end_957:
    "Конец: end_957"

label end_957:
    "Конец: end_957"

label end_957:
    "Конец: end_957"

label end_961:
    "Конец: end_961"

label end_961:
    "Конец: end_961"

label end_964:
    "Конец: end_964"

label end_964:
    "Конец: end_964"

label end_964:
    "Конец: end_964"

label end_973:
    "Конец: end_973"

label end_973:
    "Конец: end_973"

label end_975:
    "Конец: end_975"

label end_975:
    "Конец: end_975"

label end_981:
    "Конец: end_981"

label end_981:
    "Конец: end_981"

label end_981:
    "Конец: end_981"

label end_981:
    "Конец: end_981"

label end_982:
    "Конец: end_982"

label end_983:
    "Конец: end_983"

label end_990:
    "Конец: end_990"

label end_990:
    "Конец: end_990"

label end_990:
    "Конец: end_990"

label end_990:
    "Конец: end_990"

label end_991:
    "Конец: end_991"

label end_992:
    "Конец: end_992"

label end_996:
    "Конец: end_996"

label end_996:
    "Конец: end_996"

label end_996:
    "Конец: end_996"

label end_996:
    "Конец: end_996"

label end_1000:
    "Конец: end_1000"

label end_1000:
    "Конец: end_1000"

label end_1000:
    "Конец: end_1000"

label end_1002:
    "Конец: end_1002"

label end_1003:
    "Конец: end_1003"

label end_1018:
    "Конец: end_1018"

label end_1018:
    "Конец: end_1018"

label end_1019:
    "Конец: end_1019"

label end_1020:
    "Конец: end_1020"

label end_1021:
    "Конец: end_1021"

label end_1022:
    "Конец: end_1022"

label end_1024:
    "Конец: end_1024"

label end_1024:
    "Конец: end_1024"

label end_1029:
    "Конец: end_1029"

label end_1030:
    "Конец: end_1030"

label end_1033:
    "Конец: end_1033"

label end_1033:
    "Конец: end_1033"

label end_1033:
    "Конец: end_1033"

label end_1034:
    "Конец: end_1034"

label end_1035:
    "Конец: end_1035"

label end_1036:
    "Конец: end_1036"

label end_1037:
    "Конец: end_1037"

label end_1042:
    "Конец: end_1042"

label end_1042:
    "Конец: end_1042"

label end_1042:
    "Конец: end_1042"

label end_1045:
    "Конец: end_1045"

label end_1045:
    "Конец: end_1045"

label end_1045:
    "Конец: end_1045"

label end_1052:
    "Конец: end_1052"

label end_1052:
    "Конец: end_1052"

label end_1052:
    "Конец: end_1052"

label end_1053:
    "Конец: end_1053"

label end_1054:
    "Конец: end_1054"

label end_1056:
    "Конец: end_1056"

label end_1056:
    "Конец: end_1056"

label end_1060:
    "Конец: end_1060"

label end_1060:
    "Конец: end_1060"

label end_1060:
    "Конец: end_1060"

label end_1060:
    "Конец: end_1060"

label end_1068:
    "Конец: end_1068"

label end_1068:
    "Конец: end_1068"

label end_1072:
    "Конец: end_1072"

label end_1072:
    "Конец: end_1072"

label end_1072:
    "Конец: end_1072"

label end_1072:
    "Конец: end_1072"

label end_1074:
    "Конец: end_1074"

label end_1074:
    "Конец: end_1074"

label end_1077:
    "Конец: end_1077"

label end_1077:
    "Конец: end_1077"

label end_1077:
    "Конец: end_1077"

label end_1081:
    "Конец: end_1081"

label end_1081:
    "Конец: end_1081"

label end_1081:
    "Конец: end_1081"

label end_1084:
    "Конец: end_1084"

label end_1084:
    "Конец: end_1084"

label end_1093:
    "Конец: end_1093"

label end_1094:
    "Конец: end_1094"

label end_1097:
    "Конец: end_1097"

label end_1097:
    "Конец: end_1097"

label end_1097:
    "Конец: end_1097"

label end_1101:
    "Конец: end_1101"

label end_1101:
    "Конец: end_1101"

label end_1101:
    "Конец: end_1101"

label end_1101:
    "Конец: end_1101"

label end_1103:
    "Конец: end_1103"

label end_1103:
    "Конец: end_1103"

label end_1108:
    "Конец: end_1108"

label end_1108:
    "Конец: end_1108"

label end_1108:
    "Конец: end_1108"

label end_1112:
    "Конец: end_1112"

label end_1112:
    "Конец: end_1112"

label end_1112:
    "Конец: end_1112"

label end_1112:
    "Конец: end_1112"

label end_1117:
    "Конец: end_1117"

label end_1117:
    "Конец: end_1117"

label end_1119:
    "Конец: end_1119"

label end_1119:
    "Конец: end_1119"

label end_1121:
    "Конец: end_1121"

label end_1121:
    "Конец: end_1121"

label end_1124:
    "Конец: end_1124"

label end_1125:
    "Конец: end_1125"

label end_1126:
    "Конец: end_1126"

label end_1127:
    "Конец: end_1127"

label end_1137:
    "Конец: end_1137"

label end_1137:
    "Конец: end_1137"

label end_1137:
    "Конец: end_1137"

label end_1141:
    "Конец: end_1141"

label end_1141:
    "Конец: end_1141"

label end_1141:
    "Конец: end_1141"

label end_1148:
    "Конец: end_1148"

label end_1148:
    "Конец: end_1148"

label end_1148:
    "Конец: end_1148"

label end_1148:
    "Конец: end_1148"

label end_1151:
    "Конец: end_1151"

label end_1151:
    "Конец: end_1151"

label end_1151:
    "Конец: end_1151"

label end_1154:
    "Конец: end_1154"

label end_1154:
    "Конец: end_1154"

label end_1154:
    "Конец: end_1154"

label end_1161:
    "Конец: end_1161"

label end_1161:
    "Конец: end_1161"

label end_1161:
    "Конец: end_1161"

label end_1164:
    "Конец: end_1164"

label end_1164:
    "Конец: end_1164"

label end_1164:
    "Конец: end_1164"

label end_1165:
    "Конец: end_1165"

label end_1166:
    "Конец: end_1166"

label end_1170:
    "Конец: end_1170"

label end_1170:
    "Конец: end_1170"

label end_1170:
    "Конец: end_1170"

label end_1170:
    "Конец: end_1170"

label end_1172:
    "Конец: end_1172"

label end_1173:
    "Конец: end_1173"

label end_1175:
    "Конец: end_1175"

label end_1176:
    "Конец: end_1176"

label end_1183:
    "Конец: end_1183"

label end_1183:
    "Конец: end_1183"

label end_1186:
    "Конец: end_1186"

label end_1186:
    "Конец: end_1186"

label end_1186:
    "Конец: end_1186"

label end_1192:
    "Конец: end_1192"

label end_1192:
    "Конец: end_1192"

label end_1192:
    "Конец: end_1192"

label end_1193:
    "Конец: end_1193"

label end_1194:
    "Конец: end_1194"

label end_1196:
    "Конец: end_1196"

label end_1196:
    "Конец: end_1196"

label end_1203:
    "Конец: end_1203"

label end_1203:
    "Конец: end_1203"

label end_1203:
    "Конец: end_1203"

label end_1205:
    "Конец: end_1205"

label end_1205:
    "Конец: end_1205"

label end_1207:
    "Конец: end_1207"

label end_1207:
    "Конец: end_1207"

label end_1209:
    "Конец: end_1209"

label end_1209:
    "Конец: end_1209"

label end_1220:
    "Конец: end_1220"

label end_1220:
    "Конец: end_1220"

label end_1221:
    "Конец: end_1221"

label end_1222:
    "Конец: end_1222"

label end_1225:
    "Конец: end_1225"

label end_1226:
    "Конец: end_1226"

label end_1228:
    "Конец: end_1228"

label end_1228:
    "Конец: end_1228"

label end_1230:
    "Конец: end_1230"

label end_1231:
    "Конец: end_1231"

label end_1235:
    "Конец: end_1235"

label end_1235:
    "Конец: end_1235"

label end_1235:
    "Конец: end_1235"

label end_1240:
    "Конец: end_1240"

label end_1241:
    "Конец: end_1241"

label end_1242:
    "Конец: end_1242"

label end_1243:
    "Конец: end_1243"

label end_1244:
    "Конец: end_1244"
