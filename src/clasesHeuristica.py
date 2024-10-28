from abc import ABC, abstractmethod
from math import sqrt
from geopy.distance import geodesic # Libreria que calcula de manera exacta la distancia geodesica

class Heuristica(ABC):
    def __init__(self,problema):
        self.problema = problema
    
    @abstractmethod
    def distancia(self,estado,final):
        pass

    # Devuelve el tiempo estimado (coste) desde un estado hasta el estado final
    def tiempo(self, distancia):
        return distancia/self.problema.maxSpeed # D->m V->m/s T->s
    
    # Metodo al que llamamos para calcular la heurística.
    def heuristica(self, nodo):
        return self.tiempo(self.distancia(nodo.estado,self.problema.Final))
    
# Dos maneras de hacer heuristicas calculando distancias
# H1 da distancias mayores que H2.
class Heuristica1(Heuristica):
    # Euclidea. Pitagoras. (Línea recta)
    def distancia(self, estado, final):
        return sqrt((estado.latitude - final.latitude)**2 + (estado.longitude - final.longitude)**2)*100000
    
class Heuristica2(Heuristica):
    # Geodesica. (Línea recta + curvatura de la Tierra)
    def distancia(self, estado, final):
        return geodesic((estado.latitude,estado.longitude), (final.latitude,final.longitude)).meters # La usan en las soluciones. Mas exacta al ser la tierra una elipse
