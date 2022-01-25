# Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, las cuales heredan de la clase Padre Vehiculo.
# La clase padre debe tener los siguientes atributos y métodos
# Vehiculo (Clase Padre):
# -Atributos (color, ruedas)
# -Métodos ( __init__() y __str__ )
# Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
# -Atributos ( velocidad (km/hr) )
# -Métodos ( __init__() y __str__() )
# Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
# -Atributos ( tipo (urbana/montaña/etc )
# -Métodos ( __init__() y __str__() )

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f'Color: {self.color}, Con {self.ruedas} ruedas,'
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return f'Coche de {super().__str__()} Velocidad: {self.velocidad}'
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return f'Bicicleta de {super().__str__()} Tipo: {self.tipo}'

coche1 = Coche('Rojo', 4, '100 km')
print(coche1)
# Coche de Color: Rojo, Con 4 ruedas, Velocidad: 100 km

bici1 = Bicicleta('Azul', 2, 'Urbana')
print(bici1)
# Bicicleta de Color: Azul, Con 2 ruedas, Tipo: Urbana