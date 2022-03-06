import sys
from antlr4 import *
from grammar1Lexer import grammar1Lexer
from grammar1Parser import grammar1Parser
from antlr4.tree.Trees import Trees

from grammar1Visitor import grammar1Visitor
from visitorSubclass import VisitorSubclass


def main():
    #goeie website: https://faun.pub/introduction-to-antlr-python-af8a3c603d23
    input_stream = FileStream("inputfile.txt")
    lexer = grammar1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammar1Parser(stream)
    tree = parser.start()

    visistor = VisitorSubclass()
    output = visistor.visit(tree)#TODO nog een fout in volgorde van bewerkingen! (lijn 1,2 in inputfile haakjes zijn nog fout) + (weet niet zeker of de vistitor ineens mag omzetten naar AST)
    print(output.getDot())
    #print(dir(tree))
    #print(output)
    #print(dir(tree))
    #print(tree.body(0))
    #printTree(tree)
    #print(tree.getText())

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
    main()