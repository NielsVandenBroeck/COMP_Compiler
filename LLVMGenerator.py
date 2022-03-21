from AST import ASTDataType, ASTPrintf, ASTVariable, ASTOperator
from LLVMProgram import LLVMProgram, LLVMFunction


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
        elif type(node) == ASTOperator:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.createUniqueRegister(tempName)
            self._createAstOperatorLLVM(tempName, node)


    def _createAstDataTyeLLVm(self, node):
        self.currentFunction.newVarible(node.getVariableName())
        value = node.getValueObject()
        if type(value) == ASTOperator:
            self.currentFunction.setVaribleValue(node.getVariableName(), value)
            self._createAstOperatorLLVM(node.getVariableName(), value)
        elif value != None:
            value = node.getValue()
            self.currentFunction.setVaribleValue(node.getVariableName(), value)

    def _createAstPrintfLLVM(self, node):
        if type(node.nodes[0]) == ASTVariable:
            self.currentFunction.print(node.nodes[0].root)
        else:
            self.currentFunction.printValue(node.nodes[0].root)

    def _createAstOperatorLLVM(self, toRegName, node):
        if type(node.getLeftValue()) == ASTVariable and type(node.getRightValue()) == ASTVariable:
            self.currentFunction.addVarible(toRegName,node.getLeftValue().root, node.getRightValue().root)

    def preOrderTraverse(self, ast):
        if not self.isOperationNode(ast) and ast.nodes is not None:
            for node in ast.nodes:
                self.preOrderTraverse(node)

    def write(self):
        self.currentFunction.setReturnValue(0)
        with open(self.file_name, 'w') as myFile:
            myFile.write(self.program.output())
