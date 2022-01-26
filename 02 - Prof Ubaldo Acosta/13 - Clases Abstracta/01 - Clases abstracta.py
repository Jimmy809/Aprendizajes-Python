# Como ya hemos visto los métodos abstractos son aquellos que son declarados pero no tienen una implementación. 
# También hemos visto como Python nos obliga a implementarlos en la clases que heredan de nuestro interfaz. Esto es posible gracias al decorador @abstractmethod.

from abc import ABC, abstractmethod
class Clase(metaclass=ABCMeta):
    @abstractmethod
    def metodo_abstracto(self):
        pass