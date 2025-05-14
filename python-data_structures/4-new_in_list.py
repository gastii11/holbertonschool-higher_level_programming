#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copia = my_list.copy()
    largo = len(my_list)
    if idx < 0 or idx >= largo:
        return copia
    copia[idx] = element
    return copia