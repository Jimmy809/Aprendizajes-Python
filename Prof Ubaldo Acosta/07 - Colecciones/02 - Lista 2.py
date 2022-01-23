# Definimos una lista con []
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']

# para iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')
# Juan
# Karla
# Ricardo
# Maria
# No existen mas nombres en la lista

# para preguntar el largo de una lista
print(len(nombres))
# 4

# Paa agregar elementos a una lista
nombres.append('Lorenzo')
print(nombres)
# ['Juan', 'Karla', 'Ricardo', 'Maria', 'Lorenzo']

# insertar un elemento en un indice o lugar especifico
nombres.insert(1, 'Octavio')
print(nombres)
# ['Juan', 'Octavio', 'Karla', 'Ricardo', 'Maria', 'Lorenzo']

# para eliminar un elemento especifico de una lista
nombres.remove('Octavio')
print(nombres)
# ['Juan', 'Karla', 'Ricardo', 'Maria', 'Lorenzo'

# para eliminar el ultimo elemento de una lista
nombres.pop()
print(nombres)
# ['Juan', 'Karla', 'Ricardo', 'Maria']

# para eliminar una lista completa
# del nombres
# print(nombres)
# error lista no existe