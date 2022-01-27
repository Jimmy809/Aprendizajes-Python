try:
    archivo = open('prueba.txt', 'w', encoding='utf8') # abrir un archivo, si no exita lo va a crear, w para escribir, utf8 para agregar caracteres especiales
    archivo.write('Agregamos informacion al archivo\n') # agregamos informacion a nuestro archivo
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Fin del Archivo')
    # archivo.write('nueva info') # dara error por que el archivo ya esta cerrado