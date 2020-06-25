#Enunciado:Si (a**2 + b**2)/(a*b +1) es entero entonces es el máximo común divisor de a y b
# Revisión de conjetura: Este programa descubre pares de valores dentro de un rango para las cuales resulta un entero
from tqdm import tqdm
limite_inferior=int(input('Ingrese el limite inferior del rango '))
limite_superior=int(input('Ingrese el limite superior del rango '))
resultado_enteros = []
for a in tqdm(range(limite_inferior, limite_superior)):
    for b in range(limite_inferior, limite_superior):
        n=(a**2 + b**2)
        m=(a*b+1)
        if n%m==0:
            e=n/m
            # print(f'El resultado es un entero y su valor es: {e} ')
            if [b, a, e] not in resultado_enteros:
                resultado_enteros.append([a, b, e])
        # else:
        #     print('El resultado no es un entero')


print(f"Parejas de números encontrados: {len(resultado_enteros)}")
if len(resultado_enteros) > 0:
    mostrar_resultado = input('Mostrar parejas y resultado? (S/N) ')

    if mostrar_resultado.upper() == "S":
        for resultado in resultado_enteros:
            print(f"Valor a: {resultado[0]}. Valor b: {resultado[1]}. Resultado: {resultado[2]}")
