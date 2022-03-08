# Generated from grammar1.g4 by ANTLR 4.9.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\33\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3")
        buf.write(u"\2\7\2\34\n\2\f\2\16\2\37\13\2\3\3\5\3\"\n\3\3\3\3\3")
        buf.write(u"\3\3\3\3\5\3(\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\61")
        buf.write(u"\n\3\3\4\3\4\3\4\3\4\5\4\67\n\4\3\5\3\5\3\6\3\6\3\6\3")
        buf.write(u"\6\5\6?\n\6\3\7\3\7\3\7\5\7D\n\7\3\b\3\b\3\b\5\bI\n\b")
        buf.write(u"\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f")
        buf.write(u"\3\f\5\fX\n\f\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22")
        buf.write(u"\24\26\30\2\5\3\2\3\6\3\2\b\t\3\2\b\24\2\\\2\35\3\2\2")
        buf.write(u"\2\4\60\3\2\2\2\6\66\3\2\2\2\b8\3\2\2\2\n>\3\2\2\2\f")
        buf.write(u"C\3\2\2\2\16H\3\2\2\2\20J\3\2\2\2\22M\3\2\2\2\24Q\3\2")
        buf.write(u"\2\2\26W\3\2\2\2\30Y\3\2\2\2\32\34\5\4\3\2\33\32\3\2")
        buf.write(u"\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\3\3")
        buf.write(u"\2\2\2\37\35\3\2\2\2 \"\7\31\2\2! \3\2\2\2!\"\3\2\2\2")
        buf.write(u"\"#\3\2\2\2#$\5\b\5\2$%\7\7\2\2%&\7\32\2\2&(\3\2\2\2")
        buf.write(u"\'!\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\5\n\6\2*+\7\25\2\2")
        buf.write(u"+\61\3\2\2\2,-\7\7\2\2-.\5\6\4\2./\7\25\2\2/\61\3\2\2")
        buf.write(u"\2\60\'\3\2\2\2\60,\3\2\2\2\61\5\3\2\2\2\62\63\7\b\2")
        buf.write(u"\2\63\67\7\b\2\2\64\65\7\t\2\2\65\67\7\t\2\2\66\62\3")
        buf.write(u"\2\2\2\66\64\3\2\2\2\67\7\3\2\2\289\t\2\2\29\t\3\2\2")
        buf.write(u"\2:?\5\24\13\2;?\5\26\f\2<?\5\22\n\2=?\5\20\t\2>:\3\2")
        buf.write(u"\2\2>;\3\2\2\2><\3\2\2\2>=\3\2\2\2?\13\3\2\2\2@D\5\24")
        buf.write(u"\13\2AD\5\26\f\2BD\5\20\t\2C@\3\2\2\2CA\3\2\2\2CB\3\2")
        buf.write(u"\2\2D\r\3\2\2\2EI\5\24\13\2FI\5\26\f\2GI\5\22\n\2HE\3")
        buf.write(u"\2\2\2HF\3\2\2\2HG\3\2\2\2I\17\3\2\2\2JK\t\3\2\2KL\5")
        buf.write(u"\16\b\2L\21\3\2\2\2MN\5\f\7\2NO\5\30\r\2OP\5\n\6\2P\23")
        buf.write(u"\3\2\2\2QR\7\26\2\2RS\5\n\6\2ST\7\27\2\2T\25\3\2\2\2")
        buf.write(u"UX\7\30\2\2VX\7\7\2\2WU\3\2\2\2WV\3\2\2\2X\27\3\2\2\2")
        buf.write(u"YZ\t\4\2\2Z\31\3\2\2\2\13\35!\'\60\66>CHW")
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
                     u"'const'", u"'='" ]

    symbolicNames = [ u"<INVALID>", u"INT", u"FLOAT", u"CHAR", u"POINTER", 
                      u"VARIABLENAME", u"PLUS", u"MINUS", u"TIMES", u"DIV", 
                      u"GT", u"LT", u"EQ", u"GTE", u"LTE", u"NEQ", u"MOD", 
                      u"AND", u"OR", u"SEMICOLON", u"LPAREN", u"RPAREN", 
                      u"NUMBER", u"CONST", u"IS", u"WS" ]

    RULE_start = 0
    RULE_programLine = 1
    RULE_identifierOP = 2
    RULE_dataType = 3
    RULE_body = 4
    RULE_leftOperationBody = 5
    RULE_unaryBody = 6
    RULE_unary = 7
    RULE_bodyOperationBody = 8
    RULE_paren = 9
    RULE_data = 10
    RULE_operation = 11

    ruleNames =  [ u"start", u"programLine", u"identifierOP", u"dataType", 
                   u"body", u"leftOperationBody", u"unaryBody", u"unary", 
                   u"bodyOperationBody", u"paren", u"data", u"operation" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    CHAR=3
    POINTER=4
    VARIABLENAME=5
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
    CONST=23
    IS=24
    WS=25

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
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammar1Parser.INT) | (1 << grammar1Parser.FLOAT) | (1 << grammar1Parser.CHAR) | (1 << grammar1Parser.POINTER) | (1 << grammar1Parser.VARIABLENAME) | (1 << grammar1Parser.PLUS) | (1 << grammar1Parser.MINUS) | (1 << grammar1Parser.LPAREN) | (1 << grammar1Parser.NUMBER) | (1 << grammar1Parser.CONST))) != 0):
                self.state = 24
                self.programLine()
                self.state = 29
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


        def VARIABLENAME(self):
            return self.getToken(grammar1Parser.VARIABLENAME, 0)

        def IS(self):
            return self.getToken(grammar1Parser.IS, 0)

        def CONST(self):
            return self.getToken(grammar1Parser.CONST, 0)

        def identifierOP(self):
            return self.getTypedRuleContext(grammar1Parser.IdentifierOPContext,0)


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
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammar1Parser.INT) | (1 << grammar1Parser.FLOAT) | (1 << grammar1Parser.CHAR) | (1 << grammar1Parser.POINTER) | (1 << grammar1Parser.CONST))) != 0):
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==grammar1Parser.CONST:
                        self.state = 30
                        self.match(grammar1Parser.CONST)


                    self.state = 33
                    self.dataType()
                    self.state = 34
                    self.match(grammar1Parser.VARIABLENAME)
                    self.state = 35
                    self.match(grammar1Parser.IS)


                self.state = 39
                localctx.line = self.body()
                self.state = 40
                self.match(grammar1Parser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(grammar1Parser.VARIABLENAME)
                self.state = 43
                self.identifierOP()
                self.state = 44
                self.match(grammar1Parser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierOPContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.IdentifierOPContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self, i=None):
            if i is None:
                return self.getTokens(grammar1Parser.PLUS)
            else:
                return self.getToken(grammar1Parser.PLUS, i)

        def MINUS(self, i=None):
            if i is None:
                return self.getTokens(grammar1Parser.MINUS)
            else:
                return self.getToken(grammar1Parser.MINUS, i)

        def getRuleIndex(self):
            return grammar1Parser.RULE_identifierOP

        def enterRule(self, listener):
            if hasattr(listener, "enterIdentifierOP"):
                listener.enterIdentifierOP(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdentifierOP"):
                listener.exitIdentifierOP(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitIdentifierOP"):
                return visitor.visitIdentifierOP(self)
            else:
                return visitor.visitChildren(self)




    def identifierOP(self):

        localctx = grammar1Parser.IdentifierOPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_identifierOP)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammar1Parser.PLUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(grammar1Parser.PLUS)
                self.state = 49
                self.match(grammar1Parser.PLUS)
                pass
            elif token in [grammar1Parser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(grammar1Parser.MINUS)
                self.state = 51
                self.match(grammar1Parser.MINUS)
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
        self.enterRule(localctx, 6, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
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


        def data(self):
            return self.getTypedRuleContext(grammar1Parser.DataContext,0)


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
        self.enterRule(localctx, 8, self.RULE_body)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.paren()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.data()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.bodyOperationBody()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
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


        def data(self):
            return self.getTypedRuleContext(grammar1Parser.DataContext,0)


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
        self.enterRule(localctx, 10, self.RULE_leftOperationBody)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammar1Parser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.paren()
                pass
            elif token in [grammar1Parser.VARIABLENAME, grammar1Parser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.data()
                pass
            elif token in [grammar1Parser.PLUS, grammar1Parser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
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


        def data(self):
            return self.getTypedRuleContext(grammar1Parser.DataContext,0)


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
        self.enterRule(localctx, 12, self.RULE_unaryBody)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.paren()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.data()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
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
        self.enterRule(localctx, 14, self.RULE_unary)
        self._la = 0 # Token type
        try:
            localctx = grammar1Parser.UnaryExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            localctx.sign = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==grammar1Parser.PLUS or _la==grammar1Parser.MINUS):
                localctx.sign = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 73
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
        self.enterRule(localctx, 16, self.RULE_bodyOperationBody)
        try:
            localctx = grammar1Parser.OperationExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            localctx.lValue = self.leftOperationBody()
            self.state = 76
            localctx.op = self.operation()
            self.state = 77
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
        self.enterRule(localctx, 18, self.RULE_paren)
        try:
            localctx = grammar1Parser.ParenExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(grammar1Parser.LPAREN)
            self.state = 80
            localctx.value = self.body()
            self.state = 81
            self.match(grammar1Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.DataContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar1Parser.RULE_data

     
        def copyFrom(self, ctx):
            super(grammar1Parser.DataContext, self).copyFrom(ctx)



    class NumberExpressionContext(DataContext):

        def __init__(self, parser, ctx): # actually a grammar1Parser.DataContext)
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


    class VariableExpressionContext(DataContext):

        def __init__(self, parser, ctx): # actually a grammar1Parser.DataContext)
            super(grammar1Parser.VariableExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VARIABLENAME(self):
            return self.getToken(grammar1Parser.VARIABLENAME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVariableExpression"):
                listener.enterVariableExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariableExpression"):
                listener.exitVariableExpression(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitVariableExpression"):
                return visitor.visitVariableExpression(self)
            else:
                return visitor.visitChildren(self)



    def data(self):

        localctx = grammar1Parser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_data)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammar1Parser.NUMBER]:
                localctx = grammar1Parser.NumberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                localctx.value = self.match(grammar1Parser.NUMBER)
                pass
            elif token in [grammar1Parser.VARIABLENAME]:
                localctx = grammar1Parser.VariableExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(grammar1Parser.VARIABLENAME)
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
        self.enterRule(localctx, 22, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
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





