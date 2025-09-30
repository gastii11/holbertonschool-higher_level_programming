#!/usr/bin/python3
"""clase Students"""


class Student:
    """clase srudents con atributos publicos"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        
        return self.__dict__
