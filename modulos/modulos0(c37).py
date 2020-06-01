'''Modulos: colección de definiciones de variables,
funciones y tipos (entre otras cosas) que pueden ser
importados para ser usados desde cualquier programa
VENTAJAS:
-Las funciones y variables deben ser definidas sólo una vez y luego pueden ser usadfas en muchos programas sin necesidad de reescribir el código
-Permiten que un programa pueda ser organizado en varias secciones lógicas, puestas cada una en un archivo separado.
-Hacen más fácil compartir componentes con otros pragramadores-

'''

#Modulos Math

from math import pi
a=pi
print(a)

#--------
from math import factorial
a=factorial(6)
print(a)
#--------
from math import log
a=log(8,10)
print(a)
#--------
from random import choice
a=choice(['cara','cruz','robo','regalo'])
print(a)
#----------
from random import randrange
a=randrange(100)
print(a)
#-----------
from datetime import date
dia=date(2019,2,22)
print(dia)

#---------------
from datetime import date
dia=date(2019,2,23)
año=date(2019,12,31)
fin_de_año=(año-dia).days
print('faltan: ',fin_de_año,'días. ')

#----------
from fractions import Fraction
a=Fraction(2,4)
b=Fraction(4,8)

print(Fraction(a+b))





