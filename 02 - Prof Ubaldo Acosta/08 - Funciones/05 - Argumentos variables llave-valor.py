# https://ellibrodepython.com/args-kwargs-python
# para recibir un diccionario en una variable de una funcion
#  utilizaremos doble * (**) mas la variable

def listaTerminos(**terminos):
    for llave, valor in terminos.items(): # como es un diccionario iteramos la llave y el valor en la variable de terminos.itemas para entrar en cada uno
        print(f'{llave}: {valor}')
        
listaTerminos(IDE='Integrated Developement Environment', PK='Primary Key') # aqui hemos agregado dos terminos al diccionario
listaTerminos(DBMS='Database Management System') # aqui agregamos 1 mas

# IDE: Integrated Developement Environment
# PK: Primary Key
# DBMS: Database Management System