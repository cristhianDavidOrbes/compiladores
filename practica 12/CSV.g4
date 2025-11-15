grammar CSV;

csvFile : header row* EOF ;
header  : row ;
row     : field (',' field)* (NEWLINE | EOF) ;

field   : TEXT   # text
        | STRING # string
        |        # empty
        ;

TEXT    : ~[,\n\r"]+ ;
STRING  : '"' ('""'|~'"')* '"' ;
NEWLINE : '\r'? '\n' ;
WS      : [ \t]+ -> skip ;
