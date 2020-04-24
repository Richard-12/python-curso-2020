#Saber cuando un número es Negativo, Neutro o positivo con elif
a=float(input('Ingrese un número: '))
if a<0:
    R='Negativo'
elif a==0:
     R='Neutro'
else:
     R='Positivo'
print(f'El número {a} es:',R)