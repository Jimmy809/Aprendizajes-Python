# https://ellibrodepython.com/operadores-logicos
# Operador	                     Nombre                                       Ejemplo
# and	         Devuelve True si ambos elementos son True	            True and True = True
# or	         Devuelve True si al menos un elemento es True	        True or False = True
# not	         Devuelve el contrario, True si es Falso y viceversa	not True = False

# Operador and
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# Operador or
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

# operador not
print(not True)  # False
print(not False) # True
print(not not not not True) # True
print(not 0) # True
print(not 1) # False