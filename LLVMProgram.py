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
        for line in self.programArray:
            print(line)

class LLVMFunction(LLVMProgram):
    def __init__(self, functionName, returnType = "i32"):
        self.functionName = functionName
        self.programArray.append("define " + returnType + " @" + functionName + "() #0 {")
        self.programArray.append("}")

    def _addLineToFunction(self, line):
        self.programArray[len(self.programArray) - 1] = line #replace } with the new line
        self.programArray.append("}")                    #create a new line to close the bracket

    def setReturnValue(self, value, type = "i32"):
        self._addLineToFunction("ret " + type + " " + str(value))

    def newVarible(self, name, type = "i32", align = 4):
        varible = LLVMVarible(name, type, align)
        self.VaribleList[name] = varible
        self._addLineToFunction(varible.getLLVMDecString())

    def newSmartVarible(self, name, type):
        if type == int:
            self.newVarible(self, name, "i32", 4)
        elif type == chr:
            self.newVarible(self, name,  "i8", 1)
        elif type == float:
            self.newVarible(self, name,  "float", 4)

    def setVaribleValue(self, name, value):
        varible = self.VaribleList[name]
        self._addLineToFunction(varible.getLLVMIniString(value))

    def addVarible(self, toName, nameItem1, nameItem2):
        toVarible = self.VaribleList[toName]
        varible1 = self.VaribleList[nameItem1]
        varible2 = self.VaribleList[nameItem2]

        valueVariable1 = self.createUniqueRegister(varible1.LLVMname)
        self._addLineToFunction(varible1.getLLVMLoadString(valueVariable1))

        valueVariable2 = self.createUniqueRegister(varible2.LLVMname)
        self._addLineToFunction(varible2.getLLVMLoadString(valueVariable2))

        tempRegName = self.createUniqueRegister()
        self._addLineToFunction("%" + tempRegName + " = add " + toVarible.type + " %" + valueVariable1 + ", %" + valueVariable2 + "")
        self.setVaribleValue(toVarible.name, "%" + tempRegName)

    def print(self, varName, printAs = int):
        varible0 = self.VaribleList[varName]
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
            self._addLineToFunction(uniqueReg + " = fpext float " + valueVariable0 + " to double")
            valueVariable0 = uniqueReg

        self._addLineToFunction("call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @." + format + ", i64 0, i64 0), " + type + " %" + valueVariable0 + ")")

    def createUniqueRegister(self, addName = ""):
        self.adressCounter = self.adressCounter + 1
        return "uniq" + addName + self.functionName + str(self.adressCounter)

class LLVMVarible:
    def __init__(self, name, type, align = 4):
        self.name = name
        self.LLVMname = name
        self.type = type
        self.align = align

    def getLLVMDecString(self):
        return "%" + self.LLVMname + " = alloca " + self.type + ", align " + str(self.align)

    def getLLVMIniString(self, value):
        return "store " + self.type + " " + str(value) + ", " + self.type + "* %" + self.LLVMname + ", align " + str(self.align)

    def getLLVMLoadString(self, loadAdress):
        return "%" + loadAdress + " = load " + self.type + ", " + self.type + "* %" + self.LLVMname + ", align " + str(self.align)