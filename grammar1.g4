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
    : constness=CONST? t=pointerTypes? name=VARIABLENAME                                     #DeclarationExpression
    | constness=CONST? t=types? name=VARIABLENAME IS b=body                                #DeclarationAndInitalizationExpression


    | constness=CONST? t=pointerTypes?  CONST? var1=VARIABLENAME IS ('&')?var2=VARIABLENAME  #DeclarationAndInitalizationPointerExpression
    | constness=CONST? t=types?  CONST? var1=VARIABLENAME IS '*'var2=VARIABLENAME           #GetPointerValue

    | name=VARIABLENAME IS b=body                                                           #InitalizationExpression
    | var1=VARIABLENAME IS '&'var2=VARIABLENAME                                             #InitalizationPointerExpression
    | body                                                                                  #Expression
    | name=VARIABLENAME op=identifierOP                                                     #IdentifierOperationExpression
    ;


identifierOP
    : PLUS PLUS
    | MINUS MINUS
    ;

pointerTypes
    : dataType('*')?
    ;

types
    : dataType
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
    : (('a'..'z' | 'A'..'Z' | '_')('a'..'z' | 'A'..'Z' | [0-9] | '_')*)
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

