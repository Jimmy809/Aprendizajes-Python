# crear una clase rectangulo
# 2 atributos altura y base
# metodo calcular Area, formula es A=bxh  (base x altura)
# altura y base debe ser proporcionado por el usuario

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def Area(self):
        return self.base * self.altura
    
base = int(input(f'proporciona la base: '))
altura = int(input(f'proporciona la altura: '))

resultado = Rectangulo(base, altura)
print(f'Area rectangulo: {resultado.Area()}')