# Generated from dct.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("@\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3")
        buf.write("\5\3\5\3\5\6\5+\n\5\r\5\16\5,\3\5\3\5\3\6\3\6\3\6\5\6")
        buf.write("\64\n\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\2")
        buf.write("\2\13\2\4\6\b\n\f\16\20\22\2\2\2;\2\25\3\2\2\2\4#\3\2")
        buf.write("\2\2\6%\3\2\2\2\b*\3\2\2\2\n\63\3\2\2\2\f\65\3\2\2\2\16")
        buf.write("\67\3\2\2\2\20:\3\2\2\2\22=\3\2\2\2\24\26\5\4\3\2\25\24")
        buf.write("\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30")
        buf.write("\3\3\2\2\2\31\32\5\n\6\2\32\33\7\4\2\2\33\34\7\b\2\2\34")
        buf.write("$\3\2\2\2\35\36\5\n\6\2\36\37\7\4\2\2\37 \5\6\4\2 !\7")
        buf.write("\7\2\2!\"\5\n\6\2\"$\3\2\2\2#\31\3\2\2\2#\35\3\2\2\2$")
        buf.write("\5\3\2\2\2%&\5\b\5\2&\7\3\2\2\2\'(\5\n\6\2()\5\22\n\2")
        buf.write(")+\3\2\2\2*\'\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-.")
        buf.write("\3\2\2\2./\5\n\6\2/\t\3\2\2\2\60\64\7\b\2\2\61\64\5\16")
        buf.write("\b\2\62\64\5\20\t\2\63\60\3\2\2\2\63\61\3\2\2\2\63\62")
        buf.write("\3\2\2\2\64\13\3\2\2\2\65\66\7\b\2\2\66\r\3\2\2\2\678")
        buf.write("\7\5\2\289\7\b\2\29\17\3\2\2\2:;\7\6\2\2;<\7\b\2\2<\21")
        buf.write("\3\2\2\2=>\7\3\2\2>\23\3\2\2\2\6\27#,\63")
        return buf.getvalue()


class dctParser ( Parser ):

    grammarFileName = "dct.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/'", "':'", "'_'", "'#'", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COLON", "UNDERSCORE", "HASH", 
                      "SIGNEDBY", "STRING", "WS" ]

    RULE_schema = 0
    RULE_definition = 1
    RULE_expression = 2
    RULE_name = 3
    RULE_identifier = 4
    RULE_signing_chain = 5
    RULE_ustring = 6
    RULE_hstring = 7
    RULE_slash = 8

    ruleNames =  [ "schema", "definition", "expression", "name", "identifier", 
                   "signing_chain", "ustring", "hstring", "slash" ]

    EOF = Token.EOF
    T__0=1
    COLON=2
    UNDERSCORE=3
    HASH=4
    SIGNEDBY=5
    STRING=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SchemaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dctParser.DefinitionContext)
            else:
                return self.getTypedRuleContext(dctParser.DefinitionContext,i)


        def getRuleIndex(self):
            return dctParser.RULE_schema

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchema" ):
                listener.enterSchema(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchema" ):
                listener.exitSchema(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSchema" ):
                return visitor.visitSchema(self)
            else:
                return visitor.visitChildren(self)




    def schema(self):

        localctx = dctParser.SchemaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_schema)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.definition()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dctParser.UNDERSCORE) | (1 << dctParser.HASH) | (1 << dctParser.STRING))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dctParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(dctParser.IdentifierContext,i)


        def COLON(self):
            return self.getToken(dctParser.COLON, 0)

        def STRING(self):
            return self.getToken(dctParser.STRING, 0)

        def expression(self):
            return self.getTypedRuleContext(dctParser.ExpressionContext,0)


        def SIGNEDBY(self):
            return self.getToken(dctParser.SIGNEDBY, 0)

        def getRuleIndex(self):
            return dctParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = dctParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_definition)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.identifier()
                self.state = 24
                self.match(dctParser.COLON)
                self.state = 25
                self.match(dctParser.STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.identifier()
                self.state = 28
                self.match(dctParser.COLON)
                self.state = 29
                self.expression()
                self.state = 30
                self.match(dctParser.SIGNEDBY)
                self.state = 31
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(dctParser.NameContext,0)


        def getRuleIndex(self):
            return dctParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = dctParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dctParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(dctParser.IdentifierContext,i)


        def slash(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dctParser.SlashContext)
            else:
                return self.getTypedRuleContext(dctParser.SlashContext,i)


        def getRuleIndex(self):
            return dctParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = dctParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 37
                    self.identifier()
                    self.state = 38
                    self.slash()

                else:
                    raise NoViableAltException(self)
                self.state = 42 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 44
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(dctParser.STRING, 0)

        def ustring(self):
            return self.getTypedRuleContext(dctParser.UstringContext,0)


        def hstring(self):
            return self.getTypedRuleContext(dctParser.HstringContext,0)


        def getRuleIndex(self):
            return dctParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = dctParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_identifier)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dctParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(dctParser.STRING)
                pass
            elif token in [dctParser.UNDERSCORE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.ustring()
                pass
            elif token in [dctParser.HASH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.hstring()
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


    class Signing_chainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(dctParser.STRING, 0)

        def getRuleIndex(self):
            return dctParser.RULE_signing_chain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSigning_chain" ):
                listener.enterSigning_chain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSigning_chain" ):
                listener.exitSigning_chain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSigning_chain" ):
                return visitor.visitSigning_chain(self)
            else:
                return visitor.visitChildren(self)




    def signing_chain(self):

        localctx = dctParser.Signing_chainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_signing_chain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(dctParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UstringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(dctParser.UNDERSCORE, 0)

        def STRING(self):
            return self.getToken(dctParser.STRING, 0)

        def getRuleIndex(self):
            return dctParser.RULE_ustring

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUstring" ):
                listener.enterUstring(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUstring" ):
                listener.exitUstring(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUstring" ):
                return visitor.visitUstring(self)
            else:
                return visitor.visitChildren(self)




    def ustring(self):

        localctx = dctParser.UstringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ustring)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(dctParser.UNDERSCORE)

            self.state = 54
            self.match(dctParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HstringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(dctParser.HASH, 0)

        def STRING(self):
            return self.getToken(dctParser.STRING, 0)

        def getRuleIndex(self):
            return dctParser.RULE_hstring

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHstring" ):
                listener.enterHstring(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHstring" ):
                listener.exitHstring(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHstring" ):
                return visitor.visitHstring(self)
            else:
                return visitor.visitChildren(self)




    def hstring(self):

        localctx = dctParser.HstringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_hstring)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(dctParser.HASH)

            self.state = 57
            self.match(dctParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SlashContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dctParser.RULE_slash

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlash" ):
                listener.enterSlash(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlash" ):
                listener.exitSlash(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSlash" ):
                return visitor.visitSlash(self)
            else:
                return visitor.visitChildren(self)




    def slash(self):

        localctx = dctParser.SlashContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_slash)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(dctParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





