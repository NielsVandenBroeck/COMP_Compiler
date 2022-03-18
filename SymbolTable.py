from AST import *

class SymbolObject:
    def __init__(self, type, name, constness, value=0):
        self.type = type
        self.name = name
        self.constness = constness
        self.value = value

    def getObject(self):
        return self

    def setValue(self, value, node):
        if not self.constness:
            self.value = value
        else:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +" variable: \'" + self.name + "\' is of const-type and cannot be changed.")

    def getValue(self):
        return self.value

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
    def setPointer(self,node):
        if not self.constness:
            self.object = object
        else:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +" variable: \'" + self.name + "\' is of const-type and cannot be changed.")

    #set value of real adress (not pointer)
    def setValue(self, value, node):
        self.object.setValue(value, node)

    def getValue(self):
        return self.object.getValue()

class SymbolTable():
    def __init__(self, root):
        self.SymbolList = {}
        self.loopAST(root)

    def loopAST(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                self.visitChild(node.nodes[0])

    def visitChild(self, node):
        #declaration
        if type(node) is ASTConst:
            if type(node.nodes[0]) is ASTPointer:
                self.pointerDeclaration(node.nodes[0],True)
            else:
                self.variableDeclaration(node.nodes[0],True)
        elif self.IsVariableDeclarationSameTypes(node):
            self.variableDeclaration(node)

        # asignment
        if self.IsVariableAssignmentSameTypes(node):
            self.variableAssignment(node)

        #pointer declaration bv: int* b ( = a)
        if self.IsPointerDeclaration(node):
            self.pointerDeclaration(node)
        #pointer varible assignment (sets te variable where to pointer is pointing at) bv: *b = a of *b = 10;
        elif self.IsPointerVariableAssignment(node):
            self.pointerAssignment(node)
        #set a pointer to another pointer bv: a = b
        elif self.IsPointerAssignment(node):
            self.pointerAssignment(node)

    def pointerDeclaration(self, node, constness=False):
        pointer = node
        pointerName = node.getSetObject().getVariableName()

        self.ExistsError(pointerName, "already exists",node)
        object = node.getToObject()
        pointerObject = None
        if isinstance(object, ASTAdress):
            self.notExistsError(object.getVariableName(), "variable not found")
            toObject = self.SymbolList[object.getVariableName()]
            pointerObject = SymbolObjectPointer(pointerName, constness, toObject)
        elif isinstance(object, ASTVariable):
            self.notExistsError(object.getVariableName(), "pointer not found")
            pointerObject = self.SymbolList[object.getVariableName()]
        elif object == None:
            pointerObject = SymbolObjectPointer(pointerName, constness, 0)
        else:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +" variable: \'" + pointerName + "\' invalid conversion from 'idk' to 'idk*'.")


        self.SymbolList[pointerName] = pointerObject

    def pointerAssignment(self, node):
        var = node.getSetObject()
        varName = var.getVariableName()
        if not varName in self.SymbolList:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +" variable: \'" + varName + "\' has not been declared.")

        newValue = node.getToObject()
        self.replaceVariables(newValue)
        pointsToObject = node.getSetObject().getVariableName()
        newValue.correctDataType(self.SymbolList[pointsToObject].getObject().type) #TODO simplify other function to fold!!!
        self.SymbolList[pointsToObject].setValue(newValue, node)

    def variableDeclaration(self, node, constness=False):
        variable = node.nodes[0].root
        #check if variablename exists -> error
        if variable in self.SymbolList:
            exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + " Cannot declare variable: \'" + self.name + "\' more than once.")

        if len(node.nodes) == 1:
            result = 0
        else:
            if isinstance(node.nodes[0], ASTAdress):
                value = self.SymbolList[node.nodes[1].getVariableName()]
                result = value
            else:
                value = node.nodes[1]
                self.replaceVariables(value)
                value.correctDataType(node.root)
                result = value.root
        self.SymbolList[variable] = SymbolObject(node.root,variable,constness, result)

    def variableAssignment(self, node):
        if not node.root in self.SymbolList:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +" variable: \'" + node.root + "\' has not been declared.")

        #als het 2 pointers zijn bv: a = b
        if(type(node.nodes[0]) is ASTVariable and type(self.SymbolList[node.root]) == SymbolObjectPointer and type(self.SymbolList[node.nodes[0].getVariableName()]) == SymbolObjectPointer):
            self.SymbolList[node.root] = self.SymbolList[node.nodes[0].getVariableName()]
        #als er een waarde word gezet bv: *a = 10
        elif type(node.nodes[0]) is ASTAdress:
            adress = node.nodes[0]
            self.notExistsError(adress.getVariableName(), "variable not found")
            self.SymbolList[node.root] = self.SymbolList[adress.getVariableName()]
        else:
            self.replaceVariables(node.nodes[0])
            node.nodes[0].correctDataType(self.SymbolList[node.root].type)
            self.SymbolList[node.root].setValue(node.nodes[0].root, node)

    def replaceVariables(self, node):
        if type(node) is ASTPointer:
            if node.nodes[0].root in self.SymbolList:
                node.root = self.SymbolList[node.nodes[0].root].getValue()
                node.nodes = None
                return node.root
            else:
                exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + " variable: \'" + self.name + "\' has not been declared.")

        elif type(node) is ASTVariable:
            #search for variable in table
            if node.root in self.SymbolList:
                node.root = self.SymbolList[node.root].getValue()
                return node.root
            else:
                exit("[Error] line: " + str(node.line) + ", position: " + str(
                    node.position) + " variable: \'" + self.name + "\' has not been declared.")

        else:
            if node.nodes is None:
                return
            for child in node.nodes:
                self.replaceVariables(child)

    def notExistsError(self, varName, message, node):
        if varName not in self.SymbolList:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +" variable: \'" + self.name + "\' cannot be declared:" + message)

    def ExistsError(self, varName, message, node):
        if varName in self.SymbolList:
            exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + " variable: \'" + self.name + "\' cannot be declared:" + message)

    @staticmethod
    def IsVariableDeclarationSameTypes(node):
        return type(node) is ASTDataType

    @staticmethod
    def IsVariableAssignmentSameTypes(node):
        return type(node) is ASTVariable

    @staticmethod
    def IsPointerDeclaration(node):
        return type(node) is ASTPointer and type(node.getSetObject()) is not ASTVariable and type(node.getSetObject()) is not ASTAdress

    @staticmethod
    def IsPointerVariableAssignment(node):
        return type(node) is ASTPointer and type(node.getSetObject()) is ASTAdress

    @staticmethod
    def IsPointerAssignment(node):
        return type(node) is ASTPointer