grammar Calculadora;

prog: expresion EOF ;

expresion
    : expresion ('^' | '**') expresion      # Potencia
    | expresion ('*' | '/') expresion       # MulDiv
    | expresion ('+' | '-') expresion       # AddSub
    | '-' expresion                         # Negativo
    | func '(' expresion ')'                # Funcion
    | '(' expresion ')'                     # Parentesis
    | NUMBER                                # Numero
    ;

func: 'sqrt' | 'abs' | 'log' | 'sin' | 'cos' ;

NUMBER: [0-9]+ ('.' [0-9]+)? ;
WS: [ \t\r\n]+ -> skip ;
