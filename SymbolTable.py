from AST import *


class SymbolObject:
    def __init__(self, type, name, constness, value=None):
        self.type = type
        self.name = name
        self.constness = constness
        self.value = value


class SymbolTable():
    def __init__(self, root):
        self.variableList = {}
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

        #initialization
        if type(node) is ASTVariable:
            #check if variablename already exists -> error
            print(node.root)

    def variableDeclaration(self, node, constness=False):
        datatype = node.root
        variable = node.nodes[0].root
        #check if variablename exists -> error
        for existingVar in self.variableList:
            if existingVar.name == variable:
                exit("[Error] line (#todo): Cannot declare variable: \"" + existingVar.name + "\" more than once.")
                break;


        #constant fold
        value = node.nodes[0].nodes[0].root