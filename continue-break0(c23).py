#Identificar números pares e impares
print('Identificar números pares e impares')
n1=int(input('Escriba un número '))
n2=int(input(f'Escriba un número mayor o igual que {n1:}: '))

if n2 < n1:
    print(f'Ingrese un número mayor o igual que {n1:} ')
else:
    for i in range(n1,n2+1):
        if i%2==0:
            print(f'El número {i} es par')
        else:
            print(f'El número {i} es impar')