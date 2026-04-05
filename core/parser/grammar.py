RENPY_GRAMMAR = r"""
start: (_NEWLINE | statement)*

?statement: label
          | jump
          | menu
          | say
          | assignment
          | condition

label: "label" NAME ":" _NEWLINE INDENT statement+ DEDENT

jump: "jump" NAME _NEWLINE?

menu: "menu" ":" _NEWLINE INDENT menu_option+ DEDENT

menu_option: STRING ":" _NEWLINE INDENT statement+ DEDENT

say: STRING _NEWLINE?

assignment: "$" NAME "+=" NUMBER _NEWLINE?

condition: "if" NAME OP NUMBER ":" _NEWLINE INDENT statement+ DEDENT

OP: ">=" | "<=" | ">" | "<" | "=="

%import common.CNAME -> NAME
%import common.ESCAPED_STRING -> STRING
%import common.NUMBER
%import common.WS_INLINE

_NEWLINE: /(\r?\n[ \t]*)+/

%declare INDENT DEDENT

%ignore WS_INLINE
"""