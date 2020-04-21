import statistics
#Obtención del promedio de 3 números
n1=float(input('Ingrese su primera nota '))
n2=float(input('Ingrese segunda nota '))
n3=float(input('Ingrese su tercera nota '))
p = statistics.mean([n1,n2,n3])
print(f'El promedio de sus notas es: {p}')


