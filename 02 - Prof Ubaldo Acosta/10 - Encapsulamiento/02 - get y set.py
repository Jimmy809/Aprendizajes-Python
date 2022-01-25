# get y set
# get nos permitira obtener/recuperar los atributos de nuestra clase
# set nos permitira colocar/modificar los atributos de nuestra clase

class Persona:
    def __init__(self, nombre, apellido, edad): 
        self._nombre = nombre         
        self.apellido = apellido
        self.edad = edad

# con esto nos aseguramos q en la funcion __init__ se encapsule la variable y solo podamor accer atravez de este metodo llamado nombre (@property es un decorador para esto)
# con property vamos acceder de manera indirecta recuperamos el valor del atributo nombre
    @property 
    def nombre(self):
        print('Llamando al metodo get nombre')
        # 3 en el return llamamos de manera indirecta a la clase init el articulo de nombre
        return self._nombre # 1 con esto podemos llamar la variable de nombre de manera sola, con la funcion de nombre
    
    
    @nombre.setter # 4 con setter asociamos a nombre, no necesitamos colocar el guion,
    def nombre(self, nombre): # 4 aqui necesitamos el atributo para poder modificarlo
        print('Llamando al metodo set nombre')
        self._nombre = nombre
        
      
    def mostrar_detalle(self): 
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')


persona1 = Persona('Juan', 'Perez', 28) 
# 1 con esto podemos llamar la variable de nombre de manera sola, con la funcion de nombre, pero al tener arriba _ guion bajo es recomendable no hacerlo, con property ya no podemos llamarlo
# print(persona1.nombre()) 

# 2 tambien podemos acceder con el guion bajo de esta manera
# print(persona1._nombre) 

# print(persona1.nombre) # 3 de manera indirecta llamamos al metodo de la funcion nombre, con @poperty no necesitamos poner parentesis despues de nombre

# modificanos para hacer prueba q se esta modificando desde get y set
persona1.nombre = 'Juan Carlos' # 4 no necesitmos envolverlo en parentesis, ya que lo estamos llamando como un atributo de nuestra clase
print(persona1.nombre)
# persona1._nombre = 'cambio' # si intentamos hacer cambio con _ guion bajo estamos indicando que desconocemos el lenguaje de python
# print(persona1.nombre)
