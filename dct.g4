grammar dct;

schema : (definition)+;

definition: identifier COLON expression (constraints)? (certificates)?;

expression: name | identifier | literal;

name: (identifier slash)+ identifier;

identifier: STRING | ustring | hstring;

signing_chain: STRING;

literal: (AP)(STRING)(AP);

constraints: AND constraint ( OR constraint)*;

constraint: BO constraint_body (COMA constraint_body)* BC;

constraint_body: identifier COLON (literal | function);

function: STRING BRACKET;

certificates: SIGNEDBY identifier (OR identifier)*;

COLON: ':';

AP: '"';

AND: '&';

BO: '{';

BC: '}';

BRACKET: '()';

OR: '|';

COMA: ',';

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

SIGNEDBY: '<=';

slash: '/';

STRING: ([a-zA-Z])([a-zA-Z0-9]|UNDERSCORE)*;

WS: [ \r\n\t]+ -> skip;

COMMENT: '//' ~[\r\n]* -> skip;
