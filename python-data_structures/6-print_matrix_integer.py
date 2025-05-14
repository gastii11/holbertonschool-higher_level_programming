#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for n in range(len(i)):
            if n < len(i) - 1:
                print("{:d}".format(i[n]), end=" ")
            else:
                print("{:d}".format(i[n]), end="")
        print()
