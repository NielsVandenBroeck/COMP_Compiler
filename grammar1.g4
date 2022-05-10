grammar grammar1;

start
    : (programLine)*
    ;

programLine
    : l=line SEMICOLON
    | SingleComment
    | MultiLineComment
    | s=scope
    | f=function
    | IncludeStdio
    ;

function
    : ((t=dataType pointer='*'?)|'void') name=NAME '(' (p=params)? ')' s=scope
    ;

params
    : param (',' param)*
    ;

param
    : constnessB=CONST? t=dataType pointer='*'? constnessA=CONST? name=NAME
    ;

scope
    : 'if' '(' b=body ')' s1=scope ('else' s2=scope)?                                           #IfStatement
    | 'while' '(' b=body ')' s=scope                                                            #WhileLoop
    | 'for' '(' lv=lvalue IS rv=rvalue ';' b=body ';' step=line ')' s=scope                     #ForLoop
    | '{' (programLine)* '}'                                                                    #EmptyScope
    ;

line: newline
    ;

newline
    : lv=lvalue IS rv=rvalue                                                                    #LValueRvalue
    | lvalue                                                                                    #LValue
    | body                                                                                      #Expression
    | Print'('f=Format pb=printBodies')'                                                        #Printf
    | Scan'('f=Format  sv=scanVariables ')'                                                     #Scanf
    | OneTokenStatement                                                                         #OneTokenStatement
    | 'return' b=rvalue?                                                                        #ReturnKeyword
    | ((t=dataType pointer='*'?)|'void') name=NAME '(' (p=params)? ')'                          #FunctionForwardDeclaration
    ;

printBodies
    : printBody*
    ;

printBody
    : ',' b=body
    ;

scanVariables
    : scanVariable+
    ;

scanVariable
    : ',' (d=data|v=variableAdress)
    ;

lvalue
    : constnessB=CONST? t=dataType? pointer='*'? constnessA=CONST? name=NAME
    ;

rvalue
    : body
    | variableAdress
    ;

variableAdress
    : ('&')?name=NAME;


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
    | functionCall
    | negation
    ;

functionCall
    : name=NAME '(' body? (',' body)* ')'
    ;

leftOperationBody
    : paren
    | data
    | unary
    | functionCall
    | negation
    ;

unaryBody
    : paren
    | data
    | bodyOperationBody
    | negation
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
    | ((LPAREN '*'value=NAME RPAREN)|('*'value=NAME)) identifier=identifierOP?                            #PointerValueExpression
    | ((LPAREN value=NAME RPAREN)|(value=NAME)) identifier=identifierOP?                               #VariableExpression
    ;

identifierOP
    : PLUS PLUS
    | MINUS MINUS
    ;

negation
    : NEGATE b=body
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

OneTokenStatement
    : 'break'
    | 'continue'
    ;


Print
    : 'printf'
    ;

Format
    : '"'((~('%'|'"')|TYPESPECIFIER)*)'"'
    ;

Scan
    : 'scanf'
    ;

TYPESPECIFIER
    : '%d'
    | '%i'
    | '%s'
    | '%c'
    | '%f'
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

NAME
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
    : [0-9]+
    ;

FLOATINPUT
    : [0-9]+('.'[0-9]+)?
    ;

CHARINPUT
    : '\'' ((~('\'')) | ('\\' '\'') | ('\\n') | ('\\r') | ('\\t')) '\''
    ;

NEGATE
    : '!'
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

IncludeStdio
    : '#include <stdio.h>'
    ;
WS
    : [ \n\t\r]+ -> skip
    ;