#!/usr/bin/python3
"""función que devuelva True si el objeto es
una instancia de una clase que hereda"""


def inherits_from(obj, a_class):
    """función que devuelva True si el objeto es
una instancia de una clase que hereda"""
    return isinstance(obj, a_class) and type(obj) is not a_class
