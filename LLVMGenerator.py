from AST import ASTDataType, ASTPrintf, ASTVariable, ASTOperator, AST, ASTPointer, ASTWhile, ASTCondition, ASTIfElse, \
    ASTOneTokenStatement
from LLVMProgram import LLVMProgram, LLVMFunction, LLVMWhile, LLVMIfElse


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
        elif type(node) == ASTCondition:
            tempName = self.currentFunction.createUniqueRegister("whileLoopCondition")
            whileLoopCondition = node.nodes[0]
            if type(whileLoopCondition) == AST:
                self.currentFunction.newVarible(tempName, "i32", 4)
                self.currentFunction.setVaribleValue(tempName,node.nodes[0].getValue())
                self.currentFunction.setConditionVarable(tempName)
            else:
                self.currentFunction.newVarible(tempName, "i32", 4)
                self._createAstOperatorLLVM(tempName, whileLoopCondition)
                self.currentFunction.setConditionVarable(tempName)
            return True
        elif type(node) == ASTVariable:
            self._createSetAstVariableLLVM(node)
            return True
        elif type(node) == ASTWhile:
            tempCurrentFuntion = self.currentFunction
            self.currentFunction = LLVMWhile(self.currentFunction.createUniqueRegister(), self.currentFunction)
            self.preOrderTraverse(node.getCondition())
            self.currentFunction.endOfContition()
            self.preOrderTraverse(node.getScope())
            self.currentFunction.endOfLoop()
            self.currentFunction = tempCurrentFuntion
            return True
        elif type(node) == ASTIfElse:
            tempCurrentFuntion = self.currentFunction
            self.currentFunction = LLVMIfElse(self.currentFunction.createUniqueRegister(), self.currentFunction)
            self.preOrderTraverse(node.getCondition())
            self.currentFunction.endOfIfContition()
            self.preOrderTraverse(node.getIfScope())
            self.currentFunction.endOfIfStatement()
            self.currentFunction.startElse()
            if node.containsElseScope():
                self.preOrderTraverse(node.getElseScope())
            self.currentFunction.endOfElseStatement()
            self.currentFunction = tempCurrentFuntion
            return True
        elif type(node) == ASTOneTokenStatement:
            if node.root == "break":
                self.currentFunction.breakLoop()
            elif node.root == "continue":
                self.currentFunction.continueLoop()
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
