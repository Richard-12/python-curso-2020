#Continue
n=int(input('Ingrese un número '))
for i in range(1,n+1):
    if i%2==0:
        continue #salta a la inst sig
        print(i)
    else:
        print(i)
