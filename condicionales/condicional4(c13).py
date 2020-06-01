#Verificar si un número es negativo, neutro o positivo sin el uso del elif
a=float(input('Ingrese un número '))
if a<0:
    R='Negativo'
else:
    if a==0:
       R='Neutro'
    else:
       R='Positivo'
print('El número dado es: ',R)
