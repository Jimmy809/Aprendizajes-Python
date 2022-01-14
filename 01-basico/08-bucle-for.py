# for traduccion 'para' con for podremos recorer listas

for i in "Python":
    print(i)

# Salida:
# P
# y
# t
# h
# o
# n


# usamos range para especificar q es un rango del 0 al 5 para imprimir la secuencia
for i in range(0,5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4

# podemos usarlo tambien para repetir un palabra
for i in range(0,5):
    print('hola')

# Iterando cadena al revés. Haciendo uso de [::-1] se puede iterar la lista desde el último al primer elemento.

texto = "Python"
for i in texto[::-1]:
    print(i) #n,o,h,t,y,P

#Itera la cadena saltándose elementos. Con [::2] vamos tomando un elemento si y otro no.

texto = "Python"
for i in texto[::2]:
    print(i) #P,t,o


# para romper un recorido usamos break

for i in range(0,10):
    if i == 8:
        break
    print(i)
