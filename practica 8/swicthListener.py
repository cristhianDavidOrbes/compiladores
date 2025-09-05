# Generated from swicth.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .swicthParser import swicthParser
else:
    from swicthParser import swicthParser

# This class defines a complete listener for a parse tree produced by swicthParser.
class swicthListener(ParseTreeListener):

    # Enter a parse tree produced by swicthParser#programa.
    def enterPrograma(self, ctx:swicthParser.ProgramaContext):
        pass

    # Exit a parse tree produced by swicthParser#programa.
    def exitPrograma(self, ctx:swicthParser.ProgramaContext):
        pass


    # Enter a parse tree produced by swicthParser#sentencia.
    def enterSentencia(self, ctx:swicthParser.SentenciaContext):
        pass

    # Exit a parse tree produced by swicthParser#sentencia.
    def exitSentencia(self, ctx:swicthParser.SentenciaContext):
        pass


    # Enter a parse tree produced by swicthParser#switchOrden.
    def enterSwitchOrden(self, ctx:swicthParser.SwitchOrdenContext):
        pass

    # Exit a parse tree produced by swicthParser#switchOrden.
    def exitSwitchOrden(self, ctx:swicthParser.SwitchOrdenContext):
        pass


    # Enter a parse tree produced by swicthParser#caseOrden.
    def enterCaseOrden(self, ctx:swicthParser.CaseOrdenContext):
        pass

    # Exit a parse tree produced by swicthParser#caseOrden.
    def exitCaseOrden(self, ctx:swicthParser.CaseOrdenContext):
        pass


    # Enter a parse tree produced by swicthParser#defaultOrden.
    def enterDefaultOrden(self, ctx:swicthParser.DefaultOrdenContext):
        pass

    # Exit a parse tree produced by swicthParser#defaultOrden.
    def exitDefaultOrden(self, ctx:swicthParser.DefaultOrdenContext):
        pass


    # Enter a parse tree produced by swicthParser#Assign.
    def enterAssign(self, ctx:swicthParser.AssignContext):
        pass

    # Exit a parse tree produced by swicthParser#Assign.
    def exitAssign(self, ctx:swicthParser.AssignContext):
        pass


    # Enter a parse tree produced by swicthParser#Variable.
    def enterVariable(self, ctx:swicthParser.VariableContext):
        pass

    # Exit a parse tree produced by swicthParser#Variable.
    def exitVariable(self, ctx:swicthParser.VariableContext):
        pass


    # Enter a parse tree produced by swicthParser#MulDiv.
    def enterMulDiv(self, ctx:swicthParser.MulDivContext):
        pass

    # Exit a parse tree produced by swicthParser#MulDiv.
    def exitMulDiv(self, ctx:swicthParser.MulDivContext):
        pass


    # Enter a parse tree produced by swicthParser#AddSub.
    def enterAddSub(self, ctx:swicthParser.AddSubContext):
        pass

    # Exit a parse tree produced by swicthParser#AddSub.
    def exitAddSub(self, ctx:swicthParser.AddSubContext):
        pass


    # Enter a parse tree produced by swicthParser#Parens.
    def enterParens(self, ctx:swicthParser.ParensContext):
        pass

    # Exit a parse tree produced by swicthParser#Parens.
    def exitParens(self, ctx:swicthParser.ParensContext):
        pass


    # Enter a parse tree produced by swicthParser#Int.
    def enterInt(self, ctx:swicthParser.IntContext):
        pass

    # Exit a parse tree produced by swicthParser#Int.
    def exitInt(self, ctx:swicthParser.IntContext):
        pass



del swicthParser