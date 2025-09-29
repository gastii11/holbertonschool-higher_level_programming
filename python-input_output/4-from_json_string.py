#!/usr/bin/python3
"""devuelve un objeto python"""
import json


def from_json_string(my_str):
    """devuelve un objeto python"""
    return json.loads(my_str)
