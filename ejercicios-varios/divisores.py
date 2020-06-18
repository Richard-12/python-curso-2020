#Para obtener los divisores de un número menores o iguales al número
n=int(input('Ingrese un número: '))
lista_de_divisores=[]
for i in range(1,n+1):
    if n%i==0:
        lista_de_divisores.append(n)
        print(i)

print('La cantidad de divisores menores o iguales a ',n, 'es: ',len(lista_de_divisores))



