# dentro de cuadrado estan las clases figura geometrica y color, entonces hacemos una herencia multiple 
from Cuadrado import *
from Rectangulo import *

print('Creacion Objeto Cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color = 'rojo')
cuadrado1.alto = 5
print(f'Calcular el area de un cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=5, alto=9, color='azul')
rectangulo1.ancho = 5
rectangulo1.alto= 8
print(f'Calcular el area de un rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)