grammar grammar1;

start
    : (programLine)*
    ;

programLine
    : l=line SEMICOLON
    ;

line: newline
    ;

newline
    : constness=CONST? t=types name=VARIABLENAME                        #DeclarationExpression
    | constness=CONST? t=types name=VARIABLENAME IS b=body              #DeclarationAndInitalizationExpression
    | CONST? types  CONST? VARIABLENAME IS '&'VARIABLENAME              #DeclarationAndInitalizationPointerExpression
    | name=VARIABLENAME IS b=body                                       #InitalizationExpression
    | VARIABLENAME IS '&'VARIABLENAME                                   #InitalizationPointerExpression
    | body                                                              #Expression
    | name=VARIABLENAME op=identifierOP                                         #IdentifierOperationExpression
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
    : 'int '
    ;

FLOAT
    : 'float '
    ;

CHAR
    : 'char '
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

