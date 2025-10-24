grammar CSV;
csvFile
  : header row* lastRow? EOF
  ;

header: row;

row: field (COMMA field)* NL;

lastRow: field (COMMA field)*;

field
  : TEXT   # text
  | STRING # string
  |        # empty
  ;

COMMA : ',' ;

NL    : '\r'? '\n' | '\r' ;

TEXT  : ~[,\r\n"]+ ;

STRING: '"' ('""' | ~'"')* '"';


WS    : [ \t]+ -> skip ;
