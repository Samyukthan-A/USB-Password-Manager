import binascii 
import os
#import any encryption liberies 
os.system('cls')

def hex_to_tex(hex):
    return binascii.unhexlify(hex)

key = "" #input your key here
#f = (key)

def de(ps):
    text = hex_to_tex(ps)
    a = f.decrypt(text)
    return a
