import random # 1 libreria para crear un numero random

salud = 50
dificultad = 1 # 3 sera la dificultad de la pocion y se dividira en 1

pocion_salud = int(random.randint(25, 50) / dificultad) # 2 se creara un numero randon entre 25 y 50


salud = salud + pocion_salud

print(salud)