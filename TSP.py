from antlr4 import *
from dctLexer import dctLexer
from dctListener import dctListener
from dctParser import dctParser
from dctVisitor import dctVisitor
import sys
import binascii
from collections import defaultdict
from ndn.encoding import *
from itertools import product

idDict = {}
defDict = defaultdict(list)
tempDict = {}

tokenDict = {}
certDict = {}
consDict = defaultdict(list)
tagDict = {}
tempList = []
chainList = []
pubList = []

parentList = set()
childList = []
literalList = []
primary = []
parent = defaultdict(list)
children = {}
cons = {}
signer = defaultdict(list)
tempChain = []
tempChainDic = defaultdict(list)


class NestedModel(TlvModel):
    str_val = BytesField(0x84)
    tok_val = BytesField(0x85)
    cert = BytesField(0x86)
    chain = BytesField(0x87)
    #tag = BytesField(0x88)
    template = BytesField(0x88)
    publication = BytesField(0x89)

class TrustSchemaModel(TlvModel):
    inner = ModelField(0x83,NestedModel)

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
                    signer[id.value].append(c.value)
            
            if(constraints):
                cons[id.value] = constraints
            
            if(id.type == 'hString'):
                primary.append(id.value)
        
            elif(exp.type == 'id'):
                parent[exp.value.value].append(id.value)
                parentList.add(exp.value.value)
                childList.append(id.value)
                children[id.value] = exp.value.value
            
            #if(exp.type == 'id' and exp.value.type == 'hString' and constraints):
                #templateDict[id.value] = [-1,-1]
            
            
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
            tokenDict[id.value] = [-1,-1,-1]
            
        return id
            
    def visitConstraints(self, ctx:dctParser.ConstraintsContext):
        cl = []
        for c in ctx.constraint():
            cl.append(c.accept(self))
        return cl
            
    def visitConstraint(self, ctx:dctParser.ConstraintContext):
        l = []
        d = {}
        #print(len(ctx.constraint_body()))
        for c in ctx.constraint_body():
            i, s = c.accept(self)
            d[i.value] = s
        return d
        
    def visitConstraint_body(self, ctx:dctParser.Constraint_bodyContext):
        id = ctx.identifier().accept(self)
        s = []
        #print(len(ctx.components()))
        for c in ctx.components():
            s.append(c.accept(self))
        '''if(ctx.literal()):
            s = ctx.literal().accept(self)
        elif(ctx.function):
            s = ctx.function().accept(self)+'()'''
        return id, s
    
    def visitComponents(self, ctx:dctParser.ComponentsContext):
        if(ctx.literal()):
            s = ctx.literal().accept(self)
        elif(ctx.function):
            s = ctx.function().accept(self)+'()'
        return s
        
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
        return e
    
    def visitName(self, ctx:dctParser.NameContext):
        components = []
        for c in ctx.component():
            components.append(c.accept(self))
            tokenDict[c.accept(self).value] = [-1,-1,-1]
        return components


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


def expandSigner():
    for key,val in parent.items():
        #print(key,val)
        for v in val:
            #print(v,signer[v])
            if (v not in signer.keys()):
                signer[v] = signer[key]
            #print(v,signer[v])
                
def findRoot():
    for v in signer.values():
        for a in v:
            if a not in signer.keys():
                return a

def find_all_paths(graph, start, end, path =[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    #print(start)
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths

def buildTempChain():
    root = findRoot()
    #print(root)
    for key,val in parent.items():
        if key in primary:
            #print(val)
            for v in val:
                tc = find_all_paths(signer,v,root)
                #print(tc)
                #print(signer)
                for t in tc:
                    tempChain.append(t)
                #print(tempChain)
                for t in tc:
                    tempChainDic[t[0]].append(t[1:])
'''
def buildTempChain():
    tempChain = []
    for pr in primary:
        for key,val in parent.items():
            if(key == pr):
                for v in val:
                    temp = []
                    temp.append(v)
                    #print(v)
                    while(1):
                        #for k,l in signer.items():
                            #print(k,l)
                        if(v in list(signer.keys())):
                            v = signer[v]
                            temp.append(v)
                        else:
                            break
                            
                    tempChain.append(temp)
    #print(tempChain)
    return tempChain
'''

def handleCons():
    expand_cons()
    #formatPrint(consDict)
    handleParentCons()
    handleChildrenCons()
    
def expand_cons():
    for key,val in cons.items():
        #print(key,val)
        for dic in val:
            #print(dic)
            #print(dic.values())
            lis = list(product(*dic.values()))
            tl = []
            for l in lis:
                idx = 0
                temDic = {}
                for k,v in dic.items():
                    #print(k,l[idx])
                    
                    temDic[k] = l[idx]
                    idx += 1
                #print(temDic)
                tl.append(temDic)
            #print(tl)
            for t in tl:
                consDict[key].append(t)
        #print(consDict)
            #for k,v in dic.items():
                #print(k,v)
    
def handleParentCons():
    for key,val in defDict.items():
        if(key not in childList):
            names = []
            exp = val[0]
            #cons = val[1]
            if(consDict[key]):
                cons = consDict[key]
                #print(cons)
                for c in cons:
                    name = []
                    #print(cons)
                    for i , n in enumerate(exp.value):
                        #print(c)
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
            #cons = val[1]
            names = []
            for parentName in parentNames:
                if(consDict[key]):
                    cons = consDict[key]
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
                tcl = []
                idx = buildTemplate(t)
                
                for key,vals in tempChainDic.items():
                    if(key == c):
                        for val in vals:
                            #print(key,val)
                            chain = []
                            for i in range(0,len(val)):
                                certIdx = certDict[val[i]][0]
                                chain.append(certIdx)

                            if(chain in chainList):
                                tcl.append(chainList.index(chain))
                            else:
                                chainList.append(chain)
                                tcl.append(len(chainList)-1)
                    
                    
                '''
                for a in tempChain:
                    if(a[0] == c):
                        chain = []
                        for i in range(1,len(a)):
                            certIdx = certDict[a[i]][0]
                            #print(certIdx)
                            chain.append(certIdx)
                        if(chain not in chainList):
                            chainList.append(chain)
                        tcl.add(len(chainList)-1)
                #print(tcl)
                '''
                #print(tcl)
                pubList.append([idx,list(tcl)])
                                
def encode_s_tab(s_tab):
    b_s_tab = bytes(s_tab.encode())
    trustSchemaModel.inner.str_val = b_s_tab

def encode_token_table():
    s = []
    k = []
    for key,val in tokenDict.items():
        for i in key:
            k.append(ord(i))
        s.append(val[1])
        s.append(val[2])
        
    trustSchemaModel.inner.tok_val = bytearray(s)
    
def encode_cert():
    s = []
    for key,val in certDict.items():
        #s.append(val[0])
        s.append(len(val[1]))
        for i in val[1]:
            s.append(i)
    trustSchemaModel.inner.cert = bytearray(s)

def encode_chain():
    s = []
    for i,n in enumerate(chainList):
        #s.append(i)
        s.append(len(n))
        for j in n:
            s.append(j)
    trustSchemaModel.inner.chain = bytearray(s)

def encode_tag():
    s = []
    for key,val in tagDict.items():
        s.append(val[0])
        s.append(len(val[1]))
        for i in val[1]:
            s.append(i)
    trustSchemaModel.inner.tag = bytearray(s)
        
def encode_template():
    s = []
    for i,n in enumerate(tempList):
        #s.append(i)
        s.append(len(n))
        for j in n:
            s.append(j)
    trustSchemaModel.inner.template = bytearray(s)

def encode_pub():
    s = []
    for i , n in enumerate(pubList):
        #s.append(i)
        s.append(n[0])
        s.append(len(n[1]))
        for m in n[1]:
            s.append(m)
    trustSchemaModel.inner.publication = bytearray(s)
    
    
def encode():
    encode_s_tab(s_tab)
    encode_token_table()
    encode_cert()
    encode_chain()
    #encode_tag()
    encode_template()
    encode_pub()
    
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
    
def listPrint(l):
    for n in l:
        print (n)
    print('\n')

def printall():
    #formatPrint(tokenDict)
    formatPrint(certDict)
    formatPrint(tagDict)
    listPrint(chainList)
    listPrint(tempList)
    listPrint(pubList)
    

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

    trustSchemaModel = TrustSchemaModel()
    trustSchemaModel.inner = NestedModel()

    s_tab = buildStringTable()
    #formatPrint(tokenDict)
    expandSigner()
    #print(signer)
    buildTempChain()
    print(tempChainDic)
    #formatPrint(defDict)
    
    handleCons()
    
    
    buildCert()
    #formatPrint(certDict)
    buildpub()
    encode()
    printall()
    
    
    res = trustSchemaModel.encode()
    f.write(res)
    
    
    
    
        
