from AST import ASTDataType, ASTPrintf, ASTVariable, ASTOperator, AST, ASTPointer, ASTWhile,ASTFor, ASTCondition, ASTIfElse, \
    ASTOneTokenStatement, ASTFunction, ASTFunctionName, ASTReturn, ASTParameters, ASTValue, ASTAdress, ASTScanf, \
    ASTArray, ASTForwardDeclaration, ASTInt, ASTText
from LLVMProgram import LLVMProgram, LLVMFunction, LLVMWhile, LLVMIfElse

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
        if type(node) == ASTForwardDeclaration:
            return True
        if type(node) == ASTDataType:
            self._createAstDataTyeLLVm(node)
            return True
        elif type(node) == ASTArray:
            self._createASTArray(node)
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
            functionType = self.currentFunction.getFunctionType(node.getFunctionName())
            tempName = None
            if functionType != "void":
                tempName = self.currentFunction.createUniqueRegister()
                self.currentFunction.newSmartVarible(tempName, functionType)
            self._createAstOperatorLLVM(tempName, node)
            return True
        elif type(node) == ASTCondition:
            tempName = self.currentFunction.createUniqueRegister("whileLoopCondition")
            whileLoopCondition = node.nodes[0]
            if type(whileLoopCondition) == ASTValue:
                self.currentFunction.newSmartVarible(tempName, whileLoopCondition.getType())
                self.currentFunction.setVaribleValue(tempName,whileLoopCondition.getValue(), self.getArrayIndex(node))
                self.currentFunction.setConditionVarable(tempName)
            else:
                self.currentFunction.newVarible(tempName, "i32", 4)
                self._createAstOperatorLLVM(tempName, whileLoopCondition)
                self.currentFunction.setConditionVarable(tempName)
            return True
        elif type(node) == ASTVariable:
            self._createSetAstVariableLLVM(node)
            return True
        elif type(node) == ASTWhile or type(node) == ASTFor:
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

    def _createASTArray(self, node):
        self.currentFunction.newSmartArray(node.getVariableName(), node.getType(), node.getLength())

    def _createAstDataTyeLLVm(self, node):
        if node.getVariableName()[0] == '@':
            self.currentFunction.newSmartVarible(node.getVariableName(), node.getType(), True, node.getValue())
        else:
            self.currentFunction.newSmartVarible(node.getVariableName(), node.getType())
            self._createSetAstVariableLLVM(node)

    def _createAstPointerLLVm(self, node):
        if type(node) != ASTPointer:
            exit("wrong type")

        if type(node.getSetObject()) == ASTAdress:
            tempReg = self.currentFunction.createUniqueRegister("temp")
            self.currentFunction.newSmartVarible(tempReg, node.getSetObject().getType(), False)
            self.currentFunction._getLLVMVariableLoadString(self.currentFunction.getVariable(node.getSetObject().getVariableName()), tempReg)
            self._createAstOperatorLLVM(tempReg, node.getToObject())
        else:
            self.currentFunction.newSmartVariblePointer(node.getSetObject().getVariableName(), node.getSetObject().getType(), 1)
            self._createSetAstVariableLLVM(node)

    def _createASTReturnItem(self, node):
        if type(node.getReturnValue()) == ASTOperator or type(node.getReturnValue()) == ASTFunctionName:
            tempVarible = self.currentFunction.createUniqueRegister("returnValue")
            functionType = self.currentFunction.getReturnType()
            self.currentFunction.newSmartVarible(tempVarible, functionType)
            self._createAstOperatorLLVM(tempVarible, node.getReturnValue())
            self.currentFunction.setReturnValue(ASTVariable(tempVarible))
        elif type(node.getReturnValue()) == ASTPointer and (not "*" in self.currentFunction.getReturnType()):
            pointerTOValueName = self.currentFunction.createUniqueRegister(node.getReturnValue().getVariableName() + "pointerToValue")
            valueName = self.currentFunction.createUniqueRegister(node.getReturnValue().getVariableName() + "pointerToValue")
            self.currentFunction._addLine(self.currentFunction.getVariable(node.getReturnValue().getVariableName()).loadPointerValueString(pointerTOValueName))
            self.currentFunction.newSmartVarible(valueName, node.getReturnValue().getType())
            self.currentFunction.setReturnValue(ASTVariable(valueName, 0, 0, None, node.getReturnValue().getType()))
        else:
            self.currentFunction.setReturnValue(node.getReturnValue())

    def _createAstPrintfLLVM(self, node):
        printArgs = []
        for printArg in node.getAllVariables():
            if type(printArg) == ASTVariable:
                if printArg.isArrayItem():
                    valueName = self.currentFunction.createUniqueRegister(printArg.getVariableName() + "pointerToValue")
                    self.currentFunction.newSmartVarible(valueName, printArg.getType(), False)
                    self.currentFunction._addLine(
                        self.currentFunction.getVariable(printArg.getVariableName()).getPointerToIndex(valueName, self.getArrayIndex(printArg)))
                    printArgs.append(valueName)
                else:
                    printArgs.append(printArg.root)
            elif type(printArg) == ASTPointer:
                pointerTOValueName = self.currentFunction.createUniqueRegister(printArg.getVariableName() + "pointerToValue")
                valueName = self.currentFunction.createUniqueRegister(printArg.getVariableName() + "pointerToValue")
                self.currentFunction._addLine(self.currentFunction.getVariable(printArg.getVariableName()).loadPointerValueString(pointerTOValueName))
                self.currentFunction.newSmartVarible(valueName, printArg.getType())
                self.currentFunction.setVaribleValue(valueName, "%" + pointerTOValueName, self.getArrayIndex(node))
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
                self.currentFunction.setVaribleValue(tempVarName, printArg.root, self.getArrayIndex(node))
                printArgs.append(tempVarName)
            elif isinstance(printArg, ASTText):
                tempVarName = self.currentFunction.createUniqueRegister("printString")
                self.currentFunction.addPrintString(tempVarName, printArg.getString())
                printArgs.append(tempVarName)
            else:
                printArgs.append(printArg.root)
        self.currentFunction.print(node.getPrintString(), printArgs)

    def _createAstScanfLLVM(self, node):
        printArgs = []
        for printArg in node.getAllVariables():
            if type(printArg) == ASTAdress:
                printArgs.append([printArg.getVariableName(), ASTAdress])
            else:
                printArgs.append([printArg.root, ASTPointer])

        self.currentFunction.scan(node.getScanString(), printArgs)

    def _createAstOperatorLLVM(self, toVarible, node, toIndex = None):
        if node.nodes == None and type(node) != ASTFunctionName:
            self.currentFunction.setVaribleValue(toVarible, node.getValue(), self.getArrayIndex(node))
            return

        elif type(node) == ASTFunctionName:
            params = node.getFunctionParameters()
            for paramCounter in range(len(params)):
                if type(params[paramCounter]) != ASTVariable and type(params[paramCounter]) != ASTAdress:
                    tempName = self.currentFunction.createUniqueRegister()
                    self.currentFunction.newSmartVarible(tempName, params[paramCounter].getType())
                    self._createAstOperatorLLVM(tempName, params[paramCounter])
                    node.nodes[0].nodes[paramCounter] = ASTVariable(tempName, 0, 0, None, params[paramCounter].getType())

            self.currentFunction.functionCall(node.getFunctionName(), node.getFunctionParameters(), toVarible)
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
                self.currentFunction.setVaribleValue(tempName, node.getLeftValue().getValue(), self.getArrayIndex(node))
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
            self.currentFunction.setVaribleValue(valueName, "%" + pointerTOValueName, self.getArrayIndex(node))
            node.nodes[0] = ASTVariable(valueName, 0, 0, None, node.getLeftValue().getType())

        if isinstance(node.getRightValue(), ASTValue):
            if type(node.getRightValue()) == ASTVariable:
                node.nodes[1] = node.getRightValue()
            else:
                tempName = self.currentFunction.createUniqueRegister()
                self.currentFunction.newSmartVarible(tempName, node.getRightValue().getType())
                self.currentFunction.setVaribleValue(tempName, node.getRightValue().getValue(), self.getArrayIndex(node))
                node.nodes[1] = ASTVariable(tempName, 0, 0, None, node.getRightValue().getType())
        elif type(node.getRightValue()) == ASTFunctionName:
            tempName = self.currentFunction.createUniqueRegister()
            functionType = self.currentFunction.getFunctionType(node.getRightValue().getFunctionName())
            self.currentFunction.newSmartVarible(tempName, functionType)
            self._createAstOperatorLLVM(tempName, node.getRightValue())
            node.nodes[1] = ASTVariable(tempName, 0, 0, None, node.getRightValue().getType())
        elif type(node.getRightValue()) == ASTPointer:
            pointerTOValueName = self.currentFunction.createUniqueRegister(node.getRightValue().getVariableName() + "pointerToValue")
            valueName = self.currentFunction.createUniqueRegister(node.getRightValue().getVariableName() + "pointerToValue")
            self.currentFunction._addLine(self.currentFunction.getVariable(node.getRightValue().getVariableName()).loadPointerValueString(pointerTOValueName))
            self.currentFunction.newSmartVarible(valueName, node.getRightValue().getType())
            self.currentFunction.setVaribleValue(valueName, "%" + pointerTOValueName, self.getArrayIndex(node))
            node.nodes[1] = ASTVariable(valueName, 0, 0, None, node.getRightValue().getType())

        if type(node.getLeftValue()) == ASTVariable and type(node.getRightValue()) == ASTVariable:
            self.currentFunction.operationOnVarible(toVarible,node.getLeftValue().root, node.getRightValue().root, node.root,toIndex , self.getArrayIndex(node.getLeftValue()), self.getArrayIndex(node.getRightValue()))

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
            self._createAstOperatorLLVM(node.getVariableName(), value, self.getArrayIndex(node))
        elif type(value) == ASTVariable and not value.isArrayItem():
            self.currentFunction.setVaribleValue(node.getVariableName(), value, self.getArrayIndex(node))
        elif type(value) == ASTVariable and value.isArrayItem():
            parameterAdress = self.currentFunction.createUniqueRegister(value.getVariableName() + "index")
            self.currentFunction._getLLVMVariableLoadString(self.currentFunction.getVariable(value.getVariableName()), parameterAdress, self.getArrayIndex(value))
            self.currentFunction.setVaribleValue(node.getVariableName(), "%" + parameterAdress, self.getArrayIndex(node))
        elif type(value) == ASTAdress and type(node) == ASTPointer:
            self.currentFunction.setVaribleValue(node.getSetObject().getVariableName(), "%" + value.getVariableName(), self.getArrayIndex(node))
        elif value != None:
            value = value.getValue()
            self.currentFunction.setVaribleValue(node.getVariableName(), value, self.getArrayIndex(node))

    def preOrderTraverse(self, ast):
        if not self.isOperationNode(ast) and ast.nodes is not None:
            for node in ast.nodes:
                self.preOrderTraverse(node)

    def write(self):
        #self.currentFunction.setReturnValue(0)
        with open(self.file_name, 'w') as myFile:
            myFile.write(self.program.output())
            myFile.close()

    def getArrayIndex(self, arrayNode):
        if arrayNode == None:
            return None
        if type(arrayNode.getIndexItem()) == ASTVariable:
            result = self.currentFunction.createUniqueRegister("index")
            self.currentFunction._getLLVMVariableLoadString(self.currentFunction.getVariable(arrayNode.getIndex()), result)
            return "%" + result
        if type(arrayNode.getIndexItem()) != ASTValue and type(arrayNode) != ASTDataType and type(arrayNode) != ASTValue and type(arrayNode) != ASTInt and arrayNode.getIndexItem() != None:
            tempName = self.currentFunction.createUniqueRegister("index")
            self.currentFunction.newSmartVarible(tempName, int)
            self._createAstOperatorLLVM(tempName, arrayNode.getIndexItem())

            result = self.currentFunction.createUniqueRegister("index")
            self.currentFunction._getLLVMVariableLoadString(self.currentFunction.getVariable(tempName), result)
            return "%" + result
        return arrayNode.getIndex()