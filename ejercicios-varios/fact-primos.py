#obtención de factores primos
from sympy import isprime

numero=int(input('Ingrese un número natural mayor a 1 '))
factores_primos=[]
for i in range(1,numero+1):
    if numero%i == 0 and isprime(i):
        print(i)
        factores_primos.append(str(i))

factores_primos_str = "x".join(factores_primos)
print(f"{numero} = {factores_primos_str}")

