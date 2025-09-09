#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copia = my_list[:]
    if 0 <= idx < len(my_list):
        copia[idx] = element
        return copia
    else:
        return my_list
