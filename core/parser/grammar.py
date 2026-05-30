RENPY_GRAMMAR = r"""
start: (_NEWLINE | statement)*

?statement: label
          | jump
          | call
          | return_stmt
          | menu
          | say
          | assignment
          | condition
          | unknown_statement

label: "label" ("."?) NAME ":" _NEWLINE INDENT statement+ DEDENT

jump: "jump" NAME _NEWLINE?

call: "call" NAME ["from" NAME] _NEWLINE?

return_stmt: "return" _NEWLINE?

menu: "menu" ":" _NEWLINE INDENT menu_option+ DEDENT

menu_option: STRING ":" _NEWLINE INDENT statement+ DEDENT

say: STRING _NEWLINE?

# Support any $ assignment: $var=value, $ renpy.notify(...), $var=True, etc.
# Priority .2 makes it lower than NAME, STRING, etc.
assignment: DOLLAR_ASSIGN _NEWLINE?

DOLLAR_ASSIGN.2: "$" /[^\n]*/

condition: "if" NAME [OP NUMBER] ":" _NEWLINE INDENT statement+ DEDENT elif_branch* else_branch?

elif_branch: "elif" NAME [OP NUMBER] ":" _NEWLINE INDENT statement+ DEDENT

else_branch: "else" ":" _NEWLINE INDENT statement+ DEDENT

OP: ">=" | "<=" | ">" | "<" | "==" | "!="

UNKNOWN_TOKEN: "__UNKNOWN__"
unknown_statement: UNKNOWN_TOKEN _NEWLINE? (INDENT statement+ DEDENT)?

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