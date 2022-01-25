
# metodo 2, este metodo es el recomendado
class Persona: # esto es como la plantilla que vamos a utilizar para agregarle en diferente momento la carracteristicas de nuestros objetos
    def __init__(self, nombre, apellido, edad): # self es una referencia para llamarse a si misma y llamar sus metodos y atributos
        self.nombre = nombre # no es obligatorio usar el mismo nombre para declar la variable
        self.apellido = apellido
        self.edad = edad
        
# persona1 es una nueva variable
# luego llamamos a la clase Persona
# la referencia self se incluye automaticamente, aqui se manda a llamar al metodo inicializado __init__
persona1 = Persona('Juan', 'Perez', 28) # en este caso debemos pasar los argumentos a la llamada de la clase con la nueva informacion a agregar a esa clase
# metodo 1 de impresion
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
# Juan
# Perez
# 28

# metodo de impresion
persona2 = Persona('Karla', 'Gomez', 30)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
# Objeto Persona 2: Karla Gomez 30


# para modificar un atributo
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Juarez'
persona1.edad = 25
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
# Objeto Persona 1: Juan carlos Juarez 25