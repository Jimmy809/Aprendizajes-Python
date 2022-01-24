# El uso de la sentencia return permite realizar dos cosas:

# Salir de la función y transferir la ejecución de vuelta a donde se realizó la llamada.
# Devolver uno o varios parámetros, fruto de la ejecución de la función.
# En lo relativo a lo primero, una vez se llama a return se para la ejecución de la función y se vuelve o retorna al punto donde fue llamada
# Es por ello por lo que el código que va después del return no es ejecutado en el siguiente ejemplo.
# def mi_funcion():
#     print("Entra en mi_funcion")
#     return
#     print("No llega")
# mi_funcion() # Entra en mi_funcion

def sumar (a, b):
    return a + b
resultado = sumar(5, 3)
print(f'Resultado de la suma: {resultado}') # tambien podrimas llamar la funcion sin la variable resultado:  
                                            # print(f'Resultado de la suma es : {sumar(5, 3)}')