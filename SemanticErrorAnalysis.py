from AST import *

class SemanticErrorAnalysis:
    def __init__(self, root):
        self.variables = {}
        self.loopAST(root)
        self.checkOneTokenStatements(root)
        self.deleteUnusedVars(root)

    def loopAST(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                if type(node) is ASTVariable:
                    self.variables[node.root] = self.variables.get(node.root,0) + 1
                self.loopAST(node)

    def checkOneTokenStatements(self, root, inLoop=False):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                if type(node) is ASTOneTokenStatement and not inLoop:
                    exit("[Error] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". " + node.root+" statement not in scope of a loop")
                elif type(node) is ASTWhile:
                    self.checkOneTokenStatements(node, True)
                else:
                    self.checkOneTokenStatements(node, inLoop)


    def deleteUnusedVars(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                if type(node) is ASTVariable and self.variables[node.root] == 1:
                    print("[Warning] line: " + str(node.line) + ", position: " + str(node.position) + ". Variable: \'" + node.root + "\' is never used.")
                    root.nodes.remove(node)
                    return True
                elif self.deleteUnusedVars(node) and type(node) is not ASTScope:
                    root.nodes.remove(node)
                    return True



