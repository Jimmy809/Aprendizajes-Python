# Dada la siguiente tupla (13, 1, 8, 3, 2, 5, 8)
# crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for: tupla = (13, 1, 8, 3, 2, 5, 8)

tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for i in tupla:
    if i < 5:
        lista.append(i)
print(lista)
# [1, 3, 2]