# class Persona: # definimos la clase
#     pass # pass por si queremos continuar programando otras cosas y luego continuar con la clase o funciones (crear clase o funcion sin ningun contenido)

# metodo1 codigo en codigo duro, no es normal pero es posible

class Persona:
    def __init__(self): # self es una referencia para llamarse a si misma y llamar sus metodos y atributos
        self.nombre = 'Juan' # no es normal hacerlo de esta manera, pero para mostrar q si es posible
        self.apellido = 'Perez'
        self.edad = 28
        
# persona1 es una nueva variable
# luego llamamos a la clase Persona
persona1 = Persona() # la referencia self se incluye automaticamente, aqui se manda a llamar al metodo inicializado __init__
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
    