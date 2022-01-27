class Persona:
    contador_personas = 0 # el contador lo inicializamos en 0

    def __init__(self, nombre, edad):
        Persona.contador_personas +=1 # por cada persona agregada sumaremos 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'Persona [{self.id_persona} - {self.nombre} {self.edad}]'
    
persona1 = Persona('Juan', 28)
print(persona1)

persona2 = Persona('Karla', 30)
print(persona2)

# para saber cuantas pesonas tiene nuestro contador
print(f'Valor contador personas: {Persona.contador_personas}')