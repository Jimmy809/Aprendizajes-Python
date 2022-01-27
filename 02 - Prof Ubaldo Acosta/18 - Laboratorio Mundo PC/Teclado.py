from DispositivoEntrada import *

class Teclado:
    contadorTeclado = 0

    @classmethod
    def idTeclado(cls):
        cls.contadorTeclado += 1
        return cls.contadorTeclado
    
    def __init__(self, marca, tipo_entrada):
        self._idTeclado = Teclado.idTeclado()
        self._marca = marca
        self._tipo_entrada = tipo_entrada
        
        
    def __str__(self):             
        return f'ID: {self._idTeclado}, marca: {self._marca}, tipo_entrada: {self._tipo_entrada}'
        
    
    
if __name__ == '__main__':    
    teclado1 = Teclado('PS/2', 'Asus')    
    # teclado2 = DispositivoEntrada('Inalambrico', 'Samsung')
    # teclados1 = [teclado1]
    # orden1 = Teclado(teclados1)
    print(teclado1)