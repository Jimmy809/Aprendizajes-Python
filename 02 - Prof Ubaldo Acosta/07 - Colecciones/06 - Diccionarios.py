# Diccionario
# Los diccionarios en Python son una estructura de datos que permite almacenar su contenido en forma de llave y valor.
# d1 = {
#   "Nombre": "Sara",
#   "Edad": 27,
#   "Documento": 1003882
# }
# print(d1)
# {'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}

diccionario = {
    'IDE':'Integrated Devolopment Enviroment',
    'OOP':'Objet Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)
# {'IDE': 'Integrated Devolopment Enviroment', 'OOP': 'Objet Oriented Programming', 'DBMS': 'Database Management System'}

# para sabe cuanto objetos tiene un diccionario
print(len(diccionario))
# 3

# para acceder a un elemento (key)
print(diccionario['IDE'])
# Integrated Devolopment Enviroment

# otra forma de recuperar un elemento
print(diccionario.get('OPP'))

# para modificar un elemento
diccionario['IDE'] = 'integrated devolopment enviroment 2'
print(diccionario['IDE'])
# integrated devolopment enviroment 2