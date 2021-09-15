# Generated from dct.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .dctParser import dctParser
else:
    from dctParser import dctParser

# This class defines a complete listener for a parse tree produced by dctParser.
class dctListener(ParseTreeListener):

    # Enter a parse tree produced by dctParser#schema.
    def enterSchema(self, ctx:dctParser.SchemaContext):
        pass

    # Exit a parse tree produced by dctParser#schema.
    def exitSchema(self, ctx:dctParser.SchemaContext):
        pass


    # Enter a parse tree produced by dctParser#definition.
    def enterDefinition(self, ctx:dctParser.DefinitionContext):
        pass

    # Exit a parse tree produced by dctParser#definition.
    def exitDefinition(self, ctx:dctParser.DefinitionContext):
        pass


    # Enter a parse tree produced by dctParser#expression.
    def enterExpression(self, ctx:dctParser.ExpressionContext):
        pass

    # Exit a parse tree produced by dctParser#expression.
    def exitExpression(self, ctx:dctParser.ExpressionContext):
        pass


    # Enter a parse tree produced by dctParser#name.
    def enterName(self, ctx:dctParser.NameContext):
        pass

    # Exit a parse tree produced by dctParser#name.
    def exitName(self, ctx:dctParser.NameContext):
        pass


    # Enter a parse tree produced by dctParser#identifier.
    def enterIdentifier(self, ctx:dctParser.IdentifierContext):
        pass

    # Exit a parse tree produced by dctParser#identifier.
    def exitIdentifier(self, ctx:dctParser.IdentifierContext):
        pass


    # Enter a parse tree produced by dctParser#signing_chain.
    def enterSigning_chain(self, ctx:dctParser.Signing_chainContext):
        pass

    # Exit a parse tree produced by dctParser#signing_chain.
    def exitSigning_chain(self, ctx:dctParser.Signing_chainContext):
        pass


    # Enter a parse tree produced by dctParser#constraints.
    def enterConstraints(self, ctx:dctParser.ConstraintsContext):
        pass

    # Exit a parse tree produced by dctParser#constraints.
    def exitConstraints(self, ctx:dctParser.ConstraintsContext):
        pass


    # Enter a parse tree produced by dctParser#constraint.
    def enterConstraint(self, ctx:dctParser.ConstraintContext):
        pass

    # Exit a parse tree produced by dctParser#constraint.
    def exitConstraint(self, ctx:dctParser.ConstraintContext):
        pass


    # Enter a parse tree produced by dctParser#constraint_body.
    def enterConstraint_body(self, ctx:dctParser.Constraint_bodyContext):
        pass

    # Exit a parse tree produced by dctParser#constraint_body.
    def exitConstraint_body(self, ctx:dctParser.Constraint_bodyContext):
        pass


    # Enter a parse tree produced by dctParser#ustring.
    def enterUstring(self, ctx:dctParser.UstringContext):
        pass

    # Exit a parse tree produced by dctParser#ustring.
    def exitUstring(self, ctx:dctParser.UstringContext):
        pass


    # Enter a parse tree produced by dctParser#hstring.
    def enterHstring(self, ctx:dctParser.HstringContext):
        pass

    # Exit a parse tree produced by dctParser#hstring.
    def exitHstring(self, ctx:dctParser.HstringContext):
        pass


    # Enter a parse tree produced by dctParser#slash.
    def enterSlash(self, ctx:dctParser.SlashContext):
        pass

    # Exit a parse tree produced by dctParser#slash.
    def exitSlash(self, ctx:dctParser.SlashContext):
        pass



del dctParser