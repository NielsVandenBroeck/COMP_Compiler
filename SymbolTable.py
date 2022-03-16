from AST import *


class SymbolObject:
    def __init__(self, type, name, constness, value=0):
        self.type = type
        self.name = name
        self.constness = constness
        self.value = value

    def getObject(self):
        return self

class SymbolObjectPointer:
    def __init__(self, name, pointerConstness, pointsTo=0):
        self.pointerConstness = pointerConstness
        self.object = pointsTo
        self.name = name

    def getObject(self):
        if type(self.object) == SymbolObjectPointer:
            return self.object.getObject()
        return self.object

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
            self.variableDeclaration(node.nodes[0],True)
        elif type(node) is ASTDataType:
            self.variableDeclaration(node)

        #asignment
        if type(node) is ASTVariable:
            self.variableAssignment(node)

        if type(node) is ASTPointer:
            self.pointerDeclaration(node)

    def pointerDeclaration(self, node, constness=False):
        pointer = node
        pointerName = node.getSetObject().getVariableName()
        object = node.getToObject()
        #pointer = &variable
        if isinstance(object, ASTAdress):
            objectTo = self.SymbolList[object.getVariableName()]
            SymbolObjectPointer(pointerName, constness, objectTo)


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

        self.replaceVariables(node.nodes[0])
        node.nodes[0].correctDataType(self.SymbolList[node.root].type)
        self.SymbolList[node.root].value = node.nodes[0].root

    def replaceVariables(self, node):
        if type(node) is ASTVariable:
            #search for variable in table
            if node.root in self.SymbolList:
                node.root = self.SymbolList[node.root].value
                exists = True
            else:
                exit("[Error] line (#todo): variable: \"" + node.root + "\" has not been declared.")
        else:
            if node.nodes is None:
                return
            for child in node.nodes:
                self.replaceVariables(child)

    """
        def pointerDeclaration(self, node, constness=False):
            pointerName = node.nodes[0].root
            # check if variablename exists -> error
            for existingVar in self.SymbolList:
                if existingVar == variable:
                    exit("[Error] line (#todo): Cannot declare variable: \"" + existingVar + "\" more than once.")
            if len(node.nodes) == 1:
                result = 0
            else:
                value = node.nodes[1]
                self.replaceVariables(value)
                value.correctDataType(node.root)
                result = value.root
            self.SymbolList[variable] = SymbolObject(node.root, variable, constness, result)
    """