#!/usr/bin/python3
"""lectura de archivo"""


def read_file(filename=""):
    """lee el archivo  y lo imprime en stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
