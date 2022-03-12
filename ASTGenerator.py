from AST import AST
from grammar1Visitor import *
import operator

class variableTable:
    def __init__(self,type,name,constness, value=None):
        self.type = type
        self.name = name
        self.value = value
        self.constness = constness


class ASTGenerator(grammar1Visitor):
    def __init__(self):
        self.variableList = []

    # Visit a parse tree produced by grammar1Parser#start.
    def visitStart(self, ctx):
        program = AST("program", "")
        for line in ctx.getChildren():
            program.addNode(self.visitProgramLine(line))
        #program.constantFold()
        return program

    def visitProgramLine(self, ctx):
        line = AST("line", "")
        line.addNode(self.visitChildren(ctx.l))
        return line

    # Visit a parse tree produced by grammar1Parser#DeclarationExpression.
    def visitDeclarationExpression(self, ctx):
        constness = False
        if ctx.constness is not None:
            constness = True
        name = ctx.name.text

        #check if variable exists -> error
        for var in self.variableList:
            if(var.name is name):
                print("Error, cannot declare variable: \""+name+"\" more than once.")
                break

        #create variable and push to list
        newVariable = variableTable(ctx.t.getText(),name,constness)
        self.variableList.append(newVariable)
        return AST(name, "var")

    # Visit a parse tree produced by grammar1Parser#DeclarationAndInitalizationExpression.
    def visitDeclarationAndInitalizationExpression(self, ctx):
        constness = False
        if ctx.constness is not None:
            constness = True
        type = ctx.t.getText()
        name = ctx.name.text
        value = self.visit(ctx.b)

        # check if variable exists -> error
        for var in self.variableList:
            if (var.name is name):
                print("Error, cannot declare variable: \""+name+"\" more than once.")
                break

        # create variable and push to list
        newVariable = variableTable(type, name, constness, value.value)
        self.variableList.append(newVariable)
        root = AST(name,"var")
        child1 = AST("=","")
        child2 = value
        root.addNode(child1)
        child1.addNode(child2)
        return root

    # Visit a parse tree produced by grammar1Parser#DeclarationAndInitalizationPointerExpression.
    def visitDeclarationAndInitalizationPointerExpression(self, ctx):
        #todo constness for value (not for pointer)
        constness = False
        if ctx.constness is not None:
            constness = True
        type = ctx.t.getText()
        name = ctx.var1.text
        #todo value moet address zijn
        value = ctx.var2.text

        # check if variable 1 exists -> error
        # check if variable 2 exists, else -> error
        var2exists = False
        for var in self.variableList:
            if var.name is name:
                print("Error, cannot declare variable: \""+name+"\" more than once.")
                break
            if var.name is value:
                var2exists = True
        if not var2exists:
            print("Error, variable in initialization: \""+value+"\"  does not exists")

        # create variable and push to list
        newVariable = variableTable(type, name, constness, value)
        self.variableList.append(newVariable)
        root = AST(name,"var")
        child1 = AST("=","")
        child2 = AST(value,"")
        root.addNode(child1)
        child1.addNode(child2)
        return root

    # Visit a parse tree produced by grammar1Parser#InitalizationExpression.
    def visitInitalizationExpression(self, ctx):
        name = ctx.name.text
        # check if variable exists, else -> error
        exists = False
        for var in self.variableList:
            if var.name is name:
                # check if variable is const-type
                if var.constness:
                    print("Error, Cannot assign to variable: \"" + name + "\" with const-qualified type.")
                exists = True
                break
        if not exists:
            print("Error, variable: \""+name+"\" doesnt exist.")
        root = AST(name,"")
        child1 = AST("=","")
        child2 = self.visit(ctx.b)
        root.addNode(child1)
        child1.addNode(child2)
        return root

    # Visit a parse tree produced by grammar1Parser#InitalizationPointerExpression.
    def visitInitalizationPointerExpression(self, ctx):
        name = ctx.var1.text
        value = ctx.var2.text
        # check if initialization variable exists, else -> error
        # check if variable exists, else -> error
        var1Exists = False
        var2Exists = False
        for var in self.variableList:
            if var.name is name:
                # check if variable is const-type
                if var.constness:
                    print("Error, Cannot assign to variable: \"" + name + "\" with const-qualified type.")
                var1Exists = True
            if var.name is value:
                var2Exists = True
        if not var1Exists:
            print("Error, variable: \""+name+"\" doesnt exist.")
        if not var2Exists:
            print("Error, variable in initialization: \""+value+"\" does not exists")
        root = AST(name,"var")
        child1 = AST("=","")
        child2 = AST(value,"")
        root.addNode(child1)
        child1.addNode(child2)
        return root

    # Visit a parse tree produced by grammar1Parser#IdentifierOperationExpression.
    def visitIdentifierOperationExpression(self, ctx):
        name = ctx.name.text
        # check if variable exists, else -> error
        exists = False
        for var in self.variableList:
            if (var.name is name):
                # check if variable is const-type
                if var.constness:
                    print("Error, Cannot assign to variable: \"" + name + "\" with const-qualified type.")
                exists = True
                break
        if not exists:
            print("Error, variable: \""+name+"\" doesnt exist.")
        operation = ctx.op.getText()
        root = AST(operation,"")
        child = AST(name,"")
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
        if node2.value in dict1 and dict1[node2.value] < dict1[rootnode.value] and len(node2.nodes) > 1 and node2.type != "paren":
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
            if (var.name is variable):
                exists = True
                break
        if not exists:
            print("Error, variable: \""+variable+"\" doesnt exist.")
        return AST(variable, "")

    # Visit a parse tree produced by grammar1Parser#operation.
    def visitOperation(self, ctx):
        operation = ctx.getText()
        return AST(operation, "op")