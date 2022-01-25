# Encapsulamiento en programación
# El encapsulamiento o encapsulación en programación es un concepto relacionado con la programación orientada a objetos, 
# y hace referencia al ocultamiento de los estado internos de una clase al exterior. Dicho de otra manera, 
# encapsular consiste en hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desde fuera, 
# sino que tan solo el propio objeto pueda acceder a ellos.

class Persona:
    def __init__(self, nombre, apellido, edad): 
        # self.nombre =  nombre  # 1 esto es una variable publica que pe suede acceder por separado.(no es lo recomendado) ya que estamos fuera de las talulacion de la clase
        self._nombre =  nombre # 2 _nombre agregamos esto para encapsular el metodo y no se pueda acceder a a esta en el modo produccion de nuestro codigo, solo en el mode de prueba
        # self.__nombre = nombre   # 3 con los doble __ sera imposible aceder desde fuera
        self.apellido = apellido
        self.edad = edad
    
    def mostrar_detalle(self): 
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Juan', 'Perez', 28, '5875579') 
# persona1.nombre = 'Juan Carlos' # 1 esto es una variable publica que pe suede acceder por separado.(no es lo recomendado) ya que estamos fuera de las talulacion de la clase

# 2 _nombre agregamos esto para encapsular el metodo ya q no es recomendable en el modo produccion de nuestro codigo, pero aun asi se puede modificar, es como una recomendacion
# pero es la mas recomendable
persona1._nombre = 'Juan Carlos' 

# 3 con los doble __ sera imposible aceder desde fuera
# persona1.__nombre = 'Juan Carlos'


persona1.mostrar_detalle()