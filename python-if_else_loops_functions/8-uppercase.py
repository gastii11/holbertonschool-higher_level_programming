#!/usr/bin/python3
def uppercase(str):
    resultado = ""
    for i in str:
        asci = ord(i)
        if 'a' <= i <= 'z':
            asci -= 32
        resultado += chr(asci)
    print("{}".format(resultado))
