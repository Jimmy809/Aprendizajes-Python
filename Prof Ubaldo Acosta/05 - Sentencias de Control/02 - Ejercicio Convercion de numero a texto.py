numero = input('proporciona un valor entre 1 y 3: ')

if numero == 1:
    numeroTexto = 'Numero Uno'
elif numero == 2:
    numeroTexto = 'Numero Dos '
elif numero == 3:
    numeroTexto = 'Numero Tres'
else:
    numeroTexto = 'Valor fiera de rango'
    
print(f'Numero proporcionado: {numero} - {numeroTexto}')