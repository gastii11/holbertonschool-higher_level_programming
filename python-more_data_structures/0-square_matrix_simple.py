#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nueva_matrix = []
    for i in matrix:
        nueva = []
        for j in i:
            nueva.append(j ** 2)
        nueva_matrix.append(nueva)
    return nueva_matrix
