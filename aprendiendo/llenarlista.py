lista=[]
def sumar(a,b=1):
    resultado = a+b
    print(resultado)
    lista.append(resultado)
    if resultado > 10:
        return
    sumar(resultado,b)



#numero = 1
sumar(0)
print(lista)