grammar SimpAlg;

programa: 'var' '{' declaracoes '}' 'program' '{' comandos '}';

declaracoes: declaracao+;

declaracao: tipo lista_de_variaveis ';';

tipo: 'int' | 'float';

comandos: comando+;

comando: atribuicao | saida | entrada | condicional | repeticao;

atribuicao: ID '=' expressao ';';

saida: 'print' '(' lista_de_valores ')' ';';

entrada: 'scan' '(' lista_de_variaveis ')' ';';

condicional: 'if' '(' expressao_logica ')' '{' comandos '}' ('else' '{' comandos '}')?;

repeticao: 'while' '(' expressao_logica ')' '{' comandos '}';

expressao: termo (( '+' | '-' ) termo)*;

termo: fator (( '*' | '/' ) fator)*;

fator: ID | INT | FLOAT | '(' expressao ')';

// TA DANDO ERRO AQUI - TESTE: if(3 > 5)
expressao_logica: '(' expressao_logica ')' | or_expr;// relacional (( 'and' | 'or' ) relacional)*;

or_expr: and_expr ('or' and_expr);

and_expr: relacional ('and' relacional);
// ATÉ AQUI

relacional: '!' relacional | '(' relacional (('and'| 'or') relacional)? ')' | (ID | INT | FLOAT) (('<' | '>' | '<=' | '>=' | '==' | '!=') (ID | INT | FLOAT));

lista_de_valores: (ID | INT | FLOAT | STRING) (',' (ID | INT | FLOAT | STRING))*;

lista_de_variaveis: ID (',' ID)*;

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"';

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;