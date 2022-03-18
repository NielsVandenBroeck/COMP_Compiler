import sys
from antlr4 import *
from grammar1Lexer import grammar1Lexer
from grammar1Parser import grammar1Parser
from antlr4.tree.Trees import Trees

from grammar1Visitor import grammar1Visitor
from ASTGenerator import ASTGenerator
from LLVMGenerator import LLVMGenerator

def main(argv):
    #goeie website: https://faun.pub/introduction-to-antlr-python-af8a3c603d23
    input_stream = FileStream(argv[1])
    lexer = grammar1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammar1Parser(stream)
    tree = parser.start()

    visistor = ASTGenerator()
    ast = visistor.visit(tree)
    ast.constantFold()
    llvm = LLVMGenerator("OutputFiles/code.ll", ast)

    with open("OutputFiles/dotVisualization.dot", 'w') as myFile:
        myFile.write(ast.getDot())

    print("Comiling complete")
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