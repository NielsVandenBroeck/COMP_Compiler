from AST import *

class SemanticErrorAnalysis:
    def __init__(self, root):
        self.variables = {}
        self.loopAST(root)
        self.deleteUnusedVars(root)

    def loopAST(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                if type(node) is ASTVariable:
                    self.variables[node.root] = self.variables.get(node.root,0) + 1
                self.loopAST(node)

    def deleteUnusedVars(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                if type(node) is ASTVariable and self.variables[node.root] == 1:
                    print("[Warning] line: " + str(node.line) + ", position: " + str(node.position) + ". Variable: \'" + node.root + "\' is never used.")
                    root.nodes.remove(node)
                    return True
                elif self.deleteUnusedVars(node):
                    root.nodes.remove(node)
                    return True



