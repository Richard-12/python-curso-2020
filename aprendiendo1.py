# Aprendiendo sobre conjeturas (No considerar números grandes.
# Obtención de números primos dentro de ciertos rangos dados
from tqdm import tqdm
from sympy import isprime

limite_inferior=int(input('Ingrese el limite inferior del range '))
limite_superior=int(input('Ingrese el limite superior del range '))
numeros_primos = []

# for a in range(limite_inferior, limite_superior):
for a in tqdm(range(limite_inferior, limite_superior)):
    n = (2 ** (2 ** a)) + 1
    if isprime(n):
        numeros_primos.append(n)

print(f"Numeros primos encontrados: {len(numeros_primos)}")
if len(numeros_primos) > 0:
    mostrar_primos = input('Mostrar numeros primos? (S/N) ')

    if mostrar_primos.upper() == "S":
        print(numeros_primos)
