#!/usr/bin/python3
"""Una clase que hereda"""


class MyList(list):
    """clase mylist que hereda list"""
    def print_sorted(self):
        orden = sorted(self)
        print(orden)
