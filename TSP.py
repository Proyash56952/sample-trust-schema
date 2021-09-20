from antlr4 import *
from dctLexer import dctLexer
from dctListener import dctListener
from dctParser import dctParser
from dctVisitor import dctVisitor
import sys
from collections import defaultdict

idDict = {}
defDict = defaultdict(list)
cacheDict = defaultdict(list)
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
            defDict[id.value].append(exp)
            defDict[id.value].append(constraints)
            defDict[id.value].append(certificates)
            
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
        #print(ctx.STRING().getText())
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


def replace_identifier(exp,constraints):
    res = []
    if(constraints):
        for m in constraints:
            name = ''
            for n in exp.value:
                if n.value in idDict:
                    name += idDict[n.value] + '/'
                elif n.value in m:
                    name += m[n.value] + '/'
                else:
                    name += n.value + '/'
            res.append(name)
    else:
        name = ''
        for n in exp.value:
            if n.value in idDict:
                name += idDict[n.value] + '/'
            else:
                name += n.value + '/'
        res.append(name)
    return res
    
#def replace_identifier(exp):
    #name = []
    #for e in exp.value:
        #if e.value in idDict:
            #name.append(idDict[e.value])
        #else:
            #name.append(e.value)
    #return name
    
def replace_constraints(name,constraints):
    res = []
    for m in constraints:
        temp = []
        for n in name:
            print(m,n)
            #if(n in m):
                #temp.append(m[n])
                #print(m[n])
            #else:
                #temp.append(n)
        res.append(temp)
    return res
    
def add_cert(name, certificates):
    res = []
    for c in certificates:
        for n in name:
            r = n + '\t{' + c.value + '}'
            res.append(r)
    return res
            
def translate(dict,file):
    #print(defDict)
    with open (file, 'w') as output:
        for key,values in dict.items():
            _exp = values[0]
            _constraints = values[1]
            _certificates = values[2]
            
            if(_exp.type == 'id'):
                #if(_exp.value.value in cacheDict.keys()):
                    #name = cacheDict[_exp.value.value]
                #else:
                previd = defDict.get(_exp.value.value)
                #print(_exp.value.value)
                #print("hola")
                        #defDict[key][0] = previd[0]
                        #defDict[key][1] = previd[1]
                        #defDict[key][2] = previd[2]
                _exp = previd[0]
                        
                if (not _constraints and previd[1]):
                    _constraints = previd[1]
                            
                if (not _certificates and previd[2]):
                    _certificates = previd[2]
                    
                    
                #if(_exp.value in cacheDict.keys()):
                    #print(cacheDict.get(key))
                    #print("hola")
            name = replace_identifier(_exp,_constraints)
                
            #if(_constraints):
                #name = replace_constraints(name,_constraints)

            
            #print(key, name)
            
            #cacheDict[key].append(name)
            #print(cacheDict[key])
            if(_certificates):
                name = add_cert(name,_certificates)
            
            for n in name:
                print(key + ' : ' + n+'\n')

def translate_signing_chain(file):
    with open (file, 'a') as output:
        output.write('\n\n\n\n')
        output.write('Signing Chain: \n\n')
                
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
        #for key,values in defDict.items():
            

    except Exception as e:
        print("\nSyntax error occurred in the policy file!\n")
        sys.exit(1)

    translate(defDict, outputfile)
    #print(chainDict)
    #print(cert)
    #translate_signing_chain(outputfile)

        
