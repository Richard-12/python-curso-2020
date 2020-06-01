#Arreglos
#Calcular 10 números de manera aleatoria

import random

def vector_aleatorio(n):
    vector = [0]*n
    for i in range(n):
        vector[i]=random.randint(0,10)
    return vector
print('Ingrese cuántos números aleatorios desea obtener: ')
n=int(input())
aleatorio=vector_aleatorio(n)
print(aleatorio)