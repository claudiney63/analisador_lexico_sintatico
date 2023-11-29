# Generated from C:/Users/claud/GitHub/analisador_lexico_sintatico/SimpAlg.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,157,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,1,4,1,47,8,1,11,1,12,1,48,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,4,4,4,59,8,4,11,4,12,4,60,1,5,1,5,1,5,1,5,1,5,3,5,68,8,5,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,99,8,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,112,8,11,
        10,11,12,11,115,9,11,1,12,1,12,1,12,5,12,120,8,12,10,12,12,12,123,
        9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,133,8,13,1,14,
        1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,5,16,144,8,16,10,16,12,16,
        147,9,16,1,17,1,17,1,17,5,17,152,8,17,10,17,12,17,155,9,17,1,17,
        0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,4,1,0,
        6,7,1,0,16,17,1,0,18,19,1,0,20,25,153,0,36,1,0,0,0,2,46,1,0,0,0,
        4,50,1,0,0,0,6,55,1,0,0,0,8,58,1,0,0,0,10,67,1,0,0,0,12,69,1,0,0,
        0,14,74,1,0,0,0,16,80,1,0,0,0,18,86,1,0,0,0,20,100,1,0,0,0,22,108,
        1,0,0,0,24,116,1,0,0,0,26,132,1,0,0,0,28,134,1,0,0,0,30,136,1,0,
        0,0,32,140,1,0,0,0,34,148,1,0,0,0,36,37,5,1,0,0,37,38,5,2,0,0,38,
        39,3,2,1,0,39,40,5,3,0,0,40,41,5,4,0,0,41,42,5,2,0,0,42,43,3,8,4,
        0,43,44,5,3,0,0,44,1,1,0,0,0,45,47,3,4,2,0,46,45,1,0,0,0,47,48,1,
        0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,3,1,0,0,0,50,51,3,6,3,0,51,
        52,3,34,17,0,52,53,5,5,0,0,53,54,6,2,-1,0,54,5,1,0,0,0,55,56,7,0,
        0,0,56,7,1,0,0,0,57,59,3,10,5,0,58,57,1,0,0,0,59,60,1,0,0,0,60,58,
        1,0,0,0,60,61,1,0,0,0,61,9,1,0,0,0,62,68,3,12,6,0,63,68,3,14,7,0,
        64,68,3,16,8,0,65,68,3,18,9,0,66,68,3,20,10,0,67,62,1,0,0,0,67,63,
        1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,11,1,0,0,0,
        69,70,5,27,0,0,70,71,5,8,0,0,71,72,3,22,11,0,72,73,5,5,0,0,73,13,
        1,0,0,0,74,75,5,9,0,0,75,76,5,10,0,0,76,77,3,32,16,0,77,78,5,11,
        0,0,78,79,5,5,0,0,79,15,1,0,0,0,80,81,5,12,0,0,81,82,5,10,0,0,82,
        83,3,34,17,0,83,84,5,11,0,0,84,85,5,5,0,0,85,17,1,0,0,0,86,87,5,
        13,0,0,87,88,5,10,0,0,88,89,3,28,14,0,89,90,5,11,0,0,90,91,5,2,0,
        0,91,92,3,8,4,0,92,98,5,3,0,0,93,94,5,14,0,0,94,95,5,2,0,0,95,96,
        3,8,4,0,96,97,5,3,0,0,97,99,1,0,0,0,98,93,1,0,0,0,98,99,1,0,0,0,
        99,19,1,0,0,0,100,101,5,15,0,0,101,102,5,10,0,0,102,103,3,28,14,
        0,103,104,5,11,0,0,104,105,5,2,0,0,105,106,3,8,4,0,106,107,5,3,0,
        0,107,21,1,0,0,0,108,113,3,24,12,0,109,110,7,1,0,0,110,112,3,24,
        12,0,111,109,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,
        0,0,114,23,1,0,0,0,115,113,1,0,0,0,116,121,3,26,13,0,117,118,7,2,
        0,0,118,120,3,26,13,0,119,117,1,0,0,0,120,123,1,0,0,0,121,119,1,
        0,0,0,121,122,1,0,0,0,122,25,1,0,0,0,123,121,1,0,0,0,124,133,5,27,
        0,0,125,133,5,28,0,0,126,133,5,29,0,0,127,133,5,30,0,0,128,129,5,
        10,0,0,129,130,3,22,11,0,130,131,5,11,0,0,131,133,1,0,0,0,132,124,
        1,0,0,0,132,125,1,0,0,0,132,126,1,0,0,0,132,127,1,0,0,0,132,128,
        1,0,0,0,133,27,1,0,0,0,134,135,3,30,15,0,135,29,1,0,0,0,136,137,
        3,22,11,0,137,138,7,3,0,0,138,139,3,22,11,0,139,31,1,0,0,0,140,145,
        3,22,11,0,141,142,5,26,0,0,142,144,3,22,11,0,143,141,1,0,0,0,144,
        147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,33,1,0,0,0,147,145,
        1,0,0,0,148,153,5,27,0,0,149,150,5,26,0,0,150,152,5,27,0,0,151,149,
        1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,35,1,
        0,0,0,155,153,1,0,0,0,9,48,60,67,98,113,121,132,145,153
    ]

class SimpAlgParser ( Parser ):

    grammarFileName = "SimpAlg.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'{'", "'}'", "'program'", "';'", 
                     "'int'", "'float'", "'='", "'print'", "'('", "')'", 
                     "'scan'", "'if'", "'else'", "'while'", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'>'", "'<='", "'>='", "'=='", 
                     "'!='", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "FLOAT", "STRING", "Comment", "WS" ]

    RULE_programa = 0
    RULE_declaracoes = 1
    RULE_declaracao = 2
    RULE_tipo = 3
    RULE_comandos = 4
    RULE_comando = 5
    RULE_atribuicao = 6
    RULE_saida = 7
    RULE_entrada = 8
    RULE_condicional = 9
    RULE_repeticao = 10
    RULE_expressao = 11
    RULE_termo = 12
    RULE_fator = 13
    RULE_expressao_logica = 14
    RULE_relacional = 15
    RULE_lista_de_valores = 16
    RULE_lista_de_variaveis = 17

    ruleNames =  [ "programa", "declaracoes", "declaracao", "tipo", "comandos", 
                   "comando", "atribuicao", "saida", "entrada", "condicional", 
                   "repeticao", "expressao", "termo", "fator", "expressao_logica", 
                   "relacional", "lista_de_valores", "lista_de_variaveis" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    ID=27
    INT=28
    FLOAT=29
    STRING=30
    Comment=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracoes(self):
            return self.getTypedRuleContext(SimpAlgParser.DeclaracoesContext,0)


        def comandos(self):
            return self.getTypedRuleContext(SimpAlgParser.ComandosContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = SimpAlgParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(SimpAlgParser.T__0)
            self.state = 37
            self.match(SimpAlgParser.T__1)
            self.state = 38
            self.declaracoes()
            self.state = 39
            self.match(SimpAlgParser.T__2)
            self.state = 40
            self.match(SimpAlgParser.T__3)
            self.state = 41
            self.match(SimpAlgParser.T__1)
            self.state = 42
            self.comandos()
            self.state = 43
            self.match(SimpAlgParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.DeclaracaoContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracoes" ):
                return visitor.visitDeclaracoes(self)
            else:
                return visitor.visitChildren(self)




    def declaracoes(self):

        localctx = SimpAlgParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.declaracao()
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6 or _la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._lista_de_variaveis = None # Lista_de_variaveisContext

        def tipo(self):
            return self.getTypedRuleContext(SimpAlgParser.TipoContext,0)


        def lista_de_variaveis(self):
            return self.getTypedRuleContext(SimpAlgParser.Lista_de_variaveisContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = SimpAlgParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.tipo()
            self.state = 51
            localctx._lista_de_variaveis = self.lista_de_variaveis()
            self.state = 52
            self.match(SimpAlgParser.T__4)

                    // Verifica se há duplicatas na lista de variáveis
                    List<String> variaveis = (None if localctx._lista_de_variaveis is None else self._input.getText(localctx._lista_de_variaveis.start,localctx._lista_de_variaveis.stop)).split(",");
                    Set<String> variaveisSet = new HashSet<>(variaveis);

                    if (variaveis.size() != variaveisSet.size()) {
                        // Se há duplicatas, emite um erro
                        System.err.println("Erro: Variáveis com nomes duplicados na declaração.");
                        throw new RuntimeException("Variáveis com nomes duplicados na declaração.");
                    }
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpAlgParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = SimpAlgParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.ComandoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.ComandoContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandos" ):
                return visitor.visitComandos(self)
            else:
                return visitor.visitChildren(self)




    def comandos(self):

        localctx = SimpAlgParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comandos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.comando()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 134263296) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(SimpAlgParser.AtribuicaoContext,0)


        def saida(self):
            return self.getTypedRuleContext(SimpAlgParser.SaidaContext,0)


        def entrada(self):
            return self.getTypedRuleContext(SimpAlgParser.EntradaContext,0)


        def condicional(self):
            return self.getTypedRuleContext(SimpAlgParser.CondicionalContext,0)


        def repeticao(self):
            return self.getTypedRuleContext(SimpAlgParser.RepeticaoContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = SimpAlgParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comando)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.atribuicao()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.saida()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.entrada()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.condicional()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.repeticao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpAlgParser.ID, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpAlgParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = SimpAlgParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(SimpAlgParser.ID)
            self.state = 70
            self.match(SimpAlgParser.T__7)
            self.state = 71
            self.expressao()
            self.state = 72
            self.match(SimpAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_de_valores(self):
            return self.getTypedRuleContext(SimpAlgParser.Lista_de_valoresContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_saida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaida" ):
                listener.enterSaida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaida" ):
                listener.exitSaida(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaida" ):
                return visitor.visitSaida(self)
            else:
                return visitor.visitChildren(self)




    def saida(self):

        localctx = SimpAlgParser.SaidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_saida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(SimpAlgParser.T__8)
            self.state = 75
            self.match(SimpAlgParser.T__9)
            self.state = 76
            self.lista_de_valores()
            self.state = 77
            self.match(SimpAlgParser.T__10)
            self.state = 78
            self.match(SimpAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntradaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_de_variaveis(self):
            return self.getTypedRuleContext(SimpAlgParser.Lista_de_variaveisContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_entrada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrada" ):
                listener.enterEntrada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrada" ):
                listener.exitEntrada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntrada" ):
                return visitor.visitEntrada(self)
            else:
                return visitor.visitChildren(self)




    def entrada(self):

        localctx = SimpAlgParser.EntradaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_entrada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SimpAlgParser.T__11)
            self.state = 81
            self.match(SimpAlgParser.T__9)
            self.state = 82
            self.lista_de_variaveis()
            self.state = 83
            self.match(SimpAlgParser.T__10)
            self.state = 84
            self.match(SimpAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_logica(self):
            return self.getTypedRuleContext(SimpAlgParser.Expressao_logicaContext,0)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.ComandosContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.ComandosContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = SimpAlgParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(SimpAlgParser.T__12)
            self.state = 87
            self.match(SimpAlgParser.T__9)
            self.state = 88
            self.expressao_logica()
            self.state = 89
            self.match(SimpAlgParser.T__10)
            self.state = 90
            self.match(SimpAlgParser.T__1)
            self.state = 91
            self.comandos()
            self.state = 92
            self.match(SimpAlgParser.T__2)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 93
                self.match(SimpAlgParser.T__13)
                self.state = 94
                self.match(SimpAlgParser.T__1)
                self.state = 95
                self.comandos()
                self.state = 96
                self.match(SimpAlgParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_logica(self):
            return self.getTypedRuleContext(SimpAlgParser.Expressao_logicaContext,0)


        def comandos(self):
            return self.getTypedRuleContext(SimpAlgParser.ComandosContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_repeticao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeticao" ):
                listener.enterRepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeticao" ):
                listener.exitRepeticao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeticao" ):
                return visitor.visitRepeticao(self)
            else:
                return visitor.visitChildren(self)




    def repeticao(self):

        localctx = SimpAlgParser.RepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_repeticao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SimpAlgParser.T__14)
            self.state = 101
            self.match(SimpAlgParser.T__9)
            self.state = 102
            self.expressao_logica()
            self.state = 103
            self.match(SimpAlgParser.T__10)
            self.state = 104
            self.match(SimpAlgParser.T__1)
            self.state = 105
            self.comandos()
            self.state = 106
            self.match(SimpAlgParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.TermoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.TermoContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = SimpAlgParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expressao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.termo()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 109
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 110
                self.termo()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.FatorContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.FatorContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo" ):
                return visitor.visitTermo(self)
            else:
                return visitor.visitChildren(self)




    def termo(self):

        localctx = SimpAlgParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.fator()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 117
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 118
                self.fator()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpAlgParser.ID, 0)

        def INT(self):
            return self.getToken(SimpAlgParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SimpAlgParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(SimpAlgParser.STRING, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpAlgParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator" ):
                return visitor.visitFator(self)
            else:
                return visitor.visitChildren(self)




    def fator(self):

        localctx = SimpAlgParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fator)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(SimpAlgParser.ID)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(SimpAlgParser.INT)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(SimpAlgParser.FLOAT)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.match(SimpAlgParser.STRING)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.match(SimpAlgParser.T__9)
                self.state = 129
                self.expressao()
                self.state = 130
                self.match(SimpAlgParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_logicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacional(self):
            return self.getTypedRuleContext(SimpAlgParser.RelacionalContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_expressao_logica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_logica" ):
                listener.enterExpressao_logica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_logica" ):
                listener.exitExpressao_logica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao_logica" ):
                return visitor.visitExpressao_logica(self)
            else:
                return visitor.visitChildren(self)




    def expressao_logica(self):

        localctx = SimpAlgParser.Expressao_logicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expressao_logica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.relacional()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacional" ):
                listener.enterRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacional" ):
                listener.exitRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)




    def relacional(self):

        localctx = SimpAlgParser.RelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.expressao()
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 138
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_de_valoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_lista_de_valores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_de_valores" ):
                listener.enterLista_de_valores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_de_valores" ):
                listener.exitLista_de_valores(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_de_valores" ):
                return visitor.visitLista_de_valores(self)
            else:
                return visitor.visitChildren(self)




    def lista_de_valores(self):

        localctx = SimpAlgParser.Lista_de_valoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lista_de_valores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.expressao()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 141
                self.match(SimpAlgParser.T__25)
                self.state = 142
                self.expressao()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_de_variaveisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpAlgParser.ID)
            else:
                return self.getToken(SimpAlgParser.ID, i)

        def getRuleIndex(self):
            return SimpAlgParser.RULE_lista_de_variaveis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_de_variaveis" ):
                listener.enterLista_de_variaveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_de_variaveis" ):
                listener.exitLista_de_variaveis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_de_variaveis" ):
                return visitor.visitLista_de_variaveis(self)
            else:
                return visitor.visitChildren(self)




    def lista_de_variaveis(self):

        localctx = SimpAlgParser.Lista_de_variaveisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lista_de_variaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(SimpAlgParser.ID)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 149
                self.match(SimpAlgParser.T__25)
                self.state = 150
                self.match(SimpAlgParser.ID)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





