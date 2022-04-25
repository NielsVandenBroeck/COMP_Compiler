from AST import *

class SymbolObject:
    def __init__(self, type, name, constness):
        self.type = type
        self.name = name
        self.constness = constness

    def getObject(self):
        return self

class SymbolObjectPointer:
    def __init__(self, type, name, constness, objectConst, pointsTo=None):
        self.type = type
        self.constness = constness
        self.objectConst = objectConst
        if pointsTo == None:
            pointsTo = SymbolObject("nullptr", "nullptr", True)
        self.object = pointsTo

        self.name = name

    def getObject(self):
        if type(self.object) == SymbolObjectPointer:
            return self.object.getObject()
        return self.object

    # set value of real adress (not pointer)
    def setPointer(self,object, node):
        if not self.constness:
            self.object = object
        else:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +" variable: \'" + node.root + "\' is of const-type and cannot be changed.")

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
        #declaration
        if type(node) is ASTConst:
            if type(node.nodes[0]) is ASTPointer:
                self.pointerDeclaration(node.nodes[0],True)
            elif type(node.nodes[0]) is ASTDataType:
                self.variableDeclaration(node.nodes[0],True)
            else:
                print("error")
        elif self.IsVariableDeclarationSameTypes(node):
            self.variableDeclaration(node)
        #asignment
        elif self.IsVariableAssignmentSameTypes(node):
            self.variableAssignment(node)
        elif self.IsVariable(node):
            self.searchVariable(node)
        #pointer declaration bv: int* b ( = a)
        elif self.IsPointerDeclaration(node):
            self.pointerDeclaration(node)
        #pointer varible assignment (sets te variable where to pointer is pointing at) bv: *b = a of *b = 10;
        elif self.IsPointerVariableAssignment(node):
            self.pointerAssignment(node)
        #set a pointer to another pointer bv: a = b
        elif self.IsPointerAssignment(node):
            self.pointerAssignment(node)
        #check for unassigned variables in bodies
        elif self.IsBody(node):
            self.checkBody(node)
        #check returns
        elif self.IsReturn(node):
            self.checkReturnType(node)
        #check printf format
        elif self.IsPrintf(node):
            self.checkPrintf(node)
        #check scanf format
        elif self.IsScanf(node):
            self.checkScanf(node)
        #scopes
        elif self.IsScope(node):
            s = SymbolTable(node, self)
            s.loopAST()
        #functions
        elif self.IsFunction(node):
            self.addFunctionScope(node)
        else:
            self.loopAST(node)

    def getUpper(self):
        if type(self) is UpperSymbolTable:
            return self
        return self.parent.getUpper()

    def addFunctionScope(self,root):
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
        #check if function has been declared before
        functionAlreadyDeclared = self.searchFunction(returnType, functionName, params)

        if functionAlreadyDeclared is not None:
            if scope is not None:
                functionAlreadyDeclared.addScope(scope)
            return

        s = FunctionSymbolTable(scope,functionName, returnType, self.getUpper(), params)
        self.addFunctionToUpper(s)
        s.loopAST()

    def addFunctionToUpper(self,function):
        if type(self) is UpperSymbolTable:
            self.functions.append(function)
            return
        return self.parent.addFunctionToUpper(function)

    def searchFunction(self, returnType, name, params):
        if type(self) is UpperSymbolTable:
            for function in self.functions:
                if returnType == function.returnType and name == function.functionName:
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

    def pointerDeclaration(self, node, constness=False):
        objectConstness = False
        pointerType = node.nodes[0].root
        if type(node.getSetObject()) is ASTConst:
            objectConstness = True
            pointerName = node.getSetObject().nodes[0].getVariableName()
        else:
            pointerName = node.getSetObject().getVariableName()

        if pointerName in self.SymbolList:
            exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + ". Redefinition of variable: \'" +
                node.nodes[0].root + "\'.")

        object = node.getToObject()
        pointerObject = None
        if isinstance(object, ASTAdress):
            self.searchVariable(object)
            toObject = self.searchVariable(object)
            pointerObject = SymbolObjectPointer(pointerType, pointerName, constness, objectConstness, toObject)
        elif isinstance(object, ASTVariable):
            pointerObject = self.searchVariable(object)
        elif object == None:
            pointerObject = SymbolObjectPointer(pointerType, pointerName, constness, objectConstness)
        else:
            exit("[Error] line: "+ str(node.line) +", position: "+ str(node.position) +". Variable: \'" + pointerName + "\' invalid conversion from 'idk' to 'idk*'.")

        self.SymbolList[pointerName] = pointerObject

    def pointerAssignment(self, node):
        var = node.getSetObject()
        self.searchVariable(var)

        newValue = node.getToObject()

        pointsToObject = var.getVariableName()
        if self.searchVariable(newValue) != None and self.searchVariable(newValue).type != self.SymbolList[pointsToObject].type:
            print("[Warning] line: " + str(node.line) + ", position: " + str(
                node.position) + ". Implicit conversion from '" + str(self.SymbolList[pointsToObject].getObject().type) + "' to " + str(
                self.searchVariable(var).type) + ". ")

        var = node.getSetObject()
        self.searchVariable(var)


    def variableDeclaration(self, node, constness=False):
        variable = node.nodes[0].root
        #check if variablename exists -> error
        if variable in self.SymbolList:
            exit("[Error] line: " + str(node.line) + ", position: " + str(node.position) + ". Redefinition of variable: \'" + node.nodes[0].root + "\'.")

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
        self.SymbolList[variable] = SymbolObject(node.root,variable,constness)

    def variableAssignment(self, node):
        variable = self.searchVariable(node)
        if(variable.constness):
            exit("[Error] line: " + str(node.line) + ", position: " + str(
                node.position) + " variable: \'" + node.root + "\' is of const-type and cannot be changed.")

        #als het 2 pointers zijn bv: a = b
        if(type(node.nodes[0]) is ASTVariable and type(variable) == SymbolObjectPointer and type(self.searchVariable(node.nodes[0])) == SymbolObjectPointer):
            variable.setPointer(self.searchVariable(node.nodes[0]), node)
        #als er een waarde word gezet bv: *a = 10
        elif type(node.nodes[0]) is ASTAdress:
            adress = node.nodes[0]
            variable.setPointer(self.searchVariable(adress), node)
        elif type(node.nodes[0]) is ASTVariable:
            if self.searchVariable(node.nodes[0]).type is not variable.type:
                print("[Warning] line: " + str(node.line) + ", position: " + str(
                    node.position) + ". Implicit conversion from " + str(
                    self.searchVariable(node.nodes[0]).type) + " to " + str(
                    variable.type) + ". ")
        else:
            self.checkBody(node.nodes[0])
            bodyType = node.nodes[0].findType()
            if bodyType != variable.type:
                print("[Warning] line: " + str(node.line) + ", position: " + str(
                    node.position) + ". Implicit conversion from " + str(
                    bodyType) + " to " + str(
                    variable.type) + ". ")
            node.nodes[0].correctDataType(variable.type)


    def checkBody(self, root):
        if type(root) is ASTVariable:
            self.searchVariable(root)
        elif type(root) is ASTFunctionName:
            self.checkFunctionCall(root)
            root.type = self.findReturnTypeOfFunction(root.root)
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
                    compared = self.compareFunction(function,root)
                    if compared is True:
                        if function.scope is None:
                            self.addundefinedReferenceToUpper(function.functionName)
                        return
                    elif type(compared) == str:
                        exit("[Error] line: " + str(root.line) + ", position: " + str(
                            root.position) + compared)
            exit("[Error] line: " + str(root.line) + ", position: " + str(
                root.position) + ". function '"+root.root+"' does not exist.")

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
            errorText = ". Too few/many arguments to function call, expected "+ str(len(function.parameters)) +" have "+ str(functionCallCount) +"."
            return errorText
        return True

    def checkReturnType(self, node):
        if type(self) is not FunctionSymbolTable:
            self.parent.checkReturnType(node)
            return
        if self.returnType == "void":
            if node.nodes is not None:
                exit("[Error] line: " + str(node.line) + ", position: " + str(
                    node.position) + ". Void function '"+self.functionName+"' should not return a value.")
        else:
            if node.nodes is None:
                exit("[Error] line: " + str(node.line) + ", position: " + str(
                    node.position) + ". Void function '"+self.functionName+"' should return a value.")
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
                else:
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
                #Variable
                if type(node) == ASTVariable:
                    variableType = self.searchVariable(node).type
                #body
                elif type(node) == ASTOperator:
                    self.searchAllvars(node)
                    variableType = node.findType()
                #pointer
                elif type(node) == ASTPointer:
                    variableType = self.searchVariable(node.nodes[0]).type
                #int
                elif type(node) == ASTInt:
                    variableType = int
                #char
                elif type(node) == ASTChar:
                    variableType = chr
                #float
                elif type(node) == ASTFloat:
                    variableType = float
                elif type(node) == ASTFunctionName:
                    self.checkFunctionCall(root)
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
                else:
                    if formatText[i+1] == "i" or formatText[i+1] == "d":
                        formatList.append(int)
                    elif formatText[i+1] == "c":
                        formatList.append(chr)
                    elif formatText[i+1] == "f":
                        formatList.append(float)
                    elif formatText[i+1] == "s":
                        exit("[Error] line: " + str(root.line) + ", position: " + str(
                            root.position) + ". Cannot scan a string. strings are not implemented yet.")
        if len(formatList) != len(root.nodes)-1:
            exit("[Error] line: " + str(root.line) + ", position: " + str(
                root.position) + ". Too many/few parameters were given in scanf function.")
        for i in range(1,len(root.nodes)):
            node = root.nodes[i]
            if node is not None:
                #pointer
                if type(node) == ASTVariable:
                    if type(self.searchVariable(node)) is SymbolObjectPointer:
                        variableType = self.searchVariable(node).type
                    else:
                        exit("[Error] line: " + str(node.line) + ", position: " + str(
                            node.position) + ". Variable must be of type Pointer of passed by reference.")
                #address
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
                        formatList[i-1]) + "', but the argument type is '" + str(variableType) + "'.")


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
            node.type = self.SymbolList[varName].type
            return self.SymbolList[varName]
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
        return type(node) is ASTPointer and type(node.getSetObject()) is not ASTVariable and type(node.getSetObject()) is not ASTAdress

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

    def addScope(self,scope):
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
                if type(node) is ASTConst:
                    datatype = node.nodes[0].root
                    if type(node.nodes[0]) is ASTPointer:
                        pointer = True
                        if type(node.nodes[0].nodes[0]) is ASTConst:
                            datatype = node.nodes[0].nodes[0].nodes[0].root
                        else:
                            datatype = node.nodes[0].nodes[0].root
                        self.pointerDeclaration(node.nodes[0], True)
                    elif type(node.nodes[0]) is ASTDataType:
                        self.variableDeclaration(node.nodes[0], True)
                    else:
                        print("error")
                elif self.IsVariableDeclarationSameTypes(node):
                    datatype = node.root
                    self.variableDeclaration(node)
                elif self.IsPointerDeclaration(node):
                    pointer = True
                    if type(node.nodes[0]) is ASTConst:
                        datatype = node.nodes[0].nodes[0].root
                    else:
                        datatype = node.nodes[0].root
                    self.pointerDeclaration(node)
            self.parameters.append((datatype,pointer))
