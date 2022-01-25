class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos): #*args para agregar una tupla, **kwargs para diccionarios, los nombres pueden modificarse, estos valores son opcionales
        self.nombre =  nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    
    def mostrar_detalle(self): 
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores}{self.terminos}')


persona1 = Persona('Juan', 'Perez', 28, '5875579', 2, 3, 4, m='manzana', p='peras') 
persona1.mostrar_detalle()
# Persona.mostrar_detalle(persona1)
persona1.telefono = '5578548'
print(persona1.telefono)




persona2 = Persona('karla', 'Gomez', 30) 
persona2.mostrar_detalle()
