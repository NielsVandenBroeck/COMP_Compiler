# Generated from ../grammars/mathematicalExpressions.g4 by ANTLR 4.9.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\24&\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2\f")
        buf.write(u"\2\16\2\17\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\31")
        buf.write(u"\n\3\3\3\3\3\3\3\3\3\7\3\37\n\3\f\3\16\3\"\13\3\3\4\3")
        buf.write(u"\4\3\4\2\3\4\5\2\4\6\2\4\3\2\3\4\3\2\3\17\2&\2\r\3\2")
        buf.write(u"\2\2\4\30\3\2\2\2\6#\3\2\2\2\b\t\5\4\3\2\t\n\7\20\2\2")
        buf.write(u"\n\f\3\2\2\2\13\b\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r")
        buf.write(u"\16\3\2\2\2\16\3\3\2\2\2\17\r\3\2\2\2\20\21\b\3\1\2\21")
        buf.write(u"\22\t\2\2\2\22\31\5\4\3\6\23\24\7\21\2\2\24\25\5\4\3")
        buf.write(u"\2\25\26\7\22\2\2\26\31\3\2\2\2\27\31\7\23\2\2\30\20")
        buf.write(u"\3\2\2\2\30\23\3\2\2\2\30\27\3\2\2\2\31 \3\2\2\2\32\33")
        buf.write(u"\f\3\2\2\33\34\5\6\4\2\34\35\5\4\3\4\35\37\3\2\2\2\36")
        buf.write(u"\32\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\5\3\2")
        buf.write(u"\2\2\" \3\2\2\2#$\t\3\2\2$\7\3\2\2\2\5\r\30 ")
        return buf.getvalue()


class mathematicalExpressionsParser ( Parser ):

    grammarFileName = "mathematicalExpressions.g4"

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
    RULE_operation = 2

    ruleNames =  [ u"program", u"body", u"operation" ]

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
        super(mathematicalExpressionsParser, self).__init__(input, output=output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mathematicalExpressionsParser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def body(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(mathematicalExpressionsParser.BodyContext)
            else:
                return self.getTypedRuleContext(mathematicalExpressionsParser.BodyContext,i)


        def SEMICOLON(self, i=None):
            if i is None:
                return self.getTokens(mathematicalExpressionsParser.SEMICOLON)
            else:
                return self.getToken(mathematicalExpressionsParser.SEMICOLON, i)

        def getRuleIndex(self):
            return mathematicalExpressionsParser.RULE_program

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

        localctx = mathematicalExpressionsParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mathematicalExpressionsParser.PLUS) | (1 << mathematicalExpressionsParser.MINUS) | (1 << mathematicalExpressionsParser.LPAREN) | (1 << mathematicalExpressionsParser.NUMBER))) != 0):
                self.state = 6
                self.body(0)
                self.state = 7
                self.match(mathematicalExpressionsParser.SEMICOLON)
                self.state = 13
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
            super(mathematicalExpressionsParser.BodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def body(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(mathematicalExpressionsParser.BodyContext)
            else:
                return self.getTypedRuleContext(mathematicalExpressionsParser.BodyContext,i)


        def MINUS(self):
            return self.getToken(mathematicalExpressionsParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(mathematicalExpressionsParser.PLUS, 0)

        def LPAREN(self):
            return self.getToken(mathematicalExpressionsParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(mathematicalExpressionsParser.RPAREN, 0)

        def NUMBER(self):
            return self.getToken(mathematicalExpressionsParser.NUMBER, 0)

        def operation(self):
            return self.getTypedRuleContext(mathematicalExpressionsParser.OperationContext,0)


        def getRuleIndex(self):
            return mathematicalExpressionsParser.RULE_body

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
        localctx = mathematicalExpressionsParser.BodyContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_body, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathematicalExpressionsParser.PLUS, mathematicalExpressionsParser.MINUS]:
                self.state = 15
                _la = self._input.LA(1)
                if not(_la==mathematicalExpressionsParser.PLUS or _la==mathematicalExpressionsParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16
                self.body(4)
                pass
            elif token in [mathematicalExpressionsParser.LPAREN]:
                self.state = 17
                self.match(mathematicalExpressionsParser.LPAREN)
                self.state = 18
                self.body(0)
                self.state = 19
                self.match(mathematicalExpressionsParser.RPAREN)
                pass
            elif token in [mathematicalExpressionsParser.NUMBER]:
                self.state = 21
                self.match(mathematicalExpressionsParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = mathematicalExpressionsParser.BodyContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_body)
                    self.state = 24
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 25
                    self.operation()
                    self.state = 26
                    self.body(2) 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mathematicalExpressionsParser.OperationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(mathematicalExpressionsParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(mathematicalExpressionsParser.MINUS, 0)

        def TIMES(self):
            return self.getToken(mathematicalExpressionsParser.TIMES, 0)

        def DIV(self):
            return self.getToken(mathematicalExpressionsParser.DIV, 0)

        def GT(self):
            return self.getToken(mathematicalExpressionsParser.GT, 0)

        def LT(self):
            return self.getToken(mathematicalExpressionsParser.LT, 0)

        def EQ(self):
            return self.getToken(mathematicalExpressionsParser.EQ, 0)

        def GTE(self):
            return self.getToken(mathematicalExpressionsParser.GTE, 0)

        def LTE(self):
            return self.getToken(mathematicalExpressionsParser.LTE, 0)

        def NEQ(self):
            return self.getToken(mathematicalExpressionsParser.NEQ, 0)

        def MOD(self):
            return self.getToken(mathematicalExpressionsParser.MOD, 0)

        def AND(self):
            return self.getToken(mathematicalExpressionsParser.AND, 0)

        def OR(self):
            return self.getToken(mathematicalExpressionsParser.OR, 0)

        def getRuleIndex(self):
            return mathematicalExpressionsParser.RULE_operation

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

        localctx = mathematicalExpressionsParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mathematicalExpressionsParser.PLUS) | (1 << mathematicalExpressionsParser.MINUS) | (1 << mathematicalExpressionsParser.TIMES) | (1 << mathematicalExpressionsParser.DIV) | (1 << mathematicalExpressionsParser.GT) | (1 << mathematicalExpressionsParser.LT) | (1 << mathematicalExpressionsParser.EQ) | (1 << mathematicalExpressionsParser.GTE) | (1 << mathematicalExpressionsParser.LTE) | (1 << mathematicalExpressionsParser.NEQ) | (1 << mathematicalExpressionsParser.MOD) | (1 << mathematicalExpressionsParser.AND) | (1 << mathematicalExpressionsParser.OR))) != 0)):
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
         




