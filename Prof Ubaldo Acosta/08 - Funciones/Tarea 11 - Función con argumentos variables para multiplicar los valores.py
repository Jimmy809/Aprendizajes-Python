# Crear una función para multiplicar los valores recibidos de tipo numérico, 
# utilizando argumentos variables *args como parámetro de la función y regresar como resultado la multiplicación de todos los valores 
# pasados como argumentos.

def sumar(*args):
    n = 1
    for i in args:    
        n *= i
        print(n)
sumar(2, 3, 6, 9,)