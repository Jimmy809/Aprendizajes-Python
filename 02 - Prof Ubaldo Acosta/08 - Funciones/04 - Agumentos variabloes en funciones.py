# * esto es para convertirla variable a una upla
def listaNombres(*nombres):
    for nombre in nombres:
        print(nombre)
        
listaNombres('Juan', 'Karla', 'Maria', 'Ernesto')
# Juan
# Karla
# Maria
# Ernesto

# podemos agregar mas nombre
listaNombres('Laura', 'Carlos')
# Juan
# Karla
# Maria
# Ernesto
# Laura
# Carlos