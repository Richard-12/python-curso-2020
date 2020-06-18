#Obtención de la sucesión de Fibonacci para un número dado
#limite=resultado
n=int(input('Introduzca el número de términos de la sucesión de Fibonacci que desea '))
numero_de_terminos=[]
def sumar(a, b=1, n=n):
    resultado=a+b
    print(resultado)
    numero_de_terminos.append(resultado)
    if len(numero_de_terminos) == n:
        return
    sumar(a=resultado, b=a)

numero=0
sumar(a=numero, b=1, n=n)
print('Se han editado',len(numero_de_terminos),'términos de la sucesión de Fibonacci')
#La función inicia en el segundo bloque. La recursividad se produce en el primer bloque