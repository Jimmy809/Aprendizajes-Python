class ManejoArchivo:
    def __init__(self, nombre): # nombre hace referencia al archivo que vamos a llamar
        self.nombre = nombre
    
    def __enter__(self): # con enter abrimos el archivo
        print('Obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8') # aqui leemos el recurso
        return self.nombre
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error): # aqui cellramos el archivo
        print('Cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close() # confirmamos que este cerrado