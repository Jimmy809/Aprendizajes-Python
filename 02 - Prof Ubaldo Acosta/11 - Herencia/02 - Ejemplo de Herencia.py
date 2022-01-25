# object es la clase padre de todas las clases en python
# la clase padre hereda de la clase object (no necesitamos especificarlo obligatoriamente)
class Persona(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# la clase hija hereda de la clase padre que es Persona (no debemos especificarlo obligatoriamente)
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo): # 2 tambien agregamos los metodos aqui
        
        # 1 con super lo que hacemos es llamar a los metodos de la clase padre com a nombre y edad
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
empleado1 = Empleado('Juan', 28, 5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)