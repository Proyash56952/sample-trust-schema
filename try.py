from ndn.encoding import *

class Model(TlvModel):          # Model = [Name] [IntVal] [StrVal] [BoolVal]
    #name = NameField()          # Name = NAME-TYPE TLV-LENGTH ...
    token_val = BytesField(0x84)   # IntVal = INT-VAL-TYPE TLV-LENGTH nonNegativeInteger
    tag_val = BytesField(0x85)  # StrVal = STR-VAL-TYPE TLV-LENGTH *OCTET
    cert_val = BytesField(0x86)
    bool_val = BoolField(0x01)  # BoolVal = BOOL-VAL-TYPE 0
    
model = Model()
#model.name = '/name/hi'
model.token_val = b'tok'
#model.str_val = b'bit string hola'
model.tag_val = b'tag'
#assert model.encode() == b'\x07\x06\x08\x04name\x02\nbit string'
res = model.encode()
print(res)
#print(model.asdict())

#model = Model.parse(b'\x07\x06\x08\x04name\x02\nbit string')
#assert model.str_val == b'bit string'
