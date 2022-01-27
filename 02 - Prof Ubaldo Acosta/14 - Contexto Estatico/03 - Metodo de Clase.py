class MiClase:
    
    variable_clase = 'Valor variable clase'
    
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
# los metodos de clase necesitan tener el cls que es algo parecido al self de las variables
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase) # usamos cls para llamar la variable


MiClase.metodo_clase() # el cls se llama autamaticamente

miObjeto1= MiClase('variable_instancia')
miObjeto1.metodo_clase()