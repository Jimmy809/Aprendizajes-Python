from Empleado import *
from Gerente import Gerente


# desde aqui podemos mandar a llamar el str de las clases
def imprimir_detalles(objeto): # objeto sera la variable q se ba a definir como empleado o gerente
    # print(objeto)
    print(type(objeto))    
    print(objeto.mostrar_detalles())
    
    # como departamento esta solo en la clase hija de gerente, le pedimos q solo entre en departamente si se llama de la clase getente
    # y asi no da el error de que departamento no esta en la clase padre
    if isinstance(objeto, Gerente): 
        print(objeto.departamento)
    
empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)