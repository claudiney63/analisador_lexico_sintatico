grammar SimpAlg;

programa: 'var' '{' declaracoes '}' 'program' '{' comandos '}';

declaracoes: (declaracao ';')+;

declaracao: tipo ID;

tipo: 'int' | 'float';

comandos: comando+;

comando: atribuicao
       | entrada
       | saida
       | condicional
       | repeticao;

atribuicao: ID '=' expressao ';';

entrada: 'scan' '(' ID ')';

saida: 'print' '(' listaValores ')' ';';

listaValores: (expressao ',')+;

condicional: 'if' '(' expressaoLogica ')' '{' comandos '}' ('else' '{' comandos '}')?;

repeticao: 'while' '(' expressaoLogica ')' '{' comandos '}';

expressao: termo ('+' termo)*;

termo: ID | INT | FLOAT;

expressaoLogica: expressaoRelacional
              | '!' expressaoLogica
              | expressaoLogica 'and' expressaoLogica
              | expressaoLogica 'or' expressaoLogica;

expressaoRelacional: expressao '>' expressao
                  | expressao '>=' expressao
                  | expressao '<' expressao
                  | expressao '<=' expressao
                  | expressao '==' expressao
                  | expressao '!=' expressao;

ID: [a-zA-Z][a-zA-Z0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
WS: [ \t\r\n]+ -> skip;