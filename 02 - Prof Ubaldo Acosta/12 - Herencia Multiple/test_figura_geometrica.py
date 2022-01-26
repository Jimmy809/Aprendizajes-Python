# dentro de cuadrado estan las clases figura geometrica y color, entonces hacemos una herencia multiple 
from Cuadrado import *

cuadrado1 = Cuadrado(5, 'rojo')
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
# print(cuadrado1.color)
print(f'Calculo del area de un cuadrado: {cuadrado1.calcular_area()}')

# MRO - Method Resolution Order, nos dira a cuales clases ira llamando
# print(Cuadrado.mro())