from abc import ABCMeta, abstractmethod
from claseBusqueda import Busqueda


class BusquedaNoInformada(Busqueda,metaclass=ABCMeta):
    def __init__(self, problema):
        super().__init__(problema)
        # Frontera se usará como lista de nodos a ser expandidos

    def añadirNodoAFrontera(self, nodo, frontera):  # Es igual en Anchura y Profundidad
        frontera.append(nodo)

    @abstractmethod
    def extraerNodoDeFrontera(self, frontera):
        pass

class Anchura(BusquedaNoInformada):
    def extraerNodoDeFrontera(self, frontera):
        return frontera.pop(0)
    
class Profundidad(BusquedaNoInformada):
    def extraerNodoDeFrontera(self, frontera):
        return frontera.pop()
    