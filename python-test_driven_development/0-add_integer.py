#!/usr/bin/python3
"""
Módulo que contiene la función add_integer.
Permite sumar dos números enteros o flotantes.
"""


def add_integer(a, b=98):
    """
    Suma dos números enteros.

    Args:
        a (int, float): primer número.
        b (int, float, opcional): segundo número, por defecto 98.

    Returns:
        int: la suma de a y b, convertidos a enteros si son flotantes.

    Raises:
        TypeError: si a o b no son enteros ni flotantes.

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    """

    return int(a) + int(b)
