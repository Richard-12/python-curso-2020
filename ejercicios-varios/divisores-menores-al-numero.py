#Para obtener los divisores de un número menores o iguales al número
n=int(input('Ingrese un número: '))
lista_de_divisores=[]
for i in range(1,n):
    if n%i==0:
        lista_de_divisores.append(n)
        print(i)
for i in lista_de_divisores:
    n=sum(lista_de_divisores)
print('La cantidad de divisores menores o iguales a ',n, 'es: ',len(lista_de_divisores))




