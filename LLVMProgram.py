import struct

from AST import ASTVoid, ASTVariable, AST, ASTPointer


class LLVMProgram:
    adressCounter = 0
    programArray = []
    convertScore = {float: 2, int: 0, chr: 1}
    VaribleList = {}
    functionReturnTypeDict = {}
    def __init__(self):
        self.programArray.append('declare dso_local i32 @__isoc99_scanf(i8*, ...) #1') #string %d needed to print ints
        self.programArray.append('@.procentC = private unnamed_addr constant [3 x i8] c"%c\\00", align 1')  # string %c needed to print chars
        self.programArray.append('@.procentF = private unnamed_addr constant [3 x i8] c"%f\\00", align 1')  # string %f needed to print floats
        self.programArray.append('declare dso_local i32 @printf(i8*, ...) #1')  # print function
        self.parantFunction = None

    def addFunction(self, function):
        if(type(function) != LLVMFunction):
            exit("fout type")
        self.programArray = self.programArray + function.programArray

    def output(self):
        fullProgram = ""
        for line in self.programArray:
            fullProgram += "\n" + line
        return fullProgram

    def _addLine(self, line):
        self.programArray.insert(len(self.programArray) - 1, "\t" + line)  # create a new line to close the bracket

    def newVarible(self, name, type = "i32", align = 4, addLine = True):
        varible = LLVMVarible(name, type, align)
        self.setVariable(name, varible)
        if addLine:
            self._addLine(varible.getLLVMDecString())

    def newSmartVarible(self, name, type, addline = True):
        if type == int or type == "i32":
            self.newVarible(name, "i32", 4, addline)
        elif type == chr or type == "i8":
            self.newVarible(name,  "i8", 1, addline)
        elif type == float or type == "float":
            self.newVarible(name,  "float", 4, addline)
        else:
            exit("Not known type")

    def newSmartVariblePointer(self, name, type, pointerDept = 1, addline = True):
        if type == int or type == "i32":
            self.newVarible(name, "i32" + str(pointerDept * "*"), 8, addline)
        elif type == chr or type == "i8":
            self.newVarible(name,  "i8" + str(pointerDept * "*"), 2, addline)
        elif type == float or type == "float":
            self.newVarible(name,  "float" + str(pointerDept * "*"), 8, addline)
        else:
            exit("Not known type")

    def setVaribleValue(self, name, value):
        varible = self.getVariable(name)
        if type(value) == ASTVariable:
            varible1 = self.getVariable(value.getValue())
            registerVar = self.createUniqueRegister(value.getValue())
            self._addLine(varible1.getLLVMLoadString(registerVar))
            if varible.getType() != varible1.getType():
                registerVar1 = self.createUniqueRegister(value.getValue())
                self.convert(registerVar1, registerVar, varible.getType(), varible1.getType())
                registerVar = registerVar1
            value = "%" + registerVar
        self._addLine(varible.getLLVMIniString(value))

    def convert(self, toName, fromName, toType, fromType):
        toType = self.typeToLLVMType(toType)
        fromType = self.typeToLLVMType(fromType)
        typeArray = {"i32": "si", "float": "fp"}
        typeArray1 = {"i32": "i32", "float": "float", "i8": "i8"}
        if toType == chr and fromType == float:
            self._addLine("%" + toName + " = sext " + typeArray1[fromType] + " %" + fromName +" to " + typeArray1[toType])
        else:
            self._addLine("%" + toName + " = " + typeArray[fromType] + "to" + typeArray[toType] + " " + typeArray1[fromType] + " %" + fromName + " to " + typeArray1[toType])

    def createUniqueRegister(self, addName = ""):
        self.adressCounter = self.adressCounter + 1
        return "uniq" + str(addName) + self.functionName + str(self.adressCounter)

    def setVariable(self, name, varible):
        self.VaribleList[name] = varible

    def getVariable(self, name):
        if name in self.VaribleList:
            return self.VaribleList[name]
        elif self.parantFunction != None:
            return self.parantFunction.getVariable(name)
        exit("varible bestaat niet: " + name)

    def typeToLLVMType(self, type):
        typeDict = {"int": "i32", "char": "i8", ASTVoid: "void", int: "i32", float: "float", chr:"i8"}
        if type in typeDict:
            return typeDict[type]
        return type

    def getFunctionType(self, functionName):
        return self.functionReturnTypeDict[functionName].returnType

    def getFunctionCallTypes(self, functionName):
        return self.functionReturnTypeDict[functionName].parameterTypeList

    def addPrintString(self, name, printString):
        charCount = len(printString) + 1
        printStringLLVM = "@." + name + " = private unnamed_addr constant [" + str(charCount) +" x i8] c\"" + printString + "\\00\", align 1"
        self.programArray.insert(0, printStringLLVM)

class LLVMFunction(LLVMProgram):
    def __init__(self, functionName, parantFunction = None, returnType = "i32", parameters = None):
        self.parantFunction = parantFunction
        self.returnType = self.typeToLLVMType(returnType)
        self.returnItemSet = False
        parantFunction.functionReturnTypeDict[functionName] = self
        self.functionName = functionName
        self.programArray.append("define " + self.returnType + " @" + functionName + "(" + self._getParameterString(parameters) + ") #0 {")
        self.programArray.append("}")
        self._initializeParameter(parameters)
        self.parameterTypeList = self._getCallParameterTypes(parameters)

    def addPrintString(self, name, printString):
        self.parantFunction.addPrintString(name, printString)

    def _getCallParameterTypes(self, parameters):
        parameterTypeList = []
        if parameters == None or parameters == []:
            return parameterTypeList
        parameterList = parameters.getParameterList()
        for parameter in parameterList:
            parameterTypeList.append(self.typeToLLVMType(parameter.getType()) + (parameter.getPointerDept() * "*"))
        return parameterTypeList

    def _getParameterString(self, parameters):
        if parameters == None or parameters == []:
            return ""
        parameterList = parameters.getParameterList()
        parameterString = ""
        for parameter in parameterList:
            parameterString += self.typeToLLVMType(parameter.getType()) + (parameter.getPointerDept() * "*") + " %" + str("parameter" + parameter.getVariableName()) + ", "
        parameterString = parameterString[:-2]
        return parameterString

    def _initializeParameter(self, parameters):
        if parameters == None or parameters == []:
            return
        parameterList = parameters.getParameterList()
        for parameter in parameterList:
            if type(parameter) == ASTPointer:
                self.newSmartVariblePointer("parameter" + parameter.getVariableName(), parameter.getType(), parameter.getPointerDept(), False)
                self.newSmartVariblePointer(parameter.getVariableName(), parameter.getType(), parameter.getPointerDept())
            else:
                self.newSmartVarible("parameter" + parameter.getVariableName(), parameter.getType(), False)
                self.newSmartVarible(parameter.getVariableName(), parameter.getType())
            self._addLine(self.getVariable(parameter.getVariableName()).getLLVMIniString("%parameter" + parameter.getVariableName()))

    def functionCall(self, functionName, parameters, toVarible = None):
        returnType = self.getFunctionType(functionName)
        callTypeList = self.getFunctionCallTypes(functionName)

        if len(callTypeList) != len(parameters):
            exit("wrong amount of parameters")

        parameterString = ""
        for i in range(len(callTypeList)):
            value = parameters[i]
            if type(parameters[i]) == ASTVariable:
                parameterAdress = self.createUniqueRegister("parameter")
                self._addLine(self.getVariable(parameters[i].root).getLLVMLoadString(parameterAdress))
                if self.getVariable(parameters[i].root).getLLVMType() != callTypeList[i]:
                    parameterAdress1 = self.createUniqueRegister("parameter")
                    self.convert(parameterAdress1, parameterAdress, callTypeList[i],self.getVariable(parameters[i].root).getType())
                    parameterAdress = parameterAdress1

                value = "%" + parameterAdress
            elif isinstance(parameters[i], AST):
                value = parameters[i].root
            parameterString += callTypeList[i] + " " + str(value) + ", "
        parameterString = parameterString[:-2]

        if toVarible == None or returnType =="void":
            self._addLine("call " + returnType + " @" + functionName + "(" + parameterString + ")")
        else:
            tempReg = self.createUniqueRegister()
            self._addLine("%" + tempReg + " = call " + returnType + " @" + functionName + "(" + parameterString + ")")
            self._addLine(self.getVariable(toVarible).getLLVMIniString("%" + tempReg))

    def setReturnValue(self, value = ""):
        self.returnItemSet = True
        returntype = self.getFunctionType(self.functionName)

        returnItem= ""
        if type(value) == ASTVariable:
            returnVar = self.getVariable(value.root)
            self._addLine(returnVar.getLLVMLoadString("returnItem"))
            returnItem = "returnItem"
            if self.returnType != self.typeToLLVMType(returnVar.getType()):
                returnItem1 = self.createUniqueRegister("returnItem")
                self.convert(returnItem1, returnItem,self.returnType, self.typeToLLVMType(returnVar.getType()))
                returnItem = returnItem1
            returnItem = "%" + returnItem
        elif isinstance(value, AST):
            returnItem = str(value.root)
        else:
            returnItem = str(value)

        if returnItem == "void":
            self._addLine("ret void")
        else:
            self._addLine("ret " + returntype + " " + returnItem)

    def operationOnVarible(self, toName, nameItem1, nameItem2, operation):
        operations = {"+": "add", "-": "sub", "*": "mul", "/": "sdiv", "<": "icmp slt", ">": "icmp sgt", "==": "icmp eq", "!=": "icmp ne", "<=": "icmp sle",  ">=": "icmp sge"}

        toVarible = self.getVariable(toName)
        varible1 = self.getVariable(nameItem1)
        varible2 = self.getVariable(nameItem2)

        valueVariable1 = self.createUniqueRegister(varible1.LLVMname)
        self._addLine(varible1.getLLVMLoadString(valueVariable1))

        valueVariable2 = self.createUniqueRegister(varible2.LLVMname)
        self._addLine(varible2.getLLVMLoadString(valueVariable2))

        operationType = varible1.getType()
        if self.convertScore[varible1.getType()] < self.convertScore[varible2.getType()]:
            newValueVariable1 = self.createUniqueRegister(varible1.LLVMname)
            self.convert(newValueVariable1, valueVariable1, varible2.getType(), varible1.getType())
            valueVariable1 = newValueVariable1
            operationType = varible2.getType()
        elif self.convertScore[varible1.getType()] > self.convertScore[varible2.getType()]:
            newValueVariable2 = self.createUniqueRegister(varible2.LLVMname)
            self.convert(newValueVariable2, valueVariable2, varible1.getType(), varible2.getType())
            valueVariable2 = newValueVariable2

        if operationType == float:
            operations = {"+": "fadd", "-": "fsub", "*": "fmul", "/": "fsdiv", "<": "icmp slt", ">": "icmp sgt","==": "icmp eq", "!=": "icmp ne", "<=": "icmp sle", ">=": "icmp sge"}

        tempRegName = self.createUniqueRegister()
        self._addLine("%" + tempRegName + " = " + operations[operation] + " " + self.typeToLLVMType(operationType) + " %" + valueVariable1 + ", %" + valueVariable2 + "")
        if "icmp" in operations[operation]:
            tempRegName1 = self.createUniqueRegister()
            self._addLine("%" + tempRegName1 + "= zext i1 %" + tempRegName + " to i32")
            tempRegName = tempRegName1
        elif operationType != toVarible.getType():
            tempRegName1 = self.createUniqueRegister(tempRegName + "convert")
            self.convert(tempRegName1, tempRegName, toVarible.getType(), operationType)
            tempRegName = tempRegName1
        self.setVaribleValue(toVarible.name, "%" + tempRegName)

    def print(self, printString ,vars = [], printAs = None):

        printStringName = self.createUniqueRegister("printString");
        self.addPrintString(printStringName, printString)
        charCount = len(printString) + 1

        argsPrintString = ""
        for item in vars:
            varible0 = self.getVariable(item)
            valueVariable0 = self.createUniqueRegister(varible0.LLVMname)
            self._addLine(varible0.getLLVMLoadString(valueVariable0))
            type = varible0.type
            if varible0.getType() == float:
                uniqueReg = self.createUniqueRegister()
                self._addLine("%" + uniqueReg + " = fpext float %" + valueVariable0 + " to double")
                valueVariable0 = uniqueReg
            argsPrintString += type + " %" + valueVariable0 + ", "
        argsPrintString = argsPrintString[:-2]
        self._addLine("call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([" + str(charCount) + " x i8], [" + str(charCount) + " x i8]* @." + printStringName + ", i64 0, i64 0), " + argsPrintString + ")")

    def scan(self, printString ,vars = [], printAs = None):
        printStringName = self.createUniqueRegister("scanString");
        self.addPrintString(printStringName, printString)
        charCount = len(printString) + 1

        argsPrintString = ""
        for item in vars:
            varible0 = self.getVariable(item)
            valueVariable0 = self.createUniqueRegister(varible0.LLVMname)
            self._addLine(varible0.getLLVMLoadString(valueVariable0))
            type = varible0.type
            if varible0.getType() == float:
                uniqueReg = self.createUniqueRegister()
                self._addLine("%" + uniqueReg + " = fpext float %" + valueVariable0 + " to double")
                valueVariable0 = uniqueReg

            argsPrintString += type + "* %" + item + ", "
        argsPrintString = argsPrintString[:-2]
        self._addLine("call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([" + str(charCount) + " x i8], [" + str(charCount) + " x i8]* @." + printStringName + ", i64 0, i64 0), " + argsPrintString + ")")

    def printValue(self, value, printAs = int):
        type = "i32"
        format = "procentD"
        if (printAs == chr):
            format = "procentC"
        elif(printAs == float):
            format = "procentF"
            type = "double"

        self._addLine("call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @." + format + ", i64 0, i64 0), " + type + " " + str(value) + ")")

    def breakLoop(self):
        self.parantFunction.breakLoop()

    def continueLoop(self):
        self.parantFunction.continueLoop()

    def getFunctionType(self, functionName):
        return self.parantFunction.getFunctionType(functionName)

    def getFunctionCallTypes(self, functionName):
        return self.parantFunction.getFunctionCallTypes(functionName)

    def endOfFunction(self):
        defaultReturnItemDict = {"i32": 0, "void": "void", "float": "float"}
        if not self.returnItemSet:
            self.setReturnValue(defaultReturnItemDict[self.getFunctionType(self.functionName)])

class LLVMWhile(LLVMFunction):
    def __init__(self, uniqueName, parantFunction):
        self.loop = False
        self.parantFunction = parantFunction
        self.functionName = uniqueName
        self._addLineToFunctionNoTab("br label %" + "whileCondition_" + self.functionName)  #ga naar de while loop
        self._addLineToFunctionNoTab("\n" + "whileCondition_" + self.functionName + ":")          #start while condition
            #hier komt de conditie code
            #hier komt de

        #hier
    def setConditionVarable(self, varibleName):
        self.conditionVarible = varibleName

    def _addLine(self, line):
        self.parantFunction.programArray.insert(len(self.parantFunction.programArray) - 1, "\t" + line)  # create a new line to close the bracket

    def _addLineToFunctionNoTab(self, line):
        self.parantFunction.programArray.insert(len(self.parantFunction.programArray) - 1, line)  # create a new line to close the bracket

    def endOfContition(self):
        if self.loop == True:
            exit("Wrong use of while loop 1!")
        self.loop = True
        registername = self.createUniqueRegister("checkValueReg")
        self._addLine("%" + registername + " = load i32, i32* %" + self.conditionVarible + ", align 4")
        self._addLine("%conditionValue" + self.functionName + "= icmp eq i32 %" + registername + ", 1")
        self._addLine("br i1 %conditionValue" + self.functionName + ", label %" + "whileLoop_" + self.functionName + ", label %" + "endwhile_" + self.functionName)
        self._addLineToFunctionNoTab("\n" + "whileLoop_" + self.functionName + ":")  # start while loop

    def endOfLoop(self):
        if self.loop == False:
            exit("Wrong use of while loop 2!")
        self._addLine("br label %" + "whileCondition_" + self.functionName)  #ga naar de condition of while loop
        self._addLineToFunctionNoTab("\n" + "endwhile_" + self.functionName + ":")  # end while loop

    def breakLoop(self):
        self._addLine("br label %" + "endwhile_" + self.functionName)  # ga naar de condition of while loop

    def continueLoop(self):
        self._addLine("br label %" + "whileCondition_" + self.functionName)  # ga naar de condition of while loop

class LLVMIfElse(LLVMFunction):
    def __init__(self, uniqueName, parantFunction):
        self.condition = True
        self.parantFunction = parantFunction
        self.functionName = uniqueName

        #hier
    def setConditionVarable(self, varibleName):
        self.conditionVarible = varibleName

    def _addLine(self, line):
        self.parantFunction.programArray.insert(len(self.parantFunction.programArray) - 1, "\t" + line)  # create a new line to close the bracket

    def _addLineToFunctionNoTab(self, line):
        self.parantFunction.programArray.insert(len(self.parantFunction.programArray) - 1, line)  # create a new line to close the bracket

    def endOfIfContition(self):
        if self.condition != True:
            exit("Wrong use of if statment!")
        self.condition = False
        registername = self.createUniqueRegister("checkValueReg")
        self._addLine("%" + registername + " = load i32, i32* %" + self.conditionVarible + ", align 4")
        self._addLine("%conditionValue" + self.functionName + "= icmp eq i32 %" + registername + ", 1")
        self._addLine("br i1 %conditionValue" + self.functionName + ", label %" + "ifStatement_" + self.functionName + ", label %" + "elseStatement_" + self.functionName)
        self._addLineToFunctionNoTab("\n" + "ifStatement_" + self.functionName + ":")  # start while loop

    def endOfIfStatement(self):
        if self.condition != False:
            exit("Wrong use of if statement 2!")
        self._addLine("br label %" + "endIfElseStatement_" + self.functionName)  #ga naar de condition of while loop

    def startElse(self):
        self._addLineToFunctionNoTab("\n" + "elseStatement_" + self.functionName + ":")  # start while loop

    def endOfElseStatement(self):
        if self.condition != False:
            exit("Wrong use of if statement 2!")
        self._addLine("br label %" + "endIfElseStatement_" + self.functionName)  #ga naar de condition of while loop
        self._addLineToFunctionNoTab("\n" + "endIfElseStatement_" + self.functionName + ":")  # end while loop

class LLVMVarible:
    def __init__(self, name, type, align = 4):
        self.name = name
        self.LLVMname = name
        self.type = type
        self.align = align

    def getLLVMDecString(self):
        return "%" + self.LLVMname + " = alloca " + self.type + ", align " + str(self.align)

    def getType(self):
        if self.type == "float":
            return float
        elif self.type == "i8":
            return chr
        return int

    def getLLVMType(self):
        return self.type

    def getLLVMIniString(self, value):
        isRegister = False
        try:
            isRegister = value[0] == "%"
        except:
            print("not a register")

        if self.type == "float" and not isRegister:
            value = hex(struct.unpack('<Q', struct.pack('<d', value))[0])[:-7] +"0000000"#'{:.7e}'.format(value)
        elif self.type == "i8" and len(value) == 3 and value[0] == "'" and value[2] == "'":
            value = ord(value[1])

        return "store " + self.type + " " + str(value) + ", " + self.type + "* %" + self.LLVMname + ", align " + str(self.align)

    def getLLVMLoadString(self, loadAdress):
        return "%" + loadAdress + " = load " + self.type + ", " + self.type + "* %" + str(self.LLVMname) + ", align " + str(self.align)

    def loadPointerValueString(self, loadAdress):
        loadString = ""
        varType = self.type
        counter = 0
        currentAdress = loadAdress + str(counter)
        while "*" in varType:
            loadString += "%" + loadAdress + str(counter) + " = load " + varType + ", " + varType + "* %" + str(self.LLVMname) + ", align " + str(self.align) + "\n\t"
            varType = varType[:-1]
        loadString += "%" + loadAdress + " = load " + varType + ", " + varType + "* %" + loadAdress + str(counter) + ", align " + str(self.align)
        return loadString