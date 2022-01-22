# para concatenar variables y letras
# utilizamos la f antes de las comillas y dentro ponemos el texto y las variables dentro de llaves
x = 10; y = 3
print("Operadores aritméticos")
print(f"resultado de la suma x+y = {x+y}")   #13
print(f"resultado de la resta x-y = {x-y}")   #7
print(f"resultado de la multiplicacion x*y = {x*y}")   #30
print(f"resultado de la division x/y = {x/y}")   #3.3333333333333335
print(f"resultado del modulo x%y = {x%y}")   #1
print(f"resultado del exponente x**y = {x**y}") #1000
print(f"resultado del cociente x//y = {x//y}") #3

# para escribir un cadigo en varias lineas podemos usar

print(f'''
      Nombre:Odisea
      Id: 12
      Precio: 210.25
      Envio: True
      ''')