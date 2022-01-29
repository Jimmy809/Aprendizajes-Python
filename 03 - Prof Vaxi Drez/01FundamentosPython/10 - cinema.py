peliculas = {
        "Nemo": [3,5], # edad y bolestos restantes
        "Bourne": [18,5],
        "Tarzan": [15,5],
        "Spiderman": [12,5]
    }

while True:
    eleccion = input("Que pelicula te gustaria ver?: ").strip().title() # quietara los espacios y agregara mayuscula a la primera letra

    if eleccion in peliculas:
        edad = int(input("Cuantos años tienes?: ").strip())

        # verificar edad del usuario
        if edad >= peliculas[eleccion][0]:
            # verificar suficientes boletos
            num_boletos = peliculas[eleccion][1]
            
            if num_boletos > 0:
                print("Disfruta la pelicula")
                peliculas[eleccion][1] = peliculas[eleccion][1] - 1
            else:
                print("Sorry, se agotaron los boletos")
        else:
            print("Eres demasiado para ver esta pelicula")
    else:
        print("No tenemos esa pelicula")
