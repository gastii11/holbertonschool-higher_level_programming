#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nueva = []
    for i in my_list:
        if i == search:
            nueva.append(replace)
        else:
            nueva.append(i)
    return nueva
