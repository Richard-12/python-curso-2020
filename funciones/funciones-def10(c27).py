#separa una lista en pares e impares

ejemplo=[39,7,9,5,3,7,12]

def separar_lista(lista):
    lista.sort()
    pares=[]
    impares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares

pares,impares=separar_lista(ejemplo)
print(pares)
print(impares)
print(ejemplo)