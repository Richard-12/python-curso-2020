# Conjetura 3n+1

num = int(input('Ingrese un número natural mayor 1: '))
k=[]
def resultado(m):
    if m == 1:
        return

    if m % 2 == 0:
        m = m / 2
        k.append(m)
        print(m)

        while m % 2 == 0:
            m = m/2
            k.append(m)
            print(m)

        if not m % 2 == 0:
            resultado(m)
    else:
        m = 3 * m + 1
        resultado(m)

resultado(m=num)

print('El número de resultados mostrados al llegar a 1 para ',num, 'es:',len(k))

