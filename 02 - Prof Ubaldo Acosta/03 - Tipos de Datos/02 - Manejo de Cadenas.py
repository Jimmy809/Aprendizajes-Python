# Cadena o string
miGrupoFavorito = 'Aerosmith' + ' ' +'Nirvana' # para concatenar cadenas utilizaremos el signo de + para hace agregar text mas variables, etc
print('Mi grupo favorito es: ' + miGrupoFavorito) # para concatenar cadenas utilizaremos el signo de + para hace agregar text mas variables, etc

miGrupoFavorito2 = 'Metalica'
miGrupoFavorito3 = 'Gorilla'
print('Mi grupo favorito es', miGrupoFavorito2, 'y', miGrupoFavorito3) # tambien podemos concatenar con comas y en este caso se agrega el espacio por defecto



# errores comunes, tratar de hacer una operacion aritmetica, con las variables definidas como cadena o string
numero1 = '1'
numero2 = '2'
print(numero1 + numero2) # concatenacion

# solucion 1
print(int(numero1) + int(numero2)) # siempre y cuando el valor de la variable se un numero no escrito en letras


# solucion 2
numero1 = 1
numero2 = 2
print(numero1 + numero2)