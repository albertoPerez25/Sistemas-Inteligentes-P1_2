from abc import ABCMeta, abstractmethod
from claseBusqueda import Busqueda


class BusquedaNoInformada(Busqueda,metaclass=ABCMeta):
    def __init__(self, problema):
        super().__init__(problema)
<<<<<<< HEAD
        # Frontera se usará como lista de nodos a ser expandidos
=======
        self.frontera = []# Frontera se usará como lista de nodos a ser expandidos
>>>>>>> 4c7f9ad242986d6e7b2628a2b0b0b366e16f8e71

    def añadirNodoAFrontera(self, nodo, frontera):  # Es igual en Anchura y Profundidad
        frontera.append(nodo)

    @abstractmethod
    def extraerNodoDeFrontera(self, frontera):
        pass
<<<<<<< HEAD
=======
    
    def esVacia(self, frontera):                    # Es igual en Anchura y Profundidad
        return len(frontera) == 0
>>>>>>> 4c7f9ad242986d6e7b2628a2b0b0b366e16f8e71

class Anchura(BusquedaNoInformada):
    def extraerNodoDeFrontera(self, frontera):
        return frontera.pop(0)
    
class Profundidad(BusquedaNoInformada):
    def extraerNodoDeFrontera(self, frontera):
        return frontera.pop()
    