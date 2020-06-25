#Obtención de primos de Fermat  Fn=2**(2**n) +1
from tqdm import tqdm
from sympy import isprime

n=int(input('write a natural number '))
fermat=(2**(2**n)) + 1

if isprime(fermat):
    print(fermat)
else:
    print('el resultado no es primo')

