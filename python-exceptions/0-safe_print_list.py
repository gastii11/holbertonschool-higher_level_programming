#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elemntos_impresos = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            elemntos_impresos += 1
    except IndexError:
        pass
    print()
    return elemntos_impresos