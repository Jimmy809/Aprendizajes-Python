from Monitor import *
from Raton import *
from Teclado import *
from Computadora import *
# from Orden import *

class Orden:
    contador_ordenes = 0
    def __init__(self, computadoras):
        Orden.contador_ordenes+= 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = computadoras


    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)
    

    def __str__(self):
        computadoras_str = ''
        for i in self._computadoras:
            computadoras_str += i.__str__()
            
        return f'''
        Orden: {self._id_orden}
        Computadoras: {computadoras_str}
        '''
        
if __name__ == '__main__':           
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
    print(orden1)