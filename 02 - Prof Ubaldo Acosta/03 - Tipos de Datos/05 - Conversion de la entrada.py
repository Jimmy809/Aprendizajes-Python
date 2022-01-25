# Funcion input para procesar la entrada del usuario

# en este caso estamos concatenando los pedidos al usuario, no podremos realizar la suma
# numero1 = input('Escribe el primer numero: ')# ej 10
# numero2 = input('Escribe el segundo numero: ')# ej 20
# resultado = numero1 + numero2
# print('El resultado de la suma es:', resultado) # 1020 concatenara el resultado


# solucion, tenemos q convertir la funcion input a numero entero con int
numero1 = int(input('Escribe el primer numero: '))
numero2 = int(input('Escribe el segundo numero: '))
resultado = numero1 + numero2
print('El resultado de la suma es:', resultado)