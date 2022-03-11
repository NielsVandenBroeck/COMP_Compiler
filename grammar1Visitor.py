# Generated from grammar1.g4 by ANTLR 4.9.3
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by grammar1Parser.

class grammar1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammar1Parser#start.
    def visitStart(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#programLine.
    def visitProgramLine(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#line.
    def visitLine(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#DeclarationExpression.
    def visitDeclarationExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#DeclarationAndInitalizationExpression.
    def visitDeclarationAndInitalizationExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#DeclarationAndInitalizationPointerExpression.
    def visitDeclarationAndInitalizationPointerExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#InitalizationExpression.
    def visitInitalizationExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#InitalizationPointerExpression.
    def visitInitalizationPointerExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#Expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#IdentifierOperationExpression.
    def visitIdentifierOperationExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#identifierOP.
    def visitIdentifierOP(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#types.
    def visitTypes(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#dataType.
    def visitDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#body.
    def visitBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#leftOperationBody.
    def visitLeftOperationBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#unaryBody.
    def visitUnaryBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#UnaryExpression.
    def visitUnaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#OperationExpression.
    def visitOperationExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#ParenExpression.
    def visitParenExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#CharExpression.
    def visitCharExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#IntExpression.
    def visitIntExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#FloatExpression.
    def visitFloatExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#VariableExpression.
    def visitVariableExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#operation.
    def visitOperation(self, ctx):
        return self.visitChildren(ctx)


