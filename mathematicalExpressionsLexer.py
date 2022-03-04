# Generated from ../grammars/mathematicalExpressions.g4 by ANTLR 4.9.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\24a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write(u"\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write(u"\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3")
        buf.write(u"\20\3\20\3\21\3\21\3\22\3\22\6\22P\n\22\r\22\16\22Q\3")
        buf.write(u"\22\6\22U\n\22\r\22\16\22V\5\22Y\n\22\3\23\6\23\\\n\23")
        buf.write(u"\r\23\16\23]\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r")
        buf.write(u"\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write(u"!\22#\23%\24\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2d\2\3")
        buf.write(u"\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write(u"\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write(u"\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write(u"\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write(u"%\3\2\2\2\3\'\3\2\2\2\5)\3\2\2\2\7+\3\2\2\2\t-\3\2\2")
        buf.write(u"\2\13/\3\2\2\2\r\61\3\2\2\2\17\63\3\2\2\2\21\66\3\2\2")
        buf.write(u"\2\239\3\2\2\2\25<\3\2\2\2\27?\3\2\2\2\31A\3\2\2\2\33")
        buf.write(u"D\3\2\2\2\35G\3\2\2\2\37I\3\2\2\2!K\3\2\2\2#X\3\2\2\2")
        buf.write(u"%[\3\2\2\2\'(\7-\2\2(\4\3\2\2\2)*\7/\2\2*\6\3\2\2\2+")
        buf.write(u",\7,\2\2,\b\3\2\2\2-.\7\61\2\2.\n\3\2\2\2/\60\7@\2\2")
        buf.write(u"\60\f\3\2\2\2\61\62\7>\2\2\62\16\3\2\2\2\63\64\7?\2\2")
        buf.write(u"\64\65\7?\2\2\65\20\3\2\2\2\66\67\7@\2\2\678\7?\2\28")
        buf.write(u"\22\3\2\2\29:\7>\2\2:;\7?\2\2;\24\3\2\2\2<=\7#\2\2=>")
        buf.write(u"\7?\2\2>\26\3\2\2\2?@\7\'\2\2@\30\3\2\2\2AB\7(\2\2BC")
        buf.write(u"\7(\2\2C\32\3\2\2\2DE\7~\2\2EF\7~\2\2F\34\3\2\2\2GH\7")
        buf.write(u"=\2\2H\36\3\2\2\2IJ\7*\2\2J \3\2\2\2KL\7+\2\2L\"\3\2")
        buf.write(u"\2\2MO\7#\2\2NP\t\2\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2")
        buf.write(u"QR\3\2\2\2RY\3\2\2\2SU\t\2\2\2TS\3\2\2\2UV\3\2\2\2VT")
        buf.write(u"\3\2\2\2VW\3\2\2\2WY\3\2\2\2XM\3\2\2\2XT\3\2\2\2Y$\3")
        buf.write(u"\2\2\2Z\\\t\3\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3")
        buf.write(u"\2\2\2^_\3\2\2\2_`\b\23\2\2`&\3\2\2\2\7\2QVX]\3\b\2\2")
        return buf.getvalue()


class mathematicalExpressionsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIV = 4
    GT = 5
    LT = 6
    EQ = 7
    GTE = 8
    LTE = 9
    NEQ = 10
    MOD = 11
    AND = 12
    OR = 13
    SEMICOLON = 14
    LPAREN = 15
    RPAREN = 16
    NUMBER = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'+'", u"'-'", u"'*'", u"'/'", u"'>'", u"'<'", u"'=='", u"'>='", 
            u"'<='", u"'!='", u"'%'", u"'&&'", u"'||'", u"';'", u"'('", 
            u"')'" ]

    symbolicNames = [ u"<INVALID>",
            u"PLUS", u"MINUS", u"TIMES", u"DIV", u"GT", u"LT", u"EQ", u"GTE", 
            u"LTE", u"NEQ", u"MOD", u"AND", u"OR", u"SEMICOLON", u"LPAREN", 
            u"RPAREN", u"NUMBER", u"WS" ]

    ruleNames = [ u"PLUS", u"MINUS", u"TIMES", u"DIV", u"GT", u"LT", u"EQ", 
                  u"GTE", u"LTE", u"NEQ", u"MOD", u"AND", u"OR", u"SEMICOLON", 
                  u"LPAREN", u"RPAREN", u"NUMBER", u"WS" ]

    grammarFileName = u"mathematicalExpressions.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(mathematicalExpressionsLexer, self).__init__(input, output=output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


