# Generated from grammar1.g4 by ANTLR 4.9.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\32I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32")
        buf.write(u"\n\2\f\2\16\2\35\13\2\3\3\3\3\3\3\3\3\5\3#\n\3\3\3\3")
        buf.write(u"\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\5\5.\n\5\3\6\3\6\3\6\5")
        buf.write(u"\6\63\n\6\3\7\3\7\3\7\5\78\n\7\3\b\3\b\3\b\3\t\3\t\3")
        buf.write(u"\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\2\2\r\2")
        buf.write(u"\4\6\b\n\f\16\20\22\24\26\2\5\3\2\3\6\3\2\b\t\3\2\b\24")
        buf.write(u"\2F\2\33\3\2\2\2\4\"\3\2\2\2\6\'\3\2\2\2\b-\3\2\2\2\n")
        buf.write(u"\62\3\2\2\2\f\67\3\2\2\2\169\3\2\2\2\20<\3\2\2\2\22@")
        buf.write(u"\3\2\2\2\24D\3\2\2\2\26F\3\2\2\2\30\32\5\4\3\2\31\30")
        buf.write(u"\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34")
        buf.write(u"\3\3\2\2\2\35\33\3\2\2\2\36\37\5\6\4\2\37 \7\7\2\2 !")
        buf.write(u"\7\31\2\2!#\3\2\2\2\"\36\3\2\2\2\"#\3\2\2\2#$\3\2\2\2")
        buf.write(u"$%\5\b\5\2%&\7\25\2\2&\5\3\2\2\2\'(\t\2\2\2(\7\3\2\2")
        buf.write(u"\2).\5\22\n\2*.\5\24\13\2+.\5\20\t\2,.\5\16\b\2-)\3\2")
        buf.write(u"\2\2-*\3\2\2\2-+\3\2\2\2-,\3\2\2\2.\t\3\2\2\2/\63\5\22")
        buf.write(u"\n\2\60\63\5\24\13\2\61\63\5\16\b\2\62/\3\2\2\2\62\60")
        buf.write(u"\3\2\2\2\62\61\3\2\2\2\63\13\3\2\2\2\648\5\22\n\2\65")
        buf.write(u"8\5\24\13\2\668\5\20\t\2\67\64\3\2\2\2\67\65\3\2\2\2")
        buf.write(u"\67\66\3\2\2\28\r\3\2\2\29:\t\3\2\2:;\5\f\7\2;\17\3\2")
        buf.write(u"\2\2<=\5\n\6\2=>\5\26\f\2>?\5\b\5\2?\21\3\2\2\2@A\7\26")
        buf.write(u"\2\2AB\5\b\5\2BC\7\27\2\2C\23\3\2\2\2DE\7\30\2\2E\25")
        buf.write(u"\3\2\2\2FG\t\4\2\2G\27\3\2\2\2\7\33\"-\62\67")
        return buf.getvalue()


class grammar1Parser ( Parser ):

    grammarFileName = "grammar1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'int'", u"'float'", u"'CHAR'", u"'pointer'", 
                     u"<INVALID>", u"'+'", u"'-'", u"'*'", u"'/'", u"'>'", 
                     u"'<'", u"'=='", u"'>='", u"'<='", u"'!='", u"'%'", 
                     u"'&&'", u"'||'", u"';'", u"'('", u"')'", u"<INVALID>", 
                     u"'='" ]

    symbolicNames = [ u"<INVALID>", u"INT", u"FLOAT", u"CHAR", u"POINTER", 
                      u"NAME", u"PLUS", u"MINUS", u"TIMES", u"DIV", u"GT", 
                      u"LT", u"EQ", u"GTE", u"LTE", u"NEQ", u"MOD", u"AND", 
                      u"OR", u"SEMICOLON", u"LPAREN", u"RPAREN", u"NUMBER", 
                      u"IS", u"WS" ]

    RULE_start = 0
    RULE_programLine = 1
    RULE_dataType = 2
    RULE_body = 3
    RULE_leftOperationBody = 4
    RULE_unaryBody = 5
    RULE_unary = 6
    RULE_bodyOperationBody = 7
    RULE_paren = 8
    RULE_number = 9
    RULE_operation = 10

    ruleNames =  [ u"start", u"programLine", u"dataType", u"body", u"leftOperationBody", 
                   u"unaryBody", u"unary", u"bodyOperationBody", u"paren", 
                   u"number", u"operation" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    CHAR=3
    POINTER=4
    NAME=5
    PLUS=6
    MINUS=7
    TIMES=8
    DIV=9
    GT=10
    LT=11
    EQ=12
    GTE=13
    LTE=14
    NEQ=15
    MOD=16
    AND=17
    OR=18
    SEMICOLON=19
    LPAREN=20
    RPAREN=21
    NUMBER=22
    IS=23
    WS=24

    def __init__(self, input, output=sys.stdout):
        super(grammar1Parser, self).__init__(input, output=output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.StartContext, self).__init__(parent, invokingState)
            self.parser = parser

        def programLine(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(grammar1Parser.ProgramLineContext)
            else:
                return self.getTypedRuleContext(grammar1Parser.ProgramLineContext,i)


        def getRuleIndex(self):
            return grammar1Parser.RULE_start

        def enterRule(self, listener):
            if hasattr(listener, "enterStart"):
                listener.enterStart(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStart"):
                listener.exitStart(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitStart"):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = grammar1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammar1Parser.INT) | (1 << grammar1Parser.FLOAT) | (1 << grammar1Parser.CHAR) | (1 << grammar1Parser.POINTER) | (1 << grammar1Parser.PLUS) | (1 << grammar1Parser.MINUS) | (1 << grammar1Parser.LPAREN) | (1 << grammar1Parser.NUMBER))) != 0):
                self.state = 22
                self.programLine()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramLineContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.ProgramLineContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.line = None # BodyContext

        def SEMICOLON(self):
            return self.getToken(grammar1Parser.SEMICOLON, 0)

        def body(self):
            return self.getTypedRuleContext(grammar1Parser.BodyContext,0)


        def dataType(self):
            return self.getTypedRuleContext(grammar1Parser.DataTypeContext,0)


        def NAME(self):
            return self.getToken(grammar1Parser.NAME, 0)

        def IS(self):
            return self.getToken(grammar1Parser.IS, 0)

        def getRuleIndex(self):
            return grammar1Parser.RULE_programLine

        def enterRule(self, listener):
            if hasattr(listener, "enterProgramLine"):
                listener.enterProgramLine(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProgramLine"):
                listener.exitProgramLine(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitProgramLine"):
                return visitor.visitProgramLine(self)
            else:
                return visitor.visitChildren(self)




    def programLine(self):

        localctx = grammar1Parser.ProgramLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammar1Parser.INT) | (1 << grammar1Parser.FLOAT) | (1 << grammar1Parser.CHAR) | (1 << grammar1Parser.POINTER))) != 0):
                self.state = 28
                self.dataType()
                self.state = 29
                self.match(grammar1Parser.NAME)
                self.state = 30
                self.match(grammar1Parser.IS)


            self.state = 34
            localctx.line = self.body()
            self.state = 35
            self.match(grammar1Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.DataTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(grammar1Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(grammar1Parser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(grammar1Parser.CHAR, 0)

        def POINTER(self):
            return self.getToken(grammar1Parser.POINTER, 0)

        def getRuleIndex(self):
            return grammar1Parser.RULE_dataType

        def enterRule(self, listener):
            if hasattr(listener, "enterDataType"):
                listener.enterDataType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDataType"):
                listener.exitDataType(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitDataType"):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = grammar1Parser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammar1Parser.INT) | (1 << grammar1Parser.FLOAT) | (1 << grammar1Parser.CHAR) | (1 << grammar1Parser.POINTER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.BodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def paren(self):
            return self.getTypedRuleContext(grammar1Parser.ParenContext,0)


        def number(self):
            return self.getTypedRuleContext(grammar1Parser.NumberContext,0)


        def bodyOperationBody(self):
            return self.getTypedRuleContext(grammar1Parser.BodyOperationBodyContext,0)


        def unary(self):
            return self.getTypedRuleContext(grammar1Parser.UnaryContext,0)


        def getRuleIndex(self):
            return grammar1Parser.RULE_body

        def enterRule(self, listener):
            if hasattr(listener, "enterBody"):
                listener.enterBody(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBody"):
                listener.exitBody(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitBody"):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = grammar1Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.paren()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.bodyOperationBody()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.unary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftOperationBodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.LeftOperationBodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def paren(self):
            return self.getTypedRuleContext(grammar1Parser.ParenContext,0)


        def number(self):
            return self.getTypedRuleContext(grammar1Parser.NumberContext,0)


        def unary(self):
            return self.getTypedRuleContext(grammar1Parser.UnaryContext,0)


        def getRuleIndex(self):
            return grammar1Parser.RULE_leftOperationBody

        def enterRule(self, listener):
            if hasattr(listener, "enterLeftOperationBody"):
                listener.enterLeftOperationBody(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLeftOperationBody"):
                listener.exitLeftOperationBody(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitLeftOperationBody"):
                return visitor.visitLeftOperationBody(self)
            else:
                return visitor.visitChildren(self)




    def leftOperationBody(self):

        localctx = grammar1Parser.LeftOperationBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_leftOperationBody)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammar1Parser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.paren()
                pass
            elif token in [grammar1Parser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.number()
                pass
            elif token in [grammar1Parser.PLUS, grammar1Parser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.unary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryBodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.UnaryBodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def paren(self):
            return self.getTypedRuleContext(grammar1Parser.ParenContext,0)


        def number(self):
            return self.getTypedRuleContext(grammar1Parser.NumberContext,0)


        def bodyOperationBody(self):
            return self.getTypedRuleContext(grammar1Parser.BodyOperationBodyContext,0)


        def getRuleIndex(self):
            return grammar1Parser.RULE_unaryBody

        def enterRule(self, listener):
            if hasattr(listener, "enterUnaryBody"):
                listener.enterUnaryBody(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUnaryBody"):
                listener.exitUnaryBody(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitUnaryBody"):
                return visitor.visitUnaryBody(self)
            else:
                return visitor.visitChildren(self)




    def unaryBody(self):

        localctx = grammar1Parser.UnaryBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unaryBody)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.paren()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.bodyOperationBody()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.UnaryContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar1Parser.RULE_unary

     
        def copyFrom(self, ctx):
            super(grammar1Parser.UnaryContext, self).copyFrom(ctx)



    class UnaryExpressionContext(UnaryContext):

        def __init__(self, parser, ctx): # actually a grammar1Parser.UnaryContext)
            super(grammar1Parser.UnaryExpressionContext, self).__init__(parser)
            self.sign = None # Token
            self.value = None # UnaryBodyContext
            self.copyFrom(ctx)

        def unaryBody(self):
            return self.getTypedRuleContext(grammar1Parser.UnaryBodyContext,0)

        def PLUS(self):
            return self.getToken(grammar1Parser.PLUS, 0)
        def MINUS(self):
            return self.getToken(grammar1Parser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUnaryExpression"):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUnaryExpression"):
                listener.exitUnaryExpression(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitUnaryExpression"):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)



    def unary(self):

        localctx = grammar1Parser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_unary)
        self._la = 0 # Token type
        try:
            localctx = grammar1Parser.UnaryExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            localctx.sign = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==grammar1Parser.PLUS or _la==grammar1Parser.MINUS):
                localctx.sign = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 56
            localctx.value = self.unaryBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyOperationBodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.BodyOperationBodyContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar1Parser.RULE_bodyOperationBody

     
        def copyFrom(self, ctx):
            super(grammar1Parser.BodyOperationBodyContext, self).copyFrom(ctx)



    class OperationExpressionContext(BodyOperationBodyContext):

        def __init__(self, parser, ctx): # actually a grammar1Parser.BodyOperationBodyContext)
            super(grammar1Parser.OperationExpressionContext, self).__init__(parser)
            self.lValue = None # LeftOperationBodyContext
            self.op = None # OperationContext
            self.rValue = None # BodyContext
            self.copyFrom(ctx)

        def leftOperationBody(self):
            return self.getTypedRuleContext(grammar1Parser.LeftOperationBodyContext,0)

        def operation(self):
            return self.getTypedRuleContext(grammar1Parser.OperationContext,0)

        def body(self):
            return self.getTypedRuleContext(grammar1Parser.BodyContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperationExpression"):
                listener.enterOperationExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperationExpression"):
                listener.exitOperationExpression(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitOperationExpression"):
                return visitor.visitOperationExpression(self)
            else:
                return visitor.visitChildren(self)



    def bodyOperationBody(self):

        localctx = grammar1Parser.BodyOperationBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_bodyOperationBody)
        try:
            localctx = grammar1Parser.OperationExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            localctx.lValue = self.leftOperationBody()
            self.state = 59
            localctx.op = self.operation()
            self.state = 60
            localctx.rValue = self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.ParenContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar1Parser.RULE_paren

     
        def copyFrom(self, ctx):
            super(grammar1Parser.ParenContext, self).copyFrom(ctx)



    class ParenExpressionContext(ParenContext):

        def __init__(self, parser, ctx): # actually a grammar1Parser.ParenContext)
            super(grammar1Parser.ParenExpressionContext, self).__init__(parser)
            self.value = None # BodyContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(grammar1Parser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(grammar1Parser.RPAREN, 0)
        def body(self):
            return self.getTypedRuleContext(grammar1Parser.BodyContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParenExpression"):
                listener.enterParenExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenExpression"):
                listener.exitParenExpression(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitParenExpression"):
                return visitor.visitParenExpression(self)
            else:
                return visitor.visitChildren(self)



    def paren(self):

        localctx = grammar1Parser.ParenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paren)
        try:
            localctx = grammar1Parser.ParenExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(grammar1Parser.LPAREN)
            self.state = 63
            localctx.value = self.body()
            self.state = 64
            self.match(grammar1Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.NumberContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar1Parser.RULE_number

     
        def copyFrom(self, ctx):
            super(grammar1Parser.NumberContext, self).copyFrom(ctx)



    class NumberExpressionContext(NumberContext):

        def __init__(self, parser, ctx): # actually a grammar1Parser.NumberContext)
            super(grammar1Parser.NumberExpressionContext, self).__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(grammar1Parser.NUMBER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterNumberExpression"):
                listener.enterNumberExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNumberExpression"):
                listener.exitNumberExpression(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitNumberExpression"):
                return visitor.visitNumberExpression(self)
            else:
                return visitor.visitChildren(self)



    def number(self):

        localctx = grammar1Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_number)
        try:
            localctx = grammar1Parser.NumberExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            localctx.value = self.match(grammar1Parser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.OperationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(grammar1Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(grammar1Parser.MINUS, 0)

        def TIMES(self):
            return self.getToken(grammar1Parser.TIMES, 0)

        def DIV(self):
            return self.getToken(grammar1Parser.DIV, 0)

        def GT(self):
            return self.getToken(grammar1Parser.GT, 0)

        def LT(self):
            return self.getToken(grammar1Parser.LT, 0)

        def EQ(self):
            return self.getToken(grammar1Parser.EQ, 0)

        def GTE(self):
            return self.getToken(grammar1Parser.GTE, 0)

        def LTE(self):
            return self.getToken(grammar1Parser.LTE, 0)

        def NEQ(self):
            return self.getToken(grammar1Parser.NEQ, 0)

        def MOD(self):
            return self.getToken(grammar1Parser.MOD, 0)

        def AND(self):
            return self.getToken(grammar1Parser.AND, 0)

        def OR(self):
            return self.getToken(grammar1Parser.OR, 0)

        def getRuleIndex(self):
            return grammar1Parser.RULE_operation

        def enterRule(self, listener):
            if hasattr(listener, "enterOperation"):
                listener.enterOperation(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperation"):
                listener.exitOperation(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitOperation"):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = grammar1Parser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammar1Parser.PLUS) | (1 << grammar1Parser.MINUS) | (1 << grammar1Parser.TIMES) | (1 << grammar1Parser.DIV) | (1 << grammar1Parser.GT) | (1 << grammar1Parser.LT) | (1 << grammar1Parser.EQ) | (1 << grammar1Parser.GTE) | (1 << grammar1Parser.LTE) | (1 << grammar1Parser.NEQ) | (1 << grammar1Parser.MOD) | (1 << grammar1Parser.AND) | (1 << grammar1Parser.OR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





