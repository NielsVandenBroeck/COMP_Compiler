import sys
from antlr4 import *
from mathematicalExpressionsLexer import mathematicalExpressionsLexer
from mathematicalExpressionsParser import mathematicalExpressionsParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = mathematicalExpressionsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = mathematicalExpressionsParser(stream)
    tree = parser.startRule()


if __name__ == '__main__':
    main(sys.argv)
    print("test");