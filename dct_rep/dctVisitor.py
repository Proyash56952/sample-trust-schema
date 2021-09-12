# Generated from dct.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .dctParser import dctParser
else:
    from dctParser import dctParser

# This class defines a complete generic visitor for a parse tree produced by dctParser.

class dctVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by dctParser#schema.
    def visitSchema(self, ctx:dctParser.SchemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dctParser#definition.
    def visitDefinition(self, ctx:dctParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dctParser#expression.
    def visitExpression(self, ctx:dctParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dctParser#name.
    def visitName(self, ctx:dctParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dctParser#identifier.
    def visitIdentifier(self, ctx:dctParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dctParser#signing_chain.
    def visitSigning_chain(self, ctx:dctParser.Signing_chainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dctParser#ustring.
    def visitUstring(self, ctx:dctParser.UstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dctParser#hstring.
    def visitHstring(self, ctx:dctParser.HstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dctParser#slash.
    def visitSlash(self, ctx:dctParser.SlashContext):
        return self.visitChildren(ctx)



del dctParser