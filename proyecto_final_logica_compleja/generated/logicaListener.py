# Generated from logica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .logicaParser import logicaParser
else:
    from logicaParser import logicaParser

# This class defines a complete listener for a parse tree produced by logicaParser.
class logicaListener(ParseTreeListener):

    # Enter a parse tree produced by logicaParser#program.
    def enterProgram(self, ctx:logicaParser.ProgramContext):
        pass

    # Exit a parse tree produced by logicaParser#program.
    def exitProgram(self, ctx:logicaParser.ProgramContext):
        pass


    # Enter a parse tree produced by logicaParser#declaration.
    def enterDeclaration(self, ctx:logicaParser.DeclarationContext):
        pass

    # Exit a parse tree produced by logicaParser#declaration.
    def exitDeclaration(self, ctx:logicaParser.DeclarationContext):
        pass


    # Enter a parse tree produced by logicaParser#functionDecl.
    def enterFunctionDecl(self, ctx:logicaParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by logicaParser#functionDecl.
    def exitFunctionDecl(self, ctx:logicaParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by logicaParser#paramList.
    def enterParamList(self, ctx:logicaParser.ParamListContext):
        pass

    # Exit a parse tree produced by logicaParser#paramList.
    def exitParamList(self, ctx:logicaParser.ParamListContext):
        pass


    # Enter a parse tree produced by logicaParser#param.
    def enterParam(self, ctx:logicaParser.ParamContext):
        pass

    # Exit a parse tree produced by logicaParser#param.
    def exitParam(self, ctx:logicaParser.ParamContext):
        pass


    # Enter a parse tree produced by logicaParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:logicaParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by logicaParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:logicaParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by logicaParser#statement.
    def enterStatement(self, ctx:logicaParser.StatementContext):
        pass

    # Exit a parse tree produced by logicaParser#statement.
    def exitStatement(self, ctx:logicaParser.StatementContext):
        pass


    # Enter a parse tree produced by logicaParser#assignment.
    def enterAssignment(self, ctx:logicaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by logicaParser#assignment.
    def exitAssignment(self, ctx:logicaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by logicaParser#ifStatement.
    def enterIfStatement(self, ctx:logicaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by logicaParser#ifStatement.
    def exitIfStatement(self, ctx:logicaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by logicaParser#whileStatement.
    def enterWhileStatement(self, ctx:logicaParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by logicaParser#whileStatement.
    def exitWhileStatement(self, ctx:logicaParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by logicaParser#inputStmt.
    def enterInputStmt(self, ctx:logicaParser.InputStmtContext):
        pass

    # Exit a parse tree produced by logicaParser#inputStmt.
    def exitInputStmt(self, ctx:logicaParser.InputStmtContext):
        pass


    # Enter a parse tree produced by logicaParser#printStmt.
    def enterPrintStmt(self, ctx:logicaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by logicaParser#printStmt.
    def exitPrintStmt(self, ctx:logicaParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by logicaParser#returnStatement.
    def enterReturnStatement(self, ctx:logicaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by logicaParser#returnStatement.
    def exitReturnStatement(self, ctx:logicaParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by logicaParser#callStmt.
    def enterCallStmt(self, ctx:logicaParser.CallStmtContext):
        pass

    # Exit a parse tree produced by logicaParser#callStmt.
    def exitCallStmt(self, ctx:logicaParser.CallStmtContext):
        pass


    # Enter a parse tree produced by logicaParser#breakStmt.
    def enterBreakStmt(self, ctx:logicaParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by logicaParser#breakStmt.
    def exitBreakStmt(self, ctx:logicaParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by logicaParser#block.
    def enterBlock(self, ctx:logicaParser.BlockContext):
        pass

    # Exit a parse tree produced by logicaParser#block.
    def exitBlock(self, ctx:logicaParser.BlockContext):
        pass


    # Enter a parse tree produced by logicaParser#boolExpr.
    def enterBoolExpr(self, ctx:logicaParser.BoolExprContext):
        pass

    # Exit a parse tree produced by logicaParser#boolExpr.
    def exitBoolExpr(self, ctx:logicaParser.BoolExprContext):
        pass


    # Enter a parse tree produced by logicaParser#orExpr.
    def enterOrExpr(self, ctx:logicaParser.OrExprContext):
        pass

    # Exit a parse tree produced by logicaParser#orExpr.
    def exitOrExpr(self, ctx:logicaParser.OrExprContext):
        pass


    # Enter a parse tree produced by logicaParser#xorExpr.
    def enterXorExpr(self, ctx:logicaParser.XorExprContext):
        pass

    # Exit a parse tree produced by logicaParser#xorExpr.
    def exitXorExpr(self, ctx:logicaParser.XorExprContext):
        pass


    # Enter a parse tree produced by logicaParser#andExpr.
    def enterAndExpr(self, ctx:logicaParser.AndExprContext):
        pass

    # Exit a parse tree produced by logicaParser#andExpr.
    def exitAndExpr(self, ctx:logicaParser.AndExprContext):
        pass


    # Enter a parse tree produced by logicaParser#unaryExpr.
    def enterUnaryExpr(self, ctx:logicaParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by logicaParser#unaryExpr.
    def exitUnaryExpr(self, ctx:logicaParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by logicaParser#primary.
    def enterPrimary(self, ctx:logicaParser.PrimaryContext):
        pass

    # Exit a parse tree produced by logicaParser#primary.
    def exitPrimary(self, ctx:logicaParser.PrimaryContext):
        pass


    # Enter a parse tree produced by logicaParser#functionCall.
    def enterFunctionCall(self, ctx:logicaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by logicaParser#functionCall.
    def exitFunctionCall(self, ctx:logicaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by logicaParser#builtinCall.
    def enterBuiltinCall(self, ctx:logicaParser.BuiltinCallContext):
        pass

    # Exit a parse tree produced by logicaParser#builtinCall.
    def exitBuiltinCall(self, ctx:logicaParser.BuiltinCallContext):
        pass


    # Enter a parse tree produced by logicaParser#argList.
    def enterArgList(self, ctx:logicaParser.ArgListContext):
        pass

    # Exit a parse tree produced by logicaParser#argList.
    def exitArgList(self, ctx:logicaParser.ArgListContext):
        pass



del logicaParser