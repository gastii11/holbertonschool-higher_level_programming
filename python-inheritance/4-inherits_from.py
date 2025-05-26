#!/usr/bin/python3
"""true and false"""


def inherits_from(obj, a_class):
    """devuelve True si el objeto es una instancia de una
    clase que hereda de clase_base
    (directa o indirectamente),
    en caso contrario False."""
    return a_class in type(obj).__mro__[1:]
