from antlr4 import *
from gen.SimpAlgLexer import SimpAlgLexer
from gen.SimpAlgParser import SimpAlgParser

input_stream = FileStream("ex.txt")
lexer = SimpAlgLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = SimpAlgParser(tokens)
tree = parser.programa()

    # Adicione lógica adicional para testar a árvore sintática, se necessário

print(tree.toStringTree(parser))  # Imprime a árvore de análise sintática

# Exemplo de código para teste

