# Obtener el email del usuario
email = input("Cual es tu email?: ").strip() # con el metodo strip podemos borrar los espacios agregados sin kerer

#Cortar el nombre del usuario
usuario = email[:email.index("@")] # aqui se le a indicado que imprima la palabra dentro de email hasta antes de @ [:@]


#Cortar el dominio
dominio = email[email.index("@")+1:] #aqui se le a indicado que imprima la palabra dentro de email despues de @ [:@]


#Formatear el mensaje
salida = "Tu nombre de usuario es {} y tu nombre de dominio es {}".format(usuario, dominio)

#Mostrar mensaje de salida
print(salida)
