L = []

while len(L) < 5:
    nuevo_nombre = input("Agrega un nuevo nombre: ").strip().capitalize()
    L.append(nuevo_nombre)

print("La lista esta llena")
print(L)
