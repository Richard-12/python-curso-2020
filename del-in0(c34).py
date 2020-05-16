#Uso de del & in: del: borra elementos de una lista,
#in: verificas si un elemento es parte de una lista

curso='python'
lista_nueva=list(curso)
print(lista_nueva)
del lista_nueva[0]
print(lista_nueva)

#Ahora veamos el in
print('y' in curso)
print('a' in curso)
if 'y' in lista_nueva:
    print('y es parte de la lista')
if 'a' in lista_nueva:
    print(' está en la lista')


