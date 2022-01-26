# dentro de cuadrado estan las clases figura geometrica y color, entonces hacemos una herencia multiple 
from Cuadrado import *
from Rectangulo import *

# figura = FiguraGeometrica() aqui intentamos llamar la case con el metodo abstrato definido y eso nos muestra q no se puede llamar, ya que eso es lo que hace, ocultar la clase

print('Creacion Objeto Cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color = 'rojo')

# queremos que no se puedan declarar variable despues que ya se hallan inicializado debeomos quitar los metodo set de las clases
# cuadrado1.alto = 5
print(f'Calcular el area de un cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=5, alto=9, color='azul')
# rectangulo1.ancho = 5
# rectangulo1.alto= 8
print(f'Calcular el area de un rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)


# para saber la secuencia de clases que recorre
print(Cuadrado.mro())