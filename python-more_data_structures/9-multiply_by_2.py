#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nuevo = {}
    for i, valor in a_dictionary.items():
        nuevo[i] = valor * 2
    return nuevo
