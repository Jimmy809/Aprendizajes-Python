# Anteriormente hemos usado funciones nativas que vienen con Python como len() para calcular la longitud de una lista, 
# pero al igual que en otros lenguajes de programación, también podemos definir nuestras propias funciones. Para ello hacemos uso de def
# 
# Para definir una funcion usamos def
# normalmente parasepar nombres usaremos _ o escriobir la sengo palabra en mayuscula
# def mi_funcion():
# def miFuncion():

def mi_funcion():
    print('saludo desde Python') # aqui mandamos print, asi que para llamar esta funcion no es necesario usar print
    
mi_funcion() # simplemente la llamos asi
# mi_funcion()
# mi_funcion() la podemos mandar a llamar las veces que quicieramos

def mi_funcion2(nombre, apellido): # aqui agregamos parametros a nuestra funcion (en este caso variables)
    print('saludo desde mi funcion')
    print(f'Nombre: {nombre}, Apellido: {apellido}')
    
mi_funcion2('Juan', 'Perez') # aqui declaramos nuestras variables introducidas en el parametro
mi_funcion2('Karla', 'Lara') # podemos volver a usar la funcion con parametros diferentes