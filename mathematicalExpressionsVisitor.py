# Generated from ../grammars/mathematicalExpressions.g4 by ANTLR 4.9.3
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by mathematicalExpressionsParser.

class mathematicalExpressionsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mathematicalExpressionsParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematicalExpressionsParser#body.
    def visitBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematicalExpressionsParser#operation.
    def visitOperation(self, ctx):
        return self.visitChildren(ctx)


