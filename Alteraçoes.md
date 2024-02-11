# Alteraçoes para a segunda versão

## 1 - Blocos poderiam ser vazios
Onde tem escrito isso???????

## 2 - Colocou expressões aritméticas nas booleanos
~~~
// de: 
relacional: '!' relacional | '(' relacional (('and'| 'or') relacional)? ')' | expressao (('<' | '>' | '<=' | '>=' | '==' | '!=') expressao) ;

// para:
relacional: '!' relacional | '(' relacional (('and'| 'or') relacional)? ')' | (ID | INT | FLOAT) (('<' | '>' | '<=' | '>=' | '==' | '!=') (ID | INT | FLOAT)) ;
~~~

## 3 - Não temos tipo string (expressões com string).
~~~
// de: 
fator: ID | INT | FLOAT | STRING | '(' expressao ')' | '!' fator;
lista_de_valores: expressao (',' expressao)*;

// para: (Tiramos o tipo string de fator e mudamos a lista_de_valores do print)
fator: ID | INT | FLOAT | '(' expressao ')' | '!' fator; 
lista_de_valores: (ID | INT | FLOAT | STRING) (',' (ID | INT | FLOAT | STRING))*;

~~~

## 4 - Não temos ! (operação booleana) em expressões aritméticas
~~~
// de: 
fator: ID | INT | FLOAT | STRING | '(' expressao ')' | '!' fator;


// para:
fator: ID | INT | FLOAT | '(' expressao ')';

~~~

Dúvida: deveria ser aceito `if(!a)`?? 
Se sim: `relacional: '!' ID | '!' relacional | '(' relacional (('and'| 'or') relacional)? ')' | ID (('<' | '>' | '<=' | '>=' | '==' | '!=') ID);`

## 5 - Erro na precedência do and e or
~~~
// de: 
expressao_logica: '(' expressao_logica ')' | relacional (( 'and' | 'or' ) relacional)*;

// para:
expressao_logica: '(' expressao_logica ')' | or_expr;

or_expr: and_expr ('or' and_expr)? | or_expr ('or' or_expr);

and_expr: relacional ('and' relacional)? | and_expr ('and' and_expr);

relacional: '!' relacional | '(' relacional (('and'| 'or') relacional)? ')' | relacional (('<' | '>' | '<=' | '>=' | '==' | '!=') relacional) | (ID | INT | FLOAT);
~~~

## 6 - Não fez o módulo (%)
~~~
// de: 
termo: fator (( '*' | '/') fator);

// para:
termo: fator (( '*' | '/') fator)* | (INT | ID) (('%') (INT | ID))*;
~~~

## 7 - Não fez operações unárias (- e +)
~~~
// de: 
expressao: termo (( '+' | '-' ) termo)*;

// para:
expressao: termo(( '+' | '-' ) termo)* | op_unario termo;
op_unario: '+' | '-';
~~~
