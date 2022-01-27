# solo las clases hijas y padres pueden ejecutar algunos error, ver imagen para mas informacion.

# resultado = None
# a = 10
# b = 0
# try:
#     resultado = a/b
# except Exception as e:
#     print(f'Ocurrio un error: {e}')
    
# print(f'Resultado:{resultado}')  
# Ocurrio un error: division by zero
# Resultado:None, el resultado no se altera ya que hubo un error


# resultado = None
# a = '10' # probamos con una cadena
# b = 0
# try:
#     resultado = a/b
# except ZeroDivisionError as e: # con error de division en la excepcion
#     print(f'Ocurrio un error: {e}')
    
# print(f'Resultado:{resultado}')  
# # TypeError: unsupported operand type(s) for /: 'str' and 'int'


resultado = None
a = '10' # probamos con una cadena
b = 0
try:
    resultado = a/b
except Exception as e: # con error de excepcion
    print(f'Ocurrio un error: {e}')
    
print(f'Resultado:{resultado}')  
# Ocurrio un error: unsupported operand type(s) for /: 'str' and 'int'