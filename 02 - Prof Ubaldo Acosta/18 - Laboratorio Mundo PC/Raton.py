from DispositivoEntrada import *

class Raton:
    contadorRaton = 0

    @classmethod
    def idRaton(cls):
        cls.contadorRaton += 1
        return cls.contadorRaton
    
    def __init__(self, marca, tipo_entrada):
        self._idRaton = Raton.idRaton()
        self._marca = marca
        self._tipo_entrada = tipo_entrada
        
        
    def __str__(self):
        return f'ID: {self._idRaton}, marca: {self._marca}, tipo_entrada: {self._tipo_entrada}'
    
    
    
if __name__ == '__main__':    
    raton1 = Raton('HP', 'USB')    
    # raton2 = Raton('Bluetooh', 'Logitech')
    
    print(raton1)
    
        # producto1 = Producto('Camisa', 100.00)
        # producto2 = Producto('Pantalon', 150.00)
        # productos1 = [producto1, producto2]
        # orden1 = Orden(productos1)
        # print(orden1)
        # orden2 = Orden(productos1)
        # print(orden2)