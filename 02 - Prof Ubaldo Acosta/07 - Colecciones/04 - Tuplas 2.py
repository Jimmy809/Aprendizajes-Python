frutas = ('Naranja', 'Platanos', 'Guayaba')

# iterar con una tupla
for fruta in frutas:
    print(fruta)
# Naranja
# Platanos
# Guayaba

# para mostrar los elementos en una sola linea
for fruta in frutas:
    print(fruta, end=' ') # esto es de la funcion print no de tuplas
# Naranja Platanos Guayaba

# para modificar una tupla tendriamos q convertirla a una lista
frutasLista = list(frutas) # convertimos a lista la tupla
frutasLista[0] = 'Pera' # agregamo el nuevo objeto a la lista
frutas= tuple(frutasLista) # reasignamos a tupla la lista
print('\n', frutas)

# Para eliminar una tupla por completo
# del frutas
# error

# notas: necesitamos una lista y en futuro modificaremos los objetos pues usamos una lista
# si no vamos a modificar los objetos usamos una tupla
