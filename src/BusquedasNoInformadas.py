from abc import ABCMeta, abstractmethod
from claseBusqueda import Busqueda


class BusquedaNoInformada(Busqueda,metaclass=ABCMeta):
    def __init__(self, problema):
        super().__init__(problema)
        self.frontera = []  # Lista de nodos a ser expandidos

    def añadirNodoAFrontera(self, nodo, frontera):  # Es igual en Anchura y Profundidad
        if isinstance(nodo, list):                  # Añadimos los nodos nuevos a frontera ordenados por ID
            self.frontera.extend(sorted(nodo))      # Así nos ahorramos ordenar sucesores por ID en busquedas informadas
        else:
            frontera.append(nodo)

    @abstractmethod
    def extraerNodoDeFrontera(self, frontera):
        pass

    def esVacia(self, frontera):                    # Es igual en Anchura y Profundidad
        return len(frontera) != 0

class Anchura(BusquedaNoInformada):
    def extraerNodoDeFrontera(self, frontera):
        return frontera.pop(0)
    
class Profundidad(BusquedaNoInformada):
    def extraerNodoDeFrontera(self, frontera):
        return frontera.pop()
    