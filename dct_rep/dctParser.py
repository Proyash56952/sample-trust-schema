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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\6\2")
        buf.write("\34\n\2\r\2\16\2\35\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3<\n\3\3\4\3\4\5\4@\n\4\3\5")
        buf.write("\3\5\3\5\6\5E\n\5\r\5\16\5F\3\5\3\5\3\6\3\6\3\6\5\6N\n")
        buf.write("\6\3\7\3\7\3\b\3\b\3\b\7\bU\n\b\f\b\16\bX\13\b\3\t\3\t")
        buf.write("\3\t\3\t\7\t^\n\t\f\t\16\ta\13\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\2\2\16\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\2\2\2o\2\33\3\2\2\2\4;\3\2\2")
        buf.write("\2\6?\3\2\2\2\bD\3\2\2\2\nM\3\2\2\2\fO\3\2\2\2\16Q\3\2")
        buf.write("\2\2\20Y\3\2\2\2\22d\3\2\2\2\24h\3\2\2\2\26k\3\2\2\2\30")
        buf.write("n\3\2\2\2\32\34\5\4\3\2\33\32\3\2\2\2\34\35\3\2\2\2\35")
        buf.write("\33\3\2\2\2\35\36\3\2\2\2\36\3\3\2\2\2\37 \5\n\6\2 !\7")
        buf.write("\4\2\2!\"\7\r\2\2\"<\3\2\2\2#$\5\n\6\2$%\7\4\2\2%&\5\6")
        buf.write("\4\2&\'\7\f\2\2\'(\5\n\6\2(<\3\2\2\2)*\5\n\6\2*+\7\4\2")
        buf.write("\2+,\5\6\4\2,-\7\5\2\2-.\5\16\b\2.<\3\2\2\2/\60\5\n\6")
        buf.write("\2\60\61\7\4\2\2\61\62\5\6\4\2\62\63\7\5\2\2\63\64\5\16")
        buf.write("\b\2\64\65\7\f\2\2\65\66\5\n\6\2\66<\3\2\2\2\678\5\n\6")
        buf.write("\289\7\4\2\29:\5\6\4\2:<\3\2\2\2;\37\3\2\2\2;#\3\2\2\2")
        buf.write(";)\3\2\2\2;/\3\2\2\2;\67\3\2\2\2<\5\3\2\2\2=@\5\b\5\2")
        buf.write(">@\5\n\6\2?=\3\2\2\2?>\3\2\2\2@\7\3\2\2\2AB\5\n\6\2BC")
        buf.write("\5\30\r\2CE\3\2\2\2DA\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3")
        buf.write("\2\2\2GH\3\2\2\2HI\5\n\6\2I\t\3\2\2\2JN\7\r\2\2KN\5\24")
        buf.write("\13\2LN\5\26\f\2MJ\3\2\2\2MK\3\2\2\2ML\3\2\2\2N\13\3\2")
        buf.write("\2\2OP\7\r\2\2P\r\3\2\2\2QV\5\20\t\2RS\7\b\2\2SU\5\20")
        buf.write("\t\2TR\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\17\3\2\2")
        buf.write("\2XV\3\2\2\2YZ\7\6\2\2Z_\5\22\n\2[\\\7\t\2\2\\^\5\22\n")
        buf.write("\2][\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3\2\2\2a")
        buf.write("_\3\2\2\2bc\7\7\2\2c\21\3\2\2\2de\5\n\6\2ef\7\4\2\2fg")
        buf.write("\7\r\2\2g\23\3\2\2\2hi\7\n\2\2ij\7\r\2\2j\25\3\2\2\2k")
        buf.write("l\7\13\2\2lm\7\r\2\2m\27\3\2\2\2no\7\3\2\2o\31\3\2\2\2")
        buf.write("\t\35;?FMV_")
        return buf.getvalue()


class dctParser ( Parser ):

    grammarFileName = "dct.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/'", "':'", "'&'", "'{'", "'}'", "'|'", 
                     "','", "'_'", "'#'", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COLON", "AND", "BO", "BC", 
                      "OR", "COMA", "UNDERSCORE", "HASH", "SIGNEDBY", "STRING", 
                      "WS" ]

    RULE_schema = 0
    RULE_definition = 1
    RULE_expression = 2
    RULE_name = 3
    RULE_identifier = 4
    RULE_signing_chain = 5
    RULE_constraints = 6
    RULE_constraint = 7
    RULE_constraint_body = 8
    RULE_ustring = 9
    RULE_hstring = 10
    RULE_slash = 11

    ruleNames =  [ "schema", "definition", "expression", "name", "identifier", 
                   "signing_chain", "constraints", "constraint", "constraint_body", 
                   "ustring", "hstring", "slash" ]

    EOF = Token.EOF
    T__0=1
    COLON=2
    AND=3
    BO=4
    BC=5
    OR=6
    COMA=7
    UNDERSCORE=8
    HASH=9
    SIGNEDBY=10
    STRING=11
    WS=12

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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.definition()
                self.state = 27 
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

        def AND(self):
            return self.getToken(dctParser.AND, 0)

        def constraints(self):
            return self.getTypedRuleContext(dctParser.ConstraintsContext,0)


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
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.identifier()
                self.state = 30
                self.match(dctParser.COLON)
                self.state = 31
                self.match(dctParser.STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.identifier()
                self.state = 34
                self.match(dctParser.COLON)
                self.state = 35
                self.expression()
                self.state = 36
                self.match(dctParser.SIGNEDBY)
                self.state = 37
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.identifier()
                self.state = 40
                self.match(dctParser.COLON)
                self.state = 41
                self.expression()
                self.state = 42
                self.match(dctParser.AND)
                self.state = 43
                self.constraints()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.identifier()
                self.state = 46
                self.match(dctParser.COLON)
                self.state = 47
                self.expression()
                self.state = 48
                self.match(dctParser.AND)
                self.state = 49
                self.constraints()
                self.state = 50
                self.match(dctParser.SIGNEDBY)
                self.state = 51
                self.identifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.identifier()
                self.state = 54
                self.match(dctParser.COLON)
                self.state = 55
                self.expression()
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


        def identifier(self):
            return self.getTypedRuleContext(dctParser.IdentifierContext,0)


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
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.identifier()
                pass


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
            self.state = 66 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 63
                    self.identifier()
                    self.state = 64
                    self.slash()

                else:
                    raise NoViableAltException(self)
                self.state = 68 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 70
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
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dctParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(dctParser.STRING)
                pass
            elif token in [dctParser.UNDERSCORE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.ustring()
                pass
            elif token in [dctParser.HASH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
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
            self.state = 77
            self.match(dctParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dctParser.ConstraintContext)
            else:
                return self.getTypedRuleContext(dctParser.ConstraintContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(dctParser.OR)
            else:
                return self.getToken(dctParser.OR, i)

        def getRuleIndex(self):
            return dctParser.RULE_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraints" ):
                listener.enterConstraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraints" ):
                listener.exitConstraints(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraints" ):
                return visitor.visitConstraints(self)
            else:
                return visitor.visitChildren(self)




    def constraints(self):

        localctx = dctParser.ConstraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.constraint()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dctParser.OR:
                self.state = 80
                self.match(dctParser.OR)
                self.state = 81
                self.constraint()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BO(self):
            return self.getToken(dctParser.BO, 0)

        def constraint_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dctParser.Constraint_bodyContext)
            else:
                return self.getTypedRuleContext(dctParser.Constraint_bodyContext,i)


        def BC(self):
            return self.getToken(dctParser.BC, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(dctParser.COMA)
            else:
                return self.getToken(dctParser.COMA, i)

        def getRuleIndex(self):
            return dctParser.RULE_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraint" ):
                listener.enterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraint" ):
                listener.exitConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraint" ):
                return visitor.visitConstraint(self)
            else:
                return visitor.visitChildren(self)




    def constraint(self):

        localctx = dctParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(dctParser.BO)
            self.state = 88
            self.constraint_body()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dctParser.COMA:
                self.state = 89
                self.match(dctParser.COMA)
                self.state = 90
                self.constraint_body()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(dctParser.BC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constraint_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dctParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(dctParser.COLON, 0)

        def STRING(self):
            return self.getToken(dctParser.STRING, 0)

        def getRuleIndex(self):
            return dctParser.RULE_constraint_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraint_body" ):
                listener.enterConstraint_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraint_body" ):
                listener.exitConstraint_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraint_body" ):
                return visitor.visitConstraint_body(self)
            else:
                return visitor.visitChildren(self)




    def constraint_body(self):

        localctx = dctParser.Constraint_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constraint_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.identifier()
            self.state = 99
            self.match(dctParser.COLON)
            self.state = 100
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
        self.enterRule(localctx, 18, self.RULE_ustring)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(dctParser.UNDERSCORE)

            self.state = 103
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
        self.enterRule(localctx, 20, self.RULE_hstring)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(dctParser.HASH)

            self.state = 106
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
        self.enterRule(localctx, 22, self.RULE_slash)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(dctParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





