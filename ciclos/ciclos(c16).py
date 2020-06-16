# Mostrar la suma de los n primeros números
n=int(input('Ingrese el valor de un número '))
suma=0
i= 1
while i<=n:
    suma= suma + i
    i=i+1
print('La suma de los números hasta el ',n, 'es: ',suma)
