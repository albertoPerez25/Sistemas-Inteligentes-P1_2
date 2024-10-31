from abc import ABCMeta, abstractmethod
from claseBusqueda import Busqueda
<<<<<<< HEAD
=======
from queue import PriorityQueue # Para la PriorityQueue
# https://docs.python.org/3/library/queue.html#queue.PriorityQueue

>>>>>>> 4c7f9ad242986d6e7b2628a2b0b0b366e16f8e71


class BusquedaInformada(Busqueda,metaclass=ABCMeta):
    def __init__(self, problema,heuristica):
        super().__init__(problema)
<<<<<<< HEAD
        # Frontera se usará como PriorityQueue de nodos a ser expandidos
=======
        self.frontera = PriorityQueue() # Frontera se usará como PriorityQueue de nodos a ser expandidos
>>>>>>> 4c7f9ad242986d6e7b2628a2b0b0b366e16f8e71
        self.H = heuristica
    @abstractmethod
    def añadirNodoAFrontera(self, nodo, frontera):
        pass

    def extraerNodoDeFrontera(self, frontera):  # Igual en PrimeroMejor y AEstrella
<<<<<<< HEAD
        return heappop(frontera)[1]             # Sacamos el nodo que toca

class PrimeroMejor(BusquedaInformada):
    def añadirNodoAFrontera(self, nodo, frontera):                                                                                                                                                                                                                                 # Una tripla con su heuristica, orden de generación y el propio nodo
        heappush(frontera,(self.H.heuristica(nodo),nodo))   # Si la heuristica es igual se elige el de menor id                                                                            
=======
        return frontera.get()[1]                # Sacamos el nodo que toca
    
    def esVacia(self, frontera):                # Igual en PrimeroMejor y AEstrella
        return frontera.empty()

class PrimeroMejor(BusquedaInformada):
    def añadirNodoAFrontera(self, nodo, frontera):
        frontera.put((self.H.heuristica(nodo), nodo))   # Una tupla con su heuristica y el propio nodo  
                                                        # Si la heuristica es igual se elige el de menor id                                                                            
>>>>>>> 4c7f9ad242986d6e7b2628a2b0b0b366e16f8e71
class AEstrella(BusquedaInformada):
    def añadirNodoAFrontera(self, nodo, frontera):
        gn = nodo.coste   
        hn = self.H.heuristica(nodo)
<<<<<<< HEAD
        fn = hn + gn                                                        
        heappush(frontera, (fn,  nodo))
=======
        fn = hn + gn   
        frontera.put((fn, nodo))                                                     
>>>>>>> 4c7f9ad242986d6e7b2628a2b0b0b366e16f8e71
    