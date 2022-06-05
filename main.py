import binascii
import os
import struct
import sys
import time

from antlr4 import *

from ASTFixScoping import ASTFixScoping
from LLVMProgram import LLVMProgram, LLVMFunction
from MipsProgram import MipsProgram
from grammar1Lexer import grammar1Lexer
from grammar1Parser import grammar1Parser
from antlr4.tree.Trees import Trees

from grammar1Visitor import grammar1Visitor
from ASTGenerator import ASTGenerator
from LLVMGenerator import LLVMGenerator
import subprocess

def runOneLLVM(path):
    print(path + ":")
    input_stream = FileStream(path)
    lexer = grammar1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammar1Parser(stream)
    tree = parser.start()

    visistor = ASTGenerator()
    ast = visistor.visit(tree)

    ast.constantFold()

    ASTFixScoping(ast)

    with open("OutputFiles/LLVM/OneFile/dotVisualization.dot", 'w') as myFile:
        myFile.write(ast.getDot())

    llvm = LLVMGenerator("OutputFiles/LLVM/OneFile/code.ll", ast)
    llvm.write()

    print("Compiling complete")
    print()
    os.system("lli-9 " + "OutputFiles/LLVM/OneFile/code.ll")

def runMutipleLLVM():
    workingCounter = 0
    brokenCounter = 0
    brokenFiles = []
    for filename in os.listdir("testFiles/juisteTestFiles"):
        print("\n---------------")
        try:
            print(filename + ":")
            input_stream = FileStream("testFiles/juisteTestFiles/" + filename)
            lexer = grammar1Lexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = grammar1Parser(stream)
            tree = parser.start()

            visistor = ASTGenerator()
            ast = visistor.visit(tree)

            ast.constantFold()

            ASTFixScoping(ast)

            with open("OutputFiles/LLVM/MultipleFiles/" + filename.split(".")[0] + ".dot", 'w') as myFile:
                myFile.write(ast.getDot())

            llvm = LLVMGenerator("OutputFiles/LLVM/MultipleFiles/" + filename.split(".")[0] + ".ll", ast)
            llvm.write()

            print("Compiling complete")

            print()
            os.system("lli-9 " + " OutputFiles/LLVM/MultipleFiles/" + filename.split(".")[0] + ".ll")
            workingCounter += 1
            print("\nRunning complete")
        except:
            print("Failed")
            brokenCounter += 1
            brokenFiles.append(filename)
    print()
    print("aantal werkende files:", workingCounter)
    print("aantal niet werkende files:", brokenCounter, ": ", brokenFiles)

def runOneMips(path):
    print(path + ":")
    input_stream = FileStream(path)
    lexer = grammar1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammar1Parser(stream)
    tree = parser.start()

    visistor = ASTGenerator()
    ast = visistor.visit(tree)

    ast.constantFold()

    ASTFixScoping(ast)

    with open("OutputFiles/MIPS/OneFile/dotVisualization.dot", 'w') as myFile:
        myFile.write(ast.getDot())

    MipsProgram(ast)

def runMultipleMips():
    pass

def main(argv):
    if argv[1] == "llvm" and len(argv) == 2:
        runMutipleLLVM()
    elif argv[1] == "llvm" and len(argv) == 3:
        runOneLLVM(argv[2])
    elif argv[1] == "mips" and len(argv) == 2:
        runMultipleMips()
    elif argv[1] == "mips" and len(argv) == 3:
        runOneMips(argv[2])
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
