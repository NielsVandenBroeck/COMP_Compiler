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


    # Visit a parse tree produced by grammar1Parser#function.
    def visitFunction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#params.
    def visitParams(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#param.
    def visitParam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#IfStatement.
    def visitIfStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#WhileLoop.
    def visitWhileLoop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#ForLoop.
    def visitForLoop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#EmptyScope.
    def visitEmptyScope(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#line.
    def visitLine(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#LValueRvalue.
    def visitLValueRvalue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#LValue.
    def visitLValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#Expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#Printf.
    def visitPrintf(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#Scanf.
    def visitScanf(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#OneTokenStatement.
    def visitOneTokenStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#ReturnKeyword.
    def visitReturnKeyword(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#FunctionForwardDeclaration.
    def visitFunctionForwardDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#printBodies.
    def visitPrintBodies(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#printBody.
    def visitPrintBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#scanVariables.
    def visitScanVariables(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#scanVariable.
    def visitScanVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#multiAssignmentsDeclarations.
    def visitMultiAssignmentsDeclarations(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#multideclarations.
    def visitMultideclarations(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#multideclaration.
    def visitMultideclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#lvalue.
    def visitLvalue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#rvalue.
    def visitRvalue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#variableAdress.
    def visitVariableAdress(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#dataType.
    def visitDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#body.
    def visitBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#functionCall.
    def visitFunctionCall(self, ctx):
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


    # Visit a parse tree produced by grammar1Parser#PointerValueExpression.
    def visitPointerValueExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#VariableExpression.
    def visitVariableExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#VariableExpressionIdentifier.
    def visitVariableExpressionIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#identifierOP.
    def visitIdentifierOP(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#negation.
    def visitNegation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#operation.
    def visitOperation(self, ctx):
        return self.visitChildren(ctx)


