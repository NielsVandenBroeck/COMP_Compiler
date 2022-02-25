grammar mathematicalExpressions;

r : program;

program : body ';' program | body ';';

body : unary | '(' body ')' | NUMBER | body OPERATION body;

unary : '-' body | '+' body;

OPERATION : [+,-,*,/,<,>,==,&&,||];
NUMBER : '!' [0-9]* | [0-9]*;