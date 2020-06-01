#from par import pares
#a=pares(7)
#print(a)

#Llamado de la función ciclo

from par import ciclo_pares

n=int(input('Ingrese un número '))
print('Los números pares hasta',n, 'son ')
for i in ciclo_pares(n):
    print(i)
