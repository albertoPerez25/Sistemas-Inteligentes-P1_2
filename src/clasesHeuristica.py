from abc import ABC, abstractmethod
from math import sqrt

class Heuristica(ABC):
    def __init__(self,problema):
        self.problema = problema
    
    @abstractmethod
    def distancia(self,estado,final):
        pass

    # Devuelve el tiempo estimado (coste) desde un estado hasta el estado final
    def tiempo(self, distancia):
        return distancia/self.problema.maxSpeed
    
    # Metodo al que llamamos para calcular la heurística.
    def heuristica(self, nodo):
        return self.distancia(nodo.estado,self.problema.Final)
    
# Dos maneras de hacer heuristicas calculando distancias
# H1 da distancias mayores que H2.
class Heuristica1(Heuristica):
    # Restar long y lat iniciales menos finales
    def distancia(self, estado, final):
        return (abs(estado.latitude - final.latitude) 
                + abs(estado.longitude - final.longitude))
    
class Heuristica2(Heuristica):
    # Pitágoras. (Línea recta)
    def distancia(self, estado,final):
        return sqrt((estado.latitude + final.latitude)**2 
                    + (estado.longitude + final.longitude)**2)