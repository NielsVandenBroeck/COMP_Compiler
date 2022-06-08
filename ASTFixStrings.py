import re

from AST import ASTScope, ASTVariable, ASTDataType, AST, ASTParameters, ASTFunction, ASTArray, ASTPrintf, ASTInt, \
    ASTArrayIndex, ASTText, ASTScanf, ASTAdress

number = 0

class ASTFixStrings:
    def __init__(self, ast):
        self.arrayLength = {}
        self.preOrderTraverse(ast)

    def addString(self, array: ASTArray):
        if array.getType() == chr:
            self.arrayLength[array.getVariableName()] = array.getLength()

    def modifyPrintF(self, printF):
        newString = printF.getPrintString()
        toDoString = printF.getPrintString()
        itemCounter = 0
        while re.search("^.*%[0-9]*s.*", toDoString):
            if toDoString[0] == "%":
                itemCounter += 1
                format = ''
                lenght = ''
                lenghtInt = 0
                counter = 1
                while counter + 1 < len(toDoString) and (toDoString[counter + 1].isnumeric() or format == '') and not toDoString[counter] in ['s', 'c','f','d','i']:
                    lenght += toDoString[counter]
                    counter += 1
                format = toDoString[counter]
                if format != 's' or type(printF.nodes[itemCounter]) == ASTText:
                    toDoString = toDoString[1:]
                    continue

                arrayName = printF.nodes[itemCounter].getVariableName()
                if lenght != '':
                    lenghtInt = int(lenght)
                newString = newString.replace('%' + lenght + 's', '%c' * max(lenghtInt, self.arrayLength[arrayName]), 1)

                printF.nodes.pop(itemCounter)
                for i in range(max(lenghtInt, self.arrayLength[arrayName])):
                    printF.nodes.insert(itemCounter + i, ASTVariable(arrayName, childNodes=[ASTArrayIndex("index", 0,0, [ASTInt(str(i))])], type=chr))
                itemCounter += max(lenghtInt, self.arrayLength[arrayName]) - 1
            toDoString = toDoString[1:]
        printF.nodes[0].root = newString

    def modifyScanF(self, scanF: ASTScanf):
        newString = scanF.getScanString()
        toDoString = scanF.getScanString()
        itemCounter = 0
        while re.search("^.*%[0-9]*s.*", toDoString):
            if toDoString[0] == "%":
                itemCounter += 1
                format = ''
                lenght = ''
                lenghtInt = 0
                counter = 1
                while counter + 1 < len(toDoString) and (toDoString[counter + 1].isnumeric() or format == '') and not toDoString[counter] in ['s', 'c','f','d','i']:
                    lenght += toDoString[counter]
                    counter += 1
                format = toDoString[counter]
                arrayName = scanF.nodes[itemCounter].getVariableName()
                if format != 's' or not arrayName in self.arrayLength:
                    toDoString = toDoString[1:]
                    continue


                if lenght != '':
                    lenghtInt = int(lenght)
                newString = newString.replace('%' + lenght + 's', '%c' * max(lenghtInt, self.arrayLength[arrayName]), 1)

                scanF.nodes.pop(itemCounter)
                for i in range(max(lenghtInt, self.arrayLength[arrayName])):
                    scanF.nodes.insert(itemCounter + i, ASTAdress(ASTAdress, 0, 0, [ASTVariable(arrayName, childNodes=[ASTArrayIndex("index", 0,0, [ASTInt(str(i))])], type=chr)]))
                itemCounter += max(lenghtInt, self.arrayLength[arrayName]) - 1
            toDoString = toDoString[1:]
        scanF.nodes[0].root = newString

    def preOrderTraverse(self, ast: ASTPrintf):
        if type(ast) == ASTArray:
            self.addString(ast)
            return
        elif type(ast) == ASTPrintf:
            self.modifyPrintF(ast)
            return
        elif type(ast) == ASTScanf:
            self.modifyScanF(ast)
        elif ast.nodes != None:
            for node in ast.nodes:
                self.preOrderTraverse(node)
        return


