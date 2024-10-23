#clase abstracta que tendrá busqueda(), expandir(), estadisticas() e imprimirResultado()
from clasesBasicas import Nodo,Problema
from abc import ABC, ABCMeta,abstractmethod
import time,heapq

class Busqueda(ABC):
    def __init__(self, problema,cerrados = set()):
        self.problema = problema
        self.estadoInicial = problema.Inicial
        self.estadoFinal = problema.Final
        self.tInicio = 0
        self.tFinal = 0
        self.cerrados = cerrados        # para no volver a expandir nodos ya visitados
        self.nodo = Nodo(problema.Inicial)
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
            self.nGenerados = self.nGenerados + 1
        self.añadirNodoAFrontera(sucesores, self.frontera)
        return sucesores
    
    def busqueda(self):
        self.tInicio = time.time()
        self.añadirNodoAFrontera(self.nodo,self.frontera)
        while(self.esVacia(self.frontera)):
            self.nodo = self.extraerNodoDeFrontera(self.frontera)
            if (self.testObjetivo(self.nodo)):
                self.tFinal = time.time()
                return self.listaAcciones(self.nodo)
            if (not self.nodo.estado.identifier in self.cerrados):
                self.expandir(self.nodo,self.problema)                                  # Añadimos los sucesores a frontera en expandir. Ahorramos 1 for
                self.nExpandidos = self.nExpandidos + 1
                self.cerrados.add(self.nodo.estado.identifier)
        raise Exception("Frontera vacia")

    def testObjetivo(self,nodo):
        return nodo.estado.__eq__(self.problema.Final)

    def listaAcciones(self,nodo):
        sol = []
        self.nCosteTotal = nodo.coste
        while (nodo.padre):
            sol.append(nodo.accion)
            nodo = nodo.padre
        sol.reverse()
        self.imprimirResultado(sol)
        return sol

    def imprimirResultado(self,sol):
        print("Nodos generados:",self.nGenerados)
        print("Nodos expandidos:",self.nExpandidos)
        print("Tiempo de ejecución:",(self.tFinal-self.tInicio),"segundos")
        print("Profundidad:",self.nProfundidad)
        print("Coste de la solución:",self.nCosteTotal)
        print("Solución:",sol)
    
    @abstractmethod
    def añadirNodoAFrontera(self, nodo, frontera):
        pass
    @abstractmethod
    def extraerNodoDeFrontera(self, frontera):
        pass
    @abstractmethod
    def esVacia(self, frontera):
        pass

class BusquedaNoInformada(Busqueda,metaclass=ABCMeta):
    def __init__(self, problema, cerrados = set()):
        super().__init__(problema, cerrados)
        self.frontera = []              # lista de nodos

    def añadirNodoAFrontera(self, nodo, frontera):  # Es igual en Anchura y Profundidad
        if isinstance(nodo, list):
            self.frontera.extend(sorted(nodo))
        else:
            frontera.append(nodo)

    @abstractmethod
    def extraerNodoDeFrontera(self, frontera):
        pass

    def esVacia(self, frontera):                    # Es igual en Anchura y Profundidad
        return len(frontera) != 0

class BusquedaInformada(Busqueda,ABC):
    def __init__(self, problema, cerrados = set()):
        super().__init__(problema, cerrados)
        # PriorityQueue de nodos
                
    @abstractmethod
    def añadirNodoAFrontera(self, nodo, frontera):
        pass

    @abstractmethod
    def extraerNodoDeFrontera(self, frontera):
        pass

    @abstractmethod
    def esVacia(self, frontera):
        pass