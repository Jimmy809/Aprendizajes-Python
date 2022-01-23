# una tupla es muy parecido a una lista, con la diferencia que los valores no pueden ser modificados, inmutables
# tupla = (1, 2, 3)
# print(tupla) #(1, 2, 3)
# si en una tupla solo tenemos un valor debemos poner la coma, en caso q tengamos mas valores no es necesario

# Para definir una tupla usaremos ()
frutas = ('Naranja', 'Platanos', 'Guayaba')
print(frutas)
# ('Naranja', 'Platanos', 'Guayaba')

# Para saber cuantos objetos tiene una tupla
print(len(frutas))
# 3

# para acceder a un elemento
print(frutas[0])
# Naranja

# para acceder de forma inversa
print(frutas[-1])
# Guayaba

# acceder a un rango de valores
print(frutas[0:2])
# ('Naranja', 'Platanos')