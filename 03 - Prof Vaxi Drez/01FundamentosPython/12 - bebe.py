from random import choice

preguntas = [
        "Porque el cielo es azul?: ",
        "Porque hay una cara en la luna?: ",
        "Donde estan los dinosaurios?: "
    ]

pregunta = choice(preguntas) # con choice apuntando a pregunta, eligira alazar una pregunta de la lista

respuesta = input(pregunta).lower().strip()

while respuesta != "porque si":
    respuesta = input("Porque?: ").strip().lower()

print("Oh entiendo")
    
