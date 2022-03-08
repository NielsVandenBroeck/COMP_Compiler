grammar grammar1;

start
    : (programLine)*
    ;

programLine
    : (dataType NAME IS)? line=body SEMICOLON
    ;

dataType
    : INT
    | FLOAT
    | CHAR
    | POINTER
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
    :sign=(PLUS | MINUS) value=unaryBody        #UnaryExpression
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

INT
    : 'int'
    ;

FLOAT
    : 'float'
    ;

CHAR
    : 'CHAR'
    ;

POINTER
    : 'pointer'
    ;

NAME
    : (('a'..'z' | 'A'..'Z')+)
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
    : ('!')?  [0-9]+
    ;

IS
    : '='
    ;

WS
    : [ \n\t\r]+ -> skip
    ;

