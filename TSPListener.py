# Generated from TSP.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TSPParser import TSPParser
else:
    from TSPParser import TSPParser

# This class defines a complete listener for a parse tree produced by TSPParser.
class TSPListener(ParseTreeListener):

    # Enter a parse tree produced by TSPParser#policy.
    def enterPolicy(self, ctx:TSPParser.PolicyContext):
        pass

    # Exit a parse tree produced by TSPParser#policy.
    def exitPolicy(self, ctx:TSPParser.PolicyContext):
        pass


    # Enter a parse tree produced by TSPParser#policy_statement.
    def enterPolicy_statement(self, ctx:TSPParser.Policy_statementContext):
        pass

    # Exit a parse tree produced by TSPParser#policy_statement.
    def exitPolicy_statement(self, ctx:TSPParser.Policy_statementContext):
        pass


    # Enter a parse tree produced by TSPParser#location.
    def enterLocation(self, ctx:TSPParser.LocationContext):
        pass

    # Exit a parse tree produced by TSPParser#location.
    def exitLocation(self, ctx:TSPParser.LocationContext):
        pass


    # Enter a parse tree produced by TSPParser#device.
    def enterDevice(self, ctx:TSPParser.DeviceContext):
        pass

    # Exit a parse tree produced by TSPParser#device.
    def exitDevice(self, ctx:TSPParser.DeviceContext):
        pass


    # Enter a parse tree produced by TSPParser#datatype.
    def enterDatatype(self, ctx:TSPParser.DatatypeContext):
        pass

    # Exit a parse tree produced by TSPParser#datatype.
    def exitDatatype(self, ctx:TSPParser.DatatypeContext):
        pass


    # Enter a parse tree produced by TSPParser#command.
    def enterCommand(self, ctx:TSPParser.CommandContext):
        pass

    # Exit a parse tree produced by TSPParser#command.
    def exitCommand(self, ctx:TSPParser.CommandContext):
        pass


    # Enter a parse tree produced by TSPParser#report.
    def enterReport(self, ctx:TSPParser.ReportContext):
        pass

    # Exit a parse tree produced by TSPParser#report.
    def exitReport(self, ctx:TSPParser.ReportContext):
        pass


    # Enter a parse tree produced by TSPParser#command_type.
    def enterCommand_type(self, ctx:TSPParser.Command_typeContext):
        pass

    # Exit a parse tree produced by TSPParser#command_type.
    def exitCommand_type(self, ctx:TSPParser.Command_typeContext):
        pass


    # Enter a parse tree produced by TSPParser#report_type.
    def enterReport_type(self, ctx:TSPParser.Report_typeContext):
        pass

    # Exit a parse tree produced by TSPParser#report_type.
    def exitReport_type(self, ctx:TSPParser.Report_typeContext):
        pass


    # Enter a parse tree produced by TSPParser#value.
    def enterValue(self, ctx:TSPParser.ValueContext):
        pass

    # Exit a parse tree produced by TSPParser#value.
    def exitValue(self, ctx:TSPParser.ValueContext):
        pass



del TSPParser