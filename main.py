import sys
from antlr4 import *
from grammar1Lexer import grammar1Lexer
from grammar1Parser import grammar1Parser


def main():
    input_stream = FileStream("inputfile.txt")
    lexer = grammar1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammar1Parser(stream)
    tree = parser.program()


if __name__ == '__main__':
    main()
    print(+++5)
    print("test");