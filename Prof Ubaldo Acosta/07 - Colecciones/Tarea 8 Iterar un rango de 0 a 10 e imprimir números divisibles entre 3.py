# Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3
n = 10
for i in range(n):
    if i % 3 == 0:
        print(f'Valor: {i}')
        i +=1
# Valor: 0
# Valor: 3
# Valor: 6
# Valor: 9