
# Revisión de conjetura
from tqdm import tqdm
limite_inferior=int(input('Ingrese el limite inferior del range '))
limite_superior=int(input('Ingrese el limite superior del range '))
expresiones_enteras = []
for a in tqdm(range(limite_inferior, limite_superior)):
    for b in range(limite_inferior, limite_superior):
        n=(a**2 + b**2)
        m=(a*b+1)
        if n%m==0:
            e=n/m
            # print(f'La expresión es un entero y su valor es: {e} ')
            if [b, a, e] not in expresiones_enteras:
                expresiones_enteras.append([a, b, e])
        # else:
        #     print('La expresión no es un entero')


print(f"Expresiones encontradas: {len(expresiones_enteras)}")
if len(expresiones_enteras) > 0:
    mostrar_expresiones = input('Mostrar expresiones? (S/N) ')

    if mostrar_expresiones.upper() == "S":
        for expresion in expresiones_enteras:
            print(f"Valor a: {expresion[0]}. Valor b: {expresion[1]}. Expresion: {expresion[2]}")
