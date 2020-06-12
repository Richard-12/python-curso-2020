#arreglos: otro ejercicio
#Ejemplo:

#(1,5,8,9,10,9,13)
#Imprimir por pantalla los números impares a 3

A=[1,5,8,9,30,9,13]
B=[]
for i in A:
    if i>5 and i%2 !=0:
        B.append(i)
print(B)