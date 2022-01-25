def factorial(numero):
    if numero == 1: # aqui lo que indicamos que si numero llega a 1 q retorne 1 y se para la funcion ya q 1 es el ultimo numero a multiplicar
        return 1
    else:
        return numero * factorial(numero-1) # aqui se ira disminuyando el valor de numero -1
numero = 5
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')
# El factorial de 5 es 120