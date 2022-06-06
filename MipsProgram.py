import struct

class MipsVariable:
    def __init__(self, name, register, stackPointerOffset):
        self.name = name
        self.register = register
        self.stackPointerOffset = stackPointerOffset
        MipsProgram.registers[register[1]][register] = self

    def updateRegister(self, toReg):
        if self.register != None:
            MipsProgram.registers[self.register[1]][self.register] = None
        if toReg != None:
            MipsProgram.registers[toReg[1]][toReg] = self
        self.register = toReg


class MipsProgram:
    stackPointer = 0
    framePointer = 0
    dataArray = []
    programmArray = []
    mipsTypes = {int: ".word"}
    variables = {}
    dataCounter = 0
    #blijft autmoatisch up to date
    #None: no value
    #True: lockt for calculations
    #type=Mipsvariable: same value as a item on the stack
    registers = {"t": {"$t" + str(t) : None for t in range(0,10)},
                 "s": {"$s" + str(s): None for s in range(0, 8)},
                 "a": {"$a" + str(a): None for a in range(0, 4)},
                 "v": {"$v" + str(v): None for v in range(0, 2)}}

    def __init__(self, AST):
        AST.CreateMipsCode()
        print(".data")
        for line in self.dataArray:
            print(line)
        print(".text")
        print(".globl main")
        for line in self.programmArray:
            print(line)
        pass

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
        MipsProgram.programmArray.append((inspring * "\t") + line + comments)

    @staticmethod
    def addLineToDataArray(line: str):
        """
        Add a line to the data array (.data part of the mips code)
        :param line:
        :return:
        """

        name = "data"+str(MipsProgram.dataCounter)
        MipsProgram.dataArray.append("\t" + name + ":\t" + line)
        MipsProgram.dataCounter+=1
        return name


    @staticmethod
    def startOfFunction(reserve = 0):
        """
        Funtion to add the start code for a function (stack pointer)
        :param reserve: How many bytes need to be allocate for this function
        :return: None
        """
        reserve += 4 #allacte for return adress
        MipsProgram.addLineToProgramArray("sw\t$fp, 0($sp)", 1, "push oude frame pointer")
        MipsProgram.addLineToProgramArray("move\t$fp, $sp", 1,  "frame pointer wijst nu naar bovenaan de stack")
        MipsProgram.addLineToProgramArray("subu\t$sp, $sp, " + str(reserve), 1)
        MipsProgram.addLineToProgramArray("sw\t$ra, -4($fp)", 1, "slaag het return adress op op de stack")
        MipsProgram.stackPointer = -8

    @staticmethod
    def endOfFunction():
        """
        Funtion to add the end code for a function (returns to previeus function)
        :return: None
        """
        MipsProgram.addLineToProgramArray("lw\t$ra, -4($fp)",1 ,"zet het return adres terug")
        MipsProgram.addLineToProgramArray("move\t$sp, $fp", 1)
        MipsProgram.addLineToProgramArray("move\t$fp, $sp", 1, "frame pointer wijst nu naar bovenaan de stack")
        MipsProgram.addLineToProgramArray("lw\t$fp, ($sp)", 1, "zet oude frame pointer terug")
        MipsProgram.addLineToProgramArray("jr\t$ra", 1, "ga terug naar de aanroeper")
        MipsProgram.stackPointer = 0

    @staticmethod
    def storeVariable(varName, currentRegisterLocation):
        """
        Make a new variable for an item currently in a register (store word + safes in dict's and changes the stackpointer)
        :param varName: the varname
        :param currentRegisterLocation: the register
        :return: None
        """
        MipsProgram.checkRegister(currentRegisterLocation)
        MipsProgram.variables[varName] = MipsVariable(varName, currentRegisterLocation, MipsProgram.stackPointer)
        MipsProgram.addLineToProgramArray("sw\t" + currentRegisterLocation + ", " + str(MipsProgram.stackPointer) + "($fp)", 1, "store variable: " + varName)
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

        if MipsProgram.variables[varName].register != None:
            #indien de variable nog in een register zit
            fromRegister = MipsProgram.variables[varName].register
            MipsProgram.addLineToProgramArray("move\t" + toStoreRegister + ", " + fromRegister, 1, "Load variable " + varName)
        else:
            #indien de variable uit het geheugen geladen moet worden
            stackPointerOffset = MipsProgram.variables[varName].stackPointerOffset
            MipsProgram.addLineToProgramArray("lw\t" + toStoreRegister + ", " + str(stackPointerOffset) + "($fp)", 1, "Load variable " + varName)

    @staticmethod
    def updateVariable(varName, toRegisterValue):
        """
        Change a varible to a new value, and update all registers
        :param varName: varible to update
        :param toRegisterValue: register with value
        :return:
        """
        if varName in MipsProgram.variables:
            MipsProgram.addLineToProgramArray("sw\t" + toRegisterValue + ", " + str(MipsProgram.variables[varName].stackPointerOffset) + "($fp)", 1,"update variable: " + varName)
            MipsProgram.variables[varName].updateRegister(toRegisterValue)
        else:
            exit("Varible does not exists")

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
        if register[0] != "$":
            exit("Register stars with $")

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
                return tReg #retrun een vrij register

        #TODO evnetueel meer geavanceerde code, momenteel clear an temp register with a variable already saved to the stack
        for tReg in MipsProgram.registers[registerCat]:
            if type(MipsProgram.registers[registerCat][tReg]) == MipsVariable:
                MipsProgram.registers[registerCat][tReg].updateRegister(None)
                return tReg
        print("uh oh")

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
    def releaseAllRegisters(registerCat: chr):
        """
        Call this function every time a register can be released
        :param register: register name to release
        :return:
        """
        for tReg in MipsProgram.registers[registerCat]:
            if type(MipsProgram.registers[registerCat][tReg]) == MipsVariable:
                MipsProgram.registers[registerCat][tReg].updateRegister(None)

    @staticmethod
    def getVarByRegisterName(register):
        """
        Returns the var name from MipsVariable currently also safed in a register
        :param register:
        :return:
        """
        print("register", register)
        if MipsProgram.registers[register[1]][register] != None and MipsProgram.registers[register[1]][register] != True:
            return MipsProgram.registers[register[1]][register].name
        else:
            exit("If you are here you dit somthing wrong (getVarByRegisterName is not the function you need to call)")