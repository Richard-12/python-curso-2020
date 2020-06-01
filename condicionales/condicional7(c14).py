# Calificación de notas
# Datos
# n:notas
# R:respuestas

n=float(input('Ingresa su nota '))
if n<=50:
    R='Reprobado'
elif n<=80:
    R='Aprobado'
elif n<=90:
    R='Sobresaliente'
else:
    R='Excelente'
print('Su nota es ',n, R)