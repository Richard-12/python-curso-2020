#Generar los múltiplos de 3 (Horizontalmente)
#m= interruptor

n=int(input('Ingrese el número de múltiplos '))
m=3
for i in range(1,n+1):
    print(m,end ='-')
    m=m+3