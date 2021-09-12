from antlr4 import *
from dctLexer import dctLexer
from dctListener import dctListener
from dctParser import dctParser
from dctVisitor import dctVisitor
import sys

Dict = {}

class Schema:
    pass

class Identifier:
    def __init__(self):
        self.type = None
        self.value = None

class CustomVisitor(dctVisitor):
    def __init__(self):
        self.definitions = []
    
    def visitSchema(self, ctx:dctParser.SchemaContext):
        schema = Schema()
        schema.name = "Schema"
        s = []
        for c in ctx.definition():
            s.append(c.accept(self))
        schema.definition = s
        self.definitions.append(schema)
    
    def visitDefinition(self, ctx:dctParser.DefinitionContext):
        id = ctx.identifier().accept(self)
        #if(id.type == 'uString'):
            #print("hola")
        exp = ctx.expression().accept(self)
        print(exp)
        
        if(id.type == 'uString'):
            Dict[id.value] = exp.getText()
        print(Dict)
            
    def visitIdentifier(self, ctx:dctParser.IdentifierContext):
        id = Identifier()
        if(ctx.STRING()):
            id.type = 'string'
            id.value = ctx.STRING().getText()
            
        if(ctx.ustring()):
            id.type = 'uString'
            id.value = ctx.ustring().accept(self)
            
        return id
            
        
    def visitUstring(self, ctx:dctParser.UstringContext):
        return ctx.UNDERSCORE().getText() + ctx.STRING().getText()
        
    def visitHstring(self, ctx:dctParser.HstringContext):
        return ctx.HASH().getText() + ctx.STRING().getText()
        
    def visitExpression(self, ctx:dctParser.ExpressionContext):
        if (ctx.STRING()):
            return ctx.STRING()
        elif (ctx.name()):
            print("hu")

def get_parse_tree(file_name):
    schema_src_code = FileStream(file_name)
    lexer = dctLexer(schema_src_code)
    stream = CommonTokenStream(lexer)
    parser = dctParser(stream)
    tree = parser.schema()
    return tree, parser.getNumberOfSyntaxErrors()

tree, err = get_parse_tree(sys.argv[1])
if err == 0:
    visitor = CustomVisitor()
    try:
        tree.accept(visitor)
    except Exception as e:
        print("\nSyntax error occurred in the policy file!\n")
        sys.exit(1)
