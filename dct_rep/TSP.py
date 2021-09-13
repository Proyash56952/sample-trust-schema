from antlr4 import *
from dctLexer import dctLexer
from dctListener import dctListener
from dctParser import dctParser
from dctVisitor import dctVisitor
import sys

idDict = {}
defDict = {}

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
        #print(ctx.STRING())
        
        if(id.type == 'uString'):
            idDict[id.value] = ctx.STRING().getText()
            #print(Dict)
        
        elif(id.type == 'string'):
            exp = ctx.expression().accept(self)
            defDict[id.value] = exp
        
        #exp = ctx.expression().accept(self)
        #print(exp)
            
    def visitIdentifier(self, ctx:dctParser.IdentifierContext):
        id = Identifier()
        if(ctx.STRING()):
            #print("hi")
            id.type = 'string'
            id.value = ctx.STRING().getText()
            
            
        if(ctx.ustring()):
            #print("hola")
            id.type = 'uString'
            id.value = ctx.ustring().accept(self)
            #print(id.value)
            
        return id
            
        
    def visitUstring(self, ctx:dctParser.UstringContext):
        return ctx.UNDERSCORE().getText() + ctx.STRING().getText()
        
    def visitHstring(self, ctx:dctParser.HstringContext):
        return ctx.HASH().getText() + ctx.STRING().getText()
        
    def visitExpression(self, ctx:dctParser.ExpressionContext):
        if (ctx.name()):
            c = ctx.name().accept(self)
        return c
    
    def visitName(self, ctx:dctParser.NameContext):
        ids = []
        for c in ctx.identifier():
            ids.append(c.accept(self))
        return ids
            
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
        print(idDict)
        #print(defDict)

    except Exception as e:
        print("\nSyntax error occurred in the policy file!\n")
        sys.exit(1)
    
    for key,values in defDict.items():
        res = ''
        res = res + key + ' : '
        for v in values:
            if(v.type == 'uString'):
                res += idDict[v.value] + '/'
            else:
                res += v.value
    print(res)
        
