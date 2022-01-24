def desplegarNombres(nombres): # variable es nombres
    for nombre in nombres: 
        print(nombre)
nombres = ['Juan', 'Karla', 'Guillermo'] # agregamos estos datos a nuestra variable nombres [] con corchetes lo jemos convertido a una lista
desplegarNombres(nombres)
# Juan
# Karla
# Guillermo
desplegarNombres('Carlos')
# desplegarNombres(10) # el ciclo for aqui se rompe por que es un solo valor
desplegarNombres((10, 11)) # para que funcione debemos convertirlo en una tupla (()) con mas valores
# desplegarNombres([10, 11]) # asi lo convertimos a una lista