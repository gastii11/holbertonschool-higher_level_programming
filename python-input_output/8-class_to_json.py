#!/usr/bin/python3
"""devuelve la descripcion"""
import json


def class_to_json(obj):
    """devuelve la descripcion"""
    return obj.__dict__
