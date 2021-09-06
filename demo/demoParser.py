# Generated from demo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("p\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\7\2")
        buf.write("\'\n\2\f\2\16\2*\13\2\3\3\3\3\3\3\3\3\3\3\5\3\61\n\3\3")
        buf.write("\4\3\4\3\4\5\4\66\n\4\3\5\3\5\5\5:\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\5\bG\n\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\6\16Z\n\16\r\16\16\16[\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20g\n\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21n\n\21\3\21\2\2\22\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \2\2\2i\2\"\3\2\2\2\4\60\3\2\2\2\6\65\3\2\2")
        buf.write("\2\b9\3\2\2\2\n;\3\2\2\2\f?\3\2\2\2\16F\3\2\2\2\20H\3")
        buf.write("\2\2\2\22L\3\2\2\2\24P\3\2\2\2\26S\3\2\2\2\30U\3\2\2\2")
        buf.write("\32Y\3\2\2\2\34]\3\2\2\2\36f\3\2\2\2 m\3\2\2\2\"#\7\5")
        buf.write("\2\2#$\7\r\2\2$(\7\4\2\2%\'\5\4\3\2&%\3\2\2\2\'*\3\2\2")
        buf.write("\2(&\3\2\2\2()\3\2\2\2)\3\3\2\2\2*(\3\2\2\2+\61\5\b\5")
        buf.write("\2,-\5\16\b\2-.\7\3\2\2./\5\16\b\2/\61\3\2\2\2\60+\3\2")
        buf.write("\2\2\60,\3\2\2\2\61\5\3\2\2\2\62\66\5\34\17\2\63\66\5")
        buf.write("\36\20\2\64\66\5 \21\2\65\62\3\2\2\2\65\63\3\2\2\2\65")
        buf.write("\64\3\2\2\2\66\7\3\2\2\2\67:\5\n\6\28:\5\f\7\29\67\3\2")
        buf.write("\2\298\3\2\2\2:\t\3\2\2\2;<\5\26\f\2<=\7\6\2\2=>\5\32")
        buf.write("\16\2>\13\3\2\2\2?@\5\26\f\2@A\7\7\2\2AB\5\32\16\2B\r")
        buf.write("\3\2\2\2CG\5\20\t\2DG\5\22\n\2EG\5\24\13\2FC\3\2\2\2F")
        buf.write("D\3\2\2\2FE\3\2\2\2G\17\3\2\2\2HI\5\26\f\2IJ\7\b\2\2J")
        buf.write("K\5\30\r\2K\21\3\2\2\2LM\5\26\f\2MN\7\t\2\2NO\5\30\r\2")
        buf.write("O\23\3\2\2\2PQ\5\26\f\2QR\5\30\r\2R\25\3\2\2\2ST\7\n\2")
        buf.write("\2T\27\3\2\2\2UV\7\13\2\2VW\5\32\16\2W\31\3\2\2\2XZ\7")
        buf.write("\r\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\33\3")
        buf.write("\2\2\2]^\5\n\6\2^_\7\3\2\2_`\5\20\t\2`\35\3\2\2\2ab\5")
        buf.write("\f\7\2bc\7\3\2\2cd\5\20\t\2dg\3\2\2\2eg\5\22\n\2fa\3\2")
        buf.write("\2\2fe\3\2\2\2g\37\3\2\2\2hn\5\20\t\2ij\5\22\n\2jk\7\3")
        buf.write("\2\2kl\5\24\13\2ln\3\2\2\2mh\3\2\2\2mi\3\2\2\2n!\3\2\2")
        buf.write("\2\n(\60\659F[fm")
        return buf.getvalue()


class demoParser ( Parser ):

    grammarFileName = "demo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<='", "':'" ]

    symbolicNames = [ "<INVALID>", "SIGNEDBY", "COLON", "POLICY", "COMMAND", 
                      "REPLY", "OPERATOR", "USER", "MYHOUSE", "KEY", "UNDERSCORE", 
                      "STRING", "WS" ]

    RULE_policy = 0
    RULE_statement = 1
    RULE_st = 2
    RULE_msg = 3
    RULE_cmd = 4
    RULE_rep = 5
    RULE_cert = 6
    RULE_opcert = 7
    RULE_usercert = 8
    RULE_domaincert = 9
    RULE_domain = 10
    RULE_keyinfo = 11
    RULE_param = 12
    RULE_s1 = 13
    RULE_s2 = 14
    RULE_s3 = 15

    ruleNames =  [ "policy", "statement", "st", "msg", "cmd", "rep", "cert", 
                   "opcert", "usercert", "domaincert", "domain", "keyinfo", 
                   "param", "s1", "s2", "s3" ]

    EOF = Token.EOF
    SIGNEDBY=1
    COLON=2
    POLICY=3
    COMMAND=4
    REPLY=5
    OPERATOR=6
    USER=7
    MYHOUSE=8
    KEY=9
    UNDERSCORE=10
    STRING=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PolicyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POLICY(self):
            return self.getToken(demoParser.POLICY, 0)

        def STRING(self):
            return self.getToken(demoParser.STRING, 0)

        def COLON(self):
            return self.getToken(demoParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(demoParser.StatementContext)
            else:
                return self.getTypedRuleContext(demoParser.StatementContext,i)


        def getRuleIndex(self):
            return demoParser.RULE_policy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy" ):
                listener.enterPolicy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy" ):
                listener.exitPolicy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolicy" ):
                return visitor.visitPolicy(self)
            else:
                return visitor.visitChildren(self)




    def policy(self):

        localctx = demoParser.PolicyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_policy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(demoParser.POLICY)
            self.state = 33
            self.match(demoParser.STRING)
            self.state = 34
            self.match(demoParser.COLON)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==demoParser.MYHOUSE:
                self.state = 35
                self.statement()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def msg(self):
            return self.getTypedRuleContext(demoParser.MsgContext,0)


        def cert(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(demoParser.CertContext)
            else:
                return self.getTypedRuleContext(demoParser.CertContext,i)


        def SIGNEDBY(self):
            return self.getToken(demoParser.SIGNEDBY, 0)

        def getRuleIndex(self):
            return demoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = demoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.msg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.cert()
                self.state = 43
                self.match(demoParser.SIGNEDBY)
                self.state = 44
                self.cert()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s1(self):
            return self.getTypedRuleContext(demoParser.S1Context,0)


        def s2(self):
            return self.getTypedRuleContext(demoParser.S2Context,0)


        def s3(self):
            return self.getTypedRuleContext(demoParser.S3Context,0)


        def getRuleIndex(self):
            return demoParser.RULE_st

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSt" ):
                listener.enterSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSt" ):
                listener.exitSt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSt" ):
                return visitor.visitSt(self)
            else:
                return visitor.visitChildren(self)




    def st(self):

        localctx = demoParser.StContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_st)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.s1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.s2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.s3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MsgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self):
            return self.getTypedRuleContext(demoParser.CmdContext,0)


        def rep(self):
            return self.getTypedRuleContext(demoParser.RepContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_msg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMsg" ):
                listener.enterMsg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMsg" ):
                listener.exitMsg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMsg" ):
                return visitor.visitMsg(self)
            else:
                return visitor.visitChildren(self)




    def msg(self):

        localctx = demoParser.MsgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_msg)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.cmd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.rep()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domain(self):
            return self.getTypedRuleContext(demoParser.DomainContext,0)


        def COMMAND(self):
            return self.getToken(demoParser.COMMAND, 0)

        def param(self):
            return self.getTypedRuleContext(demoParser.ParamContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd" ):
                return visitor.visitCmd(self)
            else:
                return visitor.visitChildren(self)




    def cmd(self):

        localctx = demoParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.domain()
            self.state = 58
            self.match(demoParser.COMMAND)
            self.state = 59
            self.param()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domain(self):
            return self.getTypedRuleContext(demoParser.DomainContext,0)


        def REPLY(self):
            return self.getToken(demoParser.REPLY, 0)

        def param(self):
            return self.getTypedRuleContext(demoParser.ParamContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_rep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRep" ):
                listener.enterRep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRep" ):
                listener.exitRep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRep" ):
                return visitor.visitRep(self)
            else:
                return visitor.visitChildren(self)




    def rep(self):

        localctx = demoParser.RepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.domain()
            self.state = 62
            self.match(demoParser.REPLY)
            self.state = 63
            self.param()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opcert(self):
            return self.getTypedRuleContext(demoParser.OpcertContext,0)


        def usercert(self):
            return self.getTypedRuleContext(demoParser.UsercertContext,0)


        def domaincert(self):
            return self.getTypedRuleContext(demoParser.DomaincertContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_cert

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCert" ):
                listener.enterCert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCert" ):
                listener.exitCert(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCert" ):
                return visitor.visitCert(self)
            else:
                return visitor.visitChildren(self)




    def cert(self):

        localctx = demoParser.CertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cert)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.opcert()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.usercert()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.domaincert()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domain(self):
            return self.getTypedRuleContext(demoParser.DomainContext,0)


        def OPERATOR(self):
            return self.getToken(demoParser.OPERATOR, 0)

        def keyinfo(self):
            return self.getTypedRuleContext(demoParser.KeyinfoContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_opcert

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcert" ):
                listener.enterOpcert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcert" ):
                listener.exitOpcert(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcert" ):
                return visitor.visitOpcert(self)
            else:
                return visitor.visitChildren(self)




    def opcert(self):

        localctx = demoParser.OpcertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opcert)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.domain()
            self.state = 71
            self.match(demoParser.OPERATOR)
            self.state = 72
            self.keyinfo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsercertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domain(self):
            return self.getTypedRuleContext(demoParser.DomainContext,0)


        def USER(self):
            return self.getToken(demoParser.USER, 0)

        def keyinfo(self):
            return self.getTypedRuleContext(demoParser.KeyinfoContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_usercert

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsercert" ):
                listener.enterUsercert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsercert" ):
                listener.exitUsercert(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsercert" ):
                return visitor.visitUsercert(self)
            else:
                return visitor.visitChildren(self)




    def usercert(self):

        localctx = demoParser.UsercertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_usercert)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.domain()
            self.state = 75
            self.match(demoParser.USER)
            self.state = 76
            self.keyinfo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomaincertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domain(self):
            return self.getTypedRuleContext(demoParser.DomainContext,0)


        def keyinfo(self):
            return self.getTypedRuleContext(demoParser.KeyinfoContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_domaincert

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomaincert" ):
                listener.enterDomaincert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomaincert" ):
                listener.exitDomaincert(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomaincert" ):
                return visitor.visitDomaincert(self)
            else:
                return visitor.visitChildren(self)




    def domaincert(self):

        localctx = demoParser.DomaincertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_domaincert)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.domain()
            self.state = 79
            self.keyinfo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MYHOUSE(self):
            return self.getToken(demoParser.MYHOUSE, 0)

        def getRuleIndex(self):
            return demoParser.RULE_domain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomain" ):
                listener.enterDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomain" ):
                listener.exitDomain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomain" ):
                return visitor.visitDomain(self)
            else:
                return visitor.visitChildren(self)




    def domain(self):

        localctx = demoParser.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_domain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(demoParser.MYHOUSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyinfoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(demoParser.KEY, 0)

        def param(self):
            return self.getTypedRuleContext(demoParser.ParamContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_keyinfo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyinfo" ):
                listener.enterKeyinfo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyinfo" ):
                listener.exitKeyinfo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyinfo" ):
                return visitor.visitKeyinfo(self)
            else:
                return visitor.visitChildren(self)




    def keyinfo(self):

        localctx = demoParser.KeyinfoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_keyinfo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(demoParser.KEY)
            self.state = 84
            self.param()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(demoParser.STRING)
            else:
                return self.getToken(demoParser.STRING, i)

        def getRuleIndex(self):
            return demoParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = demoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.match(demoParser.STRING)
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==demoParser.STRING):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self):
            return self.getTypedRuleContext(demoParser.CmdContext,0)


        def SIGNEDBY(self):
            return self.getToken(demoParser.SIGNEDBY, 0)

        def opcert(self):
            return self.getTypedRuleContext(demoParser.OpcertContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS1" ):
                return visitor.visitS1(self)
            else:
                return visitor.visitChildren(self)




    def s1(self):

        localctx = demoParser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_s1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.cmd()
            self.state = 92
            self.match(demoParser.SIGNEDBY)
            self.state = 93
            self.opcert()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rep(self):
            return self.getTypedRuleContext(demoParser.RepContext,0)


        def SIGNEDBY(self):
            return self.getToken(demoParser.SIGNEDBY, 0)

        def opcert(self):
            return self.getTypedRuleContext(demoParser.OpcertContext,0)


        def usercert(self):
            return self.getTypedRuleContext(demoParser.UsercertContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_s2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS2" ):
                listener.enterS2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS2" ):
                listener.exitS2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS2" ):
                return visitor.visitS2(self)
            else:
                return visitor.visitChildren(self)




    def s2(self):

        localctx = demoParser.S2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_s2)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.rep()
                self.state = 96
                self.match(demoParser.SIGNEDBY)
                self.state = 97
                self.opcert()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.usercert()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opcert(self):
            return self.getTypedRuleContext(demoParser.OpcertContext,0)


        def usercert(self):
            return self.getTypedRuleContext(demoParser.UsercertContext,0)


        def SIGNEDBY(self):
            return self.getToken(demoParser.SIGNEDBY, 0)

        def domaincert(self):
            return self.getTypedRuleContext(demoParser.DomaincertContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS3" ):
                return visitor.visitS3(self)
            else:
                return visitor.visitChildren(self)




    def s3(self):

        localctx = demoParser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_s3)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.opcert()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.usercert()
                self.state = 104
                self.match(demoParser.SIGNEDBY)
                self.state = 105
                self.domaincert()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





