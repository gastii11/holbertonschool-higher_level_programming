#!/usr/bin/python3
"""clase cuadrado"""


class Square:
    """clase cuadrada"""
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError
        if size < 0:
            raise ValueError
        self.__size = size
