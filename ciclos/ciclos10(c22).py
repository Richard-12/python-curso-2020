#Generar los múltiplos de 3
# m= interruptor
n=int(input('Ingrese un número '))
m=int(input('Ingrese de qué número: '))
s= m
for i in range(1,n+1):
    print(s)
    s=s+m
