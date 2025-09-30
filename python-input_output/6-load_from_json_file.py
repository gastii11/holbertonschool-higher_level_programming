#!/usr/bin/python3
"""objeto creado mediante archivo json"""
import json


def load_from_json_file(filename):
    """crea un objeto"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data