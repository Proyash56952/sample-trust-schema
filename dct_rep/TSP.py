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
        id = ctx.getChild(0).accept(self)
        
        if(id.type == 'uString'):
            #print(type(ctx.literal().accept(self)))
            idDict[id.value] = '"' + ctx.literal().accept(self) + '"'
            #print(idDict)
        
        elif(id.type == 'hString'):
            exp = ctx.expression().accept(self)

            if ctx.constraints():
                defDict[id.value].append('type3')
                
                constraints = ctx.constraints().accept(self)
                
                for m in constraints:
                    for e in exp.value:
                        if(e.value in m):
                            #print(e.value)
                            e.value = m[e.value]
                        
                defDict[id.value].append(exp.value)
                defDict[id.value].append(constraints)
                
            else:
                defDict[id.value].append('type5')
                defDict[id.value].append(exp.value)
    
        elif(id.type == 'string'):
            if not ctx.constraints():
                exp = ctx.expression().accept(self)
            
                if(ctx.SIGNEDBY()):
                    if(exp.type == 'id'):
                        defDict[id.value].append('type2a') # id COLON exp (id) <= cert
                    else:
                        defDict[id.value].append('type2b') # id COLON exp (name) <= cert
                    defDict[id.value].append(exp.value)
                    cert = ctx.getChild(4).accept(self)
                    defDict[id.value].append(cert)
                
                else:
                    defDict[id.value].append('type5') # id colon exp (name)
                    defDict[id.value].append(exp.value)
            
            else:
                exp = ctx.expression().accept(self)
                constraints = ctx.constraints().accept(self)
                
                if (not ctx.SIGNEDBY()):
                    if (exp.type == 'id'):
                        defDict[id.value].append('type3a') # id COLON exp(id) AND constraint

                
                    elif (exp.type == 'name'):
                        defDict[id.value].append('type3b')  # id COLON exp(name) AND constraint
                    
                    defDict[id.value].append(exp.value)
                    defDict[id.value].append(constraints)
                    
                        
                else:
                    if (exp.type == 'id'):
                        defDict[id.value].append('type4a') # id COLON exp(id) AND constraint <= cert
                
                    elif (exp.type == 'name'):
                        defDict[id.value].append('type4b') # id COLON exp(name) AND constraint <= cert

                    defDict[id.value].append(exp.value)
                    defDict[id.value].append(constraints)
                    
                    cert = ctx.getChild(6).accept(self)
                    #print(cert.value)
                    defDict[id.value].append(cert)
                    
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
        s = '"'+ ctx.literal().accept(self) + '"'
        return id, s
        
    
    def visitUstring(self, ctx:dctParser.UstringContext):
        return ctx.UNDERSCORE().getText() + ctx.STRING().getText()
        
    def visitHstring(self, ctx:dctParser.HstringContext):
        return ctx.HASH().getText() + ctx.STRING().getText()
        
    def visitLiteral(self, ctx:dctParser.LiteralContext):
        #print(ctx.AP().getText())
        return ctx.STRING().getText()
        
    def visitExpression(self, ctx:dctParser.ExpressionContext):
        e = Expression()
        if (ctx.name()):
            e.value = ctx.name().accept(self)
            e.type = 'name'
        elif (ctx.identifier()):
            e.value = ctx.identifier().accept(self)
            e.type = 'id'
        return e
    
    def visitName(self, ctx:dctParser.NameContext):
        ids = []
        for c in ctx.identifier():
            ids.append(c.accept(self))
        return ids

def translate(dict):
    for key,values in dict.items():
        if values[0] in ['type2b', 'type5']:
            res = ''
            res = res + key + ' : '
            for v in values[1]:
                if(v.type == 'uString'):
                    if v.value in idDict:
                        res += idDict[v.value] + '/'
                    else:
                        res += v.value + '/'
                else:
                    res += v.value + '/'
            if(values[0] == 'type2b'):
                res += ' { '+ values[2].value + ' }'
            print(res)
        
        elif values[0] == 'type2a':
            previd = dict.get(values[1].value)
            constraints = previd[2]
            for m in constraints:
                res = ''
                res = res + key + ' : '
                for v in previd[1]:
                    #if(v.type == 'uString'):
                    if v.value in m:
                        res += m[v.value] + '/'
                    elif v.value in idDict:
                        res += idDict[v.value] + '/'
                            
                    else:
                        res += v.value + '/'
                res += ' { '+ values[2].value + ' }'
                print(res)

        elif values[0] in ['type3a', 'type4a']:
            previd = dict.get(values[1].value)
            if(previd != None):
                constraints = values[2]
                for m in constraints:
                    res = ''
                    res = res + key + ' : '
                    for v in previd[1]:
                        #if(v.type == 'uString'):
                        if v.value in m:
                            res += m[v.value] + '/'
                        elif v.value in idDict:
                            res += idDict[v.value] + '/'
                            
                        else:
                            res += v.value + '/'
                    if(values[0] == 'type3a' and len(previd) > 2):
                        res += ' { '+ previd[2].value + ' }'
                    elif (values[0] == 'type4a'):
                        res += ' { '+ values[3].value + ' }'
                    print(res)
        
        elif values[0] in ['type3b', 'type4b']:
            constraints = values[2]
            for m in constraints:
                res = ''
                res = res + key + ' : '
                for v in values[1]:
                    if(v.type == 'uString'):
                        if v.value in m:
                            res += m[v.value] + '/'
                        elif v.value in idDict:
                            res += idDict[v.value] + '/'
                            
                        else:
                            res += v.value + '/'
                    else:
                        res += v.value + '/'
                if(values[0] == 'type4b'):
                    res += ' { '+ values[3].value + ' }'
                    print(res)
                
            
            
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
        #print(idDict)

    except Exception as e:
        print("\nSyntax error occurred in the policy file!\n")
        sys.exit(1)

    translate(defDict)

        
