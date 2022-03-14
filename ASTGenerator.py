from AST import AST
from grammar1Visitor import *
import operator


class ASTGenerator(grammar1Visitor):
    def __init__(self):
        self.variableList = []

    # Visit a parse tree produced by grammar1Parser#start.
    def visitStart(self, ctx):
        program = AST("program")
        for line in ctx.getChildren():
            program.addNode(self.visitProgramLine(line))
        return program

    def visitProgramLine(self, ctx):
        line = AST("line")
        line.addNode(self.visitChildren(ctx.l))
        return line

    # Visit a parse tree produced by grammar1Parser#LValueRvalue.
    def visitLValueRvalue(self, ctx):
        print("test")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by grammar1Parser#IdentifierOperationExpression.
    def visitIdentifierOperationExpression(self, ctx):
        name = ctx.name.text
        # check if variable exists, else -> error
        exists = False
        for var in self.variableList:
            if var.name == name:
                # check if variable is const-type
                if var.constness:
                    exit("[Error] line (#todo): Cannot assign to variable: \"" + name + "\" with const-qualified type.")
                exists = True
                break
        if not exists:
            exit("[Error] line (#todo): Variable: \""+name+"\" doesnt exist.")
        operation = ctx.op.getText()
        root = AST(operation)
        child = AST(name)
        root.addNode(child)
        return root


    # Visit a parse tree produced by grammar1Parser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        sign = ctx.sign.text
        value = self.visit(ctx.value)
        rootnode = AST(sign, "op")
        rootnode.addNode(value)

        # Constant Folding
        if isinstance(value.value, float):
            if sign == '-':
                rootnode = AST(float(-value.value), "")
            else : rootnode = AST(float(value.value), "")
        return rootnode

    # Visit a parse tree produced by grammar1Parser#OperationExpression.
    def visitOperationExpression(self, ctx):
        dict1 = {'||': 0, '&&': 1, '<': 2, '>': 2, '==': 2, '<=': 2, '>=': 2, '!=': 2, '+': 3, '-': 3, '*': 4, '/': 4, '%': 4}
        node1 = self.visit(ctx.lValue)
        node2 = self.visit(ctx.rValue)

        rootnode = self.visit(ctx.op)   #gaat naar visitOperation
        rootnode.addNode(node1)
        rootnode.addNode(node2)

        #len(node2.nodes) > 1 is voor unary getallen te onderscheiden van gewone
        if node2.root in dict1 and dict1[node2.root] < dict1[rootnode.root] and len(node2.root) > 1 and node2.type != "paren":
            tempNode2 = AST(rootnode.value, "op")
            tempNode2.addNode(rootnode.getNode(0))
            tempNode2.addNode(node2.getNode(0))

            tempRootNode = AST(node2.value, "op")
            tempRootNode.addNode(tempNode2)
            tempRootNode.addNode(node2.getNode(1))
            rootnode = tempRootNode

            node1 = tempNode2
            node2 = node2.getNode(1)
        elif node2.type == "paren":
            node2.type = None
        return rootnode

    # Visit a parse tree produced by grammar1Parser#ParenExpression.
    def visitParenExpression(self, ctx):
        rootnode = self.visit(ctx.value)
        rootnode.type = "paren"
        return rootnode

    # Visit a parse tree produced by grammar1Parser#IntExpression.
    def visitIntExpression(self, ctx):
        if ctx.getText()[0] == '!':
            tempNumber = int(ctx.getText()[1:len(ctx.getText())])
            if tempNumber:
                number = 0
            else: number = 1
        else: number = int(ctx.getText())
        return AST(number, "")

    # Visit a parse tree produced by grammar1Parser#FloatExpression.
    def visitFloatExpression(self, ctx):
        if ctx.getText()[0] == '!':
            tempNumber = float(ctx.getText()[1:len(ctx.getText())])
            if tempNumber:
                number = 0.0
            else: number = 1.0
        else: number = float(ctx.getText())
        return AST(number, "")

    # Visit a parse tree produced by grammar1Parser#CharExpression.
    def visitCharExpression(self, ctx):
        char = ctx.getText()
        return AST(char, "")

    # Visit a parse tree produced by grammar1Parser#VariableExpression.
    def visitVariableExpression(self, ctx):
        variable = ctx.getText()
        #check if variable exists
        exists = False
        for var in self.variableList:
            if var.name == variable:
                # error if variable is initialized yet
                if var.value is None:
                    exit("[Error] line (#todo): Variable: \"" + var.name + "\" has not been initialized yet.")
                #replace variable with its value
                if var.value.nodes is None:
                    return AST(var.value.value)
                return var.value
        exit("[Error] line (#todo): Variable: \""+variable+"\" doesnt exist.")

    # Visit a parse tree produced by grammar1Parser#operation.
    def visitOperation(self, ctx):
        operation = ctx.getText()
        return AST(operation, "op")

    # Visit a parse tree produced by grammar1Parser#lvalue.
    def visitLvalue(self, ctx):
        AST(ctx.t.getText(),  [AST(ctx.name.text)])

        if ctx.constness != None:
            return

        return self.visitChildren(ctx)

"""
    def correctDataType(self,ast,type):
        #ast.constantFold()
        if isinstance(ast.root,str):
            ast.root = ast.root[1]
        print(ast.root)
        if type == "float":
            if isinstance(ast.root, float) or isinstance(ast.root, int):
                ast.root = float(ast.root)
            else:
                ast.root = float(ord(ast.root))
        elif type == "int":
            if isinstance(ast.root, float) or isinstance(ast.root, int):
                ast.root = int(ast.root)
            else:
                ast.root = int(ord(ast.root))
        elif type == "char":
            if isinstance(ast.root,str):
                ast.root = '\''+ast.root+'\''
            else:
                ast.root = '\'' + chr(int((ast.root))) + '\''
        print(ast.root)"""