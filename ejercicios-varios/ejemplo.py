#Proporciona los números pares menores o iguales a un número dado
n=int(input('Ingrese un número '))

for i in range(0,n+1):
    if i%2==0:
        print(i)
