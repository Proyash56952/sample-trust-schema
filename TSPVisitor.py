# Generated from TSP.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TSPParser import TSPParser
else:
    from TSPParser import TSPParser

# This class defines a complete generic visitor for a parse tree produced by TSPParser.

class TSPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TSPParser#policy.
    def visitPolicy(self, ctx:TSPParser.PolicyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSPParser#policy_statement.
    def visitPolicy_statement(self, ctx:TSPParser.Policy_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSPParser#location.
    def visitLocation(self, ctx:TSPParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSPParser#device.
    def visitDevice(self, ctx:TSPParser.DeviceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSPParser#datatype.
    def visitDatatype(self, ctx:TSPParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSPParser#command.
    def visitCommand(self, ctx:TSPParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSPParser#report.
    def visitReport(self, ctx:TSPParser.ReportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSPParser#command_type.
    def visitCommand_type(self, ctx:TSPParser.Command_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSPParser#report_type.
    def visitReport_type(self, ctx:TSPParser.Report_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSPParser#value.
    def visitValue(self, ctx:TSPParser.ValueContext):
        return self.visitChildren(ctx)



del TSPParser