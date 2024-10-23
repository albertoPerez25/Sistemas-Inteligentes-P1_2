#clase abstracta que tendrá busqueda(), expandir(), estadisticas() e imprimirResultado()
from abc import ABC
import time
from clasesBasicas import Nodo,Estado,Accion,Problema


class Busqueda(ABC):
    def __init__(self, problema,cerrados = set()):
        self.problema = problema
        self.estadoInicial = problema.Inicial
        self.estadoFinal = problema.Final
        self.tInicio = 0
        self.tFinal = 0
        self.cerrados = cerrados        # para no volver a expandir nodos ya visitados
        self.nodo = Nodo(problema.nodoInicio)
        self.frontera = None
        #estadisticas:
        self.nExpandidos = 0
        self.nProfundidad = 0
        self.nCosteTotal = 0            # nodo.coste es acumulativo
        self.nGenerados = 0

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
            self.nGenerados = self.nGenerados + 1
        return sucesores
    
    def busqueda(self):
        self.tInicio = time.time()
        self.frontera = self.añadirNodoAFrontera(self.nodo,self.frontera)
        self.nGenerados = self.nGenerados + 1
        self.cerrados.add(self.nodo.getIntersectionId(self.nodo.estado))
        while(len(self.frontera) != 0):
            self.nodo,self.extraerNodoDeFrontera(self.frontera)
            if (self.testObjetivo(self.nodo,self.nodo.estado)):
                self.tFinal = time.time()
                return self.listaSolucion(self.nodo)
            if (not self.nodo.estado.identifier in self.cerrados):
                self.expandir(self.nodo,self.problema)                                  # Añadimos los sucesores a frontera en expandir. Ahorramos 1 for
                self.nExpandidos = self.nExpandidos + 1
        raise Exception("Frontera vacia")

    def estadisticas(self):
        pass

    def imprimirResultado(self):
        pass

