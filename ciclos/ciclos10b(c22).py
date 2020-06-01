#Generar los múltiplos de 3 (Horizontalmente)
#m= interruptor

n=int(input('Ingrese el número de múltiplos '))
m=int(input('Ingrese de quién serán los multiplos: '))
s=m
for i in range(1,n+1):
    print(s, end= ' ')
    s=s+m