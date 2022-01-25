# Set
# Los sets en Python son una estructura de datos usada para almacenar elementos de una manera similar a las listas, pero con ciertas diferencias.
# no mantienen un orden  
# no podemos modificar sus elementos
# no permite almacenar objetos duplicados
# pero si es posibles agregar i eliminar objetos

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
# {'Martes', 'Venus', 'Jupiter'} se imprimen de forma aleatoria

# para conocer cuanto objetos
print(len(planetas))
# 3

# para revisar si un elemento esta presente
print('Marte' in planetas) # aqui podemos preguntar de esta dentro del set con in
# True

# para agregar un nuevo objeto
planetas.add('Tierra')
print(planetas)
# {'Marte', 'Jupiter', 'Tierra', 'Venus'} de forma aleatoria

# si intentamos agregar el mismo elemento no es posible se mantiene igual

#para eliminar un objeto
planetas.remove('Tierra')
print(planetas)
# {'Jupiter', 'Venus', 'Marte'} de forma aleatoria

# para ejecutar un comando y el comando no es valido pero no queremos que marque un error en consola
planetas.discard('Jupiter8989') # como el nombre no existe en el set con discar no presentara errores

# para eliminar todo el contenido o limpiarlo
planetas.clear()
print(planetas)

# para eliminar un set
# del planetas
# print(planetas)