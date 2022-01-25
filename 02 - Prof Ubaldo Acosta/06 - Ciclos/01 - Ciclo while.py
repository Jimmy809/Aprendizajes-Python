# El uso del while nos permite ejecutar una sección de código repetidas veces, 
# de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla. 
# Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal. 
# Llamaremos iteración a una ejecución completa del bloque de código.

condicion = True

while condicion:
    print('Ejecutando ciclo while')
    break #La sentencia break nos permite alterar el comportamiento de los bucles while y for. 
          #Concretamente, permite terminar con la ejecución del bucle.
else:
    print('Fin del ciclo while')
    
# ejemplo 2
contador = 0
while contador < 3:
    print(contador)
    contador += 1 # esto le sumara 1 a la variable contador
else:
    print('Fin ciclo while')