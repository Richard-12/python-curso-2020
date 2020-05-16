#Indices: permite indizar o indicar que caracter en una cadena se encuentra en una posición dada

#curso='python'
#print(curso[2])
#print(curso[5])
#cadena='constitucionalmente'
#print(cadena[1:5])
#print(cadena[7:])
#print(cadena[:7])
#En ambos casos anteriores no incluye la posición 7

#Tambien podemos cambiar una cadena en lista

#cadena='aeiou'
#vocales=list(cadena)
#print(vocales)

#Tambien con tuplas
#vocales='aeiou'
#vocales=tuple(cadena)
#print(vocales)
#tambien podemos usar index para ubicar un elemento
cadena='aeiou'
vocales='aeiou'
vocales=list(cadena)
print(vocales.index('i'))