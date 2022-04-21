import operator
from typing import Any
from pydoc import locate

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
            if isinstance(value1, float) or isinstance(value1, int):
                self.root = -value1
                self.nodes = None
            elif isinstance(value1, str):
                self.root = chr(-ord(value1[1]))
                self.nodes = None
            self.__class__ = AST
        # unary +
        elif len(self.nodes) == 1 and self.root == '+':
            self.root = self.nodes[0].root
            self.nodes = None
            self.__class__ = AST
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
                if resulttype == chr:
                    self.root = '\'' + resulttype(ops[self.root](value1, value2)) + '\''
                else:
                    self.root = resulttype(ops[self.root](value1, value2))
                self.nodes = None
                self.__class__ = AST

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
            if originalType is  float or originalType is int:
                self.root = destinationType(self.root)
            else:
                self.root = destinationType(ord(self.root))
        elif destinationType is chr:
            if originalType is str:
                self.root = '\''+self.root+'\''
            else:
                conversion = True
                self.root = '\'' + chr(int((self.root))) + '\''
        if conversion:
            print("[Warning] line: " + str(self.line) + ", position: " + str(
                self.position) + ". Implicit conversion from "+str(originalType) +" to "+ str(destinationType) +" changes value from "+ str(originalValue) +" to " + str(self.root) +".")


class ASTVariable(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getVariableName(self):
        return self.root

    def getVariableValue(self):
        if len(self.nodes) > 1:
            return self.nodes[1]
        return self.nodes[0]


class ASTFunctionName(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

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

class ASTVoid(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTConst(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTPointer(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getSetObject(self):
        return self.nodes[0]

    def getToObject(self):
        if len(self.nodes) <= 1:
            return None
        return self.nodes[1]

class ASTAdress(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getVariableName(self):
        return self.nodes[0].root

class ASTPrintf(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTOperator(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getOperator(self):
        return self.root

    def getLeftValue(self):
        if self.nodes == None:
            return None
        return self.nodes[0]

    def getRightValue(self):
        if self.nodes == None:
            return None
        return self.nodes[1]

class ASTWhile(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getCondition(self):
        return self.nodes[0]

    def getScope(self):
        return self.nodes[1]

class ASTIfElse(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTFunction(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTForwardDeclaration(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTParameters(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

    def getCondition(self):
        return self.nodes[0]

    def getIfScope(self):
        return self.nodes[1]

    def containsElseScope(self):
        return len(self.nodes) > 2

    def getElseScope(self):
        return self.nodes[2]

class ASTFor(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTCondition(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTScope(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTOneTokenStatement(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)

class ASTReturn(AST):
    def __init__(self, value, line, position, childNodes=None):
        super().__init__(value, line, position, childNodes)