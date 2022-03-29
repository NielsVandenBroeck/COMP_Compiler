grammar grammar1;

start
    : (programLine)*
    ;

programLine
    : l=line SEMICOLON
    | SingleComment
    | MultiLineComment
    | s=scope
    ;

scope
    : 'if' '(' b=body ')' s1=scope ('else' s2=scope)?                                           #IfStatement
    | 'while' '(' b=body ')' s=scope                                                            #WhileLoop
    | '{' (programLine)+ '}'                                                                    #EmptyScope
    ;

line: newline
    ;

newline
    : lv=lvalue IS rv=rvalue                                                                    #LValueRvalue
    | lvalue                                                                                    #LValue
    | body                                                                                      #Expression
    | name=VARIABLENAME op=identifierOP                                                         #IdentifierOperationExpression
    | Print'('b=body')'                                                                         #Printf
    ;

lvalue
    : constnessB=CONST? t=dataType? pointer='*'? constnessA=CONST? name=VARIABLENAME
    ;

rvalue
    : body
    | variableAdress
    ;

variableAdress
    : ('&')?name=VARIABLENAME;

identifierOP
    : PLUS PLUS
    | MINUS MINUS
    ;

types
    : dataType('*')?          #Type
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
    | '*'value=VARIABLENAME                                             #PointerValueExpression
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

Print
    : 'printf'
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

SingleComment
    : '//'(~('\n'))*
    ;

MultiLineComment
    : '/*'.*?'*/'
    ;

WS
    : [ \n\t\r]+ -> skip
    ;

