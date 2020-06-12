#Sucesion recursiva, cada numero es la suma de los tres anteriores
def sumar(a,b=1,c=1):
    resultado=a+b+c
    print(resultado)

    if resultado >5000:
        return
    sumar(a=resultado, b=a,c=b)
numero=0
sumar(a=numero,b=1,c=0)
