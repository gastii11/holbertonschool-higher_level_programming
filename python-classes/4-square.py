#!/usr/bin/python3
""" modulo que define la clase cuadrado"""


class Square:
    """ la clase de un cuadrado"""

    def __init__(self, size=0):
        """ inicialice el tamaño de un cuadrado"""
        self.__size = size

    @property
    def size(self):
        return self.__size
    """devuelve un valor"""

    @size.setter
    def size(self, value):
        self.__size = value
        """permite cambiar el valor"""
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")

        self.__size = self.size

        """ condiciones que tiene que cumplir"""

    def area(self):
        return self.__size ** 2
        """retorna el area cuadrada"""
