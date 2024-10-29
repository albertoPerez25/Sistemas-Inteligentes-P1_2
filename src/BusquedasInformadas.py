from abc import ABCMeta, abstractmethod
from heapq import heappush, heappop # Para la PriorityQueue
from claseBusqueda import Busqueda


class BusquedaInformada(Busqueda,metaclass=ABCMeta):
    def __init__(self, problema,heuristica):
        super().__init__(problema)
        # Frontera se usará como PriorityQueue de nodos a ser expandidos
        self.H = heuristica
    @abstractmethod
    def añadirNodoAFrontera(self, nodo, frontera):
        pass

    def extraerNodoDeFrontera(self, frontera):  # Igual en PrimeroMejor y AEstrella
        return heappop(frontera)[1]             # Sacamos el nodo que toca

class PrimeroMejor(BusquedaInformada):
    def añadirNodoAFrontera(self, nodo, frontera):                                                                                                                                                                                                                                 # Una tripla con su heuristica, orden de generación y el propio nodo
        heappush(frontera,(self.H.heuristica(nodo),nodo))   # Si la heuristica es igual se elige el de menor id                                                                            
class AEstrella(BusquedaInformada):
    def añadirNodoAFrontera(self, nodo, frontera):
        gn = nodo.coste   
        hn = self.H.heuristica(nodo)
        fn = hn + gn                                                        
        heappush(frontera, (fn,  nodo))
    