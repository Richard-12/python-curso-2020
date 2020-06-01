#Determinar si una expresión es un entero
a=int(input('Introduca el valor de a '))
b=int(input('Introduzca el valor de b '))
nume=1+a*b
deno=a+b
n=nume/deno
if nume%deno==0:
    print(f'La expresión da un entero y el resultado es: {n} ')
else:
    print(f'La expresión NO es un entero y el resultado es: {n}')