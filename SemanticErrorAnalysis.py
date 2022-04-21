from AST import *

class SemanticErrorAnalysis:
    def __init__(self, root):
        self.variables = {}
        self.loopAST(root)
        self.checkFunctions(root)
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

    def checkFunctions(self, root, foundMain=False):
        functionNames = []
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                if type(node) is ASTFunction:
                    if node.nodes[1].root in functionNames:
                        exit("[Error] line: " + str(node.line) + ", position: " + str(
                            node.position) + ". Redefinition of function: '" + node.nodes[1].root + "'.")
                    else:
                        functionNames.append(node.nodes[1].root)
                    if node.nodes[1].root == "main":
                        foundMain = True
        if not foundMain:
            exit("[Error] No main function found.")


    def checkOneTokenStatements(self, root, inLoop=False):
        if root.nodes is None:
            return
        for i in range(len(root.nodes)):
            node = root.nodes[i]
            if node is not None:
                if type(node) is ASTOneTokenStatement and inLoop:
                    del root.nodes[i+1:len(root.nodes)]
                    break
                elif type(node) is ASTOneTokenStatement and not inLoop:
                    exit("[Error] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". " + node.root+" statement not in a loop.")
                elif type(node) is ASTWhile:
                    self.checkOneTokenStatements(node, True)
                else:
                    self.checkOneTokenStatements(node, inLoop)

    def checkReturnKeyword(self, root, inFunction=False):
        if root.nodes is None:
            return
        for i in range(len(root.nodes)):
            node = root.nodes[i]
            if node is not None:
                if type(node) is ASTReturn and inFunction:
                    del root.nodes[i+1:len(root.nodes)]
                    break
                elif type(node) is ASTReturn and not inFunction:
                    exit("[Error] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". return keyword not in a function.")
                elif type(node) is ASTFunction:
                    self.checkReturnKeyword(node, True)
                else:
                    self.checkReturnKeyword(node, inFunction)

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
                elif self.deleteUnusedVars(node):
                    if type(root) is ASTScope or type(root) is AST:
                        deleteNodes.append(node)
                    else:
                        return True

        goodNodes = []
        for node in root.nodes:
            if node not in deleteNodes:
                goodNodes.append(node)
        root.nodes[:] = [node for node in goodNodes]




