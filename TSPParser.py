# Generated from TSP.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("\67\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16")
        buf.write("\2\31\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\5\6")
        buf.write("\'\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\7\3\2")
        buf.write("\4\7\3\2\b\f\3\2\17\20\3\2\21\23\3\2\24\25\2.\2\27\3\2")
        buf.write("\2\2\4\33\3\2\2\2\6 \3\2\2\2\b\"\3\2\2\2\n&\3\2\2\2\f")
        buf.write("(\3\2\2\2\16,\3\2\2\2\20\60\3\2\2\2\22\62\3\2\2\2\24\64")
        buf.write("\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\27\3\2\2\2\31\32\3\2\2\2\32\3\3\2\2\2\33\34\7\3\2\2\34")
        buf.write("\35\5\6\4\2\35\36\5\b\5\2\36\37\5\n\6\2\37\5\3\2\2\2 ")
        buf.write("!\t\2\2\2!\7\3\2\2\2\"#\t\3\2\2#\t\3\2\2\2$\'\5\f\7\2")
        buf.write("%\'\5\16\b\2&$\3\2\2\2&%\3\2\2\2\'\13\3\2\2\2()\7\r\2")
        buf.write("\2)*\5\20\t\2*+\5\24\13\2+\r\3\2\2\2,-\7\16\2\2-.\5\22")
        buf.write("\n\2./\5\24\13\2/\17\3\2\2\2\60\61\t\4\2\2\61\21\3\2\2")
        buf.write("\2\62\63\t\5\2\2\63\23\3\2\2\2\64\65\t\6\2\2\65\25\3\2")
        buf.write("\2\2\4\31&")
        return buf.getvalue()


class TSPParser ( Parser ):

    grammarFileName = "TSP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "APPNAME", "BEDROOM", "KITCHEN", "LIVINGROOM", 
                      "PATIO", "OUTLET", "TV", "AC", "MOTIONSENSOR", "HEATER", 
                      "COMMAND", "REPORT", "ONOFF", "ROTATE", "STATUS", 
                      "ANGLE", "TEMPERATURE", "ID", "DIGIT", "WS" ]

    RULE_policy = 0
    RULE_policy_statement = 1
    RULE_location = 2
    RULE_device = 3
    RULE_datatype = 4
    RULE_command = 5
    RULE_report = 6
    RULE_command_type = 7
    RULE_report_type = 8
    RULE_value = 9

    ruleNames =  [ "policy", "policy_statement", "location", "device", "datatype", 
                   "command", "report", "command_type", "report_type", "value" ]

    EOF = Token.EOF
    APPNAME=1
    BEDROOM=2
    KITCHEN=3
    LIVINGROOM=4
    PATIO=5
    OUTLET=6
    TV=7
    AC=8
    MOTIONSENSOR=9
    HEATER=10
    COMMAND=11
    REPORT=12
    ONOFF=13
    ROTATE=14
    STATUS=15
    ANGLE=16
    TEMPERATURE=17
    ID=18
    DIGIT=19
    WS=20

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

        def policy_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TSPParser.Policy_statementContext)
            else:
                return self.getTypedRuleContext(TSPParser.Policy_statementContext,i)


        def getRuleIndex(self):
            return TSPParser.RULE_policy

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

        localctx = TSPParser.PolicyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_policy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.policy_statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==TSPParser.APPNAME):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Policy_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APPNAME(self):
            return self.getToken(TSPParser.APPNAME, 0)

        def location(self):
            return self.getTypedRuleContext(TSPParser.LocationContext,0)


        def device(self):
            return self.getTypedRuleContext(TSPParser.DeviceContext,0)


        def datatype(self):
            return self.getTypedRuleContext(TSPParser.DatatypeContext,0)


        def getRuleIndex(self):
            return TSPParser.RULE_policy_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy_statement" ):
                listener.enterPolicy_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy_statement" ):
                listener.exitPolicy_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolicy_statement" ):
                return visitor.visitPolicy_statement(self)
            else:
                return visitor.visitChildren(self)




    def policy_statement(self):

        localctx = TSPParser.Policy_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_policy_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(TSPParser.APPNAME)
            self.state = 26
            self.location()
            self.state = 27
            self.device()
            self.state = 28
            self.datatype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEDROOM(self):
            return self.getToken(TSPParser.BEDROOM, 0)

        def KITCHEN(self):
            return self.getToken(TSPParser.KITCHEN, 0)

        def LIVINGROOM(self):
            return self.getToken(TSPParser.LIVINGROOM, 0)

        def PATIO(self):
            return self.getToken(TSPParser.PATIO, 0)

        def getRuleIndex(self):
            return TSPParser.RULE_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocation" ):
                listener.enterLocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocation" ):
                listener.exitLocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocation" ):
                return visitor.visitLocation(self)
            else:
                return visitor.visitChildren(self)




    def location(self):

        localctx = TSPParser.LocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_location)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TSPParser.BEDROOM) | (1 << TSPParser.KITCHEN) | (1 << TSPParser.LIVINGROOM) | (1 << TSPParser.PATIO))) != 0)):
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


    class DeviceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTLET(self):
            return self.getToken(TSPParser.OUTLET, 0)

        def TV(self):
            return self.getToken(TSPParser.TV, 0)

        def AC(self):
            return self.getToken(TSPParser.AC, 0)

        def MOTIONSENSOR(self):
            return self.getToken(TSPParser.MOTIONSENSOR, 0)

        def HEATER(self):
            return self.getToken(TSPParser.HEATER, 0)

        def getRuleIndex(self):
            return TSPParser.RULE_device

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDevice" ):
                listener.enterDevice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDevice" ):
                listener.exitDevice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDevice" ):
                return visitor.visitDevice(self)
            else:
                return visitor.visitChildren(self)




    def device(self):

        localctx = TSPParser.DeviceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_device)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TSPParser.OUTLET) | (1 << TSPParser.TV) | (1 << TSPParser.AC) | (1 << TSPParser.MOTIONSENSOR) | (1 << TSPParser.HEATER))) != 0)):
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


    class DatatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(TSPParser.CommandContext,0)


        def report(self):
            return self.getTypedRuleContext(TSPParser.ReportContext,0)


        def getRuleIndex(self):
            return TSPParser.RULE_datatype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatatype" ):
                listener.enterDatatype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatatype" ):
                listener.exitDatatype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatatype" ):
                return visitor.visitDatatype(self)
            else:
                return visitor.visitChildren(self)




    def datatype(self):

        localctx = TSPParser.DatatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_datatype)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TSPParser.COMMAND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.command()
                pass
            elif token in [TSPParser.REPORT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.report()
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


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(TSPParser.COMMAND, 0)

        def command_type(self):
            return self.getTypedRuleContext(TSPParser.Command_typeContext,0)


        def value(self):
            return self.getTypedRuleContext(TSPParser.ValueContext,0)


        def getRuleIndex(self):
            return TSPParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = TSPParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(TSPParser.COMMAND)
            self.state = 39
            self.command_type()
            self.state = 40
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReportContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPORT(self):
            return self.getToken(TSPParser.REPORT, 0)

        def report_type(self):
            return self.getTypedRuleContext(TSPParser.Report_typeContext,0)


        def value(self):
            return self.getTypedRuleContext(TSPParser.ValueContext,0)


        def getRuleIndex(self):
            return TSPParser.RULE_report

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReport" ):
                listener.enterReport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReport" ):
                listener.exitReport(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReport" ):
                return visitor.visitReport(self)
            else:
                return visitor.visitChildren(self)




    def report(self):

        localctx = TSPParser.ReportContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_report)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(TSPParser.REPORT)
            self.state = 43
            self.report_type()
            self.state = 44
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Command_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONOFF(self):
            return self.getToken(TSPParser.ONOFF, 0)

        def ROTATE(self):
            return self.getToken(TSPParser.ROTATE, 0)

        def getRuleIndex(self):
            return TSPParser.RULE_command_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand_type" ):
                listener.enterCommand_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand_type" ):
                listener.exitCommand_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand_type" ):
                return visitor.visitCommand_type(self)
            else:
                return visitor.visitChildren(self)




    def command_type(self):

        localctx = TSPParser.Command_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_command_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not(_la==TSPParser.ONOFF or _la==TSPParser.ROTATE):
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


    class Report_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATUS(self):
            return self.getToken(TSPParser.STATUS, 0)

        def ANGLE(self):
            return self.getToken(TSPParser.ANGLE, 0)

        def TEMPERATURE(self):
            return self.getToken(TSPParser.TEMPERATURE, 0)

        def getRuleIndex(self):
            return TSPParser.RULE_report_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReport_type" ):
                listener.enterReport_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReport_type" ):
                listener.exitReport_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReport_type" ):
                return visitor.visitReport_type(self)
            else:
                return visitor.visitChildren(self)




    def report_type(self):

        localctx = TSPParser.Report_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_report_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TSPParser.STATUS) | (1 << TSPParser.ANGLE) | (1 << TSPParser.TEMPERATURE))) != 0)):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TSPParser.ID, 0)

        def DIGIT(self):
            return self.getToken(TSPParser.DIGIT, 0)

        def getRuleIndex(self):
            return TSPParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = TSPParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not(_la==TSPParser.ID or _la==TSPParser.DIGIT):
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





