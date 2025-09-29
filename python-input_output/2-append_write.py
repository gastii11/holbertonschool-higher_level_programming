#!/usr/bin/python3
"""cadena al final y numero de caracteres"""


def append_write(filename="", text=""):
    """cadena al final y numero de caracteres"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
