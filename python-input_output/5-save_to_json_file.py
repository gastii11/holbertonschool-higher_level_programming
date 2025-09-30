#!/usr/bin/python3
"""función que escriba un objeto en un archivo
de texto, utilizando una representación JSON"""
import json


def save_to_json_file(my_obj, filename):
    """escribe un objeto en un archivo de texto"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
