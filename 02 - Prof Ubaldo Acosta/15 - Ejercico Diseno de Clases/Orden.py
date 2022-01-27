from DisenoClases import *

class Orden:
    contador_ordenes = 0
    
    @classmethod
    def generar_id_order(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, productos):
        self._id_orden = Orden.generar_id_order()
        self._productos = list(productos)
        
    def agregar_producto(self, producto):
        self._productos.append(producto)
        
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
        
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + ''
            
        return f'Orden: {self._id_orden}, \nProductos: {productos_str}'


if __name__ == '__main__':
        producto1 = Producto('Camisa', 100.00)
        producto2 = Producto('Pantalon', 150.00)
        productos1 = [producto1, producto2]
        orden1 = Orden(productos1)
        print(orden1)
        orden2 = Orden(productos1)
        print(orden2)