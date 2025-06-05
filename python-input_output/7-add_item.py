#!/usr/bin/python3
"""añade y guarda argumentos"""
import os
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add.item.json"

if os.path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
else:
    items = []

items.extend(sys.argv[1:])


save_to_json_file(items, filename)
