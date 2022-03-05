grammar grammar1;

program
    : (line=body SEMICOLON)*
    ;

body
    : paren
    | number
    | bodyOperationBody
    | unary
    ;

leftOperationBody
    :paren
    |number
    |unary
    ;

unaryBody
    : paren
    | number
    | bodyOperationBody
    ;

unary
    :sign=(PLUS | MINUS) value=unaryBody        #unaryExpression
    ;

bodyOperationBody
    : lValue=leftOperationBody op=operation rValue=body  #OperationExpression
    ;

paren
    : LPAREN value=body RPAREN                #ParenExpression
    ;

number
    : value=NUMBER                            #NumberExpression
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