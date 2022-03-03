from antlr4 import *
from dctLexer import dctLexer
from dctListener import dctListener
from dctParser import dctParser
from dctVisitor import dctVisitor
import sys
from collections import defaultdict
from ndn.encoding import *

idDict = {}
defDict = defaultdict(list)
tokenList = set()
tokenDict = {}
certDict = {}
tagDict = {}
templateDict = {}

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
            
            if(id.type == 'hString'):
                tagDict[id.value] = [-1,-1]
                templateDict[id.value] = [-1,-1]
        
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
        return id, s
        
    def visitCertificates(self, ctx:dctParser.CertificatesContext):
        certs = []
        for i in ctx.identifier():
            certs.append(i.accept(self))
            certDict[i.accept(self).value] = [-1,-1,-1]
        return certs
    
    def visitUstring(self, ctx:dctParser.UstringContext):
        return ctx.UNDERSCORE().getText() + ctx.STRING().getText()
        
    def visitHstring(self, ctx:dctParser.HstringContext):
        return ctx.HASH().getText() + ctx.STRING().getText()
        
    def visitLiteral(self, ctx:dctParser.LiteralContext):
        #print(ctx.STRING().getText())
        #tokenList.add(ctx.STRING().getText())
        tokenDict[ctx.STRING().getText()] = [-1,-1,-1]
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
        exp = defDict[key][0]
        constraints = defDict[key][1]
        signer = defDict[key][2]
        
        if(exp.type == 'id'):
            previd = defDict.get(exp.value.value)
            name = previd[0]
            
            if(not signer and previd[2]):
                signer = previd[2]
        else:
            name = exp

        for i,n in enumerate(name.value):
            if(constraints and n.value in constraints[0]):
                comp = constraints[0][n.value]
                cert.append(tokenDict[comp][0])
            elif(n.value in idDict):
                comp = idDict[n.value]
                cert.append(tokenDict[comp][0])
            elif(n.type == 'uString'):
                cert.append(160+i)
            else:
                comp = n.value
                cert.append(tokenDict[comp][0])
            

        if(not signer):
            signer = -1
        certDict[key] = [certIndex,cert,signer]
            
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
    print(s)
    #print(bytearray(s))
    #model.string_table = bytes(k)
    #print((bytes(s)))
    #model.token_table = bytes(s)
    trustSchemaModel.inner.tok_val = bytes(s)
    
def get_parse_tree(file_name):
    schema_src_code = FileStream(file_name)
    lexer = dctLexer(schema_src_code)
    stream = CommonTokenStream(lexer)
    parser = dctParser(stream)
    tree = parser.schema()
    return tree, parser.getNumberOfSyntaxErrors()
    

tree, err = get_parse_tree(sys.argv[1])
outputfile = sys.argv[2]
f = open(outputfile,"w")
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
    
    
    #model = Model()
    s_tab = buildStringTable()
    
    #b_s_tab = bytearray(s_tab.encode())
    #print(tokenDict)
    #print(b_s_tab)
    #model.string_table = b_s_tab
    
    #print(certDict)
    #buildTag()
    #print(tagDict)
    
    #buildCert()
    #print(certDict)
    #buildTemplate()
    #print(templateDict)
    
    encode_s_tab(s_tab)
    encode_token_table()
    
    res = trustSchemaModel.encode()
    print(res)
    f.write(str(res))
    
    
    
        
