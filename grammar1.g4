grammar grammar1;

start
    : (programLine)*
    ;

programLine
    : l=line SEMICOLON
    | SingleComment
    | MultiLineComment
    | f=function
    | s=scope
    | m=multiAssignmentsDeclarations SEMICOLON
    | IncludeStdio
    ;

function
    : ((t=dataType (pointer=(MultiPointer|TIMES))?)|'void') name=NAME '(' (p=params)? ')' s=scope
    ;

params
    : param (',' param)*
    ;

param
    : constnessB=CONST? t=dataType (pointer=(MultiPointer|TIMES))? constnessA=CONST? name=NAME ('[' array=body ']')?
    ;

scope
    : 'if' '(' b=body ')' s1=scope ('else' s2=scope)?                                           #IfStatement
    | 'while' '(' b=body ')' s=scope                                                            #WhileLoop
    | 'for' '(' lv=lvalue IS rv=rvalue ';' b=body ';' step=line ')' s=scope                     #ForLoop
    | '{' (programLine)* '}'                                                              #EmptyScope
    ;

line: newline
    ;

newline
    : lv=lvalue IS rv=rvalue                                                                    #LValueRvalue
    | lvalue                                                                                    #LValue
    | body                                                                                      #Expression
    | Print'('f=STRING pb=printBodies ')'                                                        #Printf
    | Scan'('f=STRING  sv=scanVariables ')'                                                     #Scanf
    | OneTokenStatement                                                                         #OneTokenStatement
    | 'return' b=rvalue?                                                                        #ReturnKeyword
    | ((t=dataType (pointer=(MultiPointer|TIMES))?)|'void') name=NAME '(' (p=params)? ')'                          #FunctionForwardDeclaration
    ;

printBodies
    : printBody*
    ;

printBody
    : ',' (b=body|s=STRING)
    ;

scanVariables
    : scanVariable+
    ;

scanVariable
    : ',' (d=data|v=variableAdress)
    ;

multiAssignmentsDeclarations
    : constnessB=CONST? t=dataType (pointer=(MultiPointer|TIMES))? constnessA=CONST? multidecl=multideclarations
    ;

multideclarations
    : multideclaration (',' multideclaration)+
    ;

multideclaration
    : name=NAME (('[' array=body ']')|(IS rval=rvalue))?
    ;

lvalue
    : constnessB=CONST? t=dataType? (pointer=(MultiPointer|TIMES))? constnessA=CONST? name=NAME ('[' array=body ']')?
    ;

rvalue
    : body
    | variableAdress
    ;

variableAdress
    : '&'name=NAME ('[' array=body ']')?;

dataType
    : INT
    | FLOAT
    | CHAR
    ;

body
    : paren
    | d=data
    | bodyOperationBody
    | unary
    | functionCall
    | negation
    ;

functionCall
    : name=NAME '(' (variableAdress|body)? (',' (variableAdress|body))* ')'
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
    : value=CHARINPUT                                                                   #CharExpression
    | value=INTINPUT                                                                    #IntExpression
    | value=FLOATINPUT                                                                  #FloatExpression
    | pointer=(MultiPointer|TIMES) value=NAME ('[' array=body ']')?                     #PointerValueExpression
    | identifier=identifierOP? value=NAME ('[' array=body ']')?                         #VariableExpression
    | value=NAME ('[' array=body ']')? identifier=identifierOP                          #VariableExpressionIdentifier
    ;

    //++ and --
    //| ((LPAREN '*'value=NAME RPAREN)|('*'value=NAME)) identifier=identifierOP?          #PointerValueExpression
    //| ((LPAREN value=NAME RPAREN)|(value=NAME))  identifier=identifierOP?               #VariableExpression
    //;

MultiPointer
    :  TIMES TIMES+
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

STRING
    : '"'((~('"'))*)'"'
    ;


Scan
    : 'scanf'
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