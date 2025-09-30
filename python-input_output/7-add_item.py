#!/usr/bin/python3
"""script que añade todos los argumentos a una lista de Python"""
import sys
import os
import json


def save_to_json_file(my_obj, filename):
    """escribe un objeto en un archivo de texto"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """crea un objeto"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

filename = "add_item.json"

if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
