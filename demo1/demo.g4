grammar demo;

policy: POLICY STRING COLON (statement)*;

statement: STATEMENT STRING COLON statement_body;

statement_body: sign_block signed_by_block;

sign_block: SIGN COLON (msg | cert);

signed_by_block: SIGNEDBY COLON cert;

msg: cmd | rep;

cmd: domain COMMAND param;

rep: domain REPLY param;

cert: opcert | usercert | domaincert;

opcert: domain OPERATOR keyinfo;

usercert: domain USER keyinfo;

domaincert: domain keyinfo;

domain: MYHOUSE;

keyinfo: KEY param;

param: ANY | (STRING)+;

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

POLICY: P O L I C Y;
STATEMENT: S T A T E M E N T;
SIGN: S I G N;
SIGNEDBY: S I G N E D B Y;
ANY: A N Y;
COMMAND : C O M M A N D;
REPLY: R E P L Y;
OPERATOR: O P E R A T O R;
USER: U S E R;
MYHOUSE: M Y H O U S E;
KEY: K E Y;

UNDERSCORE: ('_' | '-');
STRING: ([a-zA-Z]|UNDERSCORE)([a-zA-Z0-9]|UNDERSCORE)*;
WS: [ \r\n\t]+ -> skip;
