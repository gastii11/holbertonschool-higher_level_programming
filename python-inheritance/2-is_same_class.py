#!/usr/bin/python3
"""devuelve true o false"""


def is_same_class(obj, a_class):
    if not isinstance(obj, a_class):
        return True
    else:
        return False
