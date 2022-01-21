# Para crear una lista usaremos []
lista_nombres = ['Marcos', 'Juan', 'Caro', 'Roberto', 'Rosa']
lista_numeros = [1, 2, 3, 4, 5,]
lista_varias = [1, 5, 4, 'Mary', 'Juan', True, False, False]


# para mostar una lista
print(lista_nombres)

# para saber la cantidad de objeto que tiene la lista
print(len(lista_nombres))

# para mostrar un elemento de una lista
print(lista_nombres[1])

# para mostrar una secuencia
print(lista_numeros[2:4])

# Modificar un elemento de la lista
lista_numeros[2] = 'Jimmy'
print(lista_numeros)

# Para agregar un elemento a la lista append
lista_numeros.append(6)
print(lista_numeros)

# Para agregar un lista a una lista extend
lista_varias.extend([3, 4, 5,])
print(lista_varias)

# Para agregar un elemento en una posicion determinada insert
lista_varias.insert(4, 1)
print(lista_varias)

# pop elimina el ultimo numero
# reverse invierte la lista
# sort ordena la lista de menor a mayor
# l.sort(reverse=True) ordena la lista de mayor a menor
# remove para borrar un objeto 