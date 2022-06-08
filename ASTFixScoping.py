from AST import ASTScope, ASTVariable, ASTDataType, AST, ASTParameters, ASTFunction

number = 0

class ASTFixScoping:
    def __init__(self,scope, parantScope = None, isMips = False):
        self.symbolTable = {}
        self.parantScope = parantScope
        self.isGlobal = False
        self.isMips = isMips
        if type(scope) == AST:
            self.isGlobal = True

        if type(scope) == ASTScope or type(scope) == ASTFunction:
            if scope.nodes is not None:
                for node in scope.nodes:
                    self.preOrderTraverse(node)
        else:
            self.preOrderTraverse(scope)


    def checkAndReplaceVariable(self, variable):
        if type(variable) != ASTVariable:
            exit("wrong type not a ASTVariable")
        variable.root = self.getMostCorrectName(variable.root)

    def createVariable(self, variable):
        if type(variable) != ASTDataType:
            exit("wrong type not a ASTDataType")
        if self.checkIfNameExists(variable.getVariableName()):
            global number

            self.symbolTable[variable.getVariableName()] = variable.getVariableName() + "scope" + str(number)
            variable.nodes[0].root = variable.getVariableName() + "scope" + str(number)
            number += 1
        else:
            self.symbolTable[variable.getVariableName()] = variable.getVariableName()

        if self.isGlobal and not self.isMips:
            self.symbolTable[variable.getVariableName()] = '@' + variable.nodes[0].root
            variable.nodes[0].root = '@' + variable.nodes[0].root
        elif self.isGlobal and self.isMips:
            self.symbolTable[variable.getVariableName()] = 'µ' + variable.nodes[0].root
            variable.nodes[0].root = 'µ' + variable.nodes[0].root

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
        if type(ast) == ASTVariable:
            self.checkAndReplaceVariable(ast)

        if not type(ast) == ASTScope and not type(ast) == ASTFunction and not (type(ast) == ASTDataType) and ast.nodes != None:
            for node in ast.nodes:
                self.preOrderTraverse(node)
        elif type(ast) == ASTScope or type(ast) == ASTFunction:
            ASTFixScoping(ast, self, self.isMips)
        elif type(ast) == ASTDataType and ast.nodes != None:
            self.createVariable(ast)
        return


