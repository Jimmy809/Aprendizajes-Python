class MiClase:
    # variable de clase, son las que estan fuera de algun medo en una clase como init
    variable_clase = 'Valor variable clase'
    
    # variables de instancia son las variabes que reciben el parametro de self dentro de los metodos
    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia
        
# los metodo estaticos no pueden acceder a las variables de instancia
# por q necesitan un variable q ya este definida, como la variablo de clase
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

# accedemos a la variable de clase desde el metodo estatico
MiClase.metodo_estatico()