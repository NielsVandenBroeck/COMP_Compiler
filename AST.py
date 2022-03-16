import operator
from typing import Any

import graphviz

class AST():
    def __init__(self, value, childNodes = None):
        self.root = value
        self.nodes = childNodes

    # internal function
    def setNodesIfNeeded(self):
        if self.nodes is None:
            self.nodes = []

    # adds a node
    def addNode(self, node):
        self.setNodesIfNeeded()
        self.nodes.append(node)

    def getFirstDataType(self, node):
        print(type(node.root))
        if self.nodes is None:
            exit("no datatype found")
        if not isinstance(node.root, str):
            return node
        return self.getFirstDataType(node.nodes[0])

    def addNodeToMostLeftChild(self, node):
        if self.nodes is None:
            self.addNode(node)
            return
        print(node)
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

class ASTVariable(AST):
    def __init__(self, value, childNodes=None):
        super().__init__(value, childNodes)

class ASTDataType(AST):
    def __init__(self, value, childNodes=None):
        super().__init__(value, childNodes)

class ASTConst(AST):
    def __init__(self, value, childNodes=None):
        super().__init__(value, childNodes)





"""
    def constantFold(self):
        dict1 = {'||': 0, '&&': 1, '<': 2, '>': 2, '==': 2, '<=': 2, '>=': 2, '!=': 2, '+': 3, '-': 3, '*': 4, '/': 4, '%': 4}
        if self.nodes is None:
            return
        for i in self.nodes:
            i.constantFold()
        if len(self.nodes) == 1 and self.root == '-':
            value1 = self.nodes[0].value
            if isinstance(value1, float) or isinstance(value1, int):
                self.root = -value1
                self.nodes = None
            elif isinstance(value1, str):
                self.root = chr(-ord(value1[1]))
                self.nodes = None
        elif len(self.nodes) == 2:
            value1 = self.nodes[0].value
            value2 = self.nodes[1].value
            if self.root in dict1 and (isinstance(value1, float) or isinstance(value1, int) or isinstance(value1, str)) and (isinstance(value2, float) or isinstance(value2, int) or isinstance(value2, str)):
                if (isinstance(value1, str) and (len(value1) != 3 or value1[0] != '\'')) or (isinstance(value2, str) and (len(value2) != 3 or value2[0] != '\'')):
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
                    self.root = '\''+resulttype(ops[self.root](value1, value2))+'\''
                else:
                    self.root = resulttype(ops[self.root](value1,value2))
                self.nodes = None
"""