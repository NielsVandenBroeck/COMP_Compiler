import operator
from typing import Any
from pydoc import locate
from MipsProgram import MipsProgram
import graphviz

class AST():
    def __init__(self, root, line, position, childNodes = None):
        self.root = root
        self.nodes = childNodes
        self.line = line
        self.position = position

    def getValue(self):
        return self.root

    # internal function
    def setNodesIfNeeded(self):
        if self.nodes is None:
            self.nodes = []

    # adds a node
    def addNode(self, node):
        self.setNodesIfNeeded()
        self.nodes.append(node)

    def getFirstNonConst(self, node):
        if isinstance(node, ASTConst):
            return self.getFirstNonConst(node.nodes[0])
        return node

    def addNodeToMostLeftChild(self, node):
        if self.nodes is None:
            self.addNode(node)
            return
        self.nodes[0].addNodeToMostLeftChild(node)

    def isPriority(self):
        return self.root == "()"

    def removePriority(self):
        if(self.isPriority()):
            return self.nodes[0]
        return self

    #returns de node with index "item"
    def getNode(self, item):
        return self.nodes[item]

    def getDot(self):
        return "digraph G { \n" + self.getDotInternal(0) + "}"

    def getDotInternal(self, number = 0): #TODO kan efficienter
        test = graphviz.Digraph('AST')
        id = ' (' + str(number) + ')'
        idPlusOne = ' (' + str(number + 1) + ')'
        string = ""
        if self.nodes is None:
            return ""

        string += '"' + str(self) + id + '"' + '[label="' + str(self.root) + '"]' + "\n"
        for node in self.nodes:
            string += '"' + str(node) + idPlusOne + '"' + '[label="' + str(node.root) + '"]' + "\n"
            string += '"' + str(self) + id + '"' + "->" + '"' + str(node) + idPlusOne + '"' +"\n"
            string += node.getDotInternal(number + 1)

        return string

    def constantFold(self):
        dict1 = {'||': 0, '&&': 1, '<': 2, '>': 2, '==': 2, '<=': 2, '>=': 2, '!=': 2, '+': 3, '-': 3, '*': 4, '/': 4,
                 '%': 4}

        if self.nodes is None:
            return
        for i in self.nodes:
            i.constantFold()
        # unary -
        if len(self.nodes) == 1 and self.root == '-':
            # cannot convert variable that can still change. for example in loops or functions
            if type(self.nodes[0]) is ASTVariable:
                return
            value1 = self.nodes[0].root
            if isinstance(value1, float):
                self.root = -value1
                self.__class__ = ASTFloat
            elif isinstance(value1, int):
                self.root = -value1
                self.__class__ = ASTInt
            elif isinstance(value1, str):
                self.root = chr(-ord(value1[1]))
                self.__class__ = ASTChar
            self.nodes = None
        # unary +
        elif len(self.nodes) == 1 and self.root == '+':
            self.__class__ = type(self.nodes[0])
            self.root = self.nodes[0].root
            self.nodes = None
        #negation bv: !8
        elif len(self.nodes) == 1 and self.root == '!':
            value = self.nodes[0].root
            # cannot convert variable that can still change. for example in loops or functions
            if type(self.nodes[0]) is ASTVariable:
                return
            if isinstance(value, float):
                self.root = float(not value)
                self.__class__ = ASTFloat
            elif isinstance(value, int):
                self.root = int(not value)
                self.__class__ = ASTInt
            elif isinstance(value, str):
                self.root = chr(int(not value))
                self.__class__ = ASTChar
            else:
                print('errorr')
            self.nodes = None
        # all operations bv: 3+4
        elif len(self.nodes) == 2:
            # cannot convert variable that can still change. for example in loops or functions
            if type(self.nodes[0]) is ASTVariable or type(self.nodes[1]) is ASTVariable:
                return
            value1 = self.nodes[0].root
            value2 = self.nodes[1].root
            if self.root in dict1 and (
                    isinstance(value1, float) or isinstance(value1, int) or isinstance(value1, str)) and (
                    isinstance(value2, float) or isinstance(value2, int) or isinstance(value2, str)):
                if (isinstance(value1, str) and (len(value1) != 3 or value1[0] != '\'')) or (
                        isinstance(value2, str) and (len(value2) != 3 or value2[0] != '\'')):
                    return
                resulttype = chr
                if isinstance(value1, float) or isinstance(value2, float):
                    resulttype = float
                elif isinstance(value1, int) or isinstance(value2, int):
                    resulttype = int
                if isinstance(value1, str):
                    value1 = ord(value1[1])
                if isinstance(value2, str):
                    value2 = ord(value2[1])
                ops = {
                    '&&': operator.and_,
                    '||': operator.or_,
                    '<': operator.lt,
                    '>': operator.gt,
                    '>=': operator.ge,
                    '<=': operator.le,
                    '!=': operator.ne,
                    '==': operator.eq,
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv,
                    '%': operator.mod,
                }
                #cannot do || and && on floats or chars.
                if self.root == '||' or self.root == '&&':
                    resulttype = int
                    value1 = int(value1+0.5)
                    value2 = int(value2+0.5)
                    if value1 != 0:
                        value1 = 1
                    if value2 != 0:
                        value2 = 1
                #boolean expressions should return a boolean (int 0 or 1)
                elif self.root == '!=' or self.root == '==' or self.root == '<=' or self.root == '>=' or self.root == '>' or self.root == '<':
                    resulttype = int
                if resulttype == chr:
                    self.root = '\'' + resulttype(ops[self.root](value1, value2)) + '\''
                else:
                    self.root = resulttype(ops[self.root](value1, value2))
                self.nodes = None
                if resulttype == chr:
                    self.__class__ = ASTChar
                elif resulttype == float:
                    self.__class__ = ASTFloat
                elif resulttype == int:
                    self.__class__ = ASTInt

    def correctDataType(self,destinationType):
        if type(self) is ASTFunctionName:
            return
        self.constantFold()
        if self.nodes is not None:
            return
        originalType = type(self.root)
        originalValue = self.root
        conversion = False
        if destinationType == originalType:
            return
        if isinstance(self.root,str):
            self.root = self.root[1]
        if destinationType is float or destinationType is int:
            conversion = True
            if originalType is float or originalType is int:
                self.root = destinationType(self.root)
            else:
                self.root = destinationType(ord(self.root))
            if destinationType is float:
                self.__class__ = ASTFloat
            elif destinationType is int:
                self.__class__ = ASTInt
        elif destinationType is chr:
            if originalType is str:
                self.root = '\''+self.root+'\''
            else:
                conversion = True
                self.root = '\'' + chr(int((self.root))) + '\''
            self.__class__ = ASTChar
        #if conversion:
        #    print("[Warning] line: " + str(self.line) + ", position: " + str(
        #        self.position) + ". Implicit conversion from "+str(originalType) +" to "+ str(destinationType) +" changes value from "+ str(originalValue) +" to " + str(self.root) +".")

    def findType(self):
        intOps = ['||', '&&', '<', '>', '==', '<=','>=','!=','+','-','/','*','%']
        typeDict = {float: 0, int: 1, chr: 2}
        if type(self) is ASTOperator:
            if self.root in intOps:
                return int
            if len(self.nodes) == 1:
                return self.nodes[0].findType()
            elif len(self.nodes) == 2:
                type1 = self.nodes[0].findType()
                type2 = self.nodes[1].findType()
                if typeDict[type1] <= typeDict[type2]:
                    return type1
                else:
                    return type2
        elif type(self) is ASTVariable or type(self) is ASTInt or type(self) is ASTFloat or type(self) is ASTChar:
            return self.getType()
        elif type(self) is ASTPointer:
            return self.nodes[0].findType()
        elif type(self) is ASTFunctionName:
            return self.getType()

    def getIndex(self):#TODO
        return None

    def getIndexItem(self):
        return None

    def CreateMipsCode(self):
        if self.nodes != None:
            for node in self.nodes:
                node.CreateMipsCode()

    def neededStackSpace(self):
        total = 0
        if self.nodes != None:
            for node in self.nodes:
                total += node.neededStackSpace()
        return total

    def getPointerDept(self):
        return 0

#OK
class ASTFunction(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getReturnType(self):
        return self.nodes[0].root

    def getType(self):
        return self.nodes[0].root

    def getFunctionName(self):
        return self.nodes[1].root

    def getParameters(self):
        if len(self.nodes) == 4:
            return self.nodes[2]
        return []

    def getParametersList(self):
        if len(self.nodes) == 4:
            return self.nodes[2].nodes
        return []

    def getScope(self):
        if len(self.nodes) == 4:
            return self.nodes[3]
        return self.nodes[2]

    def neededStackSpace(self):
        totalForParameters = 0
        totalForScope = self.getScope().neededStackSpace()
        if self.getParameters() != []:
            totalForParameters = self.getParameters().neededStackSpace()
        return totalForScope+totalForParameters + 4

    def CreateMipsCode(self):
        MipsProgram.addLineToProgramArray(self.getFunctionName() + ":")
        MipsProgram.startOfFunction(self.neededStackSpace())
        aCounter = 0
        for param in self.getParametersList():
            param.CreateMipsCode()
            MipsProgram.updateVariable(param.getVariableName(), "$a" + str(aCounter))
            aCounter+=1
        MipsProgram.releaseAllRegisters('a')
        self.getScope().CreateMipsCode()
        MipsProgram.endOfFunction()

#OK
class ASTFunctionName(AST):
    def __init__(self, value, line, position, childNodes=None):
        self.type = None
        super().__init__(value, line, position, childNodes)

    def getFunctionName(self):
        return self.root

    def getFunctionParameters(self):
        if self.nodes == None:
            return []
        return self.nodes[0].nodes

    def getType(self):
        return self.type

    def CreateMipsCode(self):
        register = MipsProgram.getFreeRegister('t')
        MipsProgram.releaseAllRegisters("a")
        for param in self.getFunctionParameters():
            tempRegister = param.CreateMipsCode()
            aRegister = MipsProgram.getFreeRegister('a')
            MipsProgram.addLineToProgramArray("move\t" + aRegister + ", " + tempRegister, 1, "Move to a parameter register")
        MipsProgram.addLineToProgramArray("jal\t" + self.getFunctionName(), 1, "Go to function " + self.getFunctionName())
        MipsProgram.addLineToProgramArray("move\t" + register + ", " + "$v0", 1,"Get return value of function")
        MipsProgram.releaseAllRegisters("t")
        MipsProgram.releaseAllRegisters("a")
        return register

#OK
class ASTDataType(AST):
    def __init__(self, value, line, position, childNodes=None):
        if value == "char":
            value = "chr"
        super().__init__(locate(value), line, position, childNodes)

    def getVariableName(self):
        return self.nodes[0].root

    def getValue(self):
        if len(self.nodes) > 1:
            return self.nodes[1].root
        return None

    def getValueObject(self):
        if len(self.nodes) > 1:
            return self.nodes[1]
        return None

    def getType(self):
        return self.root

    def getMipsType(self):
        return MipsProgram.mipsTypes[self.root]

    def neededStackSpace(self):
        print("needed stack space" , self.getVariableName())
        return 4

    def CreateMipsCode(self):
        value = self.getValue()
        if value is None:
            value = 0
        if self.getVariableName()[0] == "@":    #globaal gedefinnerd
            MipsProgram.addLineToDataArray(self.getVariableName().replace("@", "GBL") + ":	" + self.getMipsType() + " " + str(value), 1)
        else:
            if self.getValue() is None:
                if self.getType() is float:
                    valueRegister = MipsProgram.getFreeRegister('f')
                else:
                    valueRegister = MipsProgram.getFreeRegister('t')
            else:
                valueRegister = self.getValueObject().CreateMipsCode()        #Get a register (locked) with a value in to safe in the variable
                if MipsProgram.checkRegister(valueRegister) is float and self.getType() is not float:
                    valueRegister = MipsProgram.floatToIntConversion(valueRegister)
                elif MipsProgram.checkRegister(valueRegister) is int and self.getType() is float:
                    valueRegister = MipsProgram.intToFloatConversion(valueRegister)
            MipsProgram.storeVariable(self.getVariableName(), valueRegister)  #store the register in the variable (sw)
            MipsProgram.releaseRegister(valueRegister)                        #release the register for other use (unlock the register)

#OK
class ASTScope(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def CreateMipsCode(self):
        if self.nodes != None:
            for node in self.nodes:
                node.CreateMipsCode()

#OK
class ASTValue(AST):
    def __init__(self, value, line = 0, position = 0, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getType(self):
        exit("bruh")

    def CreateMipsCode(self):
        value = self.root
        register = MipsProgram.getFreeRegister('t')
        MipsProgram.addLineToProgramArray("li\t" + register + ", " + str(value), 1)
        return register

#OK
class ASTInt(ASTValue):
    def __init__(self, value, line = 0, position = 0, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getType(self):
        return int

#OK
class ASTChar(ASTValue):
    def __init__(self, value, line = 0, position = 0, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getType(self):
        return chr

#OK
class ASTFloat(ASTValue):
    def __init__(self, value, line = 0, position = 0, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getType(self):
        return float

    def CreateMipsCode(self):
        value = self.root
        name = MipsProgram.addLineToDataArray(".float\t" + str(value))
        register = MipsProgram.getFreeRegister('t')
        MipsProgram.addLineToProgramArray("la\t" + register + ", " + name, 1)
        floatRegister = MipsProgram.getFreeRegister('f')
        MipsProgram.addLineToProgramArray("lwc1\t" + floatRegister + ", 0(" + register + ")", 1)
        MipsProgram.releaseRegister(register)
        return floatRegister

#OK
class ASTVariable(AST):
    def __init__(self, value, line = 0, position = 0, childNodes=None, type=None):
        self.type = type
        super().__init__(value, line, position, childNodes)

    def getVariableName(self):
        return self.root

    def getVariableValue(self):
        if len(self.nodes) > 1:
            return self.nodes[1]
        return self.nodes[0]

    def getIndex(self):
        if self.nodes != None and type(self.nodes[0]) == ASTArrayIndex:
            return self.nodes[0].nodes[0].root
        return None

    def getIndexItem(self):
        if self.nodes != None and type(self.nodes[0]) == ASTArrayIndex:
            return self.nodes[0].nodes[0]
        return None

    def isArrayItem(self):
        if self.nodes != None and type(self.nodes[0]) == ASTArrayIndex:
            return True
        return False

    def getType(self):
        if self.type == None:
            return int
        return self.type

    def isSetVarible(self):
        """
        returns True if variable set, returns false for varible get
        :return:
        """
        return not self.nodes == None

    def CreateMipsCode(self):
        if self.isSetVarible():
            #for variable change
            valueRegister = self.nodes[0].CreateMipsCode()
            if MipsProgram.checkRegister(valueRegister) is float and self.getType() is not float:
                valueRegister = MipsProgram.floatToIntConversion(valueRegister)
            elif MipsProgram.checkRegister(valueRegister) is int and self.getType() is float:
                valueRegister = MipsProgram.intToFloatConversion(valueRegister)
            MipsProgram.updateVariable(self.getVariableName(), valueRegister)
            return valueRegister
        else:
            #for variable value
            print(self.getType())
            if self.type is float:
                register = MipsProgram.getFreeRegister('f')
            else:
                register = MipsProgram.getFreeRegister('t')
            MipsProgram.loadVariable(self.getVariableName(), register)
            return register

class ASTVoid(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

#OK
class ASTConst(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

#OK
class ASTPointer(AST):
    def __init__(self, value, line, position, childNodes=None, depth=1):#TODO depth overal laten werken
        self.depth = depth
        super().__init__(value, line, position, childNodes)

    def getSetObject(self):
        return self.nodes[0]

    def getToObject(self):
        if len(self.nodes) <= 1:
            return None
        return self.nodes[1]

    def getType(self):
        return self.getSetObject().getType()

    def getPointerDept(self):
        add = 1
        if self.getSetObject() == ASTPointer:
            add = self.getPointerDept() + 1
        return add

    def getVariableName(self):
        return self.getSetObject().getVariableName()

    def isDeclaration(self):
        return type(self.nodes[0]) == ASTDataType

    def isChangeValueObject(self):
        return type(self.nodes[0]) == ASTAdress

    def isValueObject(self):
        return type(self.nodes[0]) == ASTVariable

    def CreateMipsCode(self):
        if self.isDeclaration():                #bv int* i = &a (zet een pointer op een adress)
            self.getSetObject().CreateMipsCode()
            if self.getToObject() != None:
                register = self.getToObject().CreateMipsCode()
            else:
                register = MipsProgram.getFreeRegister("t")
            MipsProgram.updateVariable(self.getVariableName(), register)
            MipsProgram.releaseRegister(register)
        elif self.isChangeValueObject():        #bv *c = 10;    (zet een pointer op een waarde)
            valueRegister = self.getToObject().CreateMipsCode()
            pointerRegister = MipsProgram.getFreeRegister("t")
            variablePointerOffset = MipsProgram.variables[self.getVariableName()].stackPointerOffset
            MipsProgram.addLineToProgramArray("lw\t" + pointerRegister + ", " + str(variablePointerOffset) + "($fp)", 1, "load adress stored in pointer " + self.getVariableName()+ "  in register: " + pointerRegister)

            while self.depth > 1:
                #MipsProgram.addLineToProgramArray("nop", 1)#TODO mag weg normaal
                MipsProgram.addLineToProgramArray("lw\t" + pointerRegister + ", " + "0(" + pointerRegister + ")", 1,"load adresses until the point to varible is reached")
                self.depth -= 1

            MipsProgram.addLineToProgramArray("sw\t" + valueRegister + ", (" + pointerRegister + ")", 1, "update the register where " + self.getVariableName() + " is pointing add to " + valueRegister)
            MipsProgram.releaseAllMipsVaribleFromRegisters()#reset all registers with MipsVariables in to prevent out of sync data between stack en regiser data
            MipsProgram.releaseRegister(valueRegister)
            MipsProgram.releaseRegister(pointerRegister)
        elif self.isValueObject():              #bv int a = *b; (neem de waarde uit een pointer)
            pointerRegister = MipsProgram.getFreeRegister("t")
            variablePointerOffset = MipsProgram.variables[self.getVariableName()].stackPointerOffset
            MipsProgram.addLineToProgramArray("lw\t" + pointerRegister + ", " + str(variablePointerOffset) + "($fp)", 1, "load adress stored in pointer " + self.getVariableName() + "  in register: " + pointerRegister)
            while self.depth > 0:
                MipsProgram.addLineToProgramArray("lw\t" + pointerRegister + ", " + "0(" + pointerRegister + ")", 1,"load adresses until the point to varible is reached")
                self.depth -= 1
            return pointerRegister
        else:
            exit("undifiend operation with pointer")

#OK
class ASTAdress(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getVariableName(self):
        return self.nodes[0].root

    def getType(self):
        return self.nodes[0].getType()

    def CreateMipsCode(self):
        #returs the adress location of a variable in a register
        register = MipsProgram.getFreeRegister("t")
        variableOffset = MipsProgram.variables[self.getVariableName()].stackPointerOffset
        MipsProgram.addLineToProgramArray("addiu\t" + register + ", $fp, " + str(variableOffset), 1, "Get adress of variable in register (" + register + " = &" + self.getVariableName() + ")")
        return register

#OK
class ASTPrintf(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getPrintString(self):
        return self.nodes[0].root

    def getAllVariables(self):
        listOfItems = self.nodes[1:]
        return listOfItems

    def CreateMipsCode(self):
        # only one string
        if len(self.nodes) == 1:
            self.nodes[0].CreateMipsCode()
            return
        strings = self.nodes[0].getString()
        arguments = self.getAllVariables()
        result = []
        for item in arguments:
            for i in range(len(strings)):
                if strings[i] == "%":
                    midString = strings[0:i]
                    if midString != "":
                        result.append(midString)
                    result.append(item)
                    strings = strings[i + 2:]
                    break
            if strings != "":
                result.append(strings)
        for item in result:
            if type(item) is not str:
                object = item
                if type(object) is ASTText:
                    object.CreateMipsCode()
                    continue
                register = item.CreateMipsCode()  # Get a register (locked) with a value to print
                if type(object) is ASTInt or object.getType() is int:
                    MipsProgram.addLineToProgramArray("move\t$a0, " + register, 1)
                    MipsProgram.addLineToProgramArray("li\t$v0, 1", 1, "print integer")
                elif type(object) is ASTFloat or object.getType() is float:
                    MipsProgram.addLineToProgramArray("mov.s\t$f12," + register, 1, "print float")
                    MipsProgram.addLineToProgramArray("li\t$v0, 2", 1)
                elif type(object) is ASTChar or object.getType() is chr:
                    MipsProgram.addLineToProgramArray("move\t$a0, " + register, 1, "print char")
                    MipsProgram.addLineToProgramArray("li\t$v0, 11", 1)
                MipsProgram.addLineToProgramArray("syscall", 1, "executes the print function")
                MipsProgram.releaseRegister(register)  # release the register for other use (unlock the register)
            else:
                self.nodes[0].CreateMipsCodeString(item)


class ASTScanf(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getScanString(self):
        return self.nodes[0].root

    def getAllVariables(self):
        listOfItems = self.nodes[1:]
        return listOfItems

    def CreateMipsCode(self):
        inputType = self.nodes[0][1] #todo bv %5s
        if inputType == "i" or "d":
            register = MipsProgram.getFreeRegister('t')            #get a free register
            MipsProgram.addLineToProgramArray("li\t$v0, 5", 1, "read integer")
        if inputType == "f":
            register = MipsProgram.getFreeRegister('f')            #get a free register
            MipsProgram.addLineToProgramArray("li\t$v0, 6", 1, "read integer")
        if inputType == "c":
            register = MipsProgram.getFreeRegister('t')            #get a free register
            MipsProgram.addLineToProgramArray("li\t$v0, 12", 1, "read integer")
        if inputType == "s":
            o = 0
            #todo idk hoe the fuck dees ga werken
        MipsProgram.addLineToProgramArray("syscall", 1, "execute read")
        MipsProgram.addLineToProgramArray("move\t" + register + ", $v0", 1, "move input to other register")
        #todo link register to adress or pointer of scanvariable

#OK
class ASTText(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getString(self):
        return self.root

    def CreateMipsCodeString(self,string):
        stringName = MipsProgram.addLineToDataArray(".asciiz\t\"" + string + "\"")
        MipsProgram.addLineToProgramArray("la\t$a0, " + stringName, 1, "loads the string into a register")
        MipsProgram.addLineToProgramArray("li\t$v0, 4", 1)
        MipsProgram.addLineToProgramArray("syscall", 1, "executes the print function")

    def CreateMipsCode(self):
        self.CreateMipsCodeString(self.getString())

#OK
class ASTOperator(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)
        self.mipsOperations = {"+": "add", "-": "sub", "*": "mul", "/": "div", "&&": "and", "||": "or", "<": "slt", ">": "sgt", "<=": "sle", ">=": "sge", "==": "seq", "!=": "sne", "%": "%"} #TODO modulo

    def getOperator(self):
        return self.root

    def getMipsOperator(self):
        return self.mipsOperations[self.getOperator()]

    def getLeftValue(self):
        if self.nodes == None:
            return None
        return self.nodes[0]

    def getRightValue(self):
        if self.nodes == None:
            return None
        if len(self.nodes) <= 1:
            return None
        return self.nodes[1]

    def getType(self):
        if len(self.nodes) <= 1:
            return self.nodes[0].getType()
        convertScore = {float: 2, int: 0, chr: 0}
        node0 = self.nodes[0].getType()
        node1 = self.nodes[1].getType()
        if convertScore[node0] > convertScore[node1]:
            return self.nodes[0].getType()
        return self.nodes[1].getType()

    def CreateMipsCode(self):
        operator = self.getMipsOperator()
        returnType = self.getType()

        #unary operations (-a and +a)
        if self.getRightValue() is None:
            leftRegister = self.getLeftValue().CreateMipsCode()  # Get a register (locked) with a value of the left node
            if operator == "sub":
                operator = "neg"
            elif operator == "add":
                return leftRegister
            if returnType is float:
                register = MipsProgram.getFreeRegister('f')  # get a free register
                operator = operator + ".s"
            else:
                register = MipsProgram.getFreeRegister('t')  # get a free register
            leftRegister = self.getLeftValue().CreateMipsCode()  # Get a register (locked) with a value of the left node
            MipsProgram.addLineToProgramArray(operator+"\t" + register+", "+leftRegister, 1, "slaat de rest van de deling op in het register")
            return register

        leftRegister = self.getLeftValue().CreateMipsCode()     #Get a register (locked) with a value of the left node
        if self.nodes[0].getType() is not returnType:
            leftRegister = MipsProgram.intToFloatConversion(leftRegister)

        rightRegister = self.getRightValue().CreateMipsCode()  # Get a register (locked) with a value of the right node
        if self.nodes[1].getType() is not returnType:
            rightRegister = MipsProgram.intToFloatConversion(rightRegister)

        if returnType is float:
            register = MipsProgram.getFreeRegister('f')  # get a free register
            operator = operator+".s"
        else:
            register = MipsProgram.getFreeRegister('t')            #get a free register

        if operator == "and" or operator == "or":
            MipsProgram.registerToBit(leftRegister)             #convert value to boolean
            MipsProgram.registerToBit(rightRegister)            #convert value to boolean

        if operator == "%":
            MipsProgram.addLineToProgramArray("div\t" + leftRegister + ", " + rightRegister, 1,"operatie tussen 2 waarden")
            MipsProgram.addLineToProgramArray("mfhi\t"+register, 1, "slaat de rest van de deling op in het register")
        else:
            MipsProgram.addLineToProgramArray(operator + "\t" + register + ", " + leftRegister  + ", " + rightRegister , 1, "operatie tussen 2 waarden")
        MipsProgram.releaseRegister(leftRegister)               #release the leftRegister for other use
        MipsProgram.releaseRegister(rightRegister)              #release the rightRegister for other use
        return register                                         #returns the register with the answer (register will be unlocked in the caller)

#OK
class ASTWhile(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getCondition(self):
        return self.nodes[0]

    def getScope(self):
        return self.nodes[1]

    def CreateMipsCode(self):
        MipsProgram.whileCounter += 1
        whileCounter = MipsProgram.whileCounter

        MipsProgram.addLineToProgramArray("whileCondition" + str(whileCounter) + ":", 1, "While Condition")
        MipsProgram.defaultTabInpring += 1

        MipsProgram.releaseAllRegisters()
        register = self.getCondition().CreateMipsCode()
        MipsProgram.registerToBit(register)
        MipsProgram.addLineToProgramArray("beqz\t" + register + ", endWhile" + str(whileCounter) , 1)
        MipsProgram.releaseAllRegisters()

        MipsProgram.defaultTabInpring -= 1
        MipsProgram.addLineToProgramArray("whileLoop" + str(whileCounter) + ":", 1, "while loop")
        MipsProgram.defaultTabInpring += 1

        self.getScope().CreateMipsCode()      #if statement
        MipsProgram.addLineToProgramArray("b\twhileCondition" + str(whileCounter), 1, "jump to condition")

        MipsProgram.defaultTabInpring -= 1
        MipsProgram.releaseAllRegisters()
        MipsProgram.addLineToProgramArray("endWhile" + str(whileCounter) + ":", 1, "end statement")

#OK
class ASTIfElse(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getCondition(self):
        return self.nodes[0]

    def getIfScope(self):
        return self.nodes[1]

    def containsElseScope(self):
        return len(self.nodes) > 2

    def getElseScope(self):
        if self.containsElseScope():
            return self.nodes[2]

    def CreateMipsCode(self):
        register = self.getCondition().CreateMipsCode()
        MipsProgram.registerToBit(register)
        MipsProgram.ifElseCounter += 1
        ifElseCounter = MipsProgram.ifElseCounter
        MipsProgram.addLineToProgramArray("beqz\t" + register + ", else" + str(ifElseCounter) , 1, "if statement")
        MipsProgram.releaseAllRegisters()


        MipsProgram.addLineToProgramArray("if" + str(ifElseCounter) + ":", 1, "if statement")
        MipsProgram.defaultTabInpring += 1

        self.getIfScope().CreateMipsCode()      #if statement
        MipsProgram.addLineToProgramArray("b\tendIf" + str(ifElseCounter), 1, "jump to the end")

        MipsProgram.defaultTabInpring -= 1

        MipsProgram.addLineToProgramArray("else" + str(ifElseCounter) + ":", 1, "else statement")

        MipsProgram.defaultTabInpring += 1
        if self.containsElseScope():
            MipsProgram.releaseAllRegisters()
            self.getElseScope().CreateMipsCode()  # else statement
        MipsProgram.defaultTabInpring -= 1
        MipsProgram.releaseAllRegisters()
        MipsProgram.addLineToProgramArray("endIf" + str(ifElseCounter) + ":", 1, "end statement")

#OK
class ASTForwardDeclaration(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getReturnType(self):
        return self.nodes[0].root

    def getFunctionName(self):
        return self.nodes[1].root

    def getParameters(self):
        if len(self.nodes) == 4:
            return self.nodes[2]
        return []

    def getParametersList(self):
        if len(self.nodes) == 4:
            return self.nodes[2].nodes
        return []

    def getScope(self):
        if len(self.nodes) == 4:
            return self.nodes[3]
        return self.nodes[2]

    def CreateMipsCode(self):
        return

#OK
class ASTParameters(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getParameterList(self):
        return self.nodes

#OK
class ASTFor(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

#OK
class ASTCondition(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def CreateMipsCode(self):
        return self.nodes[0].CreateMipsCode()

class ASTOneTokenStatement(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

#OK
class ASTReturn(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getReturnValue(self):
        if self.nodes == None:
            return None
        return self.nodes[0]

    def CreateMipsCode(self):
        valueRegister = self.getReturnValue().CreateMipsCode()           #Get a register (locked) with a value in to safe in the variable
        MipsProgram.addLineToProgramArray("move\t$v0, " + valueRegister, 1, "Set the value for return in $v0")

#OK
class ASTMultiDeclaration(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTArray(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getVariableName(self):
        return self.nodes[0].nodes[0].root

    def getLength(self):
        if len(self.nodes) > 1:
            return self.nodes[1].nodes[0].root
        return None

    def getType(self):
        return self.nodes[0].root

class ASTArrayLength(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTArrayIndex(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)