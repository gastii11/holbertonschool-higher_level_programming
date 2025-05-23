#!/usr/bin/python3

def uppercase(str):
    resultado = ""
    for caracter in str:
        if ord(caracter) >= 97 and ord(caracter) <= 122:
            resultado += chr(ord(caracter)-32)
    
        else:
            resultado += caracter
    print("{}".format(resultado))


