import struct


class LLVMProgram:
    adressCounter = 0
    programArray = []
    VaribleList = {}
    def __init__(self):
        self.programArray.append('@.procentD = private unnamed_addr constant [3 x i8] c"%d\\00", align 1') #string %d needed to print ints
        self.programArray.append('@.procentC = private unnamed_addr constant [3 x i8] c"%c\\00", align 1')  # string %c needed to print chars
        self.programArray.append('@.procentF = private unnamed_addr constant [3 x i8] c"%f\\00", align 1')  # string %f needed to print floats
        self.programArray.append('declare dso_local i32 @printf(i8*, ...) #1')  # print function

    def addFunction(self, function):
        if(type(function) != LLVMFunction):
            exit("fout type")
        self.programArray = self.programArray + function.programArray

    def output(self):
        fullProgram = ""
        for line in self.programArray:
            fullProgram += "\n" + line
        return fullProgram

class LLVMFunction(LLVMProgram):
    def __init__(self, functionName, parantFunction = None, returnType = "i32"):
        self.parantFunction = parantFunction
        self.functionName = functionName
        self.programArray.append("define " + returnType + " @" + functionName + "() #0 {")
        self.programArray.append("}")

    def getVariable(self, name):
        if name in self.VaribleList:
            return self.VaribleList[name]
        elif self.parantFunction != None:
            return self.parantFunction.getVariable(name)
        return LLVMVarible(name, "i32")
        exit("varible bestaat niet:" + name)

    def setVariable(self, name, varible):
        self.VaribleList[name] = varible

    def _addLineToFunction(self, line):
        self.programArray.insert(len(self.programArray) - 1, line)  # create a new line to close the bracket

    def setReturnValue(self, value, type = "i32"):
        self._addLineToFunction("ret " + type + " " + str(value))

    def newVarible(self, name, type = "i32", align = 4):
        varible = LLVMVarible(name, type, align)
        self.setVariable(name, varible)
        self._addLineToFunction(varible.getLLVMDecString())

    def newSmartVarible(self, name, type):
        if type == int:
            self.newVarible(name, "i32", 4)
        elif type == chr:
            self.newVarible(name,  "i8", 1)
        elif type == float:
            self.newVarible(name,  "float", 4)

    def setVaribleValue(self, name, value):
        varible = self.getVariable(name);
        self._addLineToFunction(varible.getLLVMIniString(value))

    def operationOnVarible(self, toName, nameItem1, nameItem2, operation):
        operations = {"+": "add", "-": "sub", "*": "mul", "/": "sdiv", "<": "slt", ">": "sgt", "==": "eq", "!=": "ne", "<=": "sle",  ">=": "sge"  }

        toVarible = self.getVariable(toName)
        varible1 = self.getVariable(nameItem1)
        varible2 = self.getVariable(nameItem2)

        valueVariable1 = self.createUniqueRegister(varible1.LLVMname)
        self._addLineToFunction(varible1.getLLVMLoadString(valueVariable1))

        valueVariable2 = self.createUniqueRegister(varible2.LLVMname)
        self._addLineToFunction(varible2.getLLVMLoadString(valueVariable2))

        tempRegName = self.createUniqueRegister()
        self._addLineToFunction("%" + tempRegName + " = " + operations[operation] + " " + toVarible.type + " %" + valueVariable1 + ", %" + valueVariable2 + "")
        self.setVaribleValue(toVarible.name, "%" + tempRegName)

    def print(self, varName, printAs = int):
        varible0 = self.getVariable(varName)
        valueVariable0 = self.createUniqueRegister(varible0.LLVMname)
        self._addLineToFunction(varible0.getLLVMLoadString(valueVariable0))

        type = varible0.type
        format = "procentD"
        if (printAs == chr):
            format = "procentC"
        elif(printAs == float):
            format = "procentF"
            type = "double"
            uniqueReg = self.createUniqueRegister()
            self._addLineToFunction("%" + uniqueReg + " = fpext float %" + valueVariable0 + " to double")
            valueVariable0 = uniqueReg

        self._addLineToFunction("call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @." + format + ", i64 0, i64 0), " + type + " %" + valueVariable0 + ")")

    def printValue(self, value, printAs = int):
        type = "i32"
        format = "procentD"
        if (printAs == chr):
            format = "procentC"
        elif(printAs == float):
            format = "procentF"
            type = "double"

        self._addLineToFunction("call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @." + format + ", i64 0, i64 0), " + type + " " + str(value) + ")")

    def createUniqueRegister(self, addName = ""):
        self.adressCounter = self.adressCounter + 1
        print(addName,  self.functionName)
        return "uniq" + str(addName) + self.functionName + str(self.adressCounter)

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


    def _addLineToFunction(self, line):
        self.parantFunction.programArray.insert(len(self.parantFunction.programArray) - 1, "\t" + line)  # create a new line to close the bracket

    def _addLineToFunctionNoTab(self, line):
        self.parantFunction.programArray.insert(len(self.parantFunction.programArray) - 1, line)  # create a new line to close the bracket

    def endOfContition(self, varibleName):
        if self.loop == True:
            exit("Wrong use of while loop 1!")
        self.loop = True
        self._addLineToFunction("%conditionValue" + self.functionName + "= icmp eq i32 %" + varibleName + ", 1")
        self._addLineToFunction("br i1 %conditionValue" + self.functionName + ", label %" + "whileLoop_" + self.functionName + ", label %" + "endwhile_" + self.functionName)
        self._addLineToFunctionNoTab("\n" + "whileLoop_" + self.functionName + ":")  # start while loop

    def endOfLoop(self):
        if self.loop == False:
            exit("Wrong use of while loop 2!")
        self._addLineToFunction("br label %" + "whileCondition_" + self.functionName)  #ga naar de condition of while loop
        self._addLineToFunctionNoTab("\n" + "endwhile_" + self.functionName + ":")  # end while loop


class LLVMVarible:
    def __init__(self, name, type, align = 4):
        self.name = name
        self.LLVMname = name
        self.type = type
        self.align = align

    def getLLVMDecString(self):
        return "%" + self.LLVMname + " = alloca " + self.type + ", align " + str(self.align)

    def getLLVMIniString(self, value):
        if(self.type == "float"):
            value = hex(struct.unpack('<Q', struct.pack('<d', value))[0])

        return "store " + self.type + " " + str(value) + ", " + self.type + "* %" + self.LLVMname + ", align " + str(self.align)

    def getLLVMLoadString(self, loadAdress):
        return "%" + loadAdress + " = load " + self.type + ", " + self.type + "* %" + str(self.LLVMname) + ", align " + str(self.align)