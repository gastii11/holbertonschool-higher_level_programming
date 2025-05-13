#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for elemnto in fila:
            print("{:d}".format(elemnto), end=" ")
        print()