import struct

class MipsVariable:
    def __init__(self, name, register, stackPointerOffset, isGlobal = False):
        self.name = name
        self.register = register
        self.isGlobal = isGlobal
        if isGlobal == False:
            self.stackPointerOffset = stackPointerOffset
        if register != None:
            MipsProgram.registers[register[1]][register] = self

    def updateRegister(self, toReg):
        if self.register != None:
            MipsProgram.registers[self.register[1]][self.register] = None
        if toReg != None:
            MipsProgram.registers[toReg[1]][toReg] = self
        self.register = toReg

    def getMemoryLocation(self):
        if self.isGlobal:
            return self.name
        return str(self.stackPointerOffset) + "($fp)"

    def getLocationOfsetString(self):
        if self.isGlobal:
            return self.name
        return " $fp, " + str(self.stackPointerOffset)


class MipsArray(MipsVariable):
    def __init__(self, name, register, stackStartOfArrayOffset, length, isGlobal = False):
        super(MipsArray, self).__init__(name, register, stackStartOfArrayOffset,isGlobal)
        self.lenght = length

    def getStartOfArrayOffset(self):
        return self.stackPointerOffset

    def getLocationOfsetString(self):
        if self.isGlobal:
            return self.name
        return " $fp, " + str(self.stackPointerOffset)

    def updateRegister(self, toReg):
        exit("regiset of mipsarray cannot be set")



class MipsProgram:
    stackPointer = 0
    framePointer = 0
    dataArray = []
    programmArray = []
    mipsTypes = {int: ".word", float: ".float", chr: ".word"}
    variables = {}
    dataCounter = 0
    ifElseCounter = 0
    whileCounter = 0
    defaultTabInpring = 0
    allUsedRegistersInCurrentFunction = []
    stackAllocationOfCurrentFunction = 0
    currentFunctionName = ""
    scanfCounter = 0
    #blijft autmoatisch up to date
    #None: no value
    #True: lockt for calculations
    #type=Mipsvariable: same value as a item on the stack
    registers = {"t": {"$t" + str(t) : None for t in range(10)},
                 "s": {"$s" + str(s): None for s in range(8)},
                 "a": {"$a" + str(a): None for a in range(4)},
                 "v": {"$v" + str(v): None for v in range(2)},
                 "f": {"$f" + str(f): None for f in range(32)}}

    def __init__(self, AST, file_name):
        AST.CreateMipsCode()
        with open(file_name, 'w') as myFile:
            myFile.write(".data\n")
            for line in self.dataArray:
                myFile.write(line+"\n")
            myFile.write(".text\n")
            myFile.write(".globl main\n")
            myFile.write("b\tmain\n")
            for line in self.programmArray:
                myFile.write(line+"\n")

        self.programmArray.clear()
        self.dataArray.clear()
        pass

    def write(self):
        #self.currentFunction.setReturnValue(0)
        with open(self.file_name, 'w') as myFile:
            myFile.write(self.program.output())
            myFile.close()

    @staticmethod
    def addLineToProgramArray(line: str, inspring: int = 0, comments: str=""):
        """
        Add a line to thr program array (.text part of the mips code)
        :param line: string with mips code
        :param inspring: tab count
        :return: None
        """
        if comments != "":
            comments = "\t\t # "+comments
        MipsProgram.programmArray.append((inspring * "\t") + (MipsProgram.defaultTabInpring * "\t") + line + comments)

    @staticmethod
    def addDataNumberLineToDataArray(line: str, comments: str=""):
        """
        Add a line to the data array (.data part of the mips code)
        :param line:
        :return:
        """
        if comments != "":
            comments = "\t\t # "+comments
        name = "data"+str(MipsProgram.dataCounter)
        MipsProgram.dataArray.append("\t" + name + ":\t" + line + comments)
        MipsProgram.dataCounter+=1
        return name

    @staticmethod
    def addDataLineToDataArray(line: str, comments: str = ""):
        """
        Add a line to the data array (.data part of the mips code)
        :param line:
        :return:
        """
        if comments != "":
            comments = "\t\t # " + comments
        MipsProgram.dataArray.append("\t" + line + comments)


    @staticmethod
    def startOfFunction(functionName):
        """
        Funtion to add the start code for a function (stack pointer)
        :param reserve: How many bytes need to be allocate for this function
        :return: None
        """
        MipsProgram.currentFunctionName = functionName
        MipsProgram.addLineToProgramArray(functionName + ":")
        MipsProgram.addLineToProgramArray("sw\t$fp, 0($sp)", 1, "push oude frame pointer")
        MipsProgram.addLineToProgramArray("move\t$fp, $sp", 1,  "frame pointer wijst nu naar bovenaan de stack")
        MipsProgram.stackAllocationOfCurrentFunction = len(MipsProgram.programmArray)
        #Allocation wil be done on function end and will be iserted here
        MipsProgram.addLineToProgramArray("sw\t$ra, -4($fp)", 1, "slaag het return adress op op de stack")
        MipsProgram.stackPointer = -8

    @staticmethod
    def endOfFunction(reserve):
        """
        Funtion to add the end code for a function (returns to previeus function)
        :return: None
        """
        reserve += 8
        allocLocation = MipsProgram.stackAllocationOfCurrentFunction
        allocSpace = len(MipsProgram.allUsedRegistersInCurrentFunction) * 4
        MipsProgram.programmArray.insert(allocLocation, "\tsubu\t$sp, $sp, " + str(reserve + allocSpace) + "\t#stackpointer alloc") #insert at the beginning of the function

        MipsProgram.addLineToProgramArray("endOf" + MipsProgram.currentFunctionName + ":", 1, "For returns")

        if MipsProgram.currentFunctionName != "main":
            for register in MipsProgram.allUsedRegistersInCurrentFunction:
                storeOperation = "sw"
                loadOperation = "lw"
                if MipsProgram.checkRegister(register) is float:
                    storeOperation = "swc1"
                    loadOperation = "lwc1"
                MipsProgram.programmArray.insert(allocLocation + 1, "\t"+storeOperation+"\t" + register + ", " + str(MipsProgram.stackPointer) + "($fp)\t\t#safe all registers that we will use in the stack")
                MipsProgram.addLineToProgramArray(loadOperation+"\t" + register + ", " + str(MipsProgram.stackPointer) + "($fp)", 1, "load register value from before this function")
                MipsProgram.stackPointer -= 4


            MipsProgram.addLineToProgramArray("lw\t$ra, -4($fp)",1 ,"zet het return adres terug")
            MipsProgram.addLineToProgramArray("move\t$sp, $fp", 1)
            MipsProgram.addLineToProgramArray("move\t$fp, $sp", 1, "frame pointer wijst nu naar bovenaan de stack")
            MipsProgram.addLineToProgramArray("lw\t$fp, 0($sp)", 1, "zet oude frame pointer terug")
            MipsProgram.addLineToProgramArray("jr\t$ra", 1, "ga terug naar de aanroeper")
        else:
            MipsProgram.addLineToProgramArray("li\t$v0, 10", 1)
            MipsProgram.addLineToProgramArray("syscall\t", 1, "End of program")
        MipsProgram.stackPointer = 0
        MipsProgram.stackAllocationOfCurrentFunction = 0
        MipsProgram.allUsedRegistersInCurrentFunction = []

    @staticmethod
    def storeVariable(varName, currentRegisterLocation, isGLobal = False):
        """
        Make a new variable for an item currently in a register (store word + safes in dict's and changes the stackpointer)
        :param varName: the varname
        :param currentRegisterLocation: the register
        :return: None
        """
        storeOperation = "sw"
        if currentRegisterLocation[1] == 'f':
            storeOperation = "swc1"

        MipsProgram.checkRegister(currentRegisterLocation)
        MipsProgram.addRegisterToUsedFunctionRegister(currentRegisterLocation)
        MipsProgram.variables[varName] = MipsVariable(varName, currentRegisterLocation, MipsProgram.stackPointer)
        MipsProgram.addLineToProgramArray(storeOperation+"\t" + currentRegisterLocation + ", " + str(MipsProgram.stackPointer) + "($fp)", 1, "store variable: " + varName)
        MipsProgram.stackPointer -= 4


    @staticmethod
    def loadVariable(varName, toStoreRegister):
        """
        loads a variable to a given register (auto choose between move and lw depending on the current state)
        :param varName: the name of the var in the AST
        :param toStoreRegister: the name of te register to load to
        :return: None
        """
        MipsProgram.checkVariable(varName)
        MipsProgram.checkRegister(toStoreRegister)
        MipsProgram.addRegisterToUsedFunctionRegister(toStoreRegister)

        loadOperation = "lw"
        moveOperation = "move"
        if toStoreRegister[1] == 'f':
            loadOperation = "lwc1"
            moveOperation = "mov.s"

        if MipsProgram.variables[varName].register != None:
            #indien de variable nog in een register zit
            fromRegister = MipsProgram.variables[varName].register
            MipsProgram.addLineToProgramArray(moveOperation+"\t" + toStoreRegister + ", " + fromRegister, 1, "Load variable " + varName)
        else:
            #indien de variable uit het geheugen geladen moet worden
            memoryLocation = MipsProgram.variables[varName].getMemoryLocation()
            MipsProgram.addLineToProgramArray(loadOperation+"\t" + toStoreRegister + ", " + str(memoryLocation), 1, "Load variable " + varName)



    @staticmethod
    def updateVariable(varName, toRegisterValue):
        """
        Change a varible to a new value, and update all registers
        :param varName: varible to update
        :param toRegisterValue: register with value
        :return:
        """
        print("testtesttest", varName, toRegisterValue)
        MipsProgram.addRegisterToUsedFunctionRegister(toRegisterValue)
        if varName in MipsProgram.variables:
            storeOperation = "sw"
            if toRegisterValue[1] == 'f':
                storeOperation = "swc1"
            MipsProgram.addLineToProgramArray(storeOperation+"\t" + toRegisterValue + ", " + MipsProgram.variables[varName].getMemoryLocation(), 1,"update variable: " + varName)
            MipsProgram.variables[varName].updateRegister(toRegisterValue)
        else:
            exit("Varible does not exists")

    @staticmethod
    def createArray(arrayName, lenght):
        MipsProgram.variables[arrayName] = MipsArray(arrayName, None,MipsProgram.stackPointer, lenght)
        MipsProgram.stackPointer -= (4 * lenght) #reserve space for all elements

    @staticmethod
    def loadArray(arrayName, arrayIndexRegister, toStoreRegister):
        """
        loads a variable to a given register (auto choose between move and lw depending on the current state)
        :param varName: the name of the var in the AST
        :param toStoreRegister: the name of te register to load to
        :return: None
        """
        MipsProgram.checkVariable(arrayName)
        MipsProgram.checkRegister(arrayIndexRegister)
        MipsProgram.checkRegister(toStoreRegister)
        MipsProgram.addRegisterToUsedFunctionRegister(arrayIndexRegister)
        MipsProgram.addRegisterToUsedFunctionRegister(toStoreRegister)

        arrayItemLocation = MipsProgram.getFreeRegister("t")
        # indien de variable uit het geheugen geladen moet worden
        locationOfsetString = MipsProgram.variables[arrayName].getLocationOfsetString()
        if MipsProgram.variables[arrayName].isGlobal:
            MipsProgram.addLineToProgramArray("la\t" + arrayItemLocation + "," + locationOfsetString, 1, "calculate array location")
        else:
            MipsProgram.addLineToProgramArray("subi\t" + arrayItemLocation + ", " + locationOfsetString,1, "calculate array location")
        four = MipsProgram.getFreeRegister("t")
        MipsProgram.addLineToProgramArray("li\t" + four + ", 4",1, "calculate array location")
        MipsProgram.releaseRegister(four)
        MipsProgram.addLineToProgramArray("mul\t" + arrayIndexRegister + ", " + arrayIndexRegister + ", " + four,1, "calculate array location")
        MipsProgram.addLineToProgramArray("add\t" + arrayItemLocation + ", " + arrayItemLocation + ", " + arrayIndexRegister,1, "calculate array location")
        MipsProgram.addLineToProgramArray("lw\t" + toStoreRegister + ", (" + arrayItemLocation + ")", 1,"Load variable " + arrayName + "[" + arrayIndexRegister +"]")
        MipsProgram.releaseRegister(arrayItemLocation)

    @staticmethod
    def updateArray(arrayName, arrayIndexRegister, toRegisterValue):
        """
        Change a varible to a new value, and update all registers
        :param varName: varible to update
        :param toRegisterValue: register with value
        :return:
        """
        MipsProgram.checkVariable(arrayName)
        MipsProgram.checkRegister(arrayIndexRegister)
        MipsProgram.checkRegister(toRegisterValue)
        MipsProgram.addRegisterToUsedFunctionRegister(arrayIndexRegister)
        MipsProgram.addRegisterToUsedFunctionRegister(toRegisterValue)

        arrayItemLocation = MipsProgram.getFreeRegister("t")
        # indien de variable uit het geheugen geladen moet worden
        locationOfsetString = MipsProgram.variables[arrayName].getLocationOfsetString()
        if MipsProgram.variables[arrayName].isGlobal:
            MipsProgram.addLineToProgramArray("la\t" + arrayItemLocation + "," + locationOfsetString, 1,"calculate array location")
        else:
            MipsProgram.addLineToProgramArray("subi\t" + arrayItemLocation + ", " + locationOfsetString,1, "calculate array location")

        four = MipsProgram.getFreeRegister("t")
        MipsProgram.addLineToProgramArray("li\t" + four + ", 4", 1, "calculate array location")
        MipsProgram.releaseRegister(four)
        MipsProgram.addLineToProgramArray("mul\t" + arrayIndexRegister + ", " + arrayIndexRegister + ", " + four,1, "calculate array location")
        MipsProgram.addLineToProgramArray("add\t" + arrayItemLocation + ", " + arrayItemLocation + ", " + arrayIndexRegister,1, "calculate array location")
        MipsProgram.addLineToProgramArray("sw\t" + toRegisterValue + ", (" + arrayItemLocation + ")", 1,"Load variable " + arrayName + "[" + arrayIndexRegister +"]")
        MipsProgram.releaseRegister(arrayItemLocation)

    @staticmethod
    def registerToBit(registerName):
        MipsProgram.addLineToProgramArray("sgt\t" + registerName + ", " + registerName + ", 0", 1, "convert register to 0 or 1")

    @staticmethod
    def checkRegister(register):
        """
        Function to check if register is valid
        :param register:
        :return:
        """
        if len(register) <= 1:
            exit("incorrect register")
        if register[0] != "$":
            exit("Register stars with $")


        #return type of register
        if register[1] == 'f':
            return float
        else:
            return int

    @staticmethod
    def checkVariable(varName):
        """
        function to check is variable is valid
        :param varName:
        :return:
        """
        if not varName in MipsProgram.variables:
            exit("variable not found")

    @staticmethod
    def getFreeRegister(registerCat: chr):
        """
        Get a free register, if there are no free registers, clears all registers (all data is saved on the stack) an returns the first
        :return:
        """
        #zoek voor een vrij register
        for tReg in MipsProgram.registers[registerCat]:
            if MipsProgram.registers[registerCat][tReg] == None:
                MipsProgram.registers[registerCat][tReg] = True
                MipsProgram.addRegisterToUsedFunctionRegister(tReg)
                return tReg #retrun een vrij register

        #TODO evnetueel meer geavanceerde code, momenteel clear an temp register with a variable already saved to the stack
        for tReg in MipsProgram.registers[registerCat]:
            if type(MipsProgram.registers[registerCat][tReg]) == MipsVariable:
                MipsProgram.registers[registerCat][tReg].updateRegister(None)
                MipsProgram.addRegisterToUsedFunctionRegister(tReg)
                return tReg
        exit("uh oh")

    @staticmethod
    def releaseRegister(register):
        """
        Call this function every time a register can be released
        :param register: register name to release
        :return:
        """
        if MipsProgram.registers[register[1]][register] == True or MipsProgram.registers[register[1]][register] == None:
            MipsProgram.registers[register[1]][register] = None

    @staticmethod
    def releaseAllRegisters(registerCat: chr = '*', expect = None):
        """
        Call this function to reset all registers to a None state
        :param register: register name to release
        :return:
        """
        if registerCat == '*':
            MipsProgram.releaseAllRegisters('t',expect)
            MipsProgram.releaseAllRegisters('s',expect)
            MipsProgram.releaseAllRegisters('a',expect)
            MipsProgram.releaseAllRegisters('v',expect)
            return

        for tReg in MipsProgram.registers[registerCat]:
            if tReg != expect:
                if type(MipsProgram.registers[registerCat][tReg]) == MipsVariable:
                    MipsProgram.registers[registerCat][tReg].updateRegister(None)
                MipsProgram.registers[registerCat][tReg] = None

    @staticmethod
    def releaseAllMipsVaribleFromRegisters(registerCat: chr = '*'):
        """
        Call this function to reset all registers to a None state
        :param register: register name to release
        :return:
        """
        if registerCat == '*':
            MipsProgram.releaseAllMipsVaribleFromRegisters('t')
            MipsProgram.releaseAllMipsVaribleFromRegisters('s')
            MipsProgram.releaseAllMipsVaribleFromRegisters('a')
            MipsProgram.releaseAllMipsVaribleFromRegisters('v')
            return

        for tReg in MipsProgram.registers[registerCat]:
            if type(MipsProgram.registers[registerCat][tReg]) == MipsVariable:
                MipsProgram.registers[registerCat][tReg].updateRegister(None)
                MipsProgram.registers[registerCat][tReg] = None

    @staticmethod
    def getVarByRegisterName(register):
        """
        Returns the var name from MipsVariable currently also safed in a register
        :param register:
        :return:
        """
        if MipsProgram.registers[register[1]][register] != None and MipsProgram.registers[register[1]][register] != True:
            return MipsProgram.registers[register[1]][register].name
        else:
            exit("If you are here you did something wrong (getVarByRegisterName is not the function you need to call)")



    @staticmethod
    def floatToIntConversion(fRegister):
        if MipsProgram.checkRegister(fRegister) is not float:
            return fRegister
        tRegister = MipsProgram.getFreeRegister('t')
        MipsProgram.addLineToProgramArray("cvt.w.s\t" + fRegister + ", " + fRegister, 1)
        MipsProgram.addLineToProgramArray("mfc1\t" + tRegister + ", " + fRegister, 1)
        MipsProgram.releaseRegister(fRegister)
        return tRegister

    @staticmethod
    def intToFloatConversion(tRegister):
        if MipsProgram.checkRegister(tRegister) is float:
            return tRegister
        fRegister = MipsProgram.getFreeRegister('f')
        MipsProgram.addLineToProgramArray("mtc1\t" + tRegister + ", " + fRegister, 1)
        MipsProgram.releaseRegister(tRegister)
        MipsProgram.addLineToProgramArray("cvt.s.w\t" + fRegister + ", " + fRegister, 1)
        MipsProgram.releaseRegister(tRegister)
        return fRegister

    @staticmethod
    def addRegisterToUsedFunctionRegister(register):
        print("reserve register:" + register)
        if not register in MipsProgram.allUsedRegistersInCurrentFunction:
            MipsProgram.allUsedRegistersInCurrentFunction.append(register)