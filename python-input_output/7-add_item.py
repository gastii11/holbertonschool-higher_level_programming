#!/usr/bin/python3
"""añade y guarda argumentos"""
import json


def save_to_json_file(my_obj, filename):
    """guarda un objeto json"""
    with open(filename, 'w') as add_item:
        json.dump(my_obj, add_item, indent=4)


def load_from_json_file(filename):
    """carga un objeto de un archivo json"""
    with open(filename, 'r') as add_item:
        return json.load(add_item)
