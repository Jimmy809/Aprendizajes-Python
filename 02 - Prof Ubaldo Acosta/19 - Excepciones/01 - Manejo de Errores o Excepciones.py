# Excepciones en Python
# Las excepciones en Python son una herramienta muy potente que la gran mayoría de lenguajes de programación modernos tienen. 
# Se trata de una forma de controlar el comportamiento de un programa cuando se produce un error.
# Esto es muy importante ya que salvo que tratemos este error, el programa se parará, y esto es algo que en determinadas aplicaciones no es una opción válida.
# Imaginemos que tenemos el siguiente código con dos variables a y b y realizamos su división a/b.
# a = 4
# b = 2
# c = a/b

# Pero imaginemos ahora que por cualquier motivo las variables tienen otro valor, y que por ejemplo b tiene el valor 0. 
# Si intentamos hacer la división entre cero, este programa dará un error y su ejecución terminará de manera abrupta.

# a = 4; b = 0
# print(a/b)
# # ZeroDivisionError: division by zero

# para hacer una excepcion a cualquier error, mando el mensaje del error
try:
    10/0
except Exception as e:
    print(f'Ocurrio un error: {e}')
# Ocurrio un error: division by zero

# para especificar un error en concreto
try:
    10/0
except ZeroDivisionError as e: # aqui ponemos el error deseado
    print(f'Ocurrio un error: {e}')
# Ocurrio un error: division by zero

