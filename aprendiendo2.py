from tqdm import tqdm
from sympy import isprime

limite_inferior=int(input('Ingrese el limite inferior del range '))
limite_superior=int(input('Ingrese el limite superior del range '))
numeros_pares = []
for a in tqdm(range(limite_inferior, limite_superior)):
      if a%2==0:
        numeros_pares.append(a)

print(f"Numeros pares encontrados: {len(numeros_pares)}")
if len(numeros_pares) > 0:
    mostrar_pares = input('Mostrar numeros pares? (S/N) ')

    if mostrar_pares.upper() == "S":
        print(numeros_pares)
