# Testes
##### Lista de testes
[Teste 1](#teste-1)  
[Teste 2](#teste-2)  
[Teste 3](#teste-3)  
[Teste 4](#teste-4)  
[Teste 5](#teste-5)  
[Teste 6](#teste-6)  
[Teste 7](#teste-7)  
[Teste 8](#teste-8)  
[Teste 9](#teste-9)  
[Teste 10](#teste-10)  
[Teste 11](#teste-11)  
[Teste 12](#teste-12)  

## Teste 1
testa o print e a declaracao
~~~
var {
    int x, y;
    float z;
} program {
    x = 5;
    y = x * 2;
    z = 3.14; //Ellen e Enzo
    print(x, y, z);
}
~~~
## Teste 2
exemplo de if
~~~
var {
    int a, b;
} program {
    a = 10;
    b = 20;
    if (a < b) {
        print("a é menor que b");
    } else {
        print("a não é menor que b");
    }
}
~~~
## Teste 3
while
~~~
var {
    int i;
} program {
    i = 1;
    while (i <= 5) {
        print(i);
        i = i + 1;
    }
}
~~~
## Teste 4
~~~
var {
    int num;
} program {
    scan(num);
    print("Você digitou: ", num);
    print("Teste de sting com \" ");
}
~~~
## Teste 5
~~~
var {
    int a, b, result;
} program {
    a = 3;
    b = 4;
    result = (a + b) * 2;
    print(result);
}
~~~
## Teste 6
~~~
var {
    x, y;  // Erro: Deve especificar o tipo das variáveis
} program {
    print(x + y);
}
~~~
## Teste 7
~~~
var {
    int x, y;
} program {
    x = 5;
    y = 3.14;  // Erro: Tentando atribuir um float a uma variável int
}
~~~
## Teste 8
~~~
var {
    int a;
} program {
    b = 10;  // Erro: 'b' não foi declarada
}
~~~
## Teste 9
~~~
var {
    int x;
} program {
    if (x + 2) {
        print("Isso não deveria acontecer.");
    }
}
~~~
## Teste 10
~~~
var {
    int x;
} program {
    if (x > 0  // Erro: Falta a abertura de chaves
        print("x é positivo");
    else {
        print("x é zero ou negativo");
    }
}
~~~
## Teste 11
~~~
var {
    string msg;
} program {
    msg = "Erro de string;  // Erro: String não fechada corretamente
    print(msg);
}
~~~
## Teste 12
~~~
var {
    float a, b;
} program {
    if (a + b) {  // Erro: Expressão lógica esperada
        print("Isso não deveria acontecer.");
    }
}
~~~