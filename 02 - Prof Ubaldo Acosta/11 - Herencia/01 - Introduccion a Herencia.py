# La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, 
# compartiendo sus métodos y atributos. Además de ello, una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.

# Se puede crear una clase hija con tan solo pasar como parámetro la clase de la que queremos heredar. 
# En el siguiente ejemplo vemos como se puede usar la herencia en Python, con la clase Perro que hereda de Animal. Así de fácil.

# Definimos una clase padre
class Animal:
    pass

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass
# De hecho podemos ver como efectivamente la clase Perro es la hija de Animal usando __bases__

print(Perro.__bases__)
#  (<class '__main__.Animal'>,)
# De manera similar podemos ver que clases descienden de una en concreto con __subclasses__.

print(Animal.__subclasses__())
# [<class '__main__.Perro'>]