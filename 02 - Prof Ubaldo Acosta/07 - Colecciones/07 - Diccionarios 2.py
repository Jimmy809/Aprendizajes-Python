diccionario = {
    'IDE':'Integrated Devolopment Enviroment',
    'OOP':'Objet Oriented Programming',
    'DBMS':'Database Management System'
}

# para recorrer los elementos pero solo los keys sin el valor

for termino in diccionario: # otro metodo tambien es agregarle .keys() a diccionario
    print(termino)
# IDE
# OOP
# DBMS

# para obtener solamento los valores
for valor in diccionario.values():
    print(valor)
# Integrated Devolopment Enviroment
# Objet Oriented Programming
# Database Management System

for termino, valor in diccionario.items(): # necetiamos agregar el valor mas .items al diccionario
    print(termino, valor)
# IDE Integrated Devolopment Enviroment
# OOP Objet Oriented Programming
# DBMS Database Management System

# comprobar existencia
print('IDE' in diccionario) #debemos respetar minusculas y mayusculas
# True

# para agregar elementos
diccionario['PK'] = 'Primary Key'
print(diccionario)
# {'IDE': 'Integrated Devolopment Enviroment', 'OOP': 'Objet Oriented Programming', 'DBMS': 'Database Management System', 'PK': 'Primary Key'}  

#para eliminar un elemento
diccionario.pop('DBMS')
print(diccionario)
# {'IDE': 'Integrated Devolopment Enviroment', 'OOP': 'Objet Oriented Programming', 'PK': 'Primary Key'}

# para limpiar o vaciar un diccionario
diccionario.clear()
print(diccionario)
# {}

# para eliminar un diccionario
# del diccionario
# print(diccionario)
# error no existe