# el metodo __str__ lo usarmos en el modulo a importar en este caso Persona.py
# # con str lo que permitimos es definir los valor de una clase padre un una clase hija
#     def __str__(self):
#         return f'persona: {self.nombre} {self.edad}'

# str es quien tiene definito el text que se va a imprimir cuando se llame la calse


from Persona import *

persona1 = Persona('Juan', 28)
print(persona1)

empleado1 = Empleado('Karla', 30, 5000)
print(empleado1)