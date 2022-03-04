import sys
from antlr4 import *
from mathematicalExpressionsLexer import mathematicalExpressionsLexer
from mathematicalExpressionsParser import mathematicalExpressionsParser


def main():
    input_stream = FileStream("inputfile.txt")
    lexer = mathematicalExpressionsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = mathematicalExpressionsParser(stream)
    tree = parser.program()


if __name__ == '__main__':
    main()
    print(++5)
    print("test");