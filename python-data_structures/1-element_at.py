#!/usr/bin/python3

def element_at(my_list, idx):
    largo = len(my_list)
    if idx < 0 or idx >= largo:
        return None
    return my_list[idx]
