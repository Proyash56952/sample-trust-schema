# Generated from demo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .demoParser import demoParser
else:
    from demoParser import demoParser

# This class defines a complete listener for a parse tree produced by demoParser.
class demoListener(ParseTreeListener):

    # Enter a parse tree produced by demoParser#policy.
    def enterPolicy(self, ctx:demoParser.PolicyContext):
        pass

    # Exit a parse tree produced by demoParser#policy.
    def exitPolicy(self, ctx:demoParser.PolicyContext):
        pass


    # Enter a parse tree produced by demoParser#statement.
    def enterStatement(self, ctx:demoParser.StatementContext):
        pass

    # Exit a parse tree produced by demoParser#statement.
    def exitStatement(self, ctx:demoParser.StatementContext):
        pass


    # Enter a parse tree produced by demoParser#statement_body.
    def enterStatement_body(self, ctx:demoParser.Statement_bodyContext):
        pass

    # Exit a parse tree produced by demoParser#statement_body.
    def exitStatement_body(self, ctx:demoParser.Statement_bodyContext):
        pass


    # Enter a parse tree produced by demoParser#sign_block.
    def enterSign_block(self, ctx:demoParser.Sign_blockContext):
        pass

    # Exit a parse tree produced by demoParser#sign_block.
    def exitSign_block(self, ctx:demoParser.Sign_blockContext):
        pass


    # Enter a parse tree produced by demoParser#signed_by_block.
    def enterSigned_by_block(self, ctx:demoParser.Signed_by_blockContext):
        pass

    # Exit a parse tree produced by demoParser#signed_by_block.
    def exitSigned_by_block(self, ctx:demoParser.Signed_by_blockContext):
        pass


    # Enter a parse tree produced by demoParser#msg.
    def enterMsg(self, ctx:demoParser.MsgContext):
        pass

    # Exit a parse tree produced by demoParser#msg.
    def exitMsg(self, ctx:demoParser.MsgContext):
        pass


    # Enter a parse tree produced by demoParser#cmd.
    def enterCmd(self, ctx:demoParser.CmdContext):
        pass

    # Exit a parse tree produced by demoParser#cmd.
    def exitCmd(self, ctx:demoParser.CmdContext):
        pass


    # Enter a parse tree produced by demoParser#rep.
    def enterRep(self, ctx:demoParser.RepContext):
        pass

    # Exit a parse tree produced by demoParser#rep.
    def exitRep(self, ctx:demoParser.RepContext):
        pass


    # Enter a parse tree produced by demoParser#cert.
    def enterCert(self, ctx:demoParser.CertContext):
        pass

    # Exit a parse tree produced by demoParser#cert.
    def exitCert(self, ctx:demoParser.CertContext):
        pass


    # Enter a parse tree produced by demoParser#opcert.
    def enterOpcert(self, ctx:demoParser.OpcertContext):
        pass

    # Exit a parse tree produced by demoParser#opcert.
    def exitOpcert(self, ctx:demoParser.OpcertContext):
        pass


    # Enter a parse tree produced by demoParser#usercert.
    def enterUsercert(self, ctx:demoParser.UsercertContext):
        pass

    # Exit a parse tree produced by demoParser#usercert.
    def exitUsercert(self, ctx:demoParser.UsercertContext):
        pass


    # Enter a parse tree produced by demoParser#domaincert.
    def enterDomaincert(self, ctx:demoParser.DomaincertContext):
        pass

    # Exit a parse tree produced by demoParser#domaincert.
    def exitDomaincert(self, ctx:demoParser.DomaincertContext):
        pass


    # Enter a parse tree produced by demoParser#domain.
    def enterDomain(self, ctx:demoParser.DomainContext):
        pass

    # Exit a parse tree produced by demoParser#domain.
    def exitDomain(self, ctx:demoParser.DomainContext):
        pass


    # Enter a parse tree produced by demoParser#keyinfo.
    def enterKeyinfo(self, ctx:demoParser.KeyinfoContext):
        pass

    # Exit a parse tree produced by demoParser#keyinfo.
    def exitKeyinfo(self, ctx:demoParser.KeyinfoContext):
        pass


    # Enter a parse tree produced by demoParser#param.
    def enterParam(self, ctx:demoParser.ParamContext):
        pass

    # Exit a parse tree produced by demoParser#param.
    def exitParam(self, ctx:demoParser.ParamContext):
        pass



del demoParser