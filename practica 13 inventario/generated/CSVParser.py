# Generated from CSV.g4 by ANTLR 4.13.2
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
        4,1,5,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,5,0,13,
        8,0,10,0,12,0,16,9,0,1,0,3,0,19,8,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,
        5,2,28,8,2,10,2,12,2,31,9,2,1,2,1,2,1,3,1,3,1,3,5,3,38,8,3,10,3,
        12,3,41,9,3,1,4,1,4,1,4,3,4,46,8,4,1,4,0,0,5,0,2,4,6,8,0,0,48,0,
        10,1,0,0,0,2,22,1,0,0,0,4,24,1,0,0,0,6,34,1,0,0,0,8,45,1,0,0,0,10,
        14,3,2,1,0,11,13,3,4,2,0,12,11,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,
        0,14,15,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,17,19,3,6,3,0,18,17,
        1,0,0,0,18,19,1,0,0,0,19,20,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,
        23,3,4,2,0,23,3,1,0,0,0,24,29,3,8,4,0,25,26,5,1,0,0,26,28,3,8,4,
        0,27,25,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,
        1,0,0,0,31,29,1,0,0,0,32,33,5,2,0,0,33,5,1,0,0,0,34,39,3,8,4,0,35,
        36,5,1,0,0,36,38,3,8,4,0,37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,
        0,39,40,1,0,0,0,40,7,1,0,0,0,41,39,1,0,0,0,42,46,5,3,0,0,43,46,5,
        4,0,0,44,46,1,0,0,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,
        9,1,0,0,0,5,14,18,29,39,45
    ]

class CSVParser ( Parser ):

    grammarFileName = "CSV.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "COMMA", "NL", "TEXT", "STRING", "WS" ]

    RULE_csvFile = 0
    RULE_header = 1
    RULE_row = 2
    RULE_lastRow = 3
    RULE_field = 4

    ruleNames =  [ "csvFile", "header", "row", "lastRow", "field" ]

    EOF = Token.EOF
    COMMA=1
    NL=2
    TEXT=3
    STRING=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CsvFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(CSVParser.HeaderContext,0)


        def EOF(self):
            return self.getToken(CSVParser.EOF, 0)

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.RowContext)
            else:
                return self.getTypedRuleContext(CSVParser.RowContext,i)


        def lastRow(self):
            return self.getTypedRuleContext(CSVParser.LastRowContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_csvFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCsvFile" ):
                listener.enterCsvFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCsvFile" ):
                listener.exitCsvFile(self)




    def csvFile(self):

        localctx = CSVParser.CsvFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_csvFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.header()
            self.state = 14
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 11
                    self.row() 
                self.state = 16
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 17
                self.lastRow()


            self.state = 20
            self.match(CSVParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self):
            return self.getTypedRuleContext(CSVParser.RowContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)




    def header(self):

        localctx = CSVParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.row()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.FieldContext)
            else:
                return self.getTypedRuleContext(CSVParser.FieldContext,i)


        def NL(self):
            return self.getToken(CSVParser.NL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSVParser.COMMA)
            else:
                return self.getToken(CSVParser.COMMA, i)

        def getRuleIndex(self):
            return CSVParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = CSVParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.field()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 25
                self.match(CSVParser.COMMA)
                self.state = 26
                self.field()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(CSVParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LastRowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.FieldContext)
            else:
                return self.getTypedRuleContext(CSVParser.FieldContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSVParser.COMMA)
            else:
                return self.getToken(CSVParser.COMMA, i)

        def getRuleIndex(self):
            return CSVParser.RULE_lastRow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastRow" ):
                listener.enterLastRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastRow" ):
                listener.exitLastRow(self)




    def lastRow(self):

        localctx = CSVParser.LastRowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lastRow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.field()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 35
                self.match(CSVParser.COMMA)
                self.state = 36
                self.field()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVParser.RULE_field

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CSVParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class TextContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(CSVParser.TEXT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)


    class EmptyContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)



    def field(self):

        localctx = CSVParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_field)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = CSVParser.TextContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(CSVParser.TEXT)
                pass
            elif token in [4]:
                localctx = CSVParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(CSVParser.STRING)
                pass
            elif token in [-1, 1, 2]:
                localctx = CSVParser.EmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)

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





