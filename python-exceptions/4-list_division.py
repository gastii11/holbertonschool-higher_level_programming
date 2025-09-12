#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nueva = []
    for i in range(list_length):
        try:
            resultado = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            resultado = 0
        except (TypeError, ValueError):
            print("wrong type")
            resultado = 0
        except IndexError:
            print("out of range")
            resultado = 0
        finally:
            nueva.append(resultado)
    return nueva
