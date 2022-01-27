class MiClase:
    # variable de clase, son las que estan fuera de algun medo en una clase como init
    variable_clase = 'Valor variable clase'
    
    # variables de instancia son las variabes que reciben el parametro de self dentro de los metodos
    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia
    
print(MiClase.variable_clase)

# creamos un objeto
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)

# como vemos tambien es posible llamar la variable clase desde el objeto
print(miClase.variable_clase)

# un segundo objeto para llamar la variable de intancia, y tambien es posible
miClase2 = MiClase('Otro objeo de variable de intancia')
print(miClase2.variable_instancia)

# llamando la variable clase desde un segundo objeto
print(miClase2.variable_clase)


# para asociar una nueva variable de clase a MiClase, al vuelo
MiClase.variable_clase2 = 'Valor variable de clase 2'
# para acceder ha ella desde la clase principal
print(MiClase.variable_clase2)
# para acceder a ella desde un objeto
print(miClase2.variable_clase2)