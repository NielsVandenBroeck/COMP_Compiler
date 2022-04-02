from AST import ASTDataType, ASTPrintf, ASTVariable, ASTOperator, AST, ASTPointer, ASTWhile
from LLVMProgram import LLVMProgram, LLVMFunction, LLVMWhile


class LLVMGenerator:
    def __init__(self,file_name, ast):
        self.file_name = file_name
        self.program = LLVMProgram()
        self.currentFunction = LLVMFunction("main")
        self.preOrderTraverse(ast)

    def isOperationNode(self, node):
        if type(node) == ASTDataType:
            self._createAstDataTyeLLVm(node)
            return True
        elif type(node) == ASTPrintf:
            self._createAstPrintfLLVM(node)
            return True
        elif type(node) == ASTOperator:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.createUniqueRegister(tempName)
            self._createAstOperatorLLVM(tempName, node)
            return True
        elif type(node) == ASTVariable:
            self._createSetAstVariableLLVM(node)
            return True
        elif type(node) == ASTWhile:
            self.currentFunction.setReturnValue(0)
            self.currentFunction = LLVMWhile(self.currentFunction.functionName)
            return True
        elif type(node) == ASTPointer:
            exit("pointer")
        return False

    def _createAstDataTyeLLVm(self, node):
        self.currentFunction.newVarible(node.getVariableName())
        self._createSetAstVariableLLVM(node)

    def _createAstPrintfLLVM(self, node):
        if type(node.nodes[0]) == ASTVariable:
            self.currentFunction.print(node.nodes[0].root)
        else:
            self.currentFunction.printValue(node.nodes[0].root)

    def _createAstOperatorLLVM(self, toRegName, node):
        if node.nodes == None:
            self.currentFunction.setVaribleValue(toRegName, node.getValue())

        elif type(node.getRightValue()) == ASTOperator:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.newVarible(tempName)
            self._createAstOperatorLLVM(tempName, node.getRightValue())
            node.nodes[1] = ASTVariable(tempName, 0,0)

        if type(node.getRightValue()) == AST:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.newVarible(tempName)
            self.currentFunction.setVaribleValue(tempName, node.getRightValue().getValue())
            node.nodes[1] = ASTVariable(tempName, 0, 0)

        if type(node.getLeftValue()) == AST:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.newVarible(tempName)
            self.currentFunction.setVaribleValue(tempName, node.getLeftValue().getValue())
            node.nodes[0] = ASTVariable(tempName, 0, 0)

        if type(node.getLeftValue()) == ASTVariable and type(node.getRightValue()) == ASTVariable:
            self.currentFunction.operationOnVarible(toRegName,node.getLeftValue().root, node.getRightValue().root, node.root)


    def _createSetAstVariableLLVM(self, node):
        #by declaretion
        if type(node) == ASTDataType:
            value = node.getValueObject()
        #by initialization
        else:
            value = node.getVariableValue()

        #if operation
        if type(value) == ASTOperator:
            self._createAstOperatorLLVM(node.getVariableName(), value)
        #if value
        elif value != None:
            value = value.getValue()
            self.currentFunction.setVaribleValue(node.getVariableName(), value)

    def preOrderTraverse(self, ast):
        if not self.isOperationNode(ast) and ast.nodes is not None:
            for node in ast.nodes:
                self.preOrderTraverse(node)

    def write(self):
        self.currentFunction.setReturnValue(0)
        with open(self.file_name, 'w') as myFile:
            myFile.write(self.program.output())
