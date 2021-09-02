grammar TSP;

policy: (policy_statement)+;

policy_statement: APPNAME location device datatype;

location: BEDROOM
		| KITCHEN
		| LIVINGROOM
		| PATIO;

device: OUTLET
	| TV
	| AC
	| MOTIONSENSOR
	| HEATER;

datatype: command | report;

command: COMMAND command_type value;

report: REPORT report_type value;

command_type: ONOFF
		| ROTATE;

report_type: STATUS
		| ANGLE
		| TEMPERATURE;

value: ID | DIGIT;


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


APPNAME: A P P N A M E;
BEDROOM: B E D R O O M;
KITCHEN: K I T C H E N;
LIVINGROOM: L I V I N G R O O M;
PATIO: P A T I O;
OUTLET: O U T L E T;
TV: T V;
AC: A C;
MOTIONSENSOR: M O T I O N S E N S O R;
HEATER: H E A T E R;
COMMAND: C O M M A N D;
REPORT: R E P O R T;
ONOFF: O N O F F;
ROTATE: R O T A T E;
STATUS: S T A T U S;
ANGLE: A N G L E;
TEMPERATURE: T E M P A R A T U R E;
ID: [a-zA-Z]+;
DIGIT: [0-9]+;
WS: [ \r\n\t]+ -> skip;

