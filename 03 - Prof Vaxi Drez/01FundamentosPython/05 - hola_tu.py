#Pedir nombre al usuario
nombre = input("Cual es tu nombre?: ")

#Pedir edad al usuario
edad = input("Cual es tu edad?: ")

#Pedir direccion al usuario
ciudad = input("En que ciudad vives?: ")

#Pedir hobbie al usuario
hobbie = input("Que te gusta hacer?: ")

#Crear texto de salida
string = "Tu nombre es {} y tienes {} de edad, vives en {} y te gusta {}" # este sera el mensaje y en {} se esperaran los datos pedidos
salida = string.format(nombre, edad, ciudad, hobbie) # en este caso se agrego a salida la variable string con el mensaje y 
# con format se le agrego las variable pedidas a la variable del comentario

#Imprimir texto de salida en la pantalla
print(salida)
