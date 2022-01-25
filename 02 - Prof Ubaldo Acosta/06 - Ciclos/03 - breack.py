# La sentencia break nos permite alterar el comportamiento de los bucles while y for. 
# Concretamente, permite terminar con la ejecución del bucle.

for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break # rompera el ciclo desde q encuentre la primera letra indicada(a)
else:
    print('Fin ciclo for')
        