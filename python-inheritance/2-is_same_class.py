#!/usr/bin/python3
"""exactamente una instancia de la clase especificada"""


def is_same_class(obj, a_class):
    """devuelve true si el objeto es exactamente 
    una instancia de la clase especifica"""
    return type(obj) is a_class
