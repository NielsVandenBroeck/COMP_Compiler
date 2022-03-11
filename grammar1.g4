grammar grammar1;

start
    : (programLine)*
    ;

programLine
    : (CONST? dataType VARIABLENAME IS)? line=body SEMICOLON
    | VARIABLENAME identifierOP SEMICOLON
    ;

identifierOP
    : PLUS PLUS
    | MINUS MINUS
    ;

dataType
    : INT
    | FLOAT
    | CHAR
    | POINTER
    ;

body
    : paren
    | data
    | bodyOperationBody
    | unary
    ;

leftOperationBody
    :paren
    |data
    |unary
    ;

unaryBody
    : paren
    | data
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

data
    : value=NUMBER                            #NumberExpression
    | VARIABLENAME                            #VariableExpression
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

VARIABLENAME
    : ('a'..'z' | 'A'..'Z' | '_')('a'..'z' | 'A'..'Z' | [0-9] | '_')*
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

CONST
    : 'const '
    ;

IS
    : '='
    ;

WS
    : [ \n\t\r]+ -> skip
    ;

