import binascii
import os
import struct
import sys
import time

from antlr4 import *

from ASTFixScoping import ASTFixScoping
from LLVMProgram import LLVMProgram, LLVMFunction
from grammar1Lexer import grammar1Lexer
from grammar1Parser import grammar1Parser
from antlr4.tree.Trees import Trees

from grammar1Visitor import grammar1Visitor
from ASTGenerator import ASTGenerator
from LLVMGenerator import LLVMGenerator
import subprocess


def main(argv):
    # f = 8.3
    # exit(8.3.hex())

    # hexString = "40209999A0000000"
    # exit(8.3.hex())
    # goeie website: https://faun.pub/introduction-to-antlr-python-af8a3c603d23
    workingCounter = 0
    brokenCounter = 0
    brokenFiles = []


    if (len(argv) > 1):
        print(argv[1] + ":")
        input_stream = FileStream(argv[1])
        if(len(argv) > 1):
           input_stream = FileStream(argv[1])
        lexer = grammar1Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = grammar1Parser(stream)
        tree = parser.start()

        visistor = ASTGenerator()
        ast = visistor.visit(tree)

        ast.constantFold()

        ASTFixScoping(ast)

        with open("OutputFiles/dotVisualization.dot", 'w') as myFile:
            myFile.write(ast.getDot())

        llvm = LLVMGenerator("OutputFiles/code.ll", ast)
        llvm.write()

        print("Compiling complete")

        print()
        os.system("lli-9 " + "OutputFiles/code.ll")
        print("\nRunning complete")
        os.system("lli-9 " + " OutputFiles/code.ll")
    else:
        for filename in os.listdir("testFiles/juisteTestFiles"):
            print("\n---------------")
            try:
                print(filename + ":")
                input_stream = FileStream("testFiles/juisteTestFiles/" + filename)
                if(len(argv) > 1):
                    input_stream = FileStream(argv[1])
                lexer = grammar1Lexer(input_stream)
                stream = CommonTokenStream(lexer)
                parser = grammar1Parser(stream)
                tree = parser.start()

                visistor = ASTGenerator()
                ast = visistor.visit(tree)

                ast.constantFold()

                ASTFixScoping(ast)

                with open("OutputFiles/dotVisualization.dot", 'w') as myFile:
                    myFile.write(ast.getDot())

                llvm = LLVMGenerator("OutputFiles/" + filename.split(".")[0] + ".ll", ast)
                llvm.write()

                print("Compiling complete")

                print()
                os.system("lli-9 " + " OutputFiles/" + filename.split(".")[0] + ".ll")
                workingCounter += 1
                print("\nRunning complete")
                #if (workingCounter == 7):
                #    break
            except:
                print("Failed")
                brokenCounter += 1
                brokenFiles.append(filename)
            print()

    print("aantal werkende files:", workingCounter)
    print("aantal niet werkende files:", brokenCounter, ": ", brokenFiles)

    return 0


def printTree(tree):
    if (tree.getText() == '(' or tree.getText() == ')'):
        return True

    if (tree.getChildCount() == 0 or tree == None):
        return False

    counter = 0
    for child in tree.getChildren():
        if (printTree(child)):
            print("remove child:" + child.getText())
            del tree.children[counter]
        counter += 1
    return False


if __name__ == '__main__':
    main(sys.argv)
