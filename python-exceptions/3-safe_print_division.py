def safe_print_division(a, b):
    resultado = None
    try:
        resultado = a / b
    except ZeroDivisionError:
        resultado = None
    finally:
        print("Inside result: {}".format(resultado))
    return resultado
