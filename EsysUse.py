#encode with my system.
import eSYS as e
ch=input("Encode or decode?(e/d) ")
if ch=="e":
    pTEXT=input("What is to be encoded? ")
    pKEY =input("What is the key? ")
    v=e.encode_to_STR(pTEXT,pKEY)
    print(v)
if ch=="d":
    pTEXT=input("What is to be decoded? ")
    v=e.STRdecode_to_STR(pTEXT)
    print(v)