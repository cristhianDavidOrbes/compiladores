# Generated from logica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .logicaParser import logicaParser
else:
    from logicaParser import logicaParser

# This class defines a complete generic visitor for a parse tree produced by logicaParser.

class logicaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by logicaParser#program.
    def visitProgram(self, ctx:logicaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#declaration.
    def visitDeclaration(self, ctx:logicaParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#functionDecl.
    def visitFunctionDecl(self, ctx:logicaParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#paramList.
    def visitParamList(self, ctx:logicaParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#param.
    def visitParam(self, ctx:logicaParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:logicaParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#statement.
    def visitStatement(self, ctx:logicaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#assignment.
    def visitAssignment(self, ctx:logicaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#ifStatement.
    def visitIfStatement(self, ctx:logicaParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#whileStatement.
    def visitWhileStatement(self, ctx:logicaParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#inputStmt.
    def visitInputStmt(self, ctx:logicaParser.InputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#printStmt.
    def visitPrintStmt(self, ctx:logicaParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#returnStatement.
    def visitReturnStatement(self, ctx:logicaParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#callStmt.
    def visitCallStmt(self, ctx:logicaParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#breakStmt.
    def visitBreakStmt(self, ctx:logicaParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#block.
    def visitBlock(self, ctx:logicaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#boolExpr.
    def visitBoolExpr(self, ctx:logicaParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#orExpr.
    def visitOrExpr(self, ctx:logicaParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#xorExpr.
    def visitXorExpr(self, ctx:logicaParser.XorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#andExpr.
    def visitAndExpr(self, ctx:logicaParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#unaryExpr.
    def visitUnaryExpr(self, ctx:logicaParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#primary.
    def visitPrimary(self, ctx:logicaParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#functionCall.
    def visitFunctionCall(self, ctx:logicaParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#builtinCall.
    def visitBuiltinCall(self, ctx:logicaParser.BuiltinCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicaParser#argList.
    def visitArgList(self, ctx:logicaParser.ArgListContext):
        return self.visitChildren(ctx)



del logicaParser