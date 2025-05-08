#!/usr/bin/python3
omitir = "e"
omitir1 = "q"
for i in range(97, 123):
    caracter = chr(i)
    if caracter != omitir and caracter != omitir1:
        print(caracter, end="".format(caracter))
