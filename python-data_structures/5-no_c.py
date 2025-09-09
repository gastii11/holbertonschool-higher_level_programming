#!/usr/bin/python3
def no_c(my_string):
    eliminar = "C", "c"
    resultado = "".join([i for i in my_string if i not in eliminar])
    return resultado
