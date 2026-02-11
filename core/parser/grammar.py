RENPY_GRAMMAR = r"""
start: (_NEWLINE | statement)*

?statement: label
          | jump
          | menu
          | say

label: "label" NAME ":" _NEWLINE INDENT statement+ DEDENT

jump: "jump" NAME _NEWLINE?

menu: "menu" ":" _NEWLINE INDENT menu_option+ DEDENT

menu_option: STRING ":" _NEWLINE INDENT statement+ DEDENT

say: STRING _NEWLINE?

%import common.CNAME -> NAME
%import common.ESCAPED_STRING -> STRING
%import common.WS_INLINE

_NEWLINE: /(\r?\n[ \t]*)+/

%declare INDENT DEDENT

%ignore WS_INLINE
"""
