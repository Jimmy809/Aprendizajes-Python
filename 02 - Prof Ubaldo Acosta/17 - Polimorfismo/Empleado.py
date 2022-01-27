class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'
    
    def mostrar_detalles(self): # esto se puede llamar en todas las clases hijas sin necesidas de poner el codigo en esas clases
        return self.__str__()