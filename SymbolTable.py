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
            self.replaceVariables(value)
            value.correctDataType(node.root)
            result = value.root
        self.SymbolList[variable] = SymbolObject(node.root,variable,constness, result)

    def variableAssignment(self, node):
        Exists = False
        for existingVar in self.SymbolList:
            if existingVar == node.root:
                if self.SymbolList[existingVar].constness:
                    exit("[Error] line (#todo): variable: \"" + node.root + "\" is of const-type and cannot be changed.")
                Exists = True
                break
        if not Exists:
            exit("[Error] line (#todo): variable: \"" + node.root + "\" has not been declared.")
        self.replaceVariables(node.nodes[0])
        node.nodes[0].correctDataType(self.SymbolList[node.root].type)
        self.SymbolList[node.root].value = node.nodes[0].root

    def replaceVariables(self, node):
        if type(node) is ASTVariable:
            #search for variable in table
            exists = False
            for existingVar in self.SymbolList:
                if existingVar == node.root:
                    node.root = self.SymbolList[existingVar].value
                    exists = True
                    break
            if not exists:
                exit("[Error] line (#todo): variable: \"" + node.root + "\" has not been declared.")
        else:
            if node.nodes is None:
                return
            for child in node.nodes:
                self.replaceVariables(child)

