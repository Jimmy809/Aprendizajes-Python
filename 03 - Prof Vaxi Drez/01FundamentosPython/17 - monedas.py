import random

class Moneda:
    def __init__(self, raro=False, limpio=True, caras=True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)
            

        self.es_raro = raro
        self.es_limpio = limpio
        self.caras = caras

        if self.es_raro:
            self.valor = self.valor_original * 1.25
        else:
            self.valor = self.valor_original

        if self.es_limpio:
            self.color = self.color_limpio
        else:
            self.color = self.color_oxidado

    def __del__(self):
        print("Moneda Gastada")

    def oxido(self):
        self.color = self.color_oxidado

    def limpiar(self):
        self.color = self.color_limpio

    def vueltas(self):
        caras_opciones = [True, False]
        eleccion = random.choice(caras_opciones)
        self.caras = eleccion

    def __str__(self):
        if self.valor_original >= 1:
            return "Moneda {} Libra".format(int(self.valor_original))
        else:
            return "Moneda {} Penique".format(int(self.valor_original * 100))

class Un_Penique(Moneda):
    def __init__(self):
        data = {
            "valor_original": 0.01,
            "color_limpio": "bronce",
            "color_oxidado": "marron",
            "num_bordes": 1,
            "diametro": 20.3,
            "grosor": 1.52,
            "peso": 3.56
            }
        super().__init__(**data)

class Dos_Penique(Moneda):
    def __init__(self):
        data = {
            "valor_original": 0.02,
            "color_limpio": "bronce",
            "color_oxidado": "marron",
            "num_bordes": 1,
            "diametro": 25.9,
            "grosor": 1.85,
            "peso": 7.12
            }
        super().__init__(**data)

class Cinco_Penique(Moneda):
    def __init__(self):
        data = {
            "valor_original": 0.05,
            "color_limpio": "plata",
            "color_oxidado": None,
            "num_bordes": 1,
            "diametro": 18.0,
            "grosor": 1.77,
            "peso": 3.25
            }
        super().__init__(**data)

    def oxido(self):
        self.color = self.color_limpio

        

class Libra(Moneda):
    def __init__(self):
        data = {
            "valor_original": 1.00,
            "color_limpio": "dorado",
            "color_oxidado": "verdoso",
            "num_bordes": 1,
            "diametro": 22.5,
            "grosor": 3.15,
            "peso": 9.5
            }
        super().__init__(**data)

monedas = [Libra(), Un_Penique(), Dos_Penique(), Cinco_Penique()]

for moneda in monedas:
    argumentos = [moneda, moneda.color, moneda.valor, moneda.diametro,
                  moneda.grosor, moneda.num_bordes, moneda.peso]

    cadena = "{} - Color: {}, Valor: {}, diametro(mm): {}, grosor(mm): {}, bordes: {}, peso: {}".format(*argumentos)
    print(cadena)    

    
        
