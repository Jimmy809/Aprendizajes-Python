# podemos mandarle un valor a: a y b por default
# si queremos que sean valores enteros, los datos enteros y los datos de regreso, pero es opcional
def sumar (a:int = 0, b:int = 0) -> int: 
    return a + b
resultado = sumar()
print(f'Resultado de la suma: {resultado}')
# 0

resultado = sumar(5, 3) # aqui podemos sobreescribir los valores
print(f'Resultado de la suma: {resultado}')
# 8