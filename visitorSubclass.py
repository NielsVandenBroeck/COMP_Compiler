from AST import AST
from grammar1Visitor import *


class VisitorSubclass(grammar1Visitor):

    # Visit a parse tree produced by grammar1Parser#start.
    def visitStart(self, ctx):
        program = AST("program", "")
        print(ctx.getChildCount())
        for line in ctx.getChildren():
            program.addNode(self.visitProgramLine(line))
        return program

    def visitProgramLine(self, ctx):
        print("line")
        line = AST("line", "")
        line.addNode(self.visitChildren(ctx.line))
        return line

    # Visit a parse tree produced by grammar1Parser#leftOperationBody.
    def visitLeftOperationBody(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by grammar1Parser#unaryBody.
    def visitUnaryBody(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by grammar1Parser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        sign = ctx.sign.text
        value = self.visit(ctx.value)

        rootnode = AST(sign, "OP")
        rootnode.addNode(value)

        return rootnode

    # Visit a parse tree produced by grammar1Parser#OperationExpression.
    def visitOperationExpression(self, ctx):
        dict1 = {'+': 0, '-': 1, '*': 2, "/": 3}

        node1 = self.visit(ctx.lValue)
        node2 = self.visit(ctx.rValue)

        rootnode = self.visit(ctx.op)   #gaat naar visitOperation
        rootnode.addNode(node1)
        rootnode.addNode(node2)

        #TODO volgorde van bewerkingen controleren
        #len(node2.nodes) > 1 is voor unary getallen te onderscheiden van gewone
        if node2.value in dict1 and dict1[node2.value] < dict1[rootnode.value] and len(node2.nodes) > 1 and node2.type != "paren":
            print("test")
            tempNode2 = AST(rootnode.value, "op")
            tempNode2.addNode(rootnode.getNode(0))
            tempNode2.addNode(node2.getNode(0))

            tempRootNode = AST(node2.value, "op")
            tempRootNode.addNode(tempNode2)
            tempRootNode.addNode(node2.getNode(1))

            rootnode = tempRootNode
        elif node2.type == "paren":
            node2.type = None

        return rootnode

    # Visit a parse tree produced by grammar1Parser#ParenExpression.
    def visitParenExpression(self, ctx):
        rootnode = self.visit(ctx.value)
        rootnode.type = "paren"
        return rootnode

    # Visit a parse tree produced by grammar1Parser#NumberExpression.
    def visitNumberExpression(self, ctx):
        number = int(ctx.getText())
        return AST(number, "")

    # Visit a parse tree produced by grammar1Parser#operation.
    def visitOperation(self, ctx):
        operation = ctx.getText()
        return AST(operation, "op")