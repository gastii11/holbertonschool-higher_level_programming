#!/usr/bin/python3
def safe_print_integer(value):
    try:
        entero = int(value)
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
    except TypeError:
        return False

