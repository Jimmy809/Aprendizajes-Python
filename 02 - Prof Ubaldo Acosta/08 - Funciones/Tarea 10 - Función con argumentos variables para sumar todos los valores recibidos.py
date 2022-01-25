# Crear una función para sumar los valores recibidos de tipo numérico, 
# utilizando argumentos variables *args como parámetro de la función 
# y regresar como resultado la suma de todos los valores pasados como argumentos.

def sumar(*args):
    n = 0
    for i in args:    
        n += i
        print(n)
sumar(2, 3, 6, 9,)
# 2
# 5
# 11
# 20