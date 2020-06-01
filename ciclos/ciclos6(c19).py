#Número de vocales de una frase

frase=str(input('Ingrese una frase '))
vocales='aeiouAEIOU'
contador =0
for i in frase:
    if i in vocales:
        contador=contador+1
print('El número de vocales es: ',contador)