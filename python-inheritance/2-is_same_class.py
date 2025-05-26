#!/usr/bin/python3
"""devuelve true o false"""


def is_same_class(obj, a_class):
    """devuelve True si el objeto es una instancia de la clase especificada"""
    if not isinstance(obj, a_class):
        return True
    else:
        return False
