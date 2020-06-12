#Obtención de la sucesión de Fibonacci para un número dado
#limite=resultado
n=int(input('Introduzca un número natural que detendrá la sucesión una vez el último término sea mayor o igual a este número '))

def sumar(a, b=1, n=n):
    resultado=a+b
    print(resultado)

    if resultado >=n:
        return
    sumar(a=resultado, b=a)


numero=0
sumar(a=numero, b=1, n=n)

#La función inicia en el segundo bloque. La recursividad se produce en el primer bloque