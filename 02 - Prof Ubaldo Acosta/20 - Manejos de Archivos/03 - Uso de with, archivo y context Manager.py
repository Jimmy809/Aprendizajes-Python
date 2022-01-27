# de manera automatica cierra y abre el archivo
# with open('prueba.txt', 'r', encoding='utf8') as archivo:
#     print(archivo.read())

from ManejoArchivo import *
# con with usamos nuestra clase ManejoArchivo y se le aplica los comando que hemos creado en la clase
with ManejoArchivo('prueba.txt') as archivo:
    print(archivo.read())