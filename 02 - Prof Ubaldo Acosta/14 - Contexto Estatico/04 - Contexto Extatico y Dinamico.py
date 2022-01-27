class MiClase:
    
    variable_clase = 'Valor variable clase'
    
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
        
# los metodos de clase necesitan tener el cls que es algo parecido al self de las variables
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase) # usamos cls para llamar la variable
        
    
    def metodo_instancia (self): # con los metodos de instancia, podemos acceder a los metodos de clase y al metodo estatico
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase) # tambien a las variables de clase y de instancia
        print(self.variable_instancia)
        


MiClase.metodo_clase() # el cls se llama autamaticamente

miObjeto1= MiClase('variable_instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()