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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\7\2%\n\2\f\2\16")
        buf.write("\2(\13\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\5\5\66\n\5\3\6\3\6\3\6\3\6\3\7\3\7\5\7>\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\nK\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\20\3\20\6\20_\n\20\r\20\16\20`\5\20c\n\20")
        buf.write("\3\20\2\2\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2")
        buf.write("\2\2\\\2 \3\2\2\2\4)\3\2\2\2\6.\3\2\2\2\b\61\3\2\2\2\n")
        buf.write("\67\3\2\2\2\f=\3\2\2\2\16?\3\2\2\2\20C\3\2\2\2\22J\3\2")
        buf.write("\2\2\24L\3\2\2\2\26P\3\2\2\2\30T\3\2\2\2\32W\3\2\2\2\34")
        buf.write("Y\3\2\2\2\36b\3\2\2\2 !\7\4\2\2!\"\7\20\2\2\"&\7\3\2\2")
        buf.write("#%\5\4\3\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'")
        buf.write("\3\3\2\2\2(&\3\2\2\2)*\7\5\2\2*+\7\20\2\2+,\7\3\2\2,-")
        buf.write("\5\6\4\2-\5\3\2\2\2./\5\b\5\2/\60\5\n\6\2\60\7\3\2\2\2")
        buf.write("\61\62\7\6\2\2\62\65\7\3\2\2\63\66\5\f\7\2\64\66\5\22")
        buf.write("\n\2\65\63\3\2\2\2\65\64\3\2\2\2\66\t\3\2\2\2\678\7\7")
        buf.write("\2\289\7\3\2\29:\5\22\n\2:\13\3\2\2\2;>\5\16\b\2<>\5\20")
        buf.write("\t\2=;\3\2\2\2=<\3\2\2\2>\r\3\2\2\2?@\5\32\16\2@A\7\t")
        buf.write("\2\2AB\5\36\20\2B\17\3\2\2\2CD\5\32\16\2DE\7\n\2\2EF\5")
        buf.write("\36\20\2F\21\3\2\2\2GK\5\24\13\2HK\5\26\f\2IK\5\30\r\2")
        buf.write("JG\3\2\2\2JH\3\2\2\2JI\3\2\2\2K\23\3\2\2\2LM\5\32\16\2")
        buf.write("MN\7\13\2\2NO\5\34\17\2O\25\3\2\2\2PQ\5\32\16\2QR\7\f")
        buf.write("\2\2RS\5\34\17\2S\27\3\2\2\2TU\5\32\16\2UV\5\34\17\2V")
        buf.write("\31\3\2\2\2WX\7\r\2\2X\33\3\2\2\2YZ\7\16\2\2Z[\5\36\20")
        buf.write("\2[\35\3\2\2\2\\c\7\b\2\2]_\7\20\2\2^]\3\2\2\2_`\3\2\2")
        buf.write("\2`^\3\2\2\2`a\3\2\2\2ac\3\2\2\2b\\\3\2\2\2b^\3\2\2\2")
        buf.write("c\37\3\2\2\2\b&\65=J`b")
        return buf.getvalue()


class demoParser ( Parser ):

    grammarFileName = "demo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "COLON", "POLICY", "STATEMENT", "SIGN", 
                      "SIGNEDBY", "ANY", "COMMAND", "REPLY", "OPERATOR", 
                      "USER", "MYHOUSE", "KEY", "UNDERSCORE", "STRING", 
                      "WS" ]

    RULE_policy = 0
    RULE_statement = 1
    RULE_statement_body = 2
    RULE_sign_block = 3
    RULE_signed_by_block = 4
    RULE_msg = 5
    RULE_cmd = 6
    RULE_rep = 7
    RULE_cert = 8
    RULE_opcert = 9
    RULE_usercert = 10
    RULE_domaincert = 11
    RULE_domain = 12
    RULE_keyinfo = 13
    RULE_param = 14

    ruleNames =  [ "policy", "statement", "statement_body", "sign_block", 
                   "signed_by_block", "msg", "cmd", "rep", "cert", "opcert", 
                   "usercert", "domaincert", "domain", "keyinfo", "param" ]

    EOF = Token.EOF
    COLON=1
    POLICY=2
    STATEMENT=3
    SIGN=4
    SIGNEDBY=5
    ANY=6
    COMMAND=7
    REPLY=8
    OPERATOR=9
    USER=10
    MYHOUSE=11
    KEY=12
    UNDERSCORE=13
    STRING=14
    WS=15

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
            self.state = 30
            self.match(demoParser.POLICY)
            self.state = 31
            self.match(demoParser.STRING)
            self.state = 32
            self.match(demoParser.COLON)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==demoParser.STATEMENT:
                self.state = 33
                self.statement()
                self.state = 38
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

        def STATEMENT(self):
            return self.getToken(demoParser.STATEMENT, 0)

        def STRING(self):
            return self.getToken(demoParser.STRING, 0)

        def COLON(self):
            return self.getToken(demoParser.COLON, 0)

        def statement_body(self):
            return self.getTypedRuleContext(demoParser.Statement_bodyContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(demoParser.STATEMENT)
            self.state = 40
            self.match(demoParser.STRING)
            self.state = 41
            self.match(demoParser.COLON)
            self.state = 42
            self.statement_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_block(self):
            return self.getTypedRuleContext(demoParser.Sign_blockContext,0)


        def signed_by_block(self):
            return self.getTypedRuleContext(demoParser.Signed_by_blockContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_statement_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_body" ):
                listener.enterStatement_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_body" ):
                listener.exitStatement_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_body" ):
                return visitor.visitStatement_body(self)
            else:
                return visitor.visitChildren(self)




    def statement_body(self):

        localctx = demoParser.Statement_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.sign_block()
            self.state = 45
            self.signed_by_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGN(self):
            return self.getToken(demoParser.SIGN, 0)

        def COLON(self):
            return self.getToken(demoParser.COLON, 0)

        def msg(self):
            return self.getTypedRuleContext(demoParser.MsgContext,0)


        def cert(self):
            return self.getTypedRuleContext(demoParser.CertContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_sign_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign_block" ):
                listener.enterSign_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign_block" ):
                listener.exitSign_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_block" ):
                return visitor.visitSign_block(self)
            else:
                return visitor.visitChildren(self)




    def sign_block(self):

        localctx = demoParser.Sign_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sign_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(demoParser.SIGN)
            self.state = 48
            self.match(demoParser.COLON)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 49
                self.msg()
                pass

            elif la_ == 2:
                self.state = 50
                self.cert()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Signed_by_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGNEDBY(self):
            return self.getToken(demoParser.SIGNEDBY, 0)

        def COLON(self):
            return self.getToken(demoParser.COLON, 0)

        def cert(self):
            return self.getTypedRuleContext(demoParser.CertContext,0)


        def getRuleIndex(self):
            return demoParser.RULE_signed_by_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSigned_by_block" ):
                listener.enterSigned_by_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSigned_by_block" ):
                listener.exitSigned_by_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSigned_by_block" ):
                return visitor.visitSigned_by_block(self)
            else:
                return visitor.visitChildren(self)




    def signed_by_block(self):

        localctx = demoParser.Signed_by_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_signed_by_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(demoParser.SIGNEDBY)
            self.state = 54
            self.match(demoParser.COLON)
            self.state = 55
            self.cert()
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
        self.enterRule(localctx, 10, self.RULE_msg)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.cmd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
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
        self.enterRule(localctx, 12, self.RULE_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.domain()
            self.state = 62
            self.match(demoParser.COMMAND)
            self.state = 63
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
        self.enterRule(localctx, 14, self.RULE_rep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.domain()
            self.state = 66
            self.match(demoParser.REPLY)
            self.state = 67
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
        self.enterRule(localctx, 16, self.RULE_cert)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.opcert()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.usercert()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
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
        self.enterRule(localctx, 18, self.RULE_opcert)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.domain()
            self.state = 75
            self.match(demoParser.OPERATOR)
            self.state = 76
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
        self.enterRule(localctx, 20, self.RULE_usercert)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.domain()
            self.state = 79
            self.match(demoParser.USER)
            self.state = 80
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
        self.enterRule(localctx, 22, self.RULE_domaincert)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.domain()
            self.state = 83
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
        self.enterRule(localctx, 24, self.RULE_domain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
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
        self.enterRule(localctx, 26, self.RULE_keyinfo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(demoParser.KEY)
            self.state = 88
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

        def ANY(self):
            return self.getToken(demoParser.ANY, 0)

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
        self.enterRule(localctx, 28, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [demoParser.ANY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(demoParser.ANY)
                pass
            elif token in [demoParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 91
                    self.match(demoParser.STRING)
                    self.state = 94 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==demoParser.STRING):
                        break

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





