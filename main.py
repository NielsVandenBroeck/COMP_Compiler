import binascii
import os
import struct
import sys
import time

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from ASTFixScoping import ASTFixScoping
from ASTFixStrings import ASTFixStrings
from LLVMProgram import LLVMProgram, LLVMFunction
from MipsProgram import MipsProgram
from grammar1Lexer import grammar1Lexer
from grammar1Parser import grammar1Parser
from antlr4.tree.Trees import Trees

from grammar1Visitor import grammar1Visitor
from ASTGenerator import ASTGenerator
from LLVMGenerator import LLVMGenerator
import subprocess

def generateAST(filePath):
    try:
        input_stream = FileStream(filePath)
        lexer = grammar1Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = grammar1Parser(stream)
        tree = parser.start()

        visistor = ASTGenerator()
        ast = visistor.visit(tree)
        return ast
    except:
        exit()

def runOneLLVM(path, runLLVM):
    print(path + ":")
    ast = generateAST(path)

    ast.constantFold()

    ASTFixScoping(ast)

    with open("OutputFiles/LLVM/OneFile/dotVisualization.dot", 'w') as myFile:
        myFile.write(ast.getDot())

    llvm = LLVMGenerator("OutputFiles/LLVM/OneFile/code.ll", ast)
    llvm.write()

    print("Compiling complete")
    print()
    if runLLVM:
        os.system("lli-9 " + "OutputFiles/LLVM/OneFile/code.ll")

def runMutipleLLVM(runLLVM):
    workingCounter = 0
    brokenCounter = 0
    brokenFiles = []
    for filename in os.listdir("testFiles/juisteTestFiles"):
        print("\n---------------")
        try:
            print(filename + ":")
            ast = generateAST("testFiles/juisteTestFiles/" + filename)

            ast.constantFold()

            ASTFixScoping(ast)

            with open("OutputFiles/LLVM/MultipleFiles/" + filename.split(".")[0] + ".dot", 'w') as myFile:
                myFile.write(ast.getDot())

            llvm = LLVMGenerator("OutputFiles/LLVM/MultipleFiles/" + filename.split(".")[0] + ".ll", ast)
            llvm.write()

            print("Compiling complete")

            print()
            if runLLVM:
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

def runOneMips(path, runMips):
    print(path + ":")
    ast = generateAST(path)

    ast.constantFold()

    ASTFixScoping(ast, None, True)
    ASTFixStrings(ast)

    with open("OutputFiles/MIPS/OneFile/dotVisualization.dot", 'w') as myFile:
        myFile.write(ast.getDot())

    MipsProgram(ast,"OutputFiles/Mips/OneFile/code.s")
    if runMips:
        os.system("java -jar Mars.jar " + "OutputFiles/MIPS/OneFile/code.s")

def runMultipleMips(runMips):
    workingCounter = 0
    brokenCounter = 0
    brokenFiles = []
    for filename in os.listdir("testFiles/juisteTestFiles"):
        print("\n---------------")
        try:
            print(filename + ":")
            ast = generateAST("testFiles/juisteTestFiles/" + filename)

            ast.constantFold()

            ASTFixScoping(ast, None, True)
            ASTFixStrings(ast)

            with open("OutputFiles/Mips/MultipleFiles/" + filename.split(".")[0] + ".dot", 'w') as myFile:
                myFile.write(ast.getDot())

            print("Compiling complete")

            MipsProgram(ast, "OutputFiles/Mips/MultipleFiles/" + filename.split(".")[0]+".s")
            if runMips:
                os.system("java -jar Mars.jar " + "OutputFiles/Mips/MultipleFiles/" + filename.split(".")[0]+".s")
            workingCounter += 1
            print("\nRunning complete")
        except Exception as e:
            print("Failed: ", str(e))
            brokenCounter += 1
            brokenFiles.append(filename)
    print()
    print("aantal werkende files:", workingCounter)
    print("aantal niet werkende files:", brokenCounter, ": ", brokenFiles)

def main(argv):
    if argv[1] == "llvm" and len(argv) == 3:
        runMutipleLLVM(argv[2] == "True")
    elif argv[1] == "llvm" and len(argv) == 4:
        runOneLLVM(argv[3], argv[2]  == "True")
    elif argv[1] == "mips" and len(argv) == 3:
        runMultipleMips(argv[2]  == "True")
    elif argv[1] == "mips" and len(argv) == 4:
        runOneMips(argv[3], argv[2]  == "True")
    else:
        print("wrong format start program with following parameters:")
        print("\t-python main.py llvm True/False\t\t([0]=language, [1]=run program after compile)")
        print("\t-python main.py llvm True/False file.c\t\t([0]=language, [1]=run program after compile, [2]=.c file location)")
        print("\t-python main.py mips True/False\t\t([0]=language, [1]=run program after compile)")
        print("\t-python main.py mips True/False file.c\t\t([0]=language, [1]=run program after compile, [2]=.c file location)")
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
