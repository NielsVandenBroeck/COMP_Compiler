import sys
from antlr4 import *
from grammar1Lexer import grammar1Lexer
from grammar1Parser import grammar1Parser
from antlr4.tree.Trees import Trees


def main():
    input_stream = FileStream("inputfile.txt")
    lexer = grammar1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammar1Parser(stream)
    tree = parser.program()
    print(dir(tree))
    print(tree.getText())
    printTree(tree)
    print(tree.getText())

def printTree(tree):
    if(tree.getText() == '(' or tree.getText() == ')'):
        return True
    if(tree.getChildCount() == 0):
        return False
    for child in tree.getChildren():
        if(printTree(child)):
            tree.removeLastChild()
    return False


if __name__ == '__main__':
    main()