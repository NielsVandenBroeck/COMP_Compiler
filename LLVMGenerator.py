from AST import ASTDataType, ASTPrintf, ASTVariable, ASTOperator, AST, ASTPointer, ASTWhile, ASTCondition, ASTIfElse, \
    ASTOneTokenStatement, ASTFunction, ASTFunctionName, ASTReturn, ASTParameters, ASTValue, ASTAdress, ASTScanf
from LLVMProgram import LLVMProgram, LLVMFunction, LLVMWhile, LLVMIfElse

#TODO all undifinded varible to smartvarible!!!
class LLVMGenerator:
    def __init__(self,file_name, ast):
        self.file_name = file_name

        LLVMProgram.programArray = []
        LLVMProgram.VaribleList = {}
        LLVMProgram.functionReturnTypeDict = {}

        self.program = LLVMProgram()
        self.currentFunction = self.program
        self.preOrderTraverse(ast)

    def isOperationNode(self, node):
        if type(node) == ASTDataType:
            self._createAstDataTyeLLVm(node)
            return True
        elif type(node) == ASTPointer:
            self._createAstPointerLLVm(node)
            return True
        elif type(node) == ASTPrintf:
            self._createAstPrintfLLVM(node)
            return True
        elif type(node) == ASTScanf:
            self._createAstScanfLLVM(node)
            return True
        elif type(node) == ASTOperator:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.newSmartVarible(tempName, node.getType())
            self._createAstOperatorLLVM(tempName, node)
            return True
        elif type(node) == ASTFunctionName:
            tempName = self.currentFunction.createUniqueRegister()
            functionType = self.currentFunction.getFunctionType(node.getFunctionName())
            self.currentFunction.newSmartVarible(tempName, functionType)
            self._createAstOperatorLLVM(tempName, node)
            return True
        elif type(node) == ASTCondition:
            tempName = self.currentFunction.createUniqueRegister("whileLoopCondition")
            whileLoopCondition = node.nodes[0]
            if type(whileLoopCondition) == ASTValue:
                print(node)
                self.currentFunction.newSmartVarible(tempName, whileLoopCondition.getType())
                self.currentFunction.setVaribleValue(tempName,whileLoopCondition.getValue())
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
        elif type(node) == ASTOneTokenStatement:
            if node.root == "break":
                self.currentFunction.breakLoop()
            elif node.root == "continue":
                self.currentFunction.continueLoop()
        return False

    def _createAstDataTyeLLVm(self, node):
        self.currentFunction.newSmartVarible(node.getVariableName(), node.getType())
        self._createSetAstVariableLLVM(node)

    def _createAstPointerLLVm(self, node):
        if type(node) != ASTPointer:
            exit("wrong type")
        self.currentFunction.newSmartVariblePointer(node.getSetObject().getVariableName(), node.getSetObject().getType(), 1)
        self._createSetAstVariableLLVM(node)

    def _createASTReturnItem(self, node):
        if type(node.getReturnValue()) == ASTOperator or type(node.getReturnValue()) == ASTFunctionName:
            tempVarible = self.currentFunction.createUniqueRegister("returnValue")
            functionType = self.currentFunction.returnType
            self.currentFunction.newSmartVarible(tempVarible, functionType)
            self._createAstOperatorLLVM(tempVarible, node.getReturnValue())
            self.currentFunction.setReturnValue(ASTVariable(tempVarible))
        elif type(node.getReturnValue()) == ASTPointer and (not "*" in self.currentFunction.returnType):
            pointerTOValueName = self.currentFunction.createUniqueRegister(node.getReturnValue().getVariableName() + "pointerToValue")
            valueName = self.currentFunction.createUniqueRegister(node.getReturnValue().getVariableName() + "pointerToValue")
            self.currentFunction._addLine(self.currentFunction.getVariable(node.getReturnValue().getVariableName()).loadPointerValueString(pointerTOValueName))
            self.currentFunction.newSmartVarible(valueName, node.getReturnValue().getType())
            self.currentFunction.setReturnValue(ASTVariable(valueName, 0, 0, None, node.getReturnValue().getType()))
        else:
            self.currentFunction.setReturnValue(node.getReturnValue())

    def _createAstPrintfLLVM(self, node):
        printArgs = []
        for printArg in node.getAllVaribles():
            if type(printArg) == ASTVariable:
                printArgs.append(printArg.root)
            elif type(printArg) == ASTPointer:
                pointerTOValueName = self.currentFunction.createUniqueRegister(printArg.getVariableName() + "pointerToValue")
                valueName = self.currentFunction.createUniqueRegister(printArg.getVariableName() + "pointerToValue")
                self.currentFunction._addLine(self.currentFunction.getVariable(printArg.getVariableName()).loadPointerValueString(pointerTOValueName))
                self.currentFunction.newSmartVarible(valueName, printArg.getType())
                self.currentFunction.setVaribleValue(valueName, "%" + pointerTOValueName)
                printArgs.append(valueName)
            elif type(printArg) == ASTOperator or type(printArg) == ASTFunctionName:
                tempVarible = self.currentFunction.createUniqueRegister("returnValue")
                if type(printArg) == ASTFunctionName:
                    functionType = self.currentFunction.getFunctionType(printArg.getFunctionName())
                else:
                    functionType = printArg.getType()
                self.currentFunction.newSmartVarible(tempVarible, functionType)
                self._createAstOperatorLLVM(tempVarible, printArg)
                printArgs.append(tempVarible)
            elif isinstance(printArg, ASTValue):
                tempVarName = self.currentFunction.createUniqueRegister("printTemp")
                self.currentFunction.newSmartVarible(tempVarName, printArg.getType())
                self.currentFunction.setVaribleValue(tempVarName, printArg.root)
                printArgs.append(tempVarName)
            else:
                printArgs.append(printArg.root)

        self.currentFunction.print(node.getPrintString(), printArgs)

    def _createAstScanfLLVM(self, node):
        print("scan")
        printArgs = []
        for printArg in node.getAllVaribles():
            if type(printArg) == ASTAdress:
                printArgs.append([printArg.getVariableName(), ASTAdress])
            else:
                printArgs.append([printArg.root, ASTPointer])

        self.currentFunction.scan(node.getScanString(), printArgs)

    def _createAstOperatorLLVM(self, toRegName, node):
        if node.nodes == None:
            self.currentFunction.setVaribleValue(toRegName, node.getValue())
            return

        elif type(node) == ASTFunctionName:
            params = node.nodes[0].nodes
            for paramCounter in range(len(params)):
                if type(params[paramCounter]) != ASTVariable:
                    tempName = self.currentFunction.createUniqueRegister()
                    self.currentFunction.newSmartVarible(tempName, params[paramCounter].getType())
                    self._createAstOperatorLLVM(tempName, params[paramCounter])
                    node.nodes[0].nodes[paramCounter] = ASTVariable(tempName, 0, 0, None, params[paramCounter].getType())

            self.currentFunction.functionCall(node.getFunctionName(), node.getFunctionParameters(), toRegName)
            return

        #indien
        if type(node.getRightValue()) == ASTOperator:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.newSmartVarible(tempName, node.getRightValue().getType())
            self._createAstOperatorLLVM(tempName, node.getRightValue())
            node.nodes[1] = ASTVariable(tempName, 0,0)

        if type(node.getLeftValue()) == ASTOperator:
            tempName = self.currentFunction.createUniqueRegister()
            self.currentFunction.newSmartVarible(tempName, node.getLeftValue().getType())
            self._createAstOperatorLLVM(tempName, node.getLeftValue())
            node.nodes[0] = ASTVariable(tempName, 0,0)

        if isinstance(node.getLeftValue(), ASTValue):
            if type(node.getLeftValue()) == ASTVariable:
                node.nodes[0] = node.getLeftValue()
            else:
                tempName = self.currentFunction.createUniqueRegister()
                self.currentFunction.newSmartVarible(tempName, node.getLeftValue().getType())
                self.currentFunction.setVaribleValue(tempName, node.getLeftValue().getValue())
                node.nodes[0] = ASTVariable(tempName, 0, 0)
        elif type(node.getLeftValue()) == ASTFunctionName:
            tempName = self.currentFunction.createUniqueRegister()
            functionType = self.currentFunction.getFunctionType(node.getLeftValue().getFunctionName())
            self.currentFunction.newSmartVarible(tempName, functionType)
            self._createAstOperatorLLVM(tempName, node.getLeftValue())
            node.nodes[0] = ASTVariable(tempName, 0, 0)
        elif type(node.getLeftValue()) == ASTPointer:
            pointerTOValueName = self.currentFunction.createUniqueRegister(node.getLeftValue().getVariableName() + "pointerToValue")
            valueName = self.currentFunction.createUniqueRegister(node.getLeftValue().getVariableName() + "pointerToValue")
            self.currentFunction._addLine(self.currentFunction.getVariable(node.getLeftValue().getVariableName()).loadPointerValueString(pointerTOValueName))
            self.currentFunction.newSmartVarible(valueName, node.getLeftValue().getType())
            self.currentFunction.setVaribleValue(valueName, "%" + pointerTOValueName)
            node.nodes[0] = ASTVariable(valueName, 0, 0, None, node.getLeftValue().getType())

        if isinstance(node.getRightValue(), ASTValue):
            if type(node.getRightValue()) == ASTVariable:
                node.nodes[1] = node.getRightValue()
            else:
                tempName = self.currentFunction.createUniqueRegister()
                self.currentFunction.newSmartVarible(tempName, node.getRightValue().getType())
                self.currentFunction.setVaribleValue(tempName, node.getRightValue().getValue())
                node.nodes[1] = ASTVariable(tempName, 0, 0, None, node.getRightValue().getType())
        elif type(node.getRightValue()) == ASTFunctionName:
            tempName = self.currentFunction.createUniqueRegister()
            functionType = self.currentFunction.getFunctionType(node.getLeftValue().getFunctionName())
            self.currentFunction.newSmartVarible(tempName, functionType)
            self._createAstOperatorLLVM(tempName, node.getRightValue())
            node.nodes[1] = ASTVariable(tempName, 0, 0, None, node.getRightValue().getType())
        elif type(node.getRightValue()) == ASTPointer:
            pointerTOValueName = self.currentFunction.createUniqueRegister(node.getRightValue().getVariableName() + "pointerToValue")
            valueName = self.currentFunction.createUniqueRegister(node.getRightValue().getVariableName() + "pointerToValue")
            self.currentFunction._addLine(self.currentFunction.getVariable(node.getRightValue().getVariableName()).loadPointerValueString(pointerTOValueName))
            self.currentFunction.newSmartVarible(valueName, node.getRightValue().getType())
            self.currentFunction.setVaribleValue(valueName, "%" + pointerTOValueName)
            node.nodes[1] = ASTVariable(valueName, 0, 0, None, node.getRightValue().getType())

        if type(node.getLeftValue()) == ASTVariable and type(node.getRightValue()) == ASTVariable:
            self.currentFunction.operationOnVarible(toRegName,node.getLeftValue().root, node.getRightValue().root, node.root)

    def _createSetAstVariableLLVM(self, node):
        #by declaretion
        if type(node) == ASTDataType:
            value = node.getValueObject()
        #by initialization
        elif type(node) == ASTPointer:
            value = node.getToObject()
        else:
            value = node.getVariableValue()

        #if operation
        if type(value) == ASTOperator or type(value) == ASTFunctionName:
            self._createAstOperatorLLVM(node.getVariableName(), value)
        elif type(value) == ASTVariable:
            self.currentFunction.setVaribleValue(node.getVariableName(), value)
        elif type(value) == ASTAdress and type(node) == ASTPointer:
            self.currentFunction.setVaribleValue(node.getSetObject().getVariableName(), "%" + value.getVariableName())
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
            myFile.close()
