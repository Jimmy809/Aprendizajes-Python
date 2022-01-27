resultado = None
try:
    a = int(input('primer numero: '))
    b = int(input('segundo numero: '))
    resultado = a/b
except ZeroDivisionError as e: 
    print(f'Ocurrio un error ZeroDivisionError: {e}, {type(e)}') 
except TypeError as e:         
    print(f'Ocurrio un error TypeError: {e}, {type(e)}')
except Exception as e:
    print(f'Ocurrio un error Exception: {e}, {type(e)}')
else:
    print('No se arrojo ninguna exception') # esto solo aparecera si ocurre un error
finally:
    print('Ejecucion del bloque finally') # este bloque siempre se ejecuta

print(f'Resultado: {resultado}')  
print('Continuamos..')