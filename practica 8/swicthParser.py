# Generated from swicth.g4 by ANTLR 4.13.2
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
        4,1,23,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,3,0,17,8,0,4,0,19,8,0,11,0,12,0,20,1,0,1,0,1,1,1,1,3,1,
        27,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,2,3,
        2,41,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,51,8,3,10,3,12,3,54,
        9,3,1,4,1,4,1,4,1,4,1,4,5,4,61,8,4,10,4,12,4,64,9,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,77,8,6,1,6,1,6,1,6,1,6,1,6,1,
        6,5,6,85,8,6,10,6,12,6,88,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,2,1,
        0,14,15,1,0,12,13,93,0,18,1,0,0,0,2,26,1,0,0,0,4,28,1,0,0,0,6,44,
        1,0,0,0,8,55,1,0,0,0,10,65,1,0,0,0,12,76,1,0,0,0,14,16,3,2,1,0,15,
        17,5,20,0,0,16,15,1,0,0,0,16,17,1,0,0,0,17,19,1,0,0,0,18,14,1,0,
        0,0,19,20,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,22,1,0,0,0,22,23,
        5,0,0,1,23,1,1,0,0,0,24,27,3,4,2,0,25,27,3,10,5,0,26,24,1,0,0,0,
        26,25,1,0,0,0,27,3,1,0,0,0,28,29,5,3,0,0,29,30,5,6,0,0,30,31,3,12,
        6,0,31,32,5,7,0,0,32,36,5,8,0,0,33,35,3,6,3,0,34,33,1,0,0,0,35,38,
        1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,
        39,41,3,8,4,0,40,39,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,5,
        9,0,0,43,5,1,0,0,0,44,45,5,4,0,0,45,46,5,22,0,0,46,52,5,10,0,0,47,
        48,3,10,5,0,48,49,5,20,0,0,49,51,1,0,0,0,50,47,1,0,0,0,51,54,1,0,
        0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,7,1,0,0,0,54,52,1,0,0,0,55,56,
        5,5,0,0,56,62,5,10,0,0,57,58,3,10,5,0,58,59,5,20,0,0,59,61,1,0,0,
        0,60,57,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,9,1,
        0,0,0,64,62,1,0,0,0,65,66,5,21,0,0,66,67,5,11,0,0,67,68,3,12,6,0,
        68,11,1,0,0,0,69,70,6,6,-1,0,70,77,5,22,0,0,71,77,5,21,0,0,72,73,
        5,6,0,0,73,74,3,12,6,0,74,75,5,7,0,0,75,77,1,0,0,0,76,69,1,0,0,0,
        76,71,1,0,0,0,76,72,1,0,0,0,77,86,1,0,0,0,78,79,10,5,0,0,79,80,7,
        0,0,0,80,85,3,12,6,6,81,82,10,4,0,0,82,83,7,1,0,0,83,85,3,12,6,5,
        84,78,1,0,0,0,84,81,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,
        0,0,0,87,13,1,0,0,0,88,86,1,0,0,0,10,16,20,26,36,40,52,62,76,84,
        86
    ]

class swicthParser ( Parser ):

    grammarFileName = "swicth.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'switch'", "'case'", 
                     "'default'", "'('", "')'", "'{'", "'}'", "':'", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'=='", "'!='", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "SWITCH", "CASE", "DEFAULT", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "DOBLEP", 
                      "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", 
                      "EQ", "NEQ", "SEMI", "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_switchOrden = 2
    RULE_caseOrden = 3
    RULE_defaultOrden = 4
    RULE_asignacion = 5
    RULE_expresion = 6

    ruleNames =  [ "programa", "sentencia", "switchOrden", "caseOrden", 
                   "defaultOrden", "asignacion", "expresion" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    SWITCH=3
    CASE=4
    DEFAULT=5
    LPAREN=6
    RPAREN=7
    LBRACE=8
    RBRACE=9
    DOBLEP=10
    ASSIGN=11
    PLUS=12
    MINUS=13
    MUL=14
    DIV=15
    GT=16
    LT=17
    EQ=18
    NEQ=19
    SEMI=20
    ID=21
    INT=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(swicthParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(swicthParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(swicthParser.SentenciaContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(swicthParser.SEMI)
            else:
                return self.getToken(swicthParser.SEMI, i)

        def getRuleIndex(self):
            return swicthParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = swicthParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.sentencia()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 15
                    self.match(swicthParser.SEMI)


                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==21):
                    break

            self.state = 22
            self.match(swicthParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switchOrden(self):
            return self.getTypedRuleContext(swicthParser.SwitchOrdenContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(swicthParser.AsignacionContext,0)


        def getRuleIndex(self):
            return swicthParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = swicthParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.switchOrden()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.asignacion()
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


    class SwitchOrdenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(swicthParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(swicthParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(swicthParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(swicthParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(swicthParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(swicthParser.RBRACE, 0)

        def caseOrden(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(swicthParser.CaseOrdenContext)
            else:
                return self.getTypedRuleContext(swicthParser.CaseOrdenContext,i)


        def defaultOrden(self):
            return self.getTypedRuleContext(swicthParser.DefaultOrdenContext,0)


        def getRuleIndex(self):
            return swicthParser.RULE_switchOrden

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchOrden" ):
                listener.enterSwitchOrden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchOrden" ):
                listener.exitSwitchOrden(self)




    def switchOrden(self):

        localctx = swicthParser.SwitchOrdenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_switchOrden)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(swicthParser.SWITCH)
            self.state = 29
            self.match(swicthParser.LPAREN)
            self.state = 30
            self.expresion(0)
            self.state = 31
            self.match(swicthParser.RPAREN)
            self.state = 32
            self.match(swicthParser.LBRACE)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 33
                self.caseOrden()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 39
                self.defaultOrden()


            self.state = 42
            self.match(swicthParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseOrdenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(swicthParser.CASE, 0)

        def INT(self):
            return self.getToken(swicthParser.INT, 0)

        def DOBLEP(self):
            return self.getToken(swicthParser.DOBLEP, 0)

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(swicthParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(swicthParser.AsignacionContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(swicthParser.SEMI)
            else:
                return self.getToken(swicthParser.SEMI, i)

        def getRuleIndex(self):
            return swicthParser.RULE_caseOrden

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseOrden" ):
                listener.enterCaseOrden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseOrden" ):
                listener.exitCaseOrden(self)




    def caseOrden(self):

        localctx = swicthParser.CaseOrdenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_caseOrden)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(swicthParser.CASE)
            self.state = 45
            self.match(swicthParser.INT)
            self.state = 46
            self.match(swicthParser.DOBLEP)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 47
                self.asignacion()
                self.state = 48
                self.match(swicthParser.SEMI)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultOrdenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(swicthParser.DEFAULT, 0)

        def DOBLEP(self):
            return self.getToken(swicthParser.DOBLEP, 0)

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(swicthParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(swicthParser.AsignacionContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(swicthParser.SEMI)
            else:
                return self.getToken(swicthParser.SEMI, i)

        def getRuleIndex(self):
            return swicthParser.RULE_defaultOrden

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultOrden" ):
                listener.enterDefaultOrden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultOrden" ):
                listener.exitDefaultOrden(self)




    def defaultOrden(self):

        localctx = swicthParser.DefaultOrdenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_defaultOrden)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(swicthParser.DEFAULT)
            self.state = 56
            self.match(swicthParser.DOBLEP)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 57
                self.asignacion()
                self.state = 58
                self.match(swicthParser.SEMI)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return swicthParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a swicthParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(swicthParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(swicthParser.ASSIGN, 0)
        def expresion(self):
            return self.getTypedRuleContext(swicthParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def asignacion(self):

        localctx = swicthParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            localctx = swicthParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(swicthParser.ID)
            self.state = 66
            self.match(swicthParser.ASSIGN)
            self.state = 67
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return swicthParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a swicthParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(swicthParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class MulDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a swicthParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(swicthParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(swicthParser.ExpresionContext,i)

        def MUL(self):
            return self.getToken(swicthParser.MUL, 0)
        def DIV(self):
            return self.getToken(swicthParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a swicthParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(swicthParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(swicthParser.ExpresionContext,i)

        def PLUS(self):
            return self.getToken(swicthParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(swicthParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a swicthParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(swicthParser.LPAREN, 0)
        def expresion(self):
            return self.getTypedRuleContext(swicthParser.ExpresionContext,0)

        def RPAREN(self):
            return self.getToken(swicthParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a swicthParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(swicthParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = swicthParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = swicthParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 70
                self.match(swicthParser.INT)
                pass
            elif token in [21]:
                localctx = swicthParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(swicthParser.ID)
                pass
            elif token in [6]:
                localctx = swicthParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.match(swicthParser.LPAREN)
                self.state = 73
                self.expresion(0)
                self.state = 74
                self.match(swicthParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = swicthParser.MulDivContext(self, swicthParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 78
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 79
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = swicthParser.AddSubContext(self, swicthParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 81
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 82
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 83
                        self.expresion(5)
                        pass

             
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




