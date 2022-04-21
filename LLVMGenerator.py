from AST import ASTDataType, ASTPrintf, ASTVariable, ASTOperator, AST, ASTPointer, ASTWhile, ASTCondition, ASTIfElse, \
    ASTOneTokenStatement, ASTFunction, ASTFunctionName, ASTReturn, ASTParameters
from LLVMProgram import LLVMProgram, LLVMFunction, LLVMWhile, LLVMIfElse


class LLVMGenerator:
    def __init__(self,file_name, ast):
        self.file_name = file_name
        self.program = LLVMProgram()
        self.currentFunction = self.program
        self.preOrderTraverse(ast)

    def isOperationNode(self, node):
        if type(node) == ASTDataType:
            self._createAstDataTyeLLVm(node)
            return True
        elif type(node) == ASTPrintf:
            self._createAstPrintfLLVM(node)
            return True
        elif type(node) == ASTOperator or type(node) == ASTFunctionName:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.newVarible(tempName)
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
        elif type(node) == ASTFunction:
            self.currentFunction = LLVMFunction(node.getFunctionName(), self.currentFunction, node.getReturnType(), node.getParameters())
            self.preOrderTraverse(node.getScope())
            self.currentFunction.endOfFunction()
            return True
        elif type(node) == ASTReturn:
            self._createASTReturnItem(node)
            return True
        elif type(node) == ASTFunctionName:
            self.preOrderTraverse(node.nodes[0])
            self.currentFunction.functionCall(node.getFunctionName(), node.getFunctionParameters())
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

    def _createASTReturnItem(self, node):
        if type(node.getReturnValue()) == ASTOperator or type(node.getReturnValue()) == ASTFunctionName:
            tempVarible = self.currentFunction.createUniqueRegister("returnValue")
            self.currentFunction.newVarible(tempVarible)
            self._createAstOperatorLLVM(tempVarible, node.getReturnValue())
            self.currentFunction.setReturnValue(ASTVariable(tempVarible))
        else:
            self.currentFunction.setReturnValue(node.getReturnValue())

    def _createAstPrintfLLVM(self, node):
        if type(node.nodes[0]) == ASTVariable:
            self.currentFunction.print(node.nodes[0].root)
        elif type(node.nodes[0]) == ASTOperator or type(node.nodes[0]) == ASTFunctionName:
            tempVarible = self.currentFunction.createUniqueRegister("returnValue")
            self.currentFunction.newVarible(tempVarible)
            self._createAstOperatorLLVM(tempVarible, node.nodes[0])
            self.currentFunction.print(tempVarible)
        else:
            self.currentFunction.printValue(node.nodes[0].root)

    def _createAstOperatorLLVM(self, toRegName, node):
        if node.nodes == None:
            self.currentFunction.setVaribleValue(toRegName, node.getValue())
            return

        elif type(node) == ASTFunctionName:
            params = node.nodes[0].nodes
            for paramCounter in range(len(params)):
                if type(params[paramCounter]) != ASTVariable:
                    tempName = self.currentFunction.createUniqueRegister()
                    self.currentFunction.newVarible(tempName)
                    self._createAstOperatorLLVM(tempName, params[paramCounter])
                    node.nodes[0].nodes[paramCounter] = ASTVariable(tempName, 0, 0)

            self.currentFunction.functionCall(node.getFunctionName(), node.getFunctionParameters(), toRegName)
            return

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
        elif type(node.getRightValue()) == ASTFunctionName:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.newVarible(tempName)
            self._createAstOperatorLLVM(tempName, node.getRightValue())
            node.nodes[1] = ASTVariable(tempName, 0, 0)

        if type(node.getLeftValue()) == AST:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.newVarible(tempName)
            self.currentFunction.setVaribleValue(tempName, node.getLeftValue().getValue())
            node.nodes[0] = ASTVariable(tempName, 0, 0)
        elif type(node.getLeftValue()) == ASTFunctionName:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.newVarible(tempName)
            self._createAstOperatorLLVM(tempName, node.getRightValue())
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
        if type(value) == ASTOperator or type(value) == ASTFunctionName:
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
        #self.currentFunction.setReturnValue(0)
        with open(self.file_name, 'w') as myFile:
            myFile.write(self.program.output())
