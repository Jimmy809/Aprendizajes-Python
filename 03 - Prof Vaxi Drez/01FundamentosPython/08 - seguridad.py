usuarios_conocidos = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]


while True:
    print("Hola mi nombre es Keto")
    nombre = input("Cual es tu nombre?: ").strip().capitalize()
    if nombre in usuarios_conocidos:
        print("Hola {}!".format(nombre))
        eliminar = input("Te gustaria ser eliminado del sistema (y/n)?: ").strip().lower()
        if eliminar == "y":
            usuarios_conocidos.remove(nombre)
        elif eliminar == "n":
            print("No hay problema si no deseas salir")
        else:
            print('Letra no reconocida, intenta introducir (y o n), por favor')
  
    else:
        print("Hmm no creo haberte conocido aun {}".format(nombre))
        agregar = input("Te gustaria ser agregado al sistema (y/n)?: ").strip().lower()
        if agregar == "y":
            usuarios_conocidos.append(nombre)
        elif agregar == "n":
            print("No te preocupes nos vemos")
        else:
            print('Letra no reconocida, intenta introducir (y o n), por favor')