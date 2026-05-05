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

assignment: "$" NAME OP_ASSIGN (NUMBER | NAME) _NEWLINE?

OP_ASSIGN: "+=" | "="

condition: "if" NAME [OP NUMBER] ":" _NEWLINE INDENT statement+ DEDENT

OP: ">=" | "<=" | ">" | "<" | "=="

COMMENT: /#[^\n]*/

%import common.CNAME -> NAME
%import common.ESCAPED_STRING -> STRING
%import common.NUMBER
%import common.WS_INLINE

_NEWLINE: /(\r?\n[ \t]*)+/

%declare INDENT DEDENT

%ignore WS_INLINE
%ignore COMMENT
"""