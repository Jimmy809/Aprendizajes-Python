# para que la variable se solo sea de tipo lectura, o saber por q no se puede modificar

class Persona:
    def __init__(self, nombre, apellido, edad): 
        self._nombre = nombre         
        self.apellido = apellido
        self.edad = edad


    @property 
    def nombre(self):
        print('Llamando al metodo get nombre')
       
        return self._nombre 
    
    # si no tenemos el decorador de set o setter, no podremos modificar el artributos, de forma correcta o profecion ya que necesitariamos editar el atributo _nombre con guion bajo 
    # y no es correcto hacerlo directamente, si hacemos esto nos vemos como que desconocemos e lenguaje python
    # @nombre.setter 
    # def nombre(self, nombre): 
    #     print('Llamando al metodo set nombre')
    #     self._nombre = nombre
        
      
    def mostrar_detalle(self): 
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')


persona1 = Persona('Juan', 'Perez', 28) 

persona1.nombre = 'Juan Carlos' # ya no podremos usar esta sintaxis para modificar el atributo
print(persona1.nombre)