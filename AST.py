import operator


class AST():
    def __init__(self):
        self.nodes = None
        self.value = None
        self.type = None

    def __init__(self, value, type):
        self.nodes = None
        self.value = value
        self.type = type

    # internal function
    def setNodesIfNeeded(self):
        if self.nodes is None:
            self.nodes = []

    # adds a node
    def addNode(self, node):
        self.setNodesIfNeeded()
        self.nodes.append(node)

    #returns de node with index "item"
    def getNode(self, item):
        return self.nodes[item]

    def getDot(self):
        return "digraph G { \n" + self.getDotInternal(0) + "}"

    def getDotInternal(self, number = 0): #TODO kan efficienter
        id = ' (' + str(number) + ')'
        idPlusOne = ' (' + str(number + 1) + ')'
        string = ""
        if self.nodes is None:
            return ""

        string += '"' + str(self) + id + '"' + '[label="' + self.value + '"]' + "\n"
        for node in self.nodes:
            string += '"' + str(node) + idPlusOne + '"' + '[label="' + str(node.value) + '"]' + "\n"
            string += '"' + str(self) + id + '"' + "->" + '"' + str(node) + idPlusOne + '"' +"\n"
            string += node.getDotInternal(number + 1)

        return string

    def constantFold(self):
        dict1 = {'||': 0, '&&': 1, '<': 2, '>': 2, '==': 2, '<=': 2, '>=': 2, '!=': 2, '+': 3, '-': 3, '*': 4, '/': 4, '%': 4}
        #for i in range(len(self.nodes)):
        #    self.nodes[i].constantFold()
        if self.nodes is None:
            return
        for i in self.nodes:
            i.constantFold()
        if len(self.nodes) != 2:
            return
        elif self.value in dict1 and isinstance(self.nodes[0].value, float) and isinstance(self.nodes[1].value, float):
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
            self.value = float(ops[self.value](self.nodes[0].value, self.nodes[1].value))
            self.nodes = None

