numero = int(input("ingrese numero de comprobacion: "))
def sumalista(lista_numeros):
    la_suma = 0
    lista_numeros_sumados = []
    for i in lista_numeros:
        la_suma += i
        lista_numeros_sumados.append(i)
    return la_suma


def lista_divisores(n):
    lista_de_divisores=[]
    for i in range(1,n):
        if n % i == 0:
            lista_de_divisores.append(i)
            print(i)
    return lista_de_divisores
listado_numeros = lista_divisores(numero)

resultado_suma = sumalista(lista_numeros=listado_numeros)
print('La suma de los divisores es; ',resultado_suma)