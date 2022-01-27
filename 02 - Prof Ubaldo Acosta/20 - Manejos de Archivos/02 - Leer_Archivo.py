# ‘r’: Por defecto, para leer el fichero.
# ‘w’: Para escribir en el fichero.
# ‘x’: Para la creación, fallando si ya existe.
# ‘a’: Para añadir contenido a un fichero existente.
# ‘b’: Para abrir en modo binario.
# para buscar la direccion de un archivo en windows usaremos \\ doble atra y en mac / una hacia dellante

archivo = open ('prueba.txt', 'r', encoding='utf8')
# print(archivo.read()) # para leer todo el documento

# print(archivo.read(5)) # si ponemos 5 solo leera los 5 primero caracteres

# print(archivo.readline()) # leera la primera linea
# print(archivo.readline()) # seguira en la segunda

# for linea in archivo: # con esto podemos mandar a imprimir cada una de las lineas
#     print(linea)
    
# print(archivo.readlines()) # nos regesa una lista, cada linea sera el valor en una lista
# print(archivo.readlines()[0]) # nos regresara unicamente la primera linea

# para copiar un archivo
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('se ha terminado el proceso de leer y copiar archivo')