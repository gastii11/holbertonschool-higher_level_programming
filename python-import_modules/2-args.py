#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    contador = len(args)

    if contador == 0:
        print("0 arguments.")
    else:
        print(f"{contador} argument{'s' if contador != 1 else ''}:")
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")
