# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
# Función 1. Recibir un parámetro llamado celcius y regresar el valor equivalente a fahrenheit
# La función se llama: celsius_fahrenheit(celsius) 
# La fórmula para convertir de celsius a fahrenheit es: celsius * 9/5 + 32 
# Función 2. Recibir un parámetro llamado fahrenheit y regresar el valor equivalente a celsius:
# fahrenheit_celsius(fahrenheit)         
# La fórmula para convertir de fahrenheit a celsius es:  (fahrenheit-32) * 5/9
# Los valores los debe proporcionar el usuario, utilizando la función input y convirtiendolo a tipo float.
# Deben hacer al menos dos pruebas, una donde conviertan de grados celcius a grados fahrenheit, 
# y otra donde conviertan de grados fahrenheit a grados celsius y mandar a imprimir los resultados.


# de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input('Proporciona la temperatura en celsius: '))
fahrenheit = celsius_fahrenheit(celsius)
print(f'Convercion a fahrenheit es de: {fahrenheit}')


 
# de fahrenheit a celsius      
def fahrenheit_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

fahrenheit = float(input('Proporciona la temperatura en fahrenheit: '))
celsius = fahrenheit_celcius(fahrenheit)
print(f'Convercion a celcius es de: {celsius}')