resultado = None
try:
    a = int(input('primer numero: ')) # si mandamos una letra en vez de un numero
    b = int(input('segundo numero: '))
    resultado = a/b
except ZeroDivisionError as e: 
    print(f'Ocurrio un error ZeroDivisionError: {e}, {type(e)}') 
except TypeError as e:         
    print(f'Ocurrio un error TypeError: {e}, {type(e)}')
except Exception as e:
    print(f'Ocurrio un error Exception: {e}, {type(e)}')

print(f'Resultado: {resultado}')  
print('Continuamos..')

# primer numero: a
# Ocurrio un error Exception: invalid literal for int() with base 10: 'a', <class 'ValueError'> 
# sale exception y el error en especifico, ValueError, por que no esta agregada
# Resultado:None
# Continuamos..