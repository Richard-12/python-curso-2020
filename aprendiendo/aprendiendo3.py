#Establece si un número dado es primo o no
import sympy
from sympy import isprime

def app():
    num = int(input('write a number \n '))
    if sympy.isprime(num) and sympy.isprime(num + 2):
        print(f'The numbers {num} and {num + 2} are twin prime!!')
    else:
        print(f'The numbers {num} and {num + 2} are NOT twin prime!!')


app()