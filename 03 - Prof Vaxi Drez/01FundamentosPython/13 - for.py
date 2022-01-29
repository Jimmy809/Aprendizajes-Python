estudiantes = {
    "masculino": ["Tom", "Charlie", "Harry", "Frank"],
    "femenino": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

for key in estudiantes.keys():
    for nombre in estudiantes[key]:
        if "a" in nombre:
            print(nombre)
