from antlr4 import *
from SimpAlgLexer import SimpAlgLexer
from SimpAlgParser import SimpAlgParser

def test_simpalg(input_code):
    input_stream = InputStream(input_code)
    lexer = SimpAlgLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpAlgParser(tokens)
    tree = parser.programa()

    # Adicione lógica adicional para testar a árvore sintática, se necessário

    print(tree.toStringTree(parser))  # Imprime a árvore de análise sintática

# Exemplo de código para teste
test_simpalg("""
var {
    int a, b;
}
program {
    a = 10;
    b = 5 + a;
    print("Resultado: ", b);
}
""")
