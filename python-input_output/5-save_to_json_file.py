#!/usr/bin/python3
"""escribe un objeto python en un archivo json"""
import json


def save_to_json_file(my_obj, filename):
    """escribe objeto python en un archivo json"""
    with open(filename, 'w',) as my_set:
        json.dump(my_obj, my_set, indent=4)
