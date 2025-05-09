#!/usr/bin/python3
eliminar_coma = ","
for lista in range(1, 100):
    if lista == 99:
        print(99)
    else:
        print("{:02d}".format(lista), end=", ")

