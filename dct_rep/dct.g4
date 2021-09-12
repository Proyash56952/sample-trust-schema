grammar dct;

schema : (definition)+;

definition: identifier COLON expression;

expression: name | STRING;

name: (identifier slash)+ identifier;

identifier: STRING | ustring | hstring;

signing_chain: STRING;

COLON: ':';

fragment A:('a'|'A');
fragment B:('b'|'B');
fragment C:('c'|'C');
fragment D:('d'|'D');
fragment E:('e'|'E');
fragment F:('f'|'F');
fragment G:('g'|'G');
fragment H:('h'|'H');
fragment I:('i'|'I');
fragment J:('j'|'J');
fragment K:('k'|'K');
fragment L:('l'|'L');
fragment M:('m'|'M');
fragment N:('n'|'N');
fragment O:('o'|'O');
fragment P:('p'|'P');
fragment Q:('q'|'Q');
fragment R:('r'|'R');
fragment S:('s'|'S');
fragment T:('t'|'T');
fragment U:('u'|'U');
fragment V:('v'|'V');
fragment W:('w'|'W');
fragment X:('x'|'X');
fragment Y:('y'|'Y');
fragment Z:('z'|'Z');

ustring: (UNDERSCORE)(STRING);

hstring: (HASH)(STRING);

UNDERSCORE: '_';

HASH: '#';

slash: '/';

STRING: ([a-zA-Z])([a-zA-Z0-9]|UNDERSCORE)*;

WS: [ \r\n\t]+ -> skip;
