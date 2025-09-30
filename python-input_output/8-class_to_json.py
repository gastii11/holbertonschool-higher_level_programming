#!/usr/bin/python3
"""devuelve diccionario de un objeto"""


def class_to_json(obj):
    """devuelve es un diccionario
    con todos los atributos del objeto"""
    return obj.__dict__
