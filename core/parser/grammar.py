RENPLY_GRAMMAR = r"""
start: statement+

statement: label

label: "label" NAME ":" NEWLINE INDENT label_body DEDENT

label_body: statement+

statement: jump

jump: "jump" NAME NEWLINE

%import common.CNAME -> NAME
%import common.NEWLINE
%import common.WS_INLINE
%ignore WS_INLINE
"""
