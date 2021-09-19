from antlr4 import *
from dctLexer import dctLexer
from dctListener import dctListener
from dctParser import dctParser
from dctVisitor import dctVisitor
import sys
from collections import defaultdict

idDict = {}
defDict = defaultdict(list)
#defDict = {}
chainDict = {}
pub = []
cert = set()


class Schema:
    pass

class Identifier:
    def __init__(self):
        self.type = None
        self.value = None
        self.signedby = None
        
class Expression:
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
        
        if(id.type == 'uString'):
            idDict[id.value] = '"' + ctx.expression().accept(self).value + '"'
        
        else:
            exp = ctx.expression().accept(self)
            constraints = ctx.constraints().accept(self) if ctx.constraints() else None
            certificates = ctx.certificates().accept(self) if ctx.certificates() else None
            defDict[id].append([exp,constraints,certificates])
            
    def visitIdentifier(self, ctx:dctParser.IdentifierContext):
        id = Identifier()
        
        if(ctx.STRING()):
            id.type = 'string'
            id.value = ctx.STRING().getText()
            
        elif(ctx.ustring()):
            id.type = 'uString'
            id.value = ctx.ustring().accept(self)
        
        elif (ctx.hstring()):
            id.type = 'hString'
            id.value = ctx.hstring().accept(self)
            
        return id
            
    def visitConstraints(self, ctx:dctParser.ConstraintsContext):
        cl = []
        for c in ctx.constraint():
            cl.append(c.accept(self))
        return cl
            
    def visitConstraint(self, ctx:dctParser.ConstraintContext):
        d = {}
        for c in ctx.constraint_body():
            i, s = c.accept(self)
            d[i.value] = s
        return d
        
    def visitConstraint_body(self, ctx:dctParser.Constraint_bodyContext):
        id = ctx.identifier().accept(self)
        if(ctx.literal()):
            s = '"'+ ctx.literal().accept(self) + '"'
        elif(ctx.function):
            s = ctx.function().accept(self)+'()'
        return id, s
        
    def visitCertificates(self, ctx:dctParser.CertificatesContext):
        certs = []
        for i in ctx.identifier():
            certs.append(i.accept(self))
        return certs
    
    def visitUstring(self, ctx:dctParser.UstringContext):
        return ctx.UNDERSCORE().getText() + ctx.STRING().getText()
        
    def visitHstring(self, ctx:dctParser.HstringContext):
        return ctx.HASH().getText() + ctx.STRING().getText()
        
    def visitLiteral(self, ctx:dctParser.LiteralContext):
        print(ctx.STRING().getText())
        return ctx.STRING().getText()
    
    def visitFunction(self, ctx:dctParser.FunctionContext):
        return ctx.STRING().getText()
        
    def visitExpression(self, ctx:dctParser.ExpressionContext):
        e = Expression()
        if (ctx.name()):
            e.value = ctx.name().accept(self)
            e.type = 'name'
        elif (ctx.identifier()):
            e.value = ctx.identifier().accept(self)
            e.type = 'id'
        elif (ctx.literal()):
            e.value = ctx.literal().accept(self)
            e.type = 'literal'
        return e
    
    def visitName(self, ctx:dctParser.NameContext):
        ids = []
        for c in ctx.identifier():
            ids.append(c.accept(self))
        return ids

#def translate(dict,file):
    #with open (file, 'w') as output:
        #for key,values in dict.items():
            

def translate_signing_chain(file):
    with open (file, 'a') as output:
        output.write('\n\n\n\n')
        output.write('Signing Chain: \n\n')
        #for key, value in chainDict.items():
            #if (key in ['ocommand', 'ucommand']):
                #i = key
                #res = ''
                #while i in chainDict.keys():
                    #print(chainDict[i])
                    #res += i + ' <= '
                    #i = chainDict[i]
                #res += i
                #output.write(res + '\n\n')
                
        for key, value in chainDict.items():
            i = key
            res = ''
            while i in chainDict.keys():
                    #print(chainDict[i])
                res += i + ' <= '
                i = chainDict[i]
            res += i
            output.write(res + '\n\n')
                
            
def get_parse_tree(file_name):
    schema_src_code = FileStream(file_name)
    lexer = dctLexer(schema_src_code)
    stream = CommonTokenStream(lexer)
    parser = dctParser(stream)
    tree = parser.schema()
    return tree, parser.getNumberOfSyntaxErrors()

tree, err = get_parse_tree(sys.argv[1])
outputfile = sys.argv[2]
if err == 0:
    visitor = CustomVisitor()
    try:
        tree.accept(visitor)
        print(idDict)
        #print(defDict)
        for keys,values in defDict.items():
            print(keys.value, values)
            print('\n')

    except Exception as e:
        print("\nSyntax error occurred in the policy file!\n")
        sys.exit(1)

    #translate(defDict, outputfile)
    #print(chainDict)
    #print(cert)
    #translate_signing_chain(outputfile)

        
