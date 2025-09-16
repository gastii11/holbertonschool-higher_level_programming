#!/usr/bin/python3
""""nueva clase vacia"""


class Rectangle:
    """clase rectangulo"""
    def __init__(self, width, height):
        self.__width = width
        self.__heigth = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__heigth = value
