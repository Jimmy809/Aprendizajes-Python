# clase cubo
# ancho alto y profundicada
# calcular volumen (ancho x alto x profundo)

class cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
        
    def calcular_volumen(self):
        return self.alto * self.ancho * self.profundo
    
ancho = int(input('Proporciona el ancho: '))
alto = int(input('Proporciona el alto: '))
prfundo = int(input('Proporciona lo profundo: '))
volumen1 = cubo(ancho, alto, prfundo)

print(f'Volumen cubo: {volumen1.calcular_volumen()}')