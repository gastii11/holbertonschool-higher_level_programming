#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    filas = len(matrix)
    columnas = len(matrix[0]) if filas > 0 else 0 
    matrix_cuadrada = []

    for i in range(filas):
        fila_cuadrado = []
        for j in range(columnas):
            fila_cuadrado.append(matrix[i][j] ** 2)
        matrix_cuadrada.append(fila_cuadrado)
    return matrix_cuadrada
