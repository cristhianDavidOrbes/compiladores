grammar logica;

program
    : (functionDecl | declaration | statement)+ EOF
    ;

declaration
    : BOOL ID ('=' boolExpr)? SEMI
    ;

functionDecl
    : (typeSpecifier | VOID) ID LPAREN paramList? RPAREN block
    ;

paramList
    : param (COMMA param)*
    ;

param
    : BOOL ID
    ;

typeSpecifier
    : BOOL
    ;

statement
    : assignment
    | ifStatement
    | whileStatement
    | inputStmt
    | printStmt
    | returnStatement
    | callStmt
    | breakStmt
    | SEMI
    | declaration
    ;

assignment
    : ID ASSIGN boolExpr SEMI
    ;

ifStatement
    : IF LPAREN boolExpr RPAREN block (ELSE block)?
    ;

whileStatement
    : WHILE LPAREN boolExpr RPAREN block
    ;

inputStmt
    : ID ASSIGN INPUT LPAREN RPAREN SEMI
    ;

printStmt
    : PRINT LPAREN boolExpr RPAREN SEMI
    ;

returnStatement
    : RETURN boolExpr? SEMI
    ;

callStmt
    : functionCall SEMI
    ;

breakStmt
    : BREAK SEMI
    ;

block
    : LBRACE (declaration | statement)* RBRACE
    ;



boolExpr
    : orExpr
    ;

orExpr
    : xorExpr ((OR | NOR | XNOR) xorExpr)*
    ;

xorExpr
    : andExpr ((XOR | NEQ | EQ) andExpr)*
    ;

andExpr
    : unaryExpr ((AND | NAND) unaryExpr)*
    ;

unaryExpr
    : (NOT | BANG) unaryExpr
    | primary
    ;

primary
    : builtinCall
    | functionCall
    | TRUE
    | FALSE
    | ID
    | LPAREN boolExpr RPAREN
    ;

// Llamadas a funciones del usuario: foo(a,b)
functionCall
    : ID LPAREN argList? RPAREN
    ;

// Built-ins lógicos con exactamente dos argumentos: nand(a,b), nor(a,b), xnor(a,b)
builtinCall
    : (NAND | NOR | XNOR) LPAREN boolExpr COMMA boolExpr RPAREN
    ;

argList
    : boolExpr (COMMA boolExpr)*
    ;

BOOL    : 'bool' ;
VOID    : 'void' ;

IF      : 'if' ;
ELSE    : 'else' ;
WHILE   : 'while' ;
BREAK   : 'break' ;

RETURN  : 'return' ;

INPUT   : 'input' ;
PRINT   : 'print' ;

TRUE    : 'true' ;
FALSE   : 'false' ;

AND     : 'and' ;
NAND    : 'nand' ;
OR      : 'or' ;
NOR     : 'nor' ;
NOT     : 'not' ;
XOR     : 'xor' ;
XNOR    : 'xnor' ;

BANG    : '!' ;
EQ      : '==' ;
NEQ     : '!=' ;

ASSIGN  : '=' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACE  : '{' ;
RBRACE  : '}' ;
SEMI    : ';' ;
COMMA   : ',' ;

ID      : [a-zA-Z_][a-zA-Z_0-9]* ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;
WS          : [ \t\r\n]+      -> skip ;
