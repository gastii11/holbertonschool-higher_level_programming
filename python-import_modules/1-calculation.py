#!/usr/bin/python3
from calculator_1 import add as cuentas

if __name__ == "__main__":
    a = 10
    b = 5
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    print("{} + {} = {}".format(a, b, suma))
    print("{} - {} = {}".format(a, b, suma))
    print("{} * {} = {}".format(a, b, suma))
    print("{} / {} = {}".format(a, b, suma))
