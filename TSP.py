from antlr4 import *
from dctLexer import dctLexer
from dctListener import dctListener
from dctParser import dctParser
from dctVisitor import dctVisitor
import sys
import binascii
from collections import defaultdict
from ndn.encoding import *

idDict = {}
defDict = defaultdict(list)
tokenList = set()
tokenDict = {}
certDict = {}
tagDict = {}
templateDict = {}

parentList = set()
childList = []
tempList = []
literalList = []
chainList = []
pubList = []

primary = []
parent = defaultdict(list)
children = {}
cons = {}
signer = {}
tempDict = {}
chainDict = {}

class NestedModel(TlvModel):
    str_val = BytesField(0x84)
    tok_val = BytesField(0x85)

#class TokenTableModel(TlvModel):
    #val = BytesField(0x85)
    
class TrustSchemaModel(TlvModel):
    inner = ModelField(0x83,NestedModel)
    #tok_tab = ModelField(0x83,TokenTableModel)




class Model(TlvModel):          # Model = [Name] [IntVal] [StrVal] [BoolVal]
    #name = NameField()          # Name = NAME-TYPE TLV-LENGTH ...
    string_table =BytesField(0x84)
    token_table = BytesField(0x85)   # IntVal = INT-VAL-TYPE TLV-LENGTH nonNegativeInteger
    tag_val = BytesField(0x88)  # StrVal = STR-VAL-TYPE TLV-LENGTH *OCTET
    cert_val = BytesField(0x86)
    bool_val = BoolField(0x01)  # BoolVal = BOOL-VAL-TYPE 0

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
            idDict[id.value] = ctx.expression().accept(self).value
        
        else:
            exp = ctx.expression().accept(self)
            constraints = ctx.constraints().accept(self) if ctx.constraints() else None
            certificates = ctx.certificates().accept(self) if ctx.certificates() else None
            defDict[id.value].append(exp)
            defDict[id.value].append(constraints)
            defDict[id.value].append(certificates)
            
            if(certificates):
                for c in certificates:
                    signer[id.value] = c.value
            
            if(constraints):
                #print(constraints)
                cons[id.value] = constraints
            
            if(id.type == 'hString'):
                primary.append(id.value)
                #parent[id.value] = [id.value]
                #tagDict[id.value] = [-1,-1]
                templateDict[id.value] = [-1,-1]
        
            elif(exp.type == 'id'):
                parent[exp.value.value].append(id.value)
                parentList.add(exp.value.value)
                childList.append(id.value)
                children[id.value] = exp.value.value
            
            if(exp.type == 'id' and exp.value.type == 'hString' and constraints):
                templateDict[id.value] = [-1,-1]
            
            
                
            
            
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
            #tokenList.add(id.value)
            tokenDict[id.value] = [-1,-1,-1]
            #tagDict[id.value] = [-1,-1]
            templateDict[id.value] = [-1,-1]
            
        return id
            
    def visitConstraints(self, ctx:dctParser.ConstraintsContext):
        cl = []
        for c in ctx.constraint():
            #print(c.accept(self))
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
            s = ctx.literal().accept(self)
        elif(ctx.function):
            s = ctx.function().accept(self)+'()'
        #print (id.value, s)
        return id, s
        
    def visitCertificates(self, ctx:dctParser.CertificatesContext):
        certs = []
        for i in ctx.identifier():
            certs.append(i.accept(self))
            certDict[i.accept(self).value] = [-1,-1]
        return certs
    
    def visitUstring(self, ctx:dctParser.UstringContext):
        return ctx.UNDERSCORE().getText() + ctx.STRING().getText()
        
    def visitHstring(self, ctx:dctParser.HstringContext):
        return ctx.HASH().getText() + ctx.STRING().getText()
        
    def visitLiteral(self, ctx:dctParser.LiteralContext):
        #print(ctx.STRING().getText())
        #tokenList.add(ctx.STRING().getText())
        tokenDict[ctx.STRING().getText()] = [-1,-1,-1]
        literalList.append(ctx.STRING().getText())
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
            #tokenList.add(e.value)
        return e
    
    def visitName(self, ctx:dctParser.NameContext):
        components = []
        for c in ctx.component():
            components.append(c.accept(self))
            #tokenList.add(c.accept(self).value)
            tokenDict[c.accept(self).value] = [-1,-1,-1]
        return components

    
def replace_identifier(exp):
    name = []
    for e in exp.value:
        if e.value in idDict:
            name.append(idDict[e.value])
        else:
            name.append(e.value)
    return name
    
def replace_constraints(name,constraints):
    res = []
    for m in constraints:
        temp = []
        for n in name:
            if(n in m):
                temp.append(m[n])
            else:
                temp.append(n)
        res.append(temp)
    return res

    
def generate_output (key, names, certificates):
    res = []
    for name in names:
        r = ''
        for n in name:
            r += n + '/'
        if(certificates):
            for c in certificates:
                r +='   {' + c.value + '}'
        res.append(r)
        print(key + ': ' + r)
        print('\n')
    return res
                
def translate(dict):
    for key, values in dict.items():
        _exp = values[0]
        _constraints = values[1]
        _certificates = values[2]
        names = []
        if(_exp.type == 'id'):
            previd = defDict.get(_exp.value.value)
            names = previd[0]
                                
            if (not _certificates and previd[2]):
                _certificates = previd[2]
                
        else:
            names.append(replace_identifier(_exp))
        
        if(_constraints):
            names = replace_constraints(names,_constraints)

        defDict[key][0] = names
        generate_output(key,names,_certificates)

def buildStringTable():
    index, position = 0, 0
    s_tab = ""
    for key,val in tokenDict.items():
        s_tab += key
        length = len(key)
        tokenDict[key] = [index,position, length]
        index += 1
        position += length
    return s_tab

def buildCert():
    certIndex = 0
    
    for key,val in certDict.items():
        cert = []
        exp = tempDict[key][0]

        for i,n in enumerate(exp):
            if(n in idDict):
                comp = idDict[n]
                cert.append(tokenDict[comp][0])
            elif((n.startswith ('_'))):
                cert.append(160+i)
            else:
                comp = n
                cert.append(tokenDict[comp][0])
            


        certDict[key] = [certIndex,cert]
            
        certIndex += 1


def buildTag():
    tagIndex = 0
    for key,val in tagDict.items():
        name = defDict[key][0].value
        tag = []
        for n in name:
            tag.append(tokenDict[n.value][0])
        tagDict[key] = [tagIndex, tag]
        tagIndex += 1
        
def buildTemplate():
    tempIndex = 0
    for key,val in templateDict.items():
        template = []
        exp = defDict[key][0]
        constraints = defDict[key][1]
        
        if(exp.type == 'id'):
            previd = defDict.get(exp.value.value)
            name = previd[0]
        else:
            name = exp
            
        for i,n in enumerate(name.value):
            if(constraints and n.value in constraints[0]):
                comp = constraints[0][n.value]
                template.append(tokenDict[comp][0])
            elif(n.value in idDict):
                comp = idDict[n.value]
                template.append(tokenDict[comp][0])
            elif(n.type == 'uString'):
                template.append(160+i)
            else:
                #comp = n.value
                template.append(80+i)
                
        templateDict[key] = [tempIndex,template]
        tempIndex += 1

def expandSigner():
    for key,val in parent.items():
        for v in val:
            if (v not in signer.keys()):
                signer[v] = signer[key]

def buildTempChain():
    tempChain = []
    for pr in primary:
        for key,val in parent.items():
            #print(key,val)
            if(key == pr):
                for v in val:
                    temp = []
                    temp.append(v)
                    while(1):
                        if(v in signer.keys()):
                            v = signer[v]
                            temp.append(v)
                            #print(key)
                        else:
                            break
                            
                    tempChain.append(temp)
    return tempChain
                        
'''
def handleCons():
    for key,val in defDict.items():
        exp = val[0]
        constraints = val[1]
        print(constraints)
        
        if(exp.type == 'id'):
            name = defDict[exp.value.value][0]
        else:
            name = exp
'''

def handleCons():
    handleParentCons()
    handleChildrenCons()
    
def handleParentCons():
    for key,val in defDict.items():
        if(key not in childList):
            names = []
            exp = val[0]
            cons = val[1]
            if(cons):
                for c in cons:
                    name = []
                    for i , n in enumerate(exp.value):
                        if(n.value in c):
                            comp = c[n.value]
                            name.append(comp)
                        else:
                            name.append(n.value)
                    names.append(name)
                    
            else:
                name = []
                for i,n in enumerate(exp.value):
                    name.append(n.value)
                names.append(name)

            tempDict[key] = names

def handleChildrenCons():
    for key,val in defDict.items():
        if(key in childList):
            p = children[key]
            parentNames = tempDict[p]
            cons = val[1]
            names = []
            for parentName in parentNames:
                if(cons):
                    for c in cons:
                        name = []
                        for i, n in enumerate (parentName):
                            if (n in c):
                                comp = c[n]
                                name.append(comp)
                            else:
                                name.append(n)
                        names.append(name)
                else:
                    names = parentNames
            tempDict[key] = names

def buildTag(t,idx):
    tag = []
    name = tempDict[t][0]

    for n in name:
        tag.append(tokenDict[n][0])
    tagDict[t] = [idx,tag]

def buildTemplate(name):
    temp = []
    for i,n in enumerate(name):
        if(n in idDict):
            comp = idDict[n]
            temp.append(tokenDict[comp][0])
        elif(n in literalList):
            temp.append(tokenDict[n][0])
        elif(n.startswith ('_')):
            temp.append(160+i)
        else:
            temp.append(80+i)
    tempList.append(temp)
    return len(tempList)-1
            

def buildpub():
    tagIdx = tempIdx = chainIdx = pubIdx = 0
    for p in primary:
        buildTag(p,tagIdx)
        tagIdx += 1
        for c in parent[p]:
            tems = tempDict[c]
            for t in tems:
                idx = buildTemplate(t)
                for a in tc:
                    print(c)
                    if(a[0] == c):
                        chain = []
                        for i in range(1,len(a)):
                            certIdx = certDict[a[i]][0]
                            #print(certIdx)
                            chain.append(certIdx)
                        if(chain not in chainList):
                            chainList.append(chain)
                        #chainDict[c] = [chainIdx,chain]
                        #chainIdx = len(chainDict) - 1
                pubList.append([idx,len(chainList)-1])
                #pubList.append([idx,chainIdx])
                                
def encode_s_tab(s_tab):
    b_s_tab = bytes(s_tab.encode())
    #model.string_table = b_s_tab
    #string_table_model.str_val = b_s_tab
    trustSchemaModel.inner.str_val = b_s_tab

def encode_token_table():
    s = []
    k = []
    for key,val in tokenDict.items():
        #print(val[1],val[2])
        for i in key:
            k.append(ord(i))
        s.append(val[1])
        s.append(val[2])
    #print(bytearray(k))
    #print(s)
    #print(bytearray(s))
    #model.string_table = bytes(k)
    #print((bytes(s)))
    #model.token_table = bytes(s)
    trustSchemaModel.inner.tok_val = bytearray(s)
    
def get_parse_tree(file_name):
    schema_src_code = FileStream(file_name)
    lexer = dctLexer(schema_src_code)
    stream = CommonTokenStream(lexer)
    parser = dctParser(stream)
    tree = parser.schema()
    return tree, parser.getNumberOfSyntaxErrors()
    
def formatPrint(dic):
    for key,val in dic.items():
        print(key,val)
    print('\n')

tree, err = get_parse_tree(sys.argv[1])
outputfile = sys.argv[2]
f = open(outputfile,"wb")
if err == 0:
    visitor = CustomVisitor()
    try:
        tree.accept(visitor)
        print(idDict)

    except Exception as e:
        print("\nSyntax error occurred in the policy file!\n")
        sys.exit(1)

    #translate(defDict)
    trustSchemaModel = TrustSchemaModel()
    trustSchemaModel.inner = NestedModel()
    #trustSchemaModel.tok_tab = TokenTableModel()
    '''
    print(primary)
    print(parent)
    '''
    #print(signer)
    #print(parent)
    #print(parentList)
    #print(children)
    #model = Model()
    s_tab = buildStringTable()
    
    expandSigner()
    #print(signer)
    tc = buildTempChain()
    #print(tc)
    
    
    handleCons()
    #formatPrint(tempDict)
    
    #b_s_tab = bytearray(s_tab.encode())
    
    #print('Tokens:')
    #formatPrint(tokenDict)
    
    
    
    
    buildCert()
    print('Certificate:')
    formatPrint(certDict)
    
    buildpub()
    print(tempList)
    print(chainList)
    print(pubList)
    #formatPrint(tagDict)
    #print(tempList)
    
    #print(literalList)
    '''
    buildTag()
    print('Tags:')
    formatPrint(tagDict)

    
    buildTemplate()
    print('Template:')
    formatPrint(templateDict)
    
    encode_s_tab(s_tab)
    encode_token_table()
    
    res = trustSchemaModel.encode()
    #print(res)
    f.write(res)
    '''
    
    
    
        
