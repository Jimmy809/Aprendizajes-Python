# Clases y Objetos

# class miprimeraclase:
#     # __init__, es llamado al crear el objeto. El uso de __init__ y el doble __ no es una coincidencia. 
#     # Cuando veas un método con esa forma, significa que está reservado para un uso especial del lenguaje. 
#     # En este caso sería lo que se conoce como constructor. Hay gente que llama a estos métodos mágicos.
    
#     # self, Es una variable que representa la instancia de la clase, y deberá estar siempre ahí.
#     def __init__(self): 
#         print('Hola')
        
#     # metodos    
#     def mensaje(self):
#         print('buenas tardes')
#     def mensaje1(self):
#         print('adios')
        
# # siempre llamara a la funcion que tenga el init primero
# # mensaje = miprimeraclase()

# # para llamar los demas metodos
# mensaje = miprimeraclase()
# mensaje.mensaje()
# mensaje.mensaje1()

class clase2:
    def __init__(self, numero):
        self.numero = numero
    def comparar(self):
        if self.numero > 0:
            print('El numero es positivo')
        elif self.numero < 0:
            print('El numero es negativo')
        else:
            print('El numero es cero')   
            
    # para imprimir numero menor a 10 y luego listar el numero hasta el 10 
    def ciclo(self):
        while self.numero <= 10:
            print(self.numero)
            self.numero += 1
            
# ejemplo = clase2(-12)
# ejemplo.comparar()
# ejemplo.ciclo()

# pedir un numero y utilizar comparar
# ejemplo = clase2(int(input('Dame un numero: ')))
# ejemplo.comparar()

# para hacer un ciclo
ejemplo = clase2(int(input('Dame un numero: ')))
ejemplo.ciclo()
