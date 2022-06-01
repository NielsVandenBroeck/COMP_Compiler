from AST import ASTScope, ASTVariable, ASTDataType, AST, ASTParameters, ASTFunction

number = 0

class ASTFixScoping:
    def __init__(self,scope, parantScope = None):
        self.symbolTable = {}
        self.parantScope = parantScope
        self.isGlobal = False
        if type(scope) == AST:
            self.isGlobal = True

        if type(scope) == ASTScope or type(scope) == ASTFunction:
            for node in scope.nodes:
                self.preOrderTraverse(node)
        else:
            self.preOrderTraverse(scope)


    def checkAndReplaceVariable(self, varible):
        if type(varible) != ASTVariable:
            exit("wrong type not a ASTVariable")
        varible.root = self.getMostCorrectName(varible.root)


    def createVarible(self, varible):
        if type(varible) != ASTDataType:
            exit("wrong type not a ASTDataType")
        if self.checkIfNameExists(varible.getVariableName()):
            global number
            self.symbolTable[varible.getVariableName()] = varible.getVariableName() + "scope" + str(number)
            varible.nodes[0].root = varible.getVariableName() + "scope" + str(number)
            number += 1
        else:
            self.symbolTable[varible.getVariableName()] = varible.getVariableName()

        if self.isGlobal:
            self.symbolTable[varible.getVariableName()] = '@' + varible.nodes[0].root
            varible.nodes[0].root = '@' + varible.nodes[0].root

    def getMostCorrectName(self, varName):
        if varName in self.symbolTable:
            return self.symbolTable[varName]
        elif self.parantScope != None:
            return self.parantScope.getMostCorrectName(varName)
        exit("name not found " + varName)

    def checkIfNameExists(self, varName):
        if varName in self.symbolTable:
            return True
        elif self.parantScope != None:
            return self.parantScope.checkIfNameExists(varName)
        return False

    def preOrderTraverse(self, ast):
        if not type(ast) == ASTScope and not type(ast) == ASTFunction and not type(ast) == ASTVariable and not (type(ast) == ASTDataType) and ast.nodes != None:
            for node in ast.nodes:
                self.preOrderTraverse(node)
        elif type(ast) == ASTScope or type(ast) == ASTFunction:
            ASTFixScoping(ast, self)
        elif type(ast) == ASTVariable:
            self.checkAndReplaceVariable(ast)
        elif type(ast) == ASTDataType and ast.nodes != None:
            self.createVarible(ast)
        return


