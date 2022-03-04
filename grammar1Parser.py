# Generated from grammar1.g4 by ANTLR 4.9.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\24\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\7")
        buf.write(u"\2\16\n\2\f\2\16\2\21\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\5\3\33\n\3\3\3\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$")
        buf.write(u"\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\3")
        buf.write(u"\5\3\5\3\5\2\3\4\6\2\4\6\b\2\4\3\2\3\4\3\2\3\17\2\64")
        buf.write(u"\2\17\3\2\2\2\4\32\3\2\2\2\6.\3\2\2\2\b\60\3\2\2\2\n")
        buf.write(u"\13\5\4\3\2\13\f\7\20\2\2\f\16\3\2\2\2\r\n\3\2\2\2\16")
        buf.write(u"\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\3\3\2\2\2\21")
        buf.write(u"\17\3\2\2\2\22\23\b\3\1\2\23\24\t\2\2\2\24\33\5\6\4\2")
        buf.write(u"\25\26\7\21\2\2\26\27\5\4\3\2\27\30\7\22\2\2\30\33\3")
        buf.write(u"\2\2\2\31\33\7\23\2\2\32\22\3\2\2\2\32\25\3\2\2\2\32")
        buf.write(u"\31\3\2\2\2\33\"\3\2\2\2\34\35\f\3\2\2\35\36\5\b\5\2")
        buf.write(u"\36\37\5\4\3\4\37!\3\2\2\2 \34\3\2\2\2!$\3\2\2\2\" \3")
        buf.write(u"\2\2\2\"#\3\2\2\2#\5\3\2\2\2$\"\3\2\2\2%&\7\21\2\2&\'")
        buf.write(u"\5\4\3\2\'(\7\22\2\2(/\3\2\2\2)/\7\23\2\2*+\5\4\3\2+")
        buf.write(u",\5\b\5\2,-\5\4\3\2-/\3\2\2\2.%\3\2\2\2.)\3\2\2\2.*\3")
        buf.write(u"\2\2\2/\7\3\2\2\2\60\61\t\3\2\2\61\t\3\2\2\2\6\17\32")
        buf.write(u"\".")
        return buf.getvalue()


class grammar1Parser ( Parser ):

    grammarFileName = "grammar1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'+'", u"'-'", u"'*'", u"'/'", u"'>'", 
                     u"'<'", u"'=='", u"'>='", u"'<='", u"'!='", u"'%'", 
                     u"'&&'", u"'||'", u"';'", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>", u"PLUS", u"MINUS", u"TIMES", u"DIV", 
                      u"GT", u"LT", u"EQ", u"GTE", u"LTE", u"NEQ", u"MOD", 
                      u"AND", u"OR", u"SEMICOLON", u"LPAREN", u"RPAREN", 
                      u"NUMBER", u"WS" ]

    RULE_program = 0
    RULE_body = 1
    RULE_unary = 2
    RULE_operation = 3

    ruleNames =  [ u"program", u"body", u"unary", u"operation" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    TIMES=3
    DIV=4
    GT=5
    LT=6
    EQ=7
    GTE=8
    LTE=9
    NEQ=10
    MOD=11
    AND=12
    OR=13
    SEMICOLON=14
    LPAREN=15
    RPAREN=16
    NUMBER=17
    WS=18

    def __init__(self, input, output=sys.stdout):
        super(grammar1Parser, self).__init__(input, output=output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def body(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(grammar1Parser.BodyContext)
            else:
                return self.getTypedRuleContext(grammar1Parser.BodyContext,i)


        def SEMICOLON(self, i=None):
            if i is None:
                return self.getTokens(grammar1Parser.SEMICOLON)
            else:
                return self.getToken(grammar1Parser.SEMICOLON, i)

        def getRuleIndex(self):
            return grammar1Parser.RULE_program

        def enterRule(self, listener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitProgram"):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = grammar1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammar1Parser.PLUS) | (1 << grammar1Parser.MINUS) | (1 << grammar1Parser.LPAREN) | (1 << grammar1Parser.NUMBER))) != 0):
                self.state = 8
                self.body(0)
                self.state = 9
                self.match(grammar1Parser.SEMICOLON)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def unary(self):
            return self.getTypedRuleContext(grammar1Parser.UnaryContext,0)


        def MINUS(self):
            return self.getToken(grammar1Parser.MINUS, 0)

        def PLUS(self):
            return self.getToken(grammar1Parser.PLUS, 0)

        def LPAREN(self):
            return self.getToken(grammar1Parser.LPAREN, 0)

        def body(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(grammar1Parser.BodyContext)
            else:
                return self.getTypedRuleContext(grammar1Parser.BodyContext,i)


        def RPAREN(self):
            return self.getToken(grammar1Parser.RPAREN, 0)

        def NUMBER(self):
            return self.getToken(grammar1Parser.NUMBER, 0)

        def operation(self):
            return self.getTypedRuleContext(grammar1Parser.OperationContext,0)


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



    def body(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = grammar1Parser.BodyContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_body, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammar1Parser.PLUS, grammar1Parser.MINUS]:
                self.state = 17
                _la = self._input.LA(1)
                if not(_la==grammar1Parser.PLUS or _la==grammar1Parser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 18
                self.unary()
                pass
            elif token in [grammar1Parser.LPAREN]:
                self.state = 19
                self.match(grammar1Parser.LPAREN)
                self.state = 20
                self.body(0)
                self.state = 21
                self.match(grammar1Parser.RPAREN)
                pass
            elif token in [grammar1Parser.NUMBER]:
                self.state = 23
                self.match(grammar1Parser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = grammar1Parser.BodyContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_body)
                    self.state = 26
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 27
                    self.operation()
                    self.state = 28
                    self.body(2) 
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(grammar1Parser.UnaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(grammar1Parser.LPAREN, 0)

        def body(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(grammar1Parser.BodyContext)
            else:
                return self.getTypedRuleContext(grammar1Parser.BodyContext,i)


        def RPAREN(self):
            return self.getToken(grammar1Parser.RPAREN, 0)

        def NUMBER(self):
            return self.getToken(grammar1Parser.NUMBER, 0)

        def operation(self):
            return self.getTypedRuleContext(grammar1Parser.OperationContext,0)


        def getRuleIndex(self):
            return grammar1Parser.RULE_unary

        def enterRule(self, listener):
            if hasattr(listener, "enterUnary"):
                listener.enterUnary(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUnary"):
                listener.exitUnary(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitUnary"):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = grammar1Parser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_unary)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(grammar1Parser.LPAREN)
                self.state = 36
                self.body(0)
                self.state = 37
                self.match(grammar1Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(grammar1Parser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.body(0)
                self.state = 41
                self.operation()
                self.state = 42
                self.body(0)
                pass


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
        self.enterRule(localctx, 6, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
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



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.body_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def body_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




