#clase abstracta que tendrá busqueda(), expandir(), estadisticas() e imprimirResultado()
from abc import ABC,abstractmethod
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
            sucesor.coste = nodo.coste + accion.time
            sucesor.profundidad = nodo.profundidad + 1
            if sucesor.profundidad > self.nProfundidad:
                self.nProfundidad = sucesor.profundidad
            sucesores.append(sucesor)
            self.cerrados.add(sucesor.estado.identifier)
            self.añadirNodoAFrontera(sucesor,self.frontera)
            self.nGenerados = self.nGenerados + 1
        return sucesores
    
    def busqueda(self):
        self.tInicio = time.perf_counter()
        self.frontera = self.añadirNodoAFrontera(self.nodo,self.frontera)
        self.nGenerados = self.nGenerados + 1
        self.cerrados.add(self.nodo.estado.identifier)
        while(len(self.frontera) != 0):
            self.nodo,self.extraerNodoDeFrontera(self.frontera)
            if (self.testObjetivo(self.nodo)):
                self.tFinal = time.perf_counter()
                return self.listaAcciones(self.nodo)
            if (not self.nodo.estado.identifier in self.cerrados):
                self.expandir(self.nodo,self.problema)                                  # Añadimos los sucesores a frontera en expandir. Ahorramos 1 for
                self.nExpandidos = self.nExpandidos + 1
        raise Exception("Frontera vacia")

    def testObjetivo(self,nodo):
        return nodo.estado.__eq__(self.problema.Final)
    
    def listaAcciones(self,nodo):
        sol = []
        self.nCosteTotal = nodo.coste
        while (nodo.padre):
            sol.append(nodo.accion)
            nodo = nodo.padre
        sol.append(nodo.accion)
        sol.reverse()
        self.imprimirResultado(sol)
        return sol

    def imprimirResultado(self,sol):
        print("Nodos generados: ",self.nGenerados)
        print("Nodos expandidos: ",self.nExpandidos)
        print("Tiempo de ejecución: ",(self.tFinal-self.tInicio))
        print("Profundidad: ",self.nProfundidad)
        print("Coste de la solución: ",self.nCosteTotal)
        print("Solución: ",sol)
    
    @abstractmethod
    def añadirNodoAFrontera(self, nodo, frontera):
        pass
    @abstractmethod
    def extraerNodoDeFrontera(self, frontera):
        pass
    @abstractmethod
    def esVacia(self, frontera):
        pass

