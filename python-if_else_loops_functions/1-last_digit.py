#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ultimo_digito = (number) % 10
if ultimo_digito > 5:
    print(f"Last digit of {number} is {ultimo_digito} and is greater than 5")
elif ultimo_digito == 0:
    print(f"Last digit of {number} is {ultimo_digito} and is 0")
elif ultimo_digito < 6 > 0:
    print(f"Last digit of {number} is {ultimo_digito} and is less than 6 and not 0")
