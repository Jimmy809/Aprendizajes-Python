# para definir un diccionario lo hacemos con llaves {} deben tener ej, 'nombre': 'Sara'


diccionario = {
    'Nombre': 'Jimmy',
    'Apellido': 'Reyes',
}
print(diccionario)

# para saber cuantos objetos tiene un diccionario
print(len(diccionario))

#para acceder a un objeto
print(diccionario.get('Nombre'))
print(diccionario['Nombre'])

# para modificar un diccionario
diccionario['Nombre'] = 'Jared'
print(diccionario)

# con los diccionaarios podemos anidar dentro otros diccionarios u otras listas
anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print(d)
#{'anidado1': {'a': 1, 'b': 2}, 'anidado2': {'a': 1, 'b': 2}}

#clear elimina todo el contenido del diccionario

#El método get() nos permite consultar el value para un key determinado. 
#El segundo parámetro es opcional, y en el caso de proporcionarlo es el valor a devolver si no se encuentra la key

#El método items() devuelve una lista con los keys y values del diccionario. 
#Si se convierte en list se puede indexar como si de una lista normal se tratase, siendo los primeros elementos las key y los segundos los value

#El método keys() devuelve una lista con todas las keys del diccionario.

#El método values() devuelve una lista con todos los values o valores del diccionario.

#El método pop() busca y elimina la key que se pasa como parámetro y devuelve su valor asociado. 
# Daría un error si se intenta eliminar una key que no existe.

#El método popitem() elimina de manera aleatoria un elemento del diccionario.

# El método update() se llama sobre un diccionario y tiene como entrada otro diccionario. 
# Los value son actualizados y si alguna key del nuevo diccionario no esta, es añadida.