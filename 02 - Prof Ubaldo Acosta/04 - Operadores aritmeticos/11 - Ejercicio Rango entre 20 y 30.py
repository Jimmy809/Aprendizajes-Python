edad = int(input('Introduce tu edad: '))

veintes = edad >= 20 and edad < 30
print(veintes)
treintas = edad >= 30 and edad < 40
print(treintas)

if veintes or treintas:
    # print('Dentro de rango (20s) o (30s)')
    if veintes:
        print('Dentro de los 20s')
    else:    
        print('Dentro de los 30s')        
else:
    print('No esta dentro de los 20s ni los 30s')