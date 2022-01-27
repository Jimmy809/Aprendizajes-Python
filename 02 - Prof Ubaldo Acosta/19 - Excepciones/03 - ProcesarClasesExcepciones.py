# las excepciones tambien van como  las clases deben colocarse las mas especificas primero

resultado = None
a = '10' 
b = 0
try:
    resultado = a/b
except ZeroDivisionError as e: # mandamos la excepcion de divicion
    print(f'Ocurrio un error ZeroDivisionError: {e}, {type(e)}') # con el type podemos mandar a imprimir el tipo de error q a sucedido
except TypeError as e:         # y tambien la typeerror
    print(f'Ocurrio un error TypeError: {e}, {type(e)}')
except Exception as e:
    print(f'Ocurrio un error Exception: {e}, {type(e)}')

print(f'Resultado:{resultado}')  
print('Continuamos..')

# Ocurrio un error TypeError: unsupported operand type(s) for /: 'str' and 'int', <class 'TypeError'>
# Resultado:None
# Continuamos..

# no termina de forma abrupta