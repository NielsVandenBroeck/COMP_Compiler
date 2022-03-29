from AST import *

class SymbolObject:
    def __init__(self, type, name, constness, value=None):
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
    def __init__(self, name, constness, objectConst, pointsTo=0):
        self.constness = constness
        self.objectConst = objectConst
        self.object = pointsTo
        self.name = name

    def getObject(self):
        if type(self.object) == SymbolObjectPointer:
            return self.object.getObject()
        return self.object

    # set value of real adress (not pointer)
    def setPointer(self,object, node):
        print("set pointer")
        if not self.constness:
            self.object = object
        else:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +" variable: \'" + node.root + "\' is of const-type and cannot be changed.")

    #set value of real adress (not pointer)
    def setValue(self, value, node):
        if self.objectConst:
            exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + " variable: \'" + self.name + "\' is of const-type and is not assignable.")
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
                self.visitChild(node)

    def visitChild(self, node):
        #declaration
        if type(node) is ASTConst:
            if type(node.nodes[0]) is ASTPointer:
                self.pointerDeclaration(node.nodes[0],True)
            elif type(node.nodes[0]) is ASTVariable:
                self.variableDeclaration(node.nodes[0],True)
            else:
                exit("FOUT kan object kan niet const zijn")
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
        #printf vb: printf(4+a-9)
        elif self.IsPrintFunction(node):
            self.PrintFunction(node)

    def pointerDeclaration(self, node, constness=False):
        pointer = node

        objectConstness = False
        if type(node.getSetObject()) is ASTConst:
            objectConstness = True
            pointerName = node.getSetObject().nodes[0].getVariableName()
        else:
            pointerName = node.getSetObject().getVariableName()

        self.ExistsError(pointerName, "already exists", node)
        object = node.getToObject()
        pointerObject = None
        if isinstance(object, ASTAdress):
            self.notExistsError(object.getVariableName(), "varible not found", node)
            toObject = self.SymbolList[object.getVariableName()]
            pointerObject = SymbolObjectPointer(pointerName, constness, objectConstness, toObject)
        elif isinstance(object, ASTVariable):
            self.notExistsError(object.getVariableName(), "pointer not found", node)
            pointerObject = self.SymbolList[object.getVariableName()]
        elif object == None:
            pointerObject = SymbolObjectPointer(pointerName, constness, objectConstness)
        else:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +". Variable: \'" + pointerName + "\' invalid conversion from 'idk' to 'idk*'.")


        self.SymbolList[pointerName] = pointerObject

    def pointerAssignment(self, node):
        var = node.getSetObject()
        varName = var.getVariableName()
        if not varName in self.SymbolList:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +". Variable: \'" + varName + "\' has not been declared.")

        newValue = node.getToObject()
        self.replaceVariables(newValue)
        pointsToObject = node.getSetObject().getVariableName()
        newValue.correctDataType(self.SymbolList[pointsToObject].getObject().type) #TODO simplify other function to fold!!!
        self.SymbolList[pointsToObject].setValue(newValue.root, node)

    def variableDeclaration(self, node, constness=False):
        variable = node.nodes[0].root
        #check if variablename exists -> error
        if variable in self.SymbolList:
            exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + ". Redefinition of variable: \'" + node.nodes[0].root + "\'.")

        if len(node.nodes) == 1:
            result = None
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
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +". Variable: \'" + node.root + "\' has not been declared.")

        #als het 2 pointers zijn bv: a = b
        if(type(node.nodes[0]) is ASTVariable and type(self.SymbolList[node.root]) == SymbolObjectPointer and type(self.SymbolList[node.nodes[0].getVariableName()]) == SymbolObjectPointer):
            self.SymbolList[node.root].setPointer(self.SymbolList[node.nodes[0].getVariableName()], node)
        #als er een waarde word gezet bv: *a = 10
        elif type(node.nodes[0]) is ASTAdress:
            adress = node.nodes[0]
            self.notExistsError(adress.getVariableName(), "Varible not found", node)
            self.SymbolList[node.root].setPointer(self.SymbolList[adress.getVariableName()], node)
        else:
            self.replaceVariables(node.nodes[0])
            node.nodes[0].correctDataType(self.SymbolList[node.root].type)
            self.SymbolList[node.root].setValue(node.nodes[0].root, node)

    def PrintFunction(self, node):
        self.replaceVariables(node.nodes[0])


    def replaceVariables(self, node):
        if type(node) is ASTPointer:
            if node.nodes[0].root in self.SymbolList:
                node.root = self.SymbolList[node.nodes[0].root].getValue()
                node.nodes = None
                return node.root
            else:
                exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + ". Variable: \'" + node.root + "\' has not been declared.")

        elif type(node) is ASTVariable:
            #search for variable in table
            if node.root in self.SymbolList:
                node.root = self.SymbolList[node.root].getValue()
                if node.root is None:
                    print("[Warning] line: "+ str(node.line) +", position: "+ str(node.position) +". Use of uninitialized variable. Replacing Value to 0.")
                    node.root = 0
                return node.root
            else:
                exit("[Error] line: " + str(node.line) + ", position: " + str(
                    node.position) + ". Variable: \'" + node.root + "\' has not been declared.")

        else:
            if node.nodes is None:
                return
            for child in node.nodes:
                self.replaceVariables(child)

    def checkUnusedVariables(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                ##print(node.root)
                self.checkUnusedVariables(node)

    def notExistsError(self, varName, message, node):
        if varName not in self.SymbolList:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +". Variable: \'" + node.root + "\' cannot be declared:" + message)

    def ExistsError(self, varName, message, node):
        if varName in self.SymbolList:
            exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + ". Variable: \'" + node.root + "\' cannot be declared:" + message)

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
    @staticmethod
    def IsPrintFunction(node):
        return type(node) is ASTPrintf