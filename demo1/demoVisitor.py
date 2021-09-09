# Generated from demo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .demoParser import demoParser
else:
    from demoParser import demoParser

# This class defines a complete generic visitor for a parse tree produced by demoParser.

class demoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by demoParser#policy.
    def visitPolicy(self, ctx:demoParser.PolicyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#statement.
    def visitStatement(self, ctx:demoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#statement_body.
    def visitStatement_body(self, ctx:demoParser.Statement_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#sign_block.
    def visitSign_block(self, ctx:demoParser.Sign_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#signed_by_block.
    def visitSigned_by_block(self, ctx:demoParser.Signed_by_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#msg.
    def visitMsg(self, ctx:demoParser.MsgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#cmd.
    def visitCmd(self, ctx:demoParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#rep.
    def visitRep(self, ctx:demoParser.RepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#cert.
    def visitCert(self, ctx:demoParser.CertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#opcert.
    def visitOpcert(self, ctx:demoParser.OpcertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#usercert.
    def visitUsercert(self, ctx:demoParser.UsercertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#domaincert.
    def visitDomaincert(self, ctx:demoParser.DomaincertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#domain.
    def visitDomain(self, ctx:demoParser.DomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#keyinfo.
    def visitKeyinfo(self, ctx:demoParser.KeyinfoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by demoParser#param.
    def visitParam(self, ctx:demoParser.ParamContext):
        return self.visitChildren(ctx)



del demoParser