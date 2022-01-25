# El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
# El usuario proporcionará un valor entre 0 y 10.
# Si está entre 9 y 10: imprimir una A
# Si está entre 8 y menor a 9: imprimir una B
# Si está entre 7 y menor a 8: imprimir una C
# Si está entre 6 y menor a 7: imprimir una D
# Si está entre 0 y menor a 6: imprimir una F
# cualquier otro valor debe imprimir: Valor desconocido
# Por ejemplo:
#  Proporciona un valor entre 0 y 10:
#  A
# Puedes utilizar el IDE de tu preferencia para codificar la solución y después pegar tu solución en esta herramienta.

nota = int(input('proporcionará un valor entre 0 y 10: '))

mensaje = None

if nota >= 0 and nota < 6:
    mensaje = 'F'
elif nota >= 6 and nota < 7:
    mensaje = 'D'
elif nota >=  7 and nota < 8:
    mensaje = 'C'
elif nota >= 8 and nota < 9:
    mensaje = 'B'
elif nota >= 9 and nota <= 10:
    mensaje = 'A'

else:
    mensaje = 'Valor desconocido'
print(mensaje)