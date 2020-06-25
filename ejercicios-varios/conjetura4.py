# Obtención de números primos dentro de ciertos rangos dados

from sympy import isprime
n = int(input('Ingrese un valor natural '))
numeros_primos_encontrados=[]
m=n**2
t=(n+1)**2
for i in range(m,t):
    if isprime(i):
        print(i)
        numeros_primos_encontrados.append(i)
print('El número de primos encontrados es:',len(numeros_primos_encontrados))






