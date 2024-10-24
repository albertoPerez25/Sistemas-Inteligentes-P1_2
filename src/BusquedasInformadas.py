from abc import ABCMeta, abstractmethod
import heapq
from claseBusqueda import Busqueda
from clasesHeuristica import Heuristica1,Heuristica2
from heapq import heapify

class BusquedaInformada(Busqueda,metaclass=ABCMeta):
    def __init__(self, problema):
        super().__init__(problema)
        self.frontera = [] # PriorityQueue de nodos a ser expandidos
        self.h1 = Heuristica1(problema)
        self.h2 = Heuristica2(problema)
        
    @abstractmethod
    def añadirNodoAFrontera(self, nodo, frontera):
        pass

    def extraerNodoDeFrontera(self, frontera):
        return heapq.heappop(frontera)[1]

    def esVacia(self, frontera):
        return len(frontera) != 0

class PrimeroMejor(BusquedaInformada):
    def añadirNodoAFrontera(self, nodo, frontera):
        if isinstance(nodo, list):
            for n in nodo:
                heapq.heappush(frontera, (self.h1.heuristica(n),n))
        else:
            heapq.heappush(frontera,(self.h1.heuristica(nodo),nodo))

class AEstrella(BusquedaInformada):
    pass