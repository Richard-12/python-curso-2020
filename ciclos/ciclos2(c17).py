#Mostrar una tabla de multiplicar
n= int(input('Ingrese la tabla de multiplicar que desea ver \n '))
i=1
print('La tabla de multiplicar del ',n,'es:')
while i <= 10:
    print(n,'x',i,'=',n*i)
    i=i+1
