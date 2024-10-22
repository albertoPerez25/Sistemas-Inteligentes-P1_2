#clase abstracta que tendrá busqueda(), expandir(), estadisticas() e imprimirResultado()
from abc import ABC
from clasesBasicas import Nodo,Estado,Accion,Problema


class Busqueda(ABC):
    def __init__(self, problema,cerrados = set()):
        self.problema = problema
        self.estadoInicial = problema.Inicial
        self.estadoFinal = problema.Final
        self.tInicio = 0
        self.tFinal = 0
        self.cerrados = cerrados #para no volver a expandir nodos ya visitados
        self.nodo = Nodo(problema.nodoInicio)
        self.frontera = None
        #estadisticas:
        self.nExpandidos = 0
        self.nProfundidad = 0
        self.nCosteTotal = 0 #nodo.coste es acumulativo
        self.nExplorados = 0

    def expandir(self,nodo,problema):
        sucesores = []
        for accion in problema.getAccionesDe(nodo.estado.identifier):
            sucesor = Nodo(problema.getEstado(accion.destination))
            sucesor.padre = nodo
            sucesor.accion = accion
            sucesor.coste = nodo.coste + self.costeIndividual(nodo,accion,sucesor)
            sucesor.profundidad = nodo.profundidad + 1
            if sucesor.profundidad > self.nProfundidad:
                self.nProfundidad = sucesor.profundidad
            sucesores.append(sucesor)
            self.cerrados.add(sucesor.getIntersectionId(sucesor.estado))
            self.añadirNodoAFrontera(sucesor,self.frontera)
            self.nExplorados = self.nExplorados + 1
        return sucesores
    
    def busqueda(self):
        pass

    def estadisticas(self):
        pass

    def imprimirResultado(self):
        pass

