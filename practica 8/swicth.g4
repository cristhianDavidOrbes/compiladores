grammar swicth;

programa: (sentencia (SEMI)?)+ EOF ;


sentencia
    : switchOrden
    | asignacion
    ;

switchOrden: SWITCH LPAREN expresion RPAREN LBRACE caseOrden* defaultOrden? RBRACE ;

caseOrden: CASE INT DOBLEP (asignacion SEMI)* ;

defaultOrden: DEFAULT DOBLEP (asignacion SEMI)* ;

asignacion
    : ID ASSIGN expresion  # Assign
    ;

expresion
    : expresion op=(MUL | DIV) expresion     # MulDiv
    | expresion op=(PLUS | MINUS) expresion  # AddSub
    | INT                                    # Int
    | ID                                     # Variable   
    | LPAREN expresion RPAREN                # Parens
    ;

// === TOKENS ===
IF      : 'if' ;
ELSE    : 'else' ;
SWITCH  : 'switch';
CASE    : 'case';
DEFAULT : 'default';
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACE  : '{' ;
RBRACE  : '}' ;
DOBLEP  : ':' ;
ASSIGN  : '=' ;
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
GT      : '>' ;
LT      : '<' ;
EQ      : '==' ;
NEQ     : '!=' ;
SEMI    : ';' ;

// Reglas léxicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                  // Números enteros
WS  : [ \t\r\n]+ -> skip ;      // Ignorar espacios en blanco
