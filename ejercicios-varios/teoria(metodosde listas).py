             #Metodos de listas
#append() Añade un item al final de la lista
    lista=[1,2,3,4,5]
    lista.append(6)
    lista
#clear() vacía todos los items de la lista
    lista.clear()
    lista
#extend() une una lista a otra.
    l1=[1,2,3]
    l2=[4,5,6]
    l1.extend(l2)
    l1
#count() Cuenta el número de veces que aparece un item

#index() Devuelve el indice en el que aparece un item(error si no aparece)
    ["ola","mundo"].index("mundo")
#insert Agrega un item a la lista en un indice específico
    l=[1,2,3]
    l.insert(0,0)
    l
#pop() Extrae un  item de la lista y lo borra
    l=[10,20,30,40,50]
    print(l.pop())
print(l)

#remove() Borra el item de la lista cuyo valor concuerde con el que indicamos
    l=[20,30,30,30,40]
    l.remove(30)
    print(l)
#sort() Ordena automaticamente los items de una lista por su valor de menor a mayor
lista=[5,-10,35,0,-65,100]
lista.sort()
lista

                    #Metodos de cadenas
'''
upper() Devuelve la cadena con todos los caracteres a mayusculas
    "ola Mundo.upper
lower() Devuelve la cadena con todos sus caracteres en minuscula
    "Hola Mundo".lower()
capitalize() Devuelve la cadena con su primer caracter en mayuscula
    "Hola Mundo.capitalize()
title() Devuelve la cadela con el primer  caracter de cada palabra en mayuscula
    "Hola Mundo.title()
count() Devuelve una cuenta de las veces que aparece una subcadena en la cadena
    "Hola Mundo.count()
find() Devuelve el indice en el que aparece la subcadena (-1 si no aparece)
    "Hola Mundo.find()
rfind() Devuelve el indice en el que aparece la subcadena , empezando por el final.
    "Hola Mundo.find('mundo')
isdigit() Devuelve True si la cadena es todo números(False en caso contrario)
    c="100"
    c.isdigit()
isalnum() Devuelve True si la cadena es todo número alfabeticos o caracteres
    c="ABC10034po"
    c.isalnum()
isalpha() Devuelve True si la cadena es todo caracteres albabeticos
    c = "ABC10034po"
    c.isalpha()
islower() Devuelve True si la cadena es todo minusculas:
    "Hola mundo".islower()
isupper() Devuelve True si la cadena es todo mayúsculas:
    "Hola mundo".isupper()
istitle() Devuelve True si la primera letra de cada palabra es mayúscula:
  "Hola Mundo".istitle()  
isspace() Devuelve True si la cadena es todo espacios:
    "  -  ".isspace()  
startswith() Devuelve True si la cadena empieza con una subcadena:
     "Hola mundo".startswith("Mola")
endswith() Devuelve True si la cadena acaba con una subcadena:
    "Hola mundo".endswith('mundo')
split() Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista:
  "Hola mundo mundo".split()[0]
replace() Reemplaza una subcadena de una cadena por otra y la devuelve:
  "Hola mundo".replace('o','0')
  "Hola mundo mundo mundo mundo mundo".replace(' mundo','',4)
  
'''