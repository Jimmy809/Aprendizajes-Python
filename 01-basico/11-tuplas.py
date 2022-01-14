# Las tuplas son similares a una lista,
# creadas con una variable luego () y separado por comas
from socket import NI_NUMERICHOST


nombres = ("Carlos", "Marcos", "Luz", "Luis")
numeros = (1, 2, 3, 4, 5)
valor = (True, False, True)
combinada = ("Marcos", 2, 3, 4, True, False)

#para saber la cantidad de contenido de cada tupla
print(len(nombres))

#para llamar un elemento
print(combinada[2])

#para modificar una tupla
x = list(nombres)
x[1] = "Oscar"
nombres = tuple(x)
print(nombres[1])

#para desempaquetar una tupla
#(uno, dos, tres, cuatro, cinco) = numeros
#print(uno)

# Metodos de una tupla count()
# Muestra la cantidad de veces q se encuentra ese objeto
print(numeros.count(4))

# con el index muestra en que posicion se encuentra ese numero
print(numeros.index(5))