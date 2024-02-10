grammar SimpAlg;

programa: 'var' bloco_declaracoes 'program' bloco_comandos;

bloco_declaracoes: '{' declaracoes '}';

bloco_comandos: '{' comandos '}';

declaracoes: declaracao+;

declaracao: tipo lista_de_variaveis ';';

tipo: 'int' | 'float';

comandos: comando+;

comando: atribuicao | saida | entrada | condicional | repeticao;

atribuicao: ID '=' expressao_aritmetica ';';

saida: 'print' '(' lista_de_valores ')' ';';

entrada: 'scan' '(' lista_de_variaveis ')' ';';

condicional: 'if' '(' expressao_booleana ')' bloco_comandos ('else' bloco_comandos)?;

repeticao: 'while' '(' expressao_booleana ')' bloco_comandos;

expressao_aritmetica: termo (( '+' | '-' ) termo)*;

termo: fator (( '*' | '/' ) fator)*;

fator: ID | INT | FLOAT | '(' expressao_aritmetica ')';

expressao_booleana: relacional (( 'and' | 'or' ) relacional)*;

relacional: expressao_aritmetica (('<' | '>' | '<=' | '>=' | '==' | '!=') expressao_aritmetica);

lista_de_valores: expressao_aritmetica (',' expressao_aritmetica)*;

lista_de_variaveis: ID (',' ID)*;

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: ('"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"' | '“' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '”');

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
