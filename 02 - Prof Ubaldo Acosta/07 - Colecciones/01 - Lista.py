# Listas en Python
# Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. 
# Son mutables y dinámicas, lo cual es la principal diferencia con los sets y las tuplas.
# Crear listas Python
# Las listas en Python son uno de los tipos o estructuras de datos más versátiles del lenguaje, 
# ya que permiten almacenar un conjunto arbitrario de datos. Es decir, podemos guardar en ellas prácticamente lo que sea. 
# Si vienes de otros lenguajes de programación, se podría decir que son similares a los arrays.
# lista = [1, 2, 3, 4]


# Definimos una lista con []
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']

# para imprimir igual con print
print(nombres)

# para acceder a los elementos de una lista
print(nombres[0])
# Juan

print(nombres[1])
# Karla

# para acceder de forma inversa
print(nombres[-1])
# Maria

print(nombres[-2])
# Ricardo

# para imprimir un rango de indices de una lista
print(nombres[0:2]) # sin incluir el 2
# ['Juan', 'Karla']

# Ir del inicio de la lista hasta un indice sin incluirlo este ultimo
print(nombres[:3])
# ['Juan', 'Karla', 'Ricardo'] el indice 3 Maria no se imprime

# Desde el indice indicado hasta el final
print(nombres[1:])
# ['Karla', 'Ricardo', 'Maria']

#cambiar un valor en la lista
nombres[3] = 'Ivone' # aqui estamos remplazando el indice 3 que es maria, por ivone
print(nombres)
# ['Juan', 'Karla', 'Ricardo', 'Ivone']