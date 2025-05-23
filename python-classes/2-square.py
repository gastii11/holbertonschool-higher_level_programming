#!/usr/bin/python3
""" modulo que define la clase cuadrado"""


class Square:
    """ la clase de un cuadrado"""
    def __init__(self, size=0):
        """ inicialice el tamaño de un cuadrado"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0") 
        
        """ condiciones que tiene que cumplir"""
        
        self.__size = size


