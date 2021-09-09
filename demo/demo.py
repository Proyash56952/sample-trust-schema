from antlr4 import *
from demoLexer import demoLexer
from demoListener import demoListener
from demoParser import demoParser
from demoVisitor import demoVisitor
import sys

class Policy:
    pass
    
class Command:
    pass
    
class CustomVisitor(demoVisitor):
    def __init__(self):
        self.policies = []
        
    def visitS1(self, ctx:demoParser.S1Context):
        print(ctx.cmd())
        print(ctx.SIGNEDBY())
        print(ctx.opcert())
        pol = Policy()
        pol.msg = ctx.cmd().accept(self)
        #print(pol.cmd.type)
        self.policies.append(pol)
        
    def visitCmd(self, ctx:demoParser.CmdContext):
        cmd = Command()
        cmd.domain = ctx.domain().accept(self)
        #print(ctx.domain())
        print(cmd.domain)
        cmd.param = ctx.param().accept(self)
        print(cmd.param)
        print(ctx.getChild(1))
        return cmd
        
    def visitParam(self, ctx:demoParser.ParamContext):
        p = []
        for c in ctx.STRING():
            p.append(c)
            print(c)
        return p
        
    def visitDomain(self, ctx:demoParser.DomainContext):
        return ctx.MYHOUSE()


def get_parse_tree(file_name):
    pol_src_code = FileStream(file_name)
    lexer = demoLexer(pol_src_code)
    stream = CommonTokenStream(lexer)
    parser = demoParser(stream)
    tree = parser.st()
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
