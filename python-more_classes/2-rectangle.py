#!/usr/bin/python3
"""define una clase rectangle"""


class Rectangle:
    """rectangulo con ancho y altura"""

    def __init__(self, width=0, height=0):
        """inicializa una instancia de rectangulo"""

        self.width = width
        self.height = height

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
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """arena del rectangulo"""
        return self.width * self.height
    
    if width == 0 or height == 0:
        perimeter = 0

    def perimeter(self):
        """perimetro de rectangulo"""
        return 2 * (self.width + self.height)