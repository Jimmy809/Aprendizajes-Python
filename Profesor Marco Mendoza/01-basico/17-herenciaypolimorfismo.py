# herencia y Polimorfismo

class padre:
    def __init__(self, numero):
        self.numero = numero 
        
        
    def mensaje1(self):
        print('hola buenos dias')
        
    def mensaje2(self):
        print('hola buenas tardes')
        
    def mensaje3(self):
        print('hola buenas noches')
        
        
class  hijo(padre):
    def __init__(self, numero):
        super().__init__(numero) # utilizaremos super para acceder a los metodos de la clase padre desde una clase hija
        
    def mensaje4(self):
        print('como has estado')
        print(self.numero + 10)
        
    def mensaje5(self):
        print('como va la vida')
    def mensaje6(self):
        print('hasta otra oportunidad')
        
# podemos llamar todas las funciones desde la clase hijo ya q lo indicamos aqui :(class  hijo(padre) )
ejemplo = hijo(10)
ejemplo.mensaje1()
ejemplo.mensaje2()
ejemplo.mensaje3()
ejemplo.mensaje4()
ejemplo.mensaje5()
ejemplo.mensaje6()