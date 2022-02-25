grammar mathematicalExpressions;

r : program;
program : body SEMICOLON program | body SEMICOLON;
body : unary | LBRACE body RBRACE | NUMBER | body OPERATION body;
unary : MINUS body | PLUS body;

PLUS : SPACE '+' SPACE;
MINUS : SPACE '-' SPACE;
SEMICOLON : SPACE ';' SPACE;
LBRACE : SPACE '(' SPACE;
RBRACE : SPACE ')' SPACE;
OPERATION : SPACE [+,-,*,/,<,>,==,&&,||] SPACE;
NUMBER : SPACE '!' SPACE [0-9]+ SPACE | SPACE [0-9]+ SPACE;
SPACE: [ \n\t\r]+ -> skip;