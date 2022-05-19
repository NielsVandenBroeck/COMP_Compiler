from AST import *


class SymbolObject:
    def __init__(self, type, name, constness):
        self.type = type
        self.name = name
        self.constness = constness

    def getObject(self):
        return self


class SymbolObjectArray(SymbolObject):
    def __init__(self, type, name, constness, arrayLength):
        self.arrayLength = arrayLength
        super().__init__(type, name, constness)

    def getObject(self):
        return self


class SymbolObjectPointer(SymbolObject):
    def __init__(self, type, name, constness, objectConst, pointsTo=None):
        self.objectConst = objectConst
        if pointsTo == None:
            pointsTo = SymbolObject("nullptr", "nullptr", True)
        self.object = pointsTo
        super().__init__(type, name, constness)

    def getObject(self):
        if type(self.object) == SymbolObjectPointer:
            return self.object.getObject()
        return self.object

    # set value of real adress (not pointer)
    def setPointer(self, object, node):
        if not self.constness:
            self.object = object
        else:
            exit("[Error] line: " + str(node.line) + ", position: " + str(
                node.position) + " variable: \'" + node.root + "\' is of const-type and cannot be changed.")


class SymbolObjectPointerArray(SymbolObjectPointer):
    def __init__(self, type, name, constness, objectConst, arrayLength, pointsTo=None):
        self.arrayLength = arrayLength
        super().__init__(type, name, constness, objectConst, pointsTo)


class SymbolTable():
    def __init__(self, root, parent=None):
        self.SymbolList = {}
        self.SymbolList[None] = SymbolObject("nullptr", "nullptr", True)
        self.parent = parent
        self.root = root

    def loopAST(self, root=None):
        if self.root is None:
            return
        if root is None:
            root = self.root
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                self.visitChild(node)
        if type(self) is UpperSymbolTable:
            self.checkUndefinedReferences()

    def visitChild(self, node):
        # declarations
        if type(node) is ASTConst or self.IsVariableDeclarationSameTypes(node) or self.IsPointerDeclaration(
                node) or type(node) is ASTArray:
            self.declaration(node)
        # asignment
        elif self.IsVariableAssignmentSameTypes(node):
            self.variableAssignment(node)
        # pointer variable assignment (sets the variable where to pointer is pointing to) bv: *b = a of *b = 10;
        elif self.IsPointerVariableAssignment(node):
            self.pointerAssignment(node)
        elif self.IsVariable(node):
            self.searchVariable(node)
        # check for unassigned variables in bodies
        elif self.IsBody(node):
            self.checkBody(node)
        # check returns
        elif self.IsReturn(node):
            self.checkReturnType(node)
        # check printf format
        elif self.IsPrintf(node):
            self.checkPrintf(node)
        # check scanf format
        elif self.IsScanf(node):
            self.checkScanf(node)
        # scopes
        elif self.IsScope(node):
            s = SymbolTable(node, self)
            s.loopAST()
        # functions
        elif self.IsFunction(node):
            self.addFunctionScope(node)
        else:
            self.loopAST(node)

    def getUpper(self):
        if type(self) is UpperSymbolTable:
            return self
        return self.parent.getUpper()

    def addFunctionScope(self, root):
        if root.nodes is None:
            exit("Unexpected Error.")
        params = None
        scope = None
        for node in root.nodes:
            if type(node) is ASTDataType or type(node) is ASTVoid or type(node) is ASTPointer:
                returnType = node.root
            elif type(node) is ASTFunctionName:
                functionName = node.root
            elif type(node) is ASTParameters:
                params = node
            elif type(node) is ASTScope:
                scope = node
        # check if function has been declared before
        functionAlreadyDeclared = self.searchFunction(returnType, functionName, params)

        if functionAlreadyDeclared is not None:
            if scope is not None:
                functionAlreadyDeclared.addScope(scope)
            return

        s = FunctionSymbolTable(scope, functionName, returnType, self.getUpper(), params)
        self.addFunctionToUpper(s)
        s.loopAST()

    def addFunctionToUpper(self, function):
        if type(self) is UpperSymbolTable:
            self.functions.append(function)
            return
        return self.parent.addFunctionToUpper(function)

    def searchFunction(self, returnType, name, params):
        if type(self) is UpperSymbolTable:
            for function in self.functions:
                if returnType == function.returnType and name == function.functionName:
                    if params is None and function.parameters == []:
                        return function
                    if len(params.nodes) == len(function.parameters):
                        for f1, f2 in zip(params.nodes, function.parameters):
                            pointer = False
                            while type(f1) is ASTConst or type(f1) is ASTPointer:
                                if type(f1) is ASTPointer:
                                    pointer = True
                                f1 = f1.nodes[0]
                            if f1.root != f2[0] or pointer != f2[1]:
                                return None
                        return function

            return None
        return self.parent.searchFunction(returnType, name, params)

    def declaration(self, node, constness=False, arraylength=None):
        if type(node) is ASTArray:
            self.declaration(node.nodes[0], constness, int(node.nodes[1].root))
        elif type(node) is ASTConst:
            self.declaration(node.nodes[0], True, arraylength)
        elif self.IsVariableDeclarationSameTypes(node):
            self.variableDeclaration(node, constness, arraylength)
        elif self.IsPointerDeclaration(node):
            self.pointerDeclaration(node, constness, arraylength)

    def pointerDeclaration(self, node, constness, arrayLength):
        objectConstness = False
        pointerType = node.nodes[0].root
        if type(node.getSetObject()) is ASTConst:
            objectConstness = True
            pointerName = node.getSetObject().nodes[0].getVariableName()
        else:
            pointerName = node.getSetObject().getVariableName()

        if pointerName in self.SymbolList:
            exit("[Error] line: " + str(node.line) + ", position: " + str(
                node.position) + ". Redefinition of variable: \'" +
                 node.nodes[0].root + "\'.")

        object = node.getToObject()
        self.searchVariable(object)
        pointerObject = None
        if isinstance(object, ASTAdress):
            toObject = self.searchVariable(object.nodes[0])
            if arrayLength is not None:
                pointerObject = SymbolObjectPointerArray(pointerType, pointerName, constness, objectConstness,
                                                         arrayLength, toObject)
            else:
                pointerObject = SymbolObjectPointer(pointerType, pointerName, constness, objectConstness, toObject)
        elif isinstance(object, ASTVariable):
            pointerObject = self.searchVariable(object)
        elif object == None:
            if arrayLength is not None:
                pointerObject = SymbolObjectPointerArray(pointerType, pointerName, constness, objectConstness,
                                                         arrayLength)
            else:
                pointerObject = SymbolObjectPointer(pointerType, pointerName, constness, objectConstness)
        else:
            exit("[Error] line: " + str(node.line) + ", position: " + str(
                node.position) + ". Variable: \'" + pointerName + "\' invalid conversion from 'idk' to 'idk*'.")

        self.SymbolList[pointerName] = pointerObject

    def variableDeclaration(self, node, constness, arrayLength):
        variable = node.nodes[0].root
        # check if variablename exists -> error
        if variable in self.SymbolList:
            exit("[Error] line: " + str(node.line) + ", position: " + str(
                node.position) + ". Redefinition of variable: \'" + node.nodes[0].root + "\'.")

        if isinstance(node.nodes[0], ASTAdress):
            self.searchVariable(node.nodes[1])
        elif len(node.nodes) == 2:
            if type(node.nodes[1]) is ASTVariable:
                if not self.searchVariable(node.nodes[1]).type is node.root:
                    print("[Warning] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". Implicit conversion from " + str(
                        self.searchVariable(node.nodes[1]).type) + " to " + str(
                        node.root) + ". ")
            else:
                self.checkBody(node.nodes[1])
                bodyType = node.nodes[1].findType()
                if bodyType != node.getType():
                    print("[Warning] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". Implicit conversion from " + str(
                        bodyType) + " to " + str(
                        node.getType()) + ". ")
                node.nodes[1].correctDataType(node.root)
        if arrayLength is not None:
            self.SymbolList[variable] = SymbolObjectArray(node.root, variable, constness, arrayLength)
        else:
            self.SymbolList[variable] = SymbolObject(node.root, variable, constness)

    def pointerAssignment(self, node):
        var = node.getSetObject()

        newValue = node.getToObject()

        self.searchVariable(newValue)

        pointsToName = var.getVariableName()

        pointsToObject = var.nodes[0]
        self.searchVariable(pointsToObject)

        if self.searchVariable(newValue) != None and self.searchVariable(newValue).type != self.SymbolList[
            pointsToName].type:
            print("[Warning] line: " + str(node.line) + ", position: " + str(
                node.position) + ". Implicit conversion from '" + str(
                self.SymbolList[pointsToName].getObject().type) + "' to " + str(
                self.searchVariable(var).type) + ". ")

    def variableAssignment(self, node):
        variable = self.searchVariable(node)
        if (variable.constness):
            exit("[Error] line: " + str(node.line) + ", position: " + str(
                node.position) + " variable: \'" + node.root + "\' is of const-type and cannot be changed.")
        value = node.nodes[0]

        # check if variable is array and has correct index
        if type(variable) is SymbolObjectArray or type(variable) is SymbolObjectPointerArray:
            if len(node.nodes) == 1:
                exit("[Error] line: " + str(node.line) + ", position: " + str(
                    node.position) + " variable \'" + node.root + "\': Array is not assignable.")
            value = node.nodes[1]

        symbolValue = self.searchVariable(value)

        # als het 2 pointers zijn bv: a = b
        if (type(value) is ASTVariable and type(variable) == SymbolObjectPointer and type(
                symbolValue) == SymbolObjectPointer):
            variable.setPointer(symbolValue, node)
        # als er een waarde word gezet bv: *a = 10
        elif type(value) is ASTAdress:
            value = value.nodes[0]
            variable.setPointer(self.searchVariable(value), node)
        elif type(value) is ASTVariable:
            if symbolValue.type is not variable.type:
                print("[Warning] line: " + str(node.line) + ", position: " + str(
                    node.position) + ". Implicit conversion from " + str(
                    symbolValue.type) + " to " + str(
                    variable.type) + ". ")
        else:
            self.checkBody(value)
            bodyType = value.findType()
            if bodyType != variable.type:
                print("[Warning] line: " + str(node.line) + ", position: " + str(
                    node.position) + ". Implicit conversion from " + str(
                    bodyType) + " to " + str(
                    variable.type) + ". ")
            value.correctDataType(variable.type)

    def checkBody(self, root):
        if type(root) is ASTVariable:
            self.searchVariable(root)
        elif type(root) is ASTFunctionName:
            self.checkFunctionCall(root)
            root.type = self.findReturnTypeOfFunction(root.root)
            if root.nodes is not None:
                for param in root.nodes[0].nodes:
                    self.searchVariable(param)
            self.checkFunctionCall(root)
            return
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                self.checkBody(node)

    def checkFunctionCall(self, root):
        if type(self) is not UpperSymbolTable:
            self.parent.checkFunctionCall(root)
        else:
            if self.functions is None:
                return
            for function in self.functions:
                if function is not None:
                    compared = self.compareFunction(function, root)
                    if compared is True:
                        if function.scope is None:
                            self.addundefinedReferenceToUpper(function.functionName)
                        return
                    elif type(compared) == str:
                        exit("[Error] line: " + str(root.line) + ", position: " + str(
                            root.position) + compared)
            exit("[Error] line: " + str(root.line) + ", position: " + str(
                root.position) + ". function '" + root.root + "' does not exist.")

    def addundefinedReferenceToUpper(self, functionName):
        if type(self) is UpperSymbolTable:
            self.undefinedReferences.append(functionName)
            return
        return self.parent.addundefinedReferenceToUpper(functionName)

    def checkUndefinedReferences(self):
        if len(self.undefinedReferences) > 0:
            exit("[Error] Undefined reference to '" + self.undefinedReferences[0] + "'.")

    def compareFunction(self, function, functionCall):
        functionCallCount = 0
        if functionCall.nodes is not None:
            functionCallCount = len(functionCall.nodes[0].nodes)
        if function.functionName != functionCall.root:
            return False
        elif len(function.parameters) != functionCallCount:
            errorText = ". Too few/many arguments to function call, expected " + str(
                len(function.parameters)) + " have " + str(functionCallCount) + "."
            return errorText
        return True

    def checkReturnType(self, node):
        if type(self) is not FunctionSymbolTable:
            self.parent.checkReturnType(node)
            return
        if self.returnType == "void":
            if node.nodes is not None:
                exit("[Error] line: " + str(node.line) + ", position: " + str(
                    node.position) + ". Void function '" + self.functionName + "' should not return a value.")
        else:
            if node.nodes is None:
                exit("[Error] line: " + str(node.line) + ", position: " + str(
                    node.position) + ". Void function '" + self.functionName + "' should return a value.")
            elif type(node.nodes[0]) is ASTVariable:
                if not self.searchVariable(node.nodes[0]).type is self.returnType:
                    print("[Warning] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". Implicit conversion from " + str(
                        self.searchVariable(node.nodes[0]).type) + " to " + str(
                        self.returnType) + ". ")
            else:
                self.checkBody(node.nodes[0])
                bodyType = node.nodes[0].findType()
                if bodyType != self.returnType:
                    print("[Warning] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". Implicit conversion from " + str(
                        bodyType) + " to " + str(
                        self.returnType) + ". ")
                node.nodes[0].correctDataType(self.returnType)

    def checkPrintf(self, root):
        if root.nodes is None:
            return
        formatText = root.nodes[0].root
        formatList = []
        for i in range(len(formatText)):
            if formatText[i] == '%':
                if len(formatText) < i:
                    exit("[Error] line: " + str(root.line) + ", position: " + str(
                        root.position) + ". An unkown Error occured.")
                position = i
                number = None
                while len(formatText) >= position:
                    if formatText[position].isdigit():
                        number += formatText[position]
                    else:
                        break
                print(number)
                if formatText[i + 1] == "i" or formatText[i + 1] == "d":
                    formatList.append(int)
                elif formatText[i + 1] == "c":
                    formatList.append(chr)
                elif formatText[i + 1] == "f":
                    formatList.append(float)
                elif formatText[i + 1] == "s":
                    exit("[Error] line: " + str(root.line) + ", position: " + str(
                        root.position) + ". Cannot scan a string. strings are not implemented yet.")
        if len(formatList) != len(root.nodes) - 1:
            exit("[Error] line: " + str(root.line) + ", position: " + str(
                root.position) + ". Too many/few parameters were given in scanf function.")
        for i in range(1, len(root.nodes)):
            node = root.nodes[i]
            if node is not None:
                variableType = None
                # Variable
                if type(node) == ASTVariable:
                    variableType = self.searchVariable(node).type
                # body
                elif type(node) == ASTOperator:
                    self.searchAllvars(node)
                    variableType = node.findType()
                # pointer
                elif type(node) == ASTPointer:
                    variableType = self.searchVariable(node.nodes[0]).type
                # int
                elif type(node) == ASTInt:
                    variableType = int
                # char
                elif type(node) == ASTChar:
                    variableType = chr
                # float
                elif type(node) == ASTFloat:
                    variableType = float
                elif type(node) == ASTFunctionName:
                    self.checkFunctionCall(node)
                    variableType = self.findReturnTypeOfFunction(node.root)
                if variableType != formatList[i - 1]:
                    exit("[Error] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". Printf format specifies type '" + str(
                        formatList[i - 1]) + "', but the argument type is '" + str(variableType) + "'.")

    def findReturnTypeOfFunction(self, functionName):
        if self.parent is not None:
            return self.parent.findReturnTypeOfFunction(functionName)
        else:
            for function in self.functions:
                if function.functionName == functionName:
                    return function.returnType

    def checkScanf(self, root):
        if root.nodes is None:
            return
        formatText = root.nodes[0].root
        formatList = []
        for i in range(len(formatText)):
            if formatText[i] == '%':
                if len(formatText) < i:
                    exit("[Error] line: " + str(root.line) + ", position: " + str(
                        root.position) + ". An unkown Error occured.")
                #strings
                if formatText[i + 1].isnumeric():
                    position = i+1
                    while len(formatText) >= position:
                        if formatText[position].isnumeric():
                            position += 1
                        elif formatText[i + 1] == "s":
                            break
                        else:
                            exit("[Error] line: " + str(root.line) + ", position: " + str(
                                root.position) + ". Cannot use field width on non-strings.")
                        formatList.append(str)
                if formatText[i + 1] == "i" or formatText[i + 1] == "d":
                    formatList.append(int)
                elif formatText[i + 1] == "c":
                    formatList.append(chr)
                elif formatText[i + 1] == "f":
                    formatList.append(float)
                else:
                    exit("[Error] line: " + str(root.line) + ", position: " + str(
                        root.position) + ". Unknown Format Type.")

        if len(formatList) != len(root.nodes) - 1:
            exit("[Error] line: " + str(root.line) + ", position: " + str(
                root.position) + ". Too many/few parameters were given in scanf function.")
        for i in range(1, len(root.nodes)):
            node = root.nodes[i]
            if node is not None:
                # pointer
                if type(node) == ASTVariable:
                    if type(self.searchVariable(node)) is SymbolObjectPointer:
                        variableType = self.searchVariable(node).type
                    else:
                        exit("[Error] line: " + str(node.line) + ", position: " + str(
                            node.position) + ". Variable must be of type Pointer of passed by reference.")
                # address
                elif type(node) == ASTAdress:
                    if node.nodes is None:
                        exit("[Error] line: " + str(root.line) + ", position: " + str(
                            root.position) + ". An unkown Error occured.")
                    else:
                        variableType = self.searchVariable(node.nodes[0]).type
                else:
                    exit("[Error] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". Variable must be of type Pointer of passed by reference.")
                if variableType != formatList[i - 1]:
                    exit("[Error] line: " + str(node.line) + ", position: " + str(
                        node.position) + ". Scanf format specifies type '" + str(
                        formatList[i - 1]) + "', but the argument type is '" + str(variableType) + "'.")

    def checkForwardDeclaration(self, root):
        self.addFunctionScope(root)

    def checkUnusedVariables(self, root):
        if root.nodes is None:
            return
        for node in root.nodes:
            if node is not None:
                self.checkUnusedVariables(node)

    def searchAllvars(self, root):
        if type(root) is ASTVariable:
            self.searchVariable(root)
        elif type(root) is ASTPointer:
            self.searchVariable(root.nodes[0])
        elif type(root) is ASTOperator:
            for node in root.nodes:
                self.searchAllvars(node)

    def searchVariable(self, node):
        if type(node) is not ASTVariable:
            return None
        varName = node.getVariableName()
        if varName in self.SymbolList:
            object = self.SymbolList[varName]
            node.type = object.type
            if type(object) is SymbolObjectArray or type(object) is SymbolObjectPointerArray:
                if node.nodes is None:
                    exit("[Error] line: " + str(node.line) + ", position: " + str(
                        node.position) + " variable: \'" + node.root + "\' Incompatible conversion with arrays.")
                if int(node.nodes[0].root) >= object.arrayLength:
                    exit("[Error] line: " + str(node.line) + ", position: " + str(
                        node.position) + " variable: \'" + node.root + "\' Array index " + node.nodes[
                             0].root + " is past the end of the array (which contains " + str(
                        object.arrayLength) + " elements).")
            return object
        elif self.parent is None:
            exit("[Error] line: " + str(node.line) + ", position: " + str(
                node.position) + ". Variable: \'" + varName + "\' has not been declared.")
            return None
        else:
            return self.parent.searchVariable(node)

    @staticmethod
    def IsVariableDeclarationSameTypes(node):
        return type(node) is ASTDataType

    @staticmethod
    def IsVariableAssignmentSameTypes(node):
        return type(node) is ASTVariable and node.nodes is not None

    @staticmethod
    def IsVariable(node):
        return type(node) is ASTVariable and node.nodes is None

    @staticmethod
    def IsPointerDeclaration(node):
        return type(node) is ASTPointer and type(node.getSetObject()) is not ASTVariable and type(
            node.getSetObject()) is not ASTAdress

    @staticmethod
    def IsPointerVariableAssignment(node):
        return type(node) is ASTPointer and type(node.getSetObject()) is ASTAdress

    @staticmethod
    def IsPointerAssignment(node):
        return type(node) is ASTPointer

    @staticmethod
    def IsBody(node):
        return type(node) is ASTOperator or type(node) is ASTFunctionName

    @staticmethod
    def IsReturn(node):
        return type(node) is ASTReturn

    @staticmethod
    def IsPrintf(node):
        return type(node) is ASTPrintf

    @staticmethod
    def IsScanf(node):
        return type(node) is ASTScanf

    @staticmethod
    def IsText(node):
        return type(node) is ASTText

    @staticmethod
    def IsVariable(node):
        return type(node) is ASTVariable

    @staticmethod
    def IsForwardDeclaration(node):
        return type(node) is ASTForwardDeclaration

    @staticmethod
    def IsScope(node):
        return type(node) is ASTScope

    @staticmethod
    def IsFunction(node):
        return type(node) is ASTFunction or type(node) is ASTForwardDeclaration

    @staticmethod
    def IsWhile(node):
        return type(node) is ASTWhile


class UpperSymbolTable(SymbolTable):
    def __init__(self, root):
        self.functions = []
        self.undefinedReferences = []
        super().__init__(root)


class FunctionSymbolTable(SymbolTable):
    def __init__(self, root, name, returnType, parent, parameters):
        self.scope = root
        self.functionName = name
        self.returnType = returnType
        super().__init__(root, parent)
        self.parameters = []
        self.addParameters(parameters)

    def addScope(self, scope):
        self.scope = scope
        if self.functionName in self.parent.undefinedReferences:
            self.parent.undefinedReferences.remove(self.functionName)
        self.loopAST(scope)

    def addParameters(self, root):
        if root is None:
            return
        if root.nodes is None:
            return
        for node in root.nodes:
            datatype = None
            pointer = False
            if node is not None:
                arrayLength = None
                if type(node) is ASTArray:
                    arrayLength = node.nodes[1]
                    node = node.nodes[0]
                if type(node) is ASTConst:
                    datatype = node.nodes[0].root
                    if type(node.nodes[0]) is ASTPointer:
                        pointer = True
                        if type(node.nodes[0].nodes[0]) is ASTConst:
                            datatype = node.nodes[0].nodes[0].nodes[0].root
                        else:
                            datatype = node.nodes[0].nodes[0].root
                        self.pointerDeclaration(node.nodes[0], True, arrayLength)
                    elif type(node.nodes[0]) is ASTDataType:
                        self.variableDeclaration(node.nodes[0], True, arrayLength)
                    else:
                        print("error")
                elif self.IsVariableDeclarationSameTypes(node):
                    datatype = node.root
                    self.variableDeclaration(node, False, arrayLength)
                elif self.IsPointerDeclaration(node):
                    pointer = True
                    if type(node.nodes[0]) is ASTConst:
                        datatype = node.nodes[0].nodes[0].root
                    else:
                        datatype = node.nodes[0].root
                    self.pointerDeclaration(node, False, arrayLength)
            self.parameters.append((datatype, pointer))
