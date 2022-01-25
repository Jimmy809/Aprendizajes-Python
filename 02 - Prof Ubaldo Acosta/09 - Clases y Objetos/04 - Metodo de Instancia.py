# self es la palabra this en otros lenguajes como java
# y no necesariamente en python tiene que llamarse self, podemos editarla, siempre sera el primer atributo


class Persona:
    def __init__(self, nombre, edad):
        self.nombre =  nombre
        self.edad = edad
    # metodo 3 de impresion a consola, las recomendada
    def mostrar_detalle(self): # funcion para mostrar o imprimir en consola 
        print(f'Persona: {self.nombre} {self.edad}')

# intancia 1
persona1 = Persona('Juan', 28) # declaramos la variable con los atributos
persona1.mostrar_detalle()
# Persona: Juan 28


# metodo 4 de imprecion a consola no es muy comun
Persona.mostrar_detalle(persona1)
# Persona: Juan 28

# agregando un nuevo atributo a el objeto persona1 en particular, persona2 no podra acceder a este atributo
persona1.telefono = '5578548'
print(persona1.telefono)
# 5578548


#instancia 2
persona2 = Persona('karla', 30) # declaramos otra variable con otros atributos
persona2.mostrar_detalle()
# Persona: karla 30