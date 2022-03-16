from AST import *

class SymbolObject:
    def __init__(self, type, name, constness, value=0):
        self.type = type
        self.name = name
        self.constness = constness
        self.value = value

    def getObject(self):
        return self

    def setValue(self, value):
        if not self.constness:
            self.value = value
        else:
            exit("[Error] line (#todo): variable: \"" + self.name + "\" is of const-type and cannot be changed.")

class SymbolObjectPointer:
    def __init__(self, name, constness, pointsTo=0):
        self.constness = constness
        self.object = pointsTo
        self.name = name

    def getObject(self):
        if type(self.object) == SymbolObjectPointer:
            return self.object.getObject()
        return self.object

    # set value of real adress (not pointer)
    def setPointer(self):
        if not self.constness:
            self.object = object
        else:
            exit("[Error] line (#todo): variable (pointer): \"" + self.name + "\" is of const-type and cannot be changed.")

    #set value of real adress (not pointer)
    def setValue(self, value):
        self.object.setValue(value)

class SymbolTable():
    def __init__(self, root):
        self.SymbolList = {}
        self.loopAST(root)

    def loopAST(self, root):
        for node in root.nodes:
            self.visitChild(node.nodes[0])

    def visitChild(self, node):
        #declaration
        if type(node) is ASTConst:
            if type(node.nodes[0]) is ASTPointer:
                self.pointerDeclaration(node.nodes[0],True)
            else:
                self.variableDeclaration(node.nodes[0],True)
        elif type(node) is ASTDataType:
            self.variableDeclaration(node)

        #asignment
        if type(node) is ASTVariable:
            self.variableAssignment(node)

        if type(node) is ASTPointer and type(node.getSetObject()) is not ASTVariable:
            #pointer declaration
            self.pointerDeclaration(node)
        elif type(node) is ASTPointer:
            self.pointerAssignment(node)

    def pointerDeclaration(self, node, constness=False):
        pointer = node
        pointerName = node.getSetObject().getVariableName()
        self.ExistsError(pointerName, "already exists")
        object = node.getToObject()
        pointerObject = None
        if isinstance(object, ASTAdress):
            self.notExistsError(object.getVariableName(), "varible not found")

            toObject = self.SymbolList[object.getVariableName()]
            pointerObject = SymbolObjectPointer(pointerName, constness, toObject)
        elif isinstance(object, ASTVariable):
            self.notExistsError(object.getVariableName(), "pointer not found")
            pointerObject = self.SymbolList[object.getVariableName()]
        elif object == None:
            pointerObject = SymbolObjectPointer(pointerName, constness, 0)
        else:
            exit("wrong pointer type: ", object)

        self.SymbolList[pointerName] = pointerObject

    def pointerAssignment(self, node):
        var = node.getSetObject()
        varName = var.getVariableName()
        if varName in self.SymbolList:
            if self.SymbolList[varName].constness:
                exit("[Error] line (#todo): variable: \"" + varName + "\" is of const-type and cannot be changed.")
        else:
            exit("[Error] line (#todo): variable: \"" + varName + "\" has not been declared.")

        newValue = node.getToObject()
        self.replaceVariables(newValue)
        pointsToObject = node.getSetObject().getVariableName()
        newValue.correctDataType(self.SymbolList[pointsToObject].getObject().type) #TODO simplify other function to fold!!!
        self.SymbolList[pointsToObject].setValue(newValue)

    def variableDeclaration(self, node, constness=False):
        variable = node.nodes[0].root
        #check if variablename exists -> error
        if variable in self.SymbolList:
            exit("[Error] line (#todo): Cannot declare variable: \"" + variable + "\" more than once.")

        if len(node.nodes) == 1:
            result = 0
        else:
            value = node.nodes[1]
            self.replaceVariables(value)
            value.correctDataType(node.root)
            result = value.root
        self.SymbolList[variable] = SymbolObject(node.root,variable,constness, result)

    def variableAssignment(self, node):

        if node.root in self.SymbolList:
            if self.SymbolList[node.root].constness:
                exit("[Error] line (#todo): variable: \"" + node.root + "\" is of const-type and cannot be changed.")
        else:
            exit("[Error] line (#todo): variable: \"" + node.root + "\" has not been declared.")

        #als het 2 pointers zijn
        if(type(node.nodes[0]) is ASTVariable and type(self.SymbolList[node.root]) == SymbolObjectPointer and type(self.SymbolList[node.nodes[0].getVariableName()]) == SymbolObjectPointer):
            self.SymbolList[node.root] = self.SymbolList[node.nodes[0].getVariableName()];
        else:
            self.replaceVariables(node.nodes[0])
            print("test", node.nodes[0].root, self.SymbolList[node.root].type)
            node.nodes[0].correctDataType(self.SymbolList[node.root].type)
            self.SymbolList[node.root].setValue(node.nodes[0].root)

    def replaceVariables(self, node):
        if type(node) is ASTVariable:
            print("let's gooooo")
            #search for variable in table
            if node.root in self.SymbolList:
                node.root = self.SymbolList[node.root].value
                return node.root
            else:
                exit("[Error] line (#todo): variable: \"" + node.root + "\" has not been declared.")
        else:
            if node.nodes is None:
                return
            for child in node.nodes:
                self.replaceVariables(child)

    def notExistsError(self, varName, message):
        if varName not in self.SymbolList:
            exit("[Error] line (#todo): Cannot declare variable: \"" + object.getVariableName() + "\"" + message)

    def ExistsError(self, varName, message):
        if varName in self.SymbolList:
            exit("[Error] line (#todo): Cannot declare variable: \"" + object.getVariableName() + "\"" + message)