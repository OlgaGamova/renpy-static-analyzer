RENPLY_GRAMMAR = r"""
start: statement+

statement: label
         | jump
         | menu
         | menu_option
         | say

label: "label" NAME ":" statement*

jump: "jump" NAME

menu: "menu" ":" menu_option+

menu_option: STRING ":" statement+

say: STRING

%import common.CNAME -> NAME
%import common.ESCAPED_STRING -> STRING
%import common.WS
%ignore WS
"""
