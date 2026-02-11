RENPLY_GRAMMAR = r"""
start: statement+

statement: label
         | jump
         | say
         | menu

// -----------------
// LABEL
// -----------------

label: "label" NAME ":" statement*

// -----------------
// JUMP
// -----------------

jump: "jump" NAME

// -----------------
// SAY
// -----------------

say: STRING
   | NAME STRING

// -----------------
// MENU
// -----------------

menu: "menu" ":" menu_option+

menu_option: STRING ":" statement*

// -----------------
// TOKENS
// -----------------

%import common.CNAME -> NAME
%import common.ESCAPED_STRING -> STRING
%import common.WS
%ignore WS
"""
