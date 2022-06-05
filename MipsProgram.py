import struct

class MipsProgram:
    stackCounter = 0
    data = []
    programmArray = []
    mipsTypes = {int: ""}

    def __init__(self, AST):
        AST.CreateMipsCode()
        print(".data")
        for line in self.data:
            print(line)
        for line in self.programmArray:
            print(line)
        pass

    @staticmethod
    def addLineToProgramArray(line: str):
        MipsProgram.programmArray.append(line)

    @staticmethod
    def addLineToDataArray(line: str):
        MipsProgram.programmArray.append(line)


