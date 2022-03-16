from AST import *


class SymbolObject:
    def __init__(self, type, name, constness, value=0):
        self.type = type
        self.name = name
        self.constness = constness
        self.value = value


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
            self.variableDeclaration(node.nodes[0],True)
        elif type(node) is ASTDataType:
            self.variableDeclaration(node)

        #asignment
        if type(node) is ASTVariable:
            self.variableAssignment(node)

    def variableDeclaration(self, node, constness=False):
        variable = node.nodes[0].root
        #check if variablename exists -> error
        for existingVar in self.SymbolList:
            if existingVar == variable:
                exit("[Error] line (#todo): Cannot declare variable: \"" + existingVar + "\" more than once.")
        if len(node.nodes) == 1:
            result = 0
        else:
            value = node.nodes[1]
            value.constantFold()
            result = value.root
        self.SymbolList[variable] = SymbolObject(node.root,variable,constness, result)

    def variableAssignment(self, node):
        Exists = False
        for existingVar in self.SymbolList:
            if existingVar == node.root:
                Exists = True
                break
        if not Exists:
            exit("[Error] line (#todo): variable: \"" + node.root + "\" has not been declared.")
        self.SymbolList[node.root].value = node.nodes[0].root