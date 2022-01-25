# while traduccion "mientras"
# El uso del while nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla. 
# Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal. Llamaremos iteración a una ejecución completa del bloque de código.

#while a a iniciar en 1 y ponemos una suma de numero +1 para ir sumando, hasta llegar a 10 y paramos
numero = 1
while numero <= 10:
    print(numero)
    numero += 1

#break para detener el ciclo del 1 al 20 paramos en 6
numero2 = 1
while numero2 <= 20:
    print(numero2)
    if numero2 == 6:
        break
    numero2 += 1


# repeticioncon continue
numero3 = 0

while numero3 <= 10:
    numero3 +=1
    if numero3 == 6:
        continue # aqui hace q no pare en el 6 continuara hasta el final del while 10
    print(numero3)

# suma de numeros naturales sumara el numero del usuario las mismas cantidades de veces
num = int(input('introduce un numero'))

resul = 0
contro = 1

while contro <= num:
    resul += contro
    contro += 1
print('la suma de los numeros es:', resul)