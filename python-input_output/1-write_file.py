#!/usr/bin/python3
"""escribe y devuelve el numero de caracteres"""


def write_file(filename="", text=""):
    """escribe y devuelve el numero de caracteres, crea archivo"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
