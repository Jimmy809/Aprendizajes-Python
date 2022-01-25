# con * importamos todas las clases de un archivo, en este caso de persona
# from Persona import *
from Persona import Persona

print('Creacion objetos'.center(30,'-')) # crear titulos con rayas o caracteres
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()
print('Eliminacion de objetos'.center(30,'-'))
# con esto eliminamos el objeto creado
del persona1 # aqui llamamos al metodo destructor


# hemos agregado el metodo destructor dentro de la clase en el modulo importado
# def __del__(self): # metodo destructor
#         print(f'Persona: {self._nombre} {self.apellido}')


# si hay archivos importados y ejecutandose
# saldran primero y luego saldra main donde empieza este archiovo
# print(__name__)