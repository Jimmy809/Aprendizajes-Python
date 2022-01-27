class Monitor:
    contadorMonitor = 0

    @classmethod
    def idMonitor(cls):
        cls.contadorMonitor += 1
        return cls.contadorMonitor
    
    def __init__(self, marca, tamano):
        self._idMonitor = Monitor.idMonitor()
        self._marca = marca
        self._tamano = tamano
        
        
    @property 
    def tamano(self):
        return self._tamano 
    
    
    @tamano.setter 
    def tamano(self, tamano):         
        self._tamano = tamano
        
        
    @property 
    def marca(self):
        return self._marca 
    
    
    @marca.setter 
    def marca(self, marca):         
        self._marca = marca
        
        
    def __str__(self):            
        return f'ID: {self._idMonitor}, marca: {self._marca}, tamaño: {self._tamano}'
    
    
    
if __name__ == '__main__':
    monitor1 = Monitor('Asus', 37)
    print(monitor1)
    monitor2 = Monitor('Acer', 27)
    # teclado1 = DispositivoEntrada('PS/2', 'Asus')    
    # teclado2 = DispositivoEntrada('Inalambrico', 'Samsung')
    # monitores1 = [teclado1]
    # orden1 = Teclado(monitores1)
    # print(orden1)