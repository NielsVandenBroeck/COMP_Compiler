grammar grammar1;

start
    : (programLine)*
    ;

programLine
    : CONST? types VARIABLENAME SEMICOLON                                       #DeclarationExpression
    | CONST? types VARIABLENAME IS line=body SEMICOLON                          #DeclarationAndInitalizationExpression
    | CONST? types  CONST? VARIABLENAME IS line='&'VARIABLENAME SEMICOLON       #DeclarationAndInitalizationPointerExpression
    | VARIABLENAME IS line=body SEMICOLON                                       #InitalizationExpression
    | VARIABLENAME IS line='&'VARIABLENAME SEMICOLON                            #InitalizationPointerExpression
    | line=body SEMICOLON                                                       #Expression
    | VARIABLENAME identifierOP SEMICOLON                                       #IdentifierOperationExpression
    ;


identifierOP
    : PLUS PLUS
    | MINUS MINUS
    ;

types
    : dataType'*'?
    ;

dataType
    : INT
    | FLOAT
    | CHAR
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
    :sign=(PLUS | MINUS) value=unaryBody                                #UnaryExpression
    ;

bodyOperationBody
    : lValue=leftOperationBody op=operation rValue=body                 #OperationExpression
    ;

paren
    : LPAREN value=body RPAREN                                          #ParenExpression
    ;

data
    : value=CHARINPUT                                                   #CharExpression
    | value=INTINPUT                                                    #IntExpression
    | value=FLOATINPUT                                                  #FloatExpression
    | VARIABLENAME                                                      #VariableExpression
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
    : 'char'
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

INTINPUT
    : ('!')?  [0-9]+
    ;

FLOATINPUT
    : ('!')?  [0-9]+('.'[0-9]+)?
    ;

CHARINPUT
    : '\'' ((~('\'')) | ('\\' '\'') | ('\\n') | ('\\r') | ('\\t')) '\''
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

