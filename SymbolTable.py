from AST import *

class SymbolObject:
    def __init__(self, type, name, constness):
        self.type = type
        self.name = name
        self.constness = constness

    def getObject(self):
        return self

class SymbolObjectPointer:
    def __init__(self, type, name, constness, objectConst, pointsTo=None):
        self.type = type
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

class SymbolTable():
    def __init__(self, root, parent=None):
        self.SymbolList = {}
        self.parent = parent
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
            elif type(node.nodes[0]) is ASTDataType:
                self.variableDeclaration(node.nodes[0],True)
            else:
                print("huh")
        elif self.IsVariableDeclarationSameTypes(node):
            self.variableDeclaration(node)
        # asignment
        elif self.IsVariableAssignmentSameTypes(node):
            self.variableAssignment(node)
        #pointer declaration bv: int* b ( = a)
        elif self.IsPointerDeclaration(node):
            self.pointerDeclaration(node)
        #pointer varible assignment (sets te variable where to pointer is pointing at) bv: *b = a of *b = 10;
        elif self.IsPointerVariableAssignment(node):
            self.pointerAssignment(node)
        #set a pointer to another pointer bv: a = b
        elif self.IsPointerAssignment(node):
            self.pointerAssignment(node)
        #check for unassigned variables in bodies
        elif self.IsBody(node):
            self.checkBody(node)
        elif self.IsScope(node):
            SymbolTable(node, self)
        else:
            self.loopAST(node)

    def pointerDeclaration(self, node, constness=False):
        objectConstness = False
        pointerType = node.nodes[0].root
        if type(node.getSetObject()) is ASTConst:
            objectConstness = True
            pointerName = node.getSetObject().nodes[0].getVariableName()
        else:
            pointerName = node.getSetObject().getVariableName()

        if pointerName in self.SymbolList:
            exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + ". Redefinition of variable: \'" +
                node.nodes[0].root + "\'.")

        object = node.getToObject()
        pointerObject = None
        if isinstance(object, ASTAdress):
            self.searchVariable(object)
            toObject = self.searchVariable(object)
            pointerObject = SymbolObjectPointer(pointerType, pointerName, constness, objectConstness,toObject)
        elif isinstance(object, ASTVariable):
            pointerObject = self.searchVariable(object)
        elif object == None:
            pointerObject = SymbolObjectPointer(pointerType, pointerName, constness, objectConstness)
        else:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +". Variable: \'" + pointerName + "\' invalid conversion from 'idk' to 'idk*'.")

        self.SymbolList[pointerName] = pointerObject

    def pointerAssignment(self, node):
        var = node.getSetObject()
        self.searchVariable(var)

        newValue = node.getToObject()

        pointsToObject = var.getVariableName()
        if self.searchVariable(newValue).type != self.SymbolList[pointsToObject].type:
            print("[Warning] line: " + str(node.line) + ", position: " + str(
                node.position) + ". Implicit conversion from '" + str(self.SymbolList[pointsToObject].getObject().type) + "' to " + str(
                self.searchVariable(var).type) + ". ")

        var = node.getSetObject()
        self.searchVariable(var)




    def variableDeclaration(self, node, constness=False):
        variable = node.nodes[0].root
        #check if variablename exists -> error
        if variable in self.SymbolList:
            exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + ". Redefinition of variable: \'" + node.nodes[0].root + "\'.")

        if isinstance(node.nodes[0], ASTAdress):
            self.searchVariable(node.nodes[1])
        else:
            if type(node.nodes[1]) is ASTVariable:
                if not self.searchVariable(node.nodes[1]).type is node.root:
                    print("[Warning] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". Implicit conversion from " + str(
                        self.searchVariable(node.nodes[1]).type) + " to " + str(
                        node.root) + ". ")
            else:
                node.nodes[1].correctDataType(node.root)
        self.SymbolList[variable] = SymbolObject(node.root,variable,constness)

    def variableAssignment(self, node):
        if(self.searchVariable(node).constness):
            exit("[Error] line: " + str(node.line) + ", position: " + str(
                node.position) + " variable: \'" + node.root + "\' is of const-type and cannot be changed.")

        #als het 2 pointers zijn bv: a = b
        if(type(node.nodes[0]) is ASTVariable and type(self.searchVariable(node)) == SymbolObjectPointer and type(self.searchVariable(node.nodes[0])) == SymbolObjectPointer):
            self.searchVariable(node).setPointer(self.searchVariable(node.nodes[0]), node)
        #als er een waarde word gezet bv: *a = 10
        elif type(node.nodes[0]) is ASTAdress:
            adress = node.nodes[0]
            self.searchVariable(node).setPointer(self.searchVariable(adress), node)
        else:
            node.nodes[0].correctDataType(self.searchVariable(node).type)
            self.searchVariable(node)

    def checkBody(self, root):
        if type(root) is ASTVariable:
            self.searchVariable(root)
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                self.checkBody(node)

    def checkUnusedVariables(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                self.checkUnusedVariables(node)

    def searchVariable(self, node):
        if type(node) is not ASTVariable and type(node) is not ASTAdress:
            return None
        varName = node.getVariableName()
        if varName in self.SymbolList:
            return self.SymbolList[varName]
        elif self.parent is None:
            exit("[Error] line: " + str(node.line) + ", position: " + str(
                node.position) + ". Variable: \'" + varName + "\' has not been declared.")
            return None
        else:
            return self.parent.searchVariable(node)

    @staticmethod
    def IsVariableDeclarationSameTypes(node):
        return type(node) is ASTDataType

    @staticmethod
    def IsVariableAssignmentSameTypes(node):
        return type(node) is ASTVariable and node.nodes is not None

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
    def IsBody(node):
        return type(node) is ASTOperator

    @staticmethod
    def IsScope(node):
        return type(node) is ASTScope