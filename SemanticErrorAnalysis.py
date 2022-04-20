from AST import *

class SemanticErrorAnalysis:
    def __init__(self, root):
        self.variables = {}
        self.loopAST(root)
        self.checkOneTokenStatements(root)
        self.checkReturnKeyword(root)
        self.deleteUnusedVars(root)

    def loopAST(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                if type(node) is ASTVariable:
                    self.variables[node.root] = self.variables.get(node.root,0) + 1
                self.loopAST(node)

    def checkOneTokenStatements(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                if type(node) is ASTOneTokenStatement:
                    exit("[Error] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". " + node.root+" statement not in a loop.")
                elif type(node) is ASTWhile:
                    continue
                else:
                    self.checkOneTokenStatements(node)

    def checkReturnKeyword(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                if type(node) is ASTReturn:
                    exit("[Error] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". " + node.root+" return keyword not in a function.")
                elif type(node) is ASTFunction:
                    continue
                else:
                    self.checkReturnKeyword(node)

    def deleteUnusedVars(self, root):
        if root.nodes is None:
            return
        deleteNodes = []
        for node in root.nodes:
            if node is not None:
                if type(node) is ASTParameters:
                    continue
                if type(node) is ASTVariable and self.variables[node.root] == 1:
                    print("[Warning] line: " + str(node.line) + ", position: " + str(node.position) + ". Variable: \'" + node.root + "\' is never used.")
                    deleteNodes.append(node)
                    return True
                elif self.deleteUnusedVars(node) and type(node) is not ASTScope:
                    deleteNodes.append(node)
                    return True
        goodNodes = []
        for node in root.nodes:
            if node not in deleteNodes:
                goodNodes.append(node)
        root.nodes[:] = [node for node in goodNodes]




