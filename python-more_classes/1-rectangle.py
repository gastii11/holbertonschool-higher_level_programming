#!/usr/bin/python3
""""nueva clase vacia"""


class Rectangle:
    """clase rectangulo"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__heigth = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")

    @property
    def heigth(self):
        return self.__heigth

    @heigth.setter
    def width(self, value):
        if not isinstance(value, int):
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")
