grammar mathematicalExpressions;

program
    : (body SEMICOLON)*
    ;

body
    : (MINUS | PLUS) unary
    | LPAREN body RPAREN
    | NUMBER
    | body operation body
    ;

unary
    : LPAREN body RPAREN
    | NUMBER
    | body operation body
    ;

operation
    : PLUS
    | MINUS
    | TIMES
    | DIV
    | GT
    | LT
    | EQ
    | GTE
    | LTE
    | NEQ
    | MOD
    | AND
    | OR
    ;

PLUS
    : '+'
    ;

MINUS
    : '-'
    ;

TIMES
   : '*'
   ;

DIV
   : '/'
   ;

GT
   : '>'
   ;

LT
   : '<'
   ;

EQ
   : '=='
   ;

GTE
   : '>='
   ;

LTE
   : '<='
   ;

NEQ
   : '!='
   ;

MOD
   : '%'
   ;

AND
   : '&&'
   ;

OR
   : '||'
   ;

SEMICOLON
    : ';'
    ;

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

NUMBER
    : '!'  [0-9]+
    | [0-9]+
    ;

WS
    : [ \n\t\r]+ -> skip
    ;