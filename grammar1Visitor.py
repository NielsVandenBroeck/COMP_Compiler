# Generated from grammar1.g4 by ANTLR 4.9.3
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by grammar1Parser.

class grammar1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammar1Parser#program.
    def visitProgram(self, ctx):
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


    # Visit a parse tree produced by grammar1Parser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#OperationExpression.
    def visitOperationExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#ParenExpression.
    def visitParenExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#NumberExpression.
    def visitNumberExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#operation.
    def visitOperation(self, ctx):
        return self.visitChildren(ctx)


