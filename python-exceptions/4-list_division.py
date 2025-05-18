#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lista_nueva = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                print("wrong type")
                resultado = 0
            elif b == 0:
                print("division by 0")
                resultado = 0
            else:
                resultado = a / b
        
        except IndexError:
            print("out of range")
            resultado = 0
        finally:
            lista_nueva.append(resultado)

    return lista_nueva