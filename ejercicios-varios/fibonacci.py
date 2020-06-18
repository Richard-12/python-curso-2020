#Obtención de la sucesión de Fibonacci para un número dado
def sumar(a,b=1):
    resultado=a+b
    print(resultado)
    if resultado >5000:
        return
    sumar(a=resultado, b=a)
numero=0
sumar(a=numero)

