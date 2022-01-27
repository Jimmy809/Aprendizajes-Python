from NumerosIdenticosException import NumeroIdenticosException
resultado = None
try:
    a = int(input('primer numero: '))
    b = int(input('segundo numero: '))
    if a == b: # compararemos si son iguales
        raise NumeroIdenticosException ('numero identicos') # con raise agregamos nuestra esception a codigo
    resultado = a/b
except ZeroDivisionError as e: 
    print(f'Ocurrio un error ZeroDivisionError: {e}, {type(e)}') 
except TypeError as e:         
    print(f'Ocurrio un error TypeError: {e}, {type(e)}')
except Exception as e:
    print(f'Ocurrio un error Exception: {e}, {type(e)}')
else:
    print('No se arrojo ninguna exception') 
finally:
    print('Ejecucion del bloque finally') 

print(f'Resultado: {resultado}')  
print('Continuamos..')

# primer numero: 10
# segundo numero: 10
# Ocurrio un error Exception: numero identicos, <class 'NumerosIdenticosException.NumeroIdenticosException'>
# Ejecucion del bloque finally
# Resultado: None
# Continuamos..