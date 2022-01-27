from Monitor import *
from Raton import *
from Teclado import *
from Computadora import *
from Orden import *

    
    
    
    
    

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 15)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)
# print(computadora1)

teclado2 = Teclado('Acer', 'Bluetooth')
raton2 = Raton('Acer', 'USB')
monitor2 = Monitor('Acer', 15)
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
# print(computadora2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
# print(orden1)

teclado3 = Teclado('Asus', 'Bluetooth')
raton3 = Raton('Asus', 'USB')
monitor3 = Monitor('Asus', 15)
computadora3 = Computadora('Asus', monitor3, teclado3, raton3)

orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)