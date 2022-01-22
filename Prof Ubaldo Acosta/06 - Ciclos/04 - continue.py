# for i in range(6):
#     if i % 2 == 0: # verificamos que sea divisible entre 2 y asi deducimos q es un numero par
#         print(f'Valor: {i}') # i imprimira cada indice en el rango de 0 a 6, en esete caso solo los numero pares

# Concretamente, continue se salta todo el código restante en la iteración actual 
# y vuelve al principio en el caso de que aún queden iteraciones por completar.
# La diferencia entre el break y continue es que el continue no rompe el bucle, 
# si no que pasa a la siguiente iteración saltando el código pendiente.

for i in range(6):
    if i % 2 != 0: # verificamos que sea no divisible entre 2 y asi deducimos q es un numero es impar
        continue # lo contrario de break, en este caso si seguira ejecutando el ciclo for
    print(f'Volor: {i}')
# Valor: 0
# Valor: 2
# Valor: 4
    
cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue # a detectado la palabra P, pero aun asi continuara buscando los demas indices
    print(letra)
# Salida:
# y
# t
# h
# o
# n