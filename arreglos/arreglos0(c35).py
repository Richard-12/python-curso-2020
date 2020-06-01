#Arreglos: permite organizar información en vectores o en matrices

n=int(input('Ingrese el tamaño del arreglo: '))
m=int(input('Ingrese de qué número desea los múltiplos: '))
A=[]
#for i in range(0,n):
 #   A.append(i*m)
  #  print(A)
#O también puede presentarlo secuencialmente colocando el print dentro del for


for i in range(0,n):
    A.append(i*m)
print(A)


