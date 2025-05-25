#!/usr/bin/python3
""" modulo que define la clase cuadrado"""


class Square:
    """ la clase de un cuadrado"""

    def __init__(self, size=0, position=(0, 0)):
        """ inicialice el tamaño de un cuadrado"""
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2
        """retorna el area cuadrada"""

    def my_print(self):
        if self.size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
