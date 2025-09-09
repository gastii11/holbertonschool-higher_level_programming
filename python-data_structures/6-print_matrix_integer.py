#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        largo = " ".join(["{}"] * len(fila))
        print(largo.format(*fila))
