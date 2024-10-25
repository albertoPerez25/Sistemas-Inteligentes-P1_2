from abc import ABCMeta, abstractmethod
from heapq import heappush, heappop # Para la PriorityQueue
from claseBusqueda import Busqueda
from clasesHeuristica import Heuristica1,Heuristica2


class BusquedaInformada(Busqueda,metaclass=ABCMeta):
    def __init__(self, problema):
        super().__init__(problema)
        self.frontera = []  # PriorityQueue de nodos a ser expandidos
        self.h1 = Heuristica1(problema)
        self.h2 = Heuristica2(problema)
        
    @abstractmethod
    def añadirNodoAFrontera(self, nodo, frontera):
        pass

    def extraerNodoDeFrontera(self, frontera):  # Igual en PrimeroMejor y AEstrella
        return heappop(frontera)[2]             # Sacamos el nodo que toca

    def esVacia(self, frontera):                # Igual en PrimeroMejor y AEstrella
        return len(frontera) != 0

class PrimeroMejor(BusquedaInformada):
    def añadirNodoAFrontera(self, nodo, frontera):
        if isinstance(nodo, list):                                              # Como en noInformada, si es una lista de sucesores
            for n in nodo:                                                      # la recorremos y añadimos ordenadamente los nodos 
                heappush(frontera, (self.h1.heuristica(n),n.nGenerado,n))                                                                                                                                                                  
        else:                                                                   # Una tripla con su heuristica, orden de generación y el propio nodo
            heappush(frontera,(self.h1.heuristica(nodo),nodo.nGenerado,nodo))   # Si la heuristica es igual se elige el generado antes 
                                                                                # como hacemos en clase.
class AEstrella(BusquedaInformada):
    pass