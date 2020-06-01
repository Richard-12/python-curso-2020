#Arreglos con vectores y Matrices

import numpy as np

#vector=np.array([6,7,1,2,3])
#print(vector.astype(float))
#print(vector.astype(str))
#print(vector.astype(int))

#Podemos hacer operaciones con vectores
#a=np.array([6,7,1,2,3])
#b=np.array([6,7,5,8,1])
#print(a+b)

#a=np.array([6,7,1,2,3])
#b=np.array([6,7,5,8,1])
#print(a>b)

#vector=np.array([6,7,1,2,3])
#print(vector[3])

#Ahora con algunas funciones

#vector=np.array([6,7,1,2,3])
#print(vector.max())

#argmax, argmin: otorga la posición del máximo o mínimo valor
#print(vector.argmax())
#print(vector.argmin())
# podemos sumar los elementos de un vector
#print(vector.sum())
#print(vector.prod())

# MATREICES

#matriz=np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(matriz)

#Operaciones

#matriza=np.array([[1,2,3],[4,5,6],[7,8,9]])
#matrizb=np.array([[0,2,3],[4,5,6],[7,8,9]])
#print(matriza+matrizb)

#con funciones
vector=np.array([6,7,1,2,3])
matriz=np.array([[1,2,3],[4,5,6],[7,8,9]])

print('vector ',vector.size)
print('matriz ',matriz.size)