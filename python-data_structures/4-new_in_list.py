#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    largo = len(my_list)
    if idx < 0 or idx >= largo:
        return my_list
    