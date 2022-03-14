from AST import AST
from grammar1Visitor import *
import operator


class variableTable:
    def __init__(self, type, name, constness, node=None):
        self.type = type
        self.name = name
        self.constness = constness
        #AST node
        self.value = node



class ASTGenerator(grammar1Visitor):
    def __init__(self):
        self.variableList = []

    # Visit a parse tree produced by grammar1Parser#start.
    def visitStart(self, ctx):
        program = AST("program", "")
        for line in ctx.getChildren():
            program.addNode(self.visitProgramLine(line))
        program.constantFold()
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
            if var.name == name:
                exit("[Error] line (#todo): Cannot declare variable: \""+name+"\" more than once.")

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
            if var.name == name:
                exit("[Error] line (#todo): Cannot declare variable: \""+name+"\" more than once.")
                break

        # create variable and push to list
        newVariable = variableTable(type, name, constness, value)
        self.variableList.append(newVariable)
        root = AST(name,"var")
        child1 = AST("=","")
        root.addNode(child1)
        child1.addNode(value)
        self.correctDataType(value,type)
        return root

    # Visit a parse tree produced by grammar1Parser#DeclarationAndInitalizationPointerExpression.
    def visitDeclarationAndInitalizationPointerExpression(self, ctx):
        #todo constness for value (not for pointer)
        constness = False
        if ctx.constness is not None:
            constness = True

        type = ctx.t.getText()
        name = ctx.var1.text

        #Find var and set value to pointer for this var
        value = None
        for var in self.variableList:
            print("bestaande var", var)
            if var.name == ctx.var2.text:
                value = var
                print(value, "!=", var)

        if value == None:
            exit("[Error] line (#todo): Variable in initialization: \""+value.text+"\"  does not exists")

        print("Pointer to ", value)

        # check if variable 1 exists -> error
        # check if variable 2 exists, else -> error
        for var in self.variableList:
            if var.name == name:
                exit("[Error] line (#todo): Cannot declare variable: \""+name+"\" more than once.")
                break

        root = AST(name,"var")
        child1 = AST("=","")
        child2 = AST(value,"")

        # create variable and push to list
        newVariable = variableTable(type, name, constness, child2)
        self.variableList.append(newVariable)
        root.addNode(child1)
        child1.addNode(child2)
        return root

    # Visit a parse tree produced by grammar1Parser#PointerValueExpression.
    def visitPointerValueExpression(self, ctx):
        value = None
        print(self.variableList)
        print("zoeken: " , ctx.value.text)
        var2exists = False
        for var in self.variableList:
            if var.name == ctx.value.text:
                var2exists = True
                print("test", var.value.value.value.value)
                value = var.value.value.value.value
                #pointers van pointers
                while(isinstance(value, variableTable)):
                    print("test bruh")
                    value = value.value.value

        if not var2exists:
            exit("[Error] line (#todo): Variable in initialization: \"" + value.text + "\"  does not exists")

        return AST(value,"")

    # Visit a parse tree produced by grammar1Parser#InitalizationExpression.
    def visitInitalizationExpression(self, ctx):
        name = ctx.name.text
        datatype = None
        root = AST(name, "var")
        child1 = AST("=", "")
        child2 = self.visit(ctx.b)

        # check if variable exists, else -> error
        exists = False
        for var in self.variableList:
            if var.name == name:
                # check if variable is const-type
                if var.constness:
                    exit("[Error] line (#todo): Cannot assign to variable: \"" + name + "\" with const-qualified type.")
                exists = True
                datatype = var.type
                var.value = child2
                break
        if not exists:
            exit("[Error] line (#todo): Variable: \""+name+"\" doesnt exist.")

        root.addNode(child1)
        child1.addNode(child2)
        self.correctDataType(child2,datatype)
        return root

    # Visit a parse tree produced by grammar1Parser#InitalizationPointerExpression.
    def visitInitalizationPointerExpression(self, ctx):
        #TODO const
        name = ctx.var1.text

        varToSet = None
        value = None
        for var in self.variableList:
            if var.name == ctx.var2.text:
                value = var

        if value == None:
            exit("[Error] line (#todo): Variable in initialization: \"" + value.text + "\"  does not exists")

        for var in self.variableList:
            if var.name == ctx.var1.text:
                var.value = AST(value, "")
                print("value waarde", value)

        print("Pointer to xxxx ", value)

        # check if initialization variable exists, else -> error
        # check if variable exists, else -> error

        """
        var1Exists = False
        var2Exists = False
        for var in self.variableList:
            print("item", var.name)
            if var.name == name:
                # check if variable is const-type
                if var.constness:
                    exit("[Error] line (#todo): Cannot assign to variable: \"" + name + "\" with const-qualified type.")
                var1Exists = True
            if var.name == ctx.var2.text:
                var2Exists = True
        if not var1Exists:
            exit("[Error] line (#todo): Variable: \""+name+"\" doesnt exist.")
        if not var2Exists:
            exit("[Error] line (#todo): Variable in initialization: \""+value+"\" does not exists")"""


        root = AST(name,"var")
        child1 = AST("=","")
        child2 = AST(value,"var")

        root.addNode(child1)
        child1.addNode(child2)
        return root

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
            if var.name == variable:
                # error if variable is initialized yet
                if var.value is None:
                    exit("[Error] line (#todo): Variable: \"" + var.name + "\" has not been initialized yet.")
                #replace variable with its value
                if var.value.nodes is None:
                    return AST(var.value.value,"")
                return var.value
        exit("[Error] line (#todo): Variable: \""+variable+"\" doesnt exist.")

    # Visit a parse tree produced by grammar1Parser#operation.
    def visitOperation(self, ctx):
        operation = ctx.getText()
        return AST(operation, "op")

    def correctDataType(self,ast,type):
        ast.constantFold()
        if isinstance(ast.value,str):
            ast.value = ast.value[1]
        print(ast.value)
        if type == "float":
            if isinstance(ast.value, float) or isinstance(ast.value, int):
                ast.value = float(ast.value)
            else:
                ast.value = float(ord(ast.value))
        elif type == "int":
            if isinstance(ast.value, float) or isinstance(ast.value, int):
                ast.value = int(ast.value)
            else:
                ast.value = int(ord(ast.value))
        elif type == "char":
            if isinstance(ast.value,str):
                ast.value = '\''+ast.value+'\''
            else:
                ast.value = '\'' + chr(int((ast.value))) + '\''
        print(ast.value)