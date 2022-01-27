# obj1 + obj2
# obj.__add__(pbj2)

# add o +
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'
    
# sub o -
    def __sub__(self, otro):
        return self.edad - otro.edad
    
persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 20)
print(persona1 + persona2)
print(persona1 - persona2)