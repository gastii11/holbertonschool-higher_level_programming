#!/usr/bin/python3
def no_c(my_string):

    nuevo_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            nuevo_string += i
    return nuevo_string
