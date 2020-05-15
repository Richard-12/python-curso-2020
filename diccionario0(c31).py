#Diccionarios, arreglos
edades={'victor':30,'Rafael':40,'Enrique':23, 'Carlos':45}
print(edades)

#aplicación de propiedades anteriores

#caso del valor depositado

print(edades['Carlos'])

#cambiar valores en el diccionario
edades['victor']= 48
print(edades)

#Para mostrar los elementos del diccionario
for i in edades:
    print(i,edades[i])