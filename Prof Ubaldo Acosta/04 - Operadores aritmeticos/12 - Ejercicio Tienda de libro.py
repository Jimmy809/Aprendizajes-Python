# proporciona los siguitens datos del libro:
# proporciona el nombre: programacion con python
# Proporciona el ID: 422
# Proporcione el precio: 2550.00
# indica si el envio es gratuito (true/false):true
# luego desplegar toda la informacion
print('Proporcione los siguientes datos del libro')
nombre = input('Proporciona el nombre del libro: ')
id = int(input('Proporciona el ID: '))
precio = float(input('Proporciona el precio: '))
envio = input('Proporciona si el envio es gratuito (True/False')
if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorecto, Debe escribir True/False'

print(f'''
      Nombre: {nombre}
      Id: {id}
      Precio: {precio}
      Envio: {envio}
      ''')