'''Un teorema de Fermat, Si p es un número primo, entonces para cada número natural a mayor que cero a**p es congruente con a módulo p'''
a=int(input('Ingrese un número entero mayor que cero '))
p=int(input('Introduzca un número primo '))
n=a**p-a
if n%p==0:
    print('En efecto,Fermat no se equivocó ')
else:
    print('Eureka, e conseguido un contraejemplo, Fermat falló ')
