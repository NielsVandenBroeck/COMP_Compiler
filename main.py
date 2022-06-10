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
        input_stream = FileStream(filePath)
        lexer = grammar1Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = grammar1Parser(stream)
        tree = parser.start()

        visistor = ASTGenerator()
        ast = visistor.visit(tree)
        return ast

def runOneLLVM(path, runLLVM):
    print(path + ":")
    ast = generateAST(path)
    path = path.split('.')[0]
    ast.constantFold()

    ASTFixScoping(ast)

    with open(path+".dot", 'w') as myFile:
        myFile.write(ast.getDot())

    llvm = LLVMGenerator(path+".ll", ast)
    llvm.write()

    print("Compiling complete")
    print()
    if runLLVM:
        os.system("lli-9 " + path+".ll")

def runMutipleLLVM(inputDir,runLLVM):
    if not os.path.exists(inputDir+"OutputFiles"):
        os.mkdir(inputDir + "OutputFiles")
    outputPath = inputDir+"OutputFiles/"

    workingCounter = 0
    brokenCounter = 0
    brokenFiles = []
    for filename in os.listdir(inputDir):
        print("\n---------------")
        try:
            print(filename + ":")
            ast = generateAST(inputDir + filename)

            ast.constantFold()

            ASTFixScoping(ast)

            with open(outputPath + filename.split(".")[0] + ".dot", 'w') as myFile:
                myFile.write(ast.getDot())

            llvm = LLVMGenerator(outputPath + filename.split(".")[0] + ".ll", ast)
            llvm.write()

            print("Compiling complete")

            print()
            if runLLVM:
                os.system("lli-9 " + outputPath + filename.split(".")[0] + ".ll")
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
    path = path.split('.')[0]
    ast.constantFold()

    ASTFixScoping(ast, None, True)
    ASTFixStrings(ast)

    with open(path+".dot", 'w') as myFile:
        myFile.write(ast.getDot())

    MipsProgram(ast,path+".s")
    if runMips:
        os.system("java -jar Mars.jar " + path+".s")

def runMultipleMips(inputDir, runMips):
    if not os.path.exists(inputDir+"OutputFiles"):
        os.mkdir(inputDir + "OutputFiles")
    outputPath = inputDir+"OutputFiles/"
    workingCounter = 0
    brokenCounter = 0
    brokenFiles = []
    for filename in os.listdir(inputDir):
        print("\n---------------")
        try:
            print(filename + ":")
            ast = generateAST(inputDir + filename)

            ast.constantFold()

            ASTFixScoping(ast, None, True)
            ASTFixStrings(ast)

            with open(outputPath + filename.split(".")[0] + ".dot", 'w') as myFile:
                myFile.write(ast.getDot())

            print("Compiling complete")

            MipsProgram(ast, outputPath + filename.split(".")[0]+".s")
            if runMips:
                os.system("java -jar Mars.jar " + outputPath + filename.split(".")[0]+".s")
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
    language = argv[1]
    runCompiledfile = argv[2] == "True"
    input = argv[3]
    if language == "llvm" and os.path.isdir(input):
        runMutipleLLVM(input, runCompiledfile)
    elif language == "llvm" and os.path.isfile(input):
        runOneLLVM(input, runCompiledfile)
    elif language == "mips"  and os.path.isdir(input):
        runMultipleMips(input,runCompiledfile)
    elif language == "mips"  and os.path.isfile(input):
        runOneMips(input, runCompiledfile)
    else:
        print("wrong format start program with following parameters:")
        print("\t-python main.py llvm True/False file/folder\t\t::([0]=language, [1]=run program after compile, [2]=file/folder location)")
        print("\t-python main.py mips True/False file/folder\t\t::([0]=language, [1]=run program after compile, [2]=file/folder location)")
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
