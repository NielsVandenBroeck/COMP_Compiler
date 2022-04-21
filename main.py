import binascii
import struct
import sys
import time
import bitstring

from antlr4 import *

from LLVMProgram import LLVMProgram, LLVMFunction
from grammar1Lexer import grammar1Lexer
from grammar1Parser import grammar1Parser
from antlr4.tree.Trees import Trees

from grammar1Visitor import grammar1Visitor
from ASTGenerator import ASTGenerator
from LLVMGenerator import LLVMGenerator
import subprocess

def main(argv):
    #f = 8.3
    #exit(8.3.hex())

    #hexString = "40209999A0000000"
    #exit(8.3.hex())
    #goeie website: https://faun.pub/introduction-to-antlr-python-af8a3c603d23
    input_stream = FileStream("ErrorFile.txt")
    if(len(argv) > 1):
        input_stream = FileStream(argv[1])
    lexer = grammar1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammar1Parser(stream)
    tree = parser.start()

    visistor = ASTGenerator()
    ast = visistor.visit(tree)

    ast.constantFold()

    with open("OutputFiles/dotVisualization.dot", 'w') as myFile:
        myFile.write(ast.getDot())


    llvm = LLVMGenerator("OutputFiles/code.ll", ast)
    llvm.write()

    with open("OutputFiles/dotVisualization1.dot", 'w') as myFile:
        myFile.write(ast.getDot())


    print("Comiling complete")

    print("Running programm")

    """
    program = LLVMProgram()


    mainFunction = LLVMFunction("main")

    
    mainFunction.newVarible("a")
    mainFunction.setVaribleValue("a", 3)

    mainFunction.newVarible("b")
    mainFunction.setVaribleValue("b", 6)

    mainFunction.setVaribleValue("a", 10)
    mainFunction.setVaribleValue("a", 13)
    mainFunction.setVaribleValue("a", 17)
    mainFunction.setVaribleValue("a", 19)

    mainFunction.newVarible("c")
    mainFunction.addVarible("c", "a", "b")

    mainFunction.setVaribleValue("a", 5)

    mainFunction.newVarible("d")
    mainFunction.addVarible("d", "a", "b")

    mainFunction.print("c")
    mainFunction.newVarible("e", "i8", 1) #i8 = char, i32 is a signed number
    mainFunction.setVaribleValue("e", ord('\n'))
    mainFunction.print("e", chr)

    mainFunction.print("d")
    

    mainFunction.newSmartVarible("a", float)
    mainFunction.setVaribleValue("a", 8.3)
    mainFunction.print("a", float)

    mainFunction.setReturnValue(0)
    program.addFunction(mainFunction)

    program.output()
    """


    return 0

def printTree(tree):
    if(tree.getText() == '(' or tree.getText() == ')'):
        return True

    if (tree.getChildCount() == 0 or tree == None):
        return False

    counter = 0
    for child in tree.getChildren():
        if(printTree(child)):
            print("remove child:"  + child.getText())
            del tree.children[counter]
        counter += 1
    return False


if __name__ == '__main__':
    main(sys.argv)