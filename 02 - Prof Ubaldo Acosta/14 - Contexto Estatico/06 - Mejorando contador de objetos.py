class Persona:
    contador_personas = 0 # el contador lo inicializamos en 0
    
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        # Persona.contador_personas +=1 # con el metodo de clase ya no necesitamos agregar este codigo al metodo init
        self.id_persona = Persona.generar_siguiente_valor() # sino la clase metodo
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'Persona [{self.id_persona} - {self.nombre} {self.edad}]'
    
persona1 = Persona('Juan', 28)
print(persona1)

persona2 = Persona('Karla', 30)
print(persona2)

persona3 = Persona('Eduaro', 25)
print(persona3)

# ahora para aumentar el numero del contador sin necesidad de agregar un objeto 
Persona.generar_siguiente_valor()
# 4

persona4 = Persona('Maria', 35)
print(persona4)
#5

# para saber cuantas pesonas tiene nuestro contador
print(f'Valor contador personas: {Persona.contador_personas}')