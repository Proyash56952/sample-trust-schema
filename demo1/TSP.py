from antlr4 import *
from demoLexer import demoLexer
from demoListener import demoListener
from demoParser import demoParser
from demoVisitor import demoVisitor
import sys

class Policy:
    pass

class Statement:
    pass
    
class AST:
    def __init__(self):
        self.type = None
        self.name = None
        self.domain = None

class CustomVisitor(demoVisitor):
    def __init__(self):
        self.policies = []
    
    def visitPolicy(self, ctx:demoParser.PolicyContext):
        pol = Policy()
        pol.name = ctx.STRING()
        st = []
        for c in ctx.statement():
            st.append(c.accept(self))
        pol.statements = st
        self.policies.append(pol)
    
    def visitStatement(self, ctx:demoParser.StatementContext):
        s = Statement()
        s.name = ctx.STRING()
        #print(inv.name)
        s.sign, s.signedby = ctx.statement_body().accept(self)
        return s
    
    def visitStatement_body(self, ctx:demoParser.Statement_bodyContext):
        sign = ctx.sign_block().accept(self)
        signedby = ctx.signed_by_block().accept(self)
        return sign, signedby

    def visitSign_block(self, ctx:demoParser.Sign_blockContext):
        if ctx.msg():
            block = ctx.msg().accept(self)
        elif ctx.cert():
            block = ctx.cert().accept(self)
        return block
            
    def visitMsg(self, ctx:demoParser.MsgContext):
        if ctx.cmd():
            msg = ctx.cmd().accept(self)
        elif ctx.rep():
            msg = ctx.rep().accept(self)
        return msg
    
    def visitCert(self, ctx:demoParser.CertContext):
        if ctx.opcert():
            cert = ctx.opcert().accept(self)
        elif ctx.usercert():
            cert = ctx.usercert().accept(self)
        elif ctx.domaincert():
            cert = ctx.domaincert().accept(self)
        return cert
        
    def visitCmd(self, ctx:demoParser.CmdContext):
        cmdNode = AST()
        cmdNode.domain = str(ctx.domain().accept(self))
        cmdNode.type = 'msg'
        cmdNode.name = 'cmd'
        return cmdNode
        
    def visitRep(self, ctx:demoParser.RepContext):
        repNode = AST()
        repNode.domain= str(ctx.domain().accept(self))
        repNode.type = 'msg'
        repNode.name = 'rep'
        return repNode
        
    def visitOpcert(self, ctx:demoParser.OpcertContext):
        opcertNode = AST()
        opcertNode.domain = str(ctx.domain().accept(self))
        opcertNode.type = 'cert'
        opcertNode.name = 'opcert'
        return opcertNode
        
    def visitUsercert(self, ctx:demoParser.UsercertContext):
        usercertNode = AST()
        usercertNode.domain= str(ctx.domain().accept(self))
        usercertNode.type = 'cert'
        usercertNode.name = 'usercert'
        return usercertNode
        
    def visitDomaincert(self, ctx:demoParser.DomaincertContext):
        domaincertNode = AST()
        domaincertNode.domain= str(ctx.domain().accept(self))
        domaincertNode.type = 'cert'
        domaincertNode.name = 'domaincert'
        return domaincertNode
        
    def visitDomain(self, ctx:demoParser.DomainContext):
        dom = ctx.MYHOUSE()
        return dom

def translate(root):
    s = root.type + ' type packet named ' + root.name
    return s

def get_parse_tree(file_name):
    pol_src_code = FileStream(file_name)
    lexer = demoLexer(pol_src_code)
    stream = CommonTokenStream(lexer)
    parser = demoParser(stream)
    tree = parser.policy()
    return tree, parser.getNumberOfSyntaxErrors()
 
tree, err = get_parse_tree(sys.argv[1])
if err == 0:
    visitor = CustomVisitor()
    try:
        tree.accept(visitor)
    except Exception as e:
        print("\nSyntax error occurred in the policy file!\n")
        sys.exit(1)
    print(visitor.policies)
    statements = []
    for p in visitor.policies:
        statements.extend(p.statements)
    print(statements)
    for s in statements:
        sign_ast = s.sign
        signedby_ast = s.signedby
        sign_string = translate (sign_ast)
        signedby_string = translate(signedby_ast)
        print('A '+ sign_string + ' should be signed by ' + signedby_string)
