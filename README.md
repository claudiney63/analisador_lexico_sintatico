# analisador_lexico_sintatico
Repositório referente a implementação do analisador léxico e sintático de uma linguagem simplificada utilizando o ANTLR.

## Para instalar o pacote antlr4 no python, exdcute essa linha de codigo usando o pip:
```
pip install antlr4-python3-runtime
```

## Para gerar os tokens e parte do analisador usando a gramatica, execute esse codigo:
```
antlr4 SimpAlg.g4
```

## para gerar a arvore do parser, essas linha de codigo pode ser utlizada:
```
compile SimpAlg*.java
```
e logo após, essa linha:
```
grun SimpAlg programa -gui
```
irá abrir espaço para digitar os caracteres que serão categorizados(tokerização), ao terminar de escrever, 
aperte CTRL + Z e ENTER. Note que "programa", pode mudar, considerando a regra inicial da gramatica.

## Exemplo para essa gramatica:
```
var {
    int a, b;
}
program {
    a = 10;
    b = 5 + a;
    print("Resultado: ", b);
}
```

## Imagem da arvore de derivação do exemplo acima:
![image](https://github.com/claudiney63/analisador_lexico_sintatico/assets/40923082/a0544bb9-eaaf-4621-9492-cfb0a4ddc21b)

