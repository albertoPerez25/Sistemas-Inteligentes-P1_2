#clase abstracta que tendrá busqueda(), expandir(), estadisticas() e imprimirResultado()
from clasesBasicas import Nodo,Problema
from abc import ABC, ABCMeta,abstractmethod
import time,heapq

class Busqueda(ABC):
    def __init__(self, problema):
        self.problema = problema
        self.estadoInicial = problema.Inicial
        self.estadoFinal = problema.Final
        self.tInicio = 0
        self.tFinal = 0
        self.cerrados = set()        # para no volver a expandir nodos ya visitados
        self.nodo = Nodo(problema.Inicial)
        self.frontera = None
        #estadisticas:
        self.nExpandidos = 0
        self.nProfundidad = 0
        self.nCosteTotal = 0           
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
                sucesores = self.expandir(self.nodo, self.problema)     # Obtenemos los sucesores con Expandir()
                self.añadirNodoAFrontera(sucesores, self.frontera)      # Añadimos los sucesores a frontera.
                self.nExpandidos = self.nExpandidos + 1
                self.cerrados.add(self.nodo.estado.identifier)
        raise Exception("Frontera vacia")

    def testObjetivo(self,nodo):
        return nodo.estado.__eq__(self.problema.Final)

    def listaAcciones(self,nodo):
        sol = []                         # Lista de acciones que han llevado desde el final al inicial
        self.nCosteTotal = nodo.coste    # nodo.coste es acumulativo
        while (nodo.padre):
            sol.append(nodo.accion)
            nodo = nodo.padre
        sol.reverse()                   # Ahora es una lista de acciones desde el inicial al final
        self.imprimirResultado(sol)
        return sol

    def imprimirResultado(self,sol):
        print("Nodos generados:",self.nGenerados)
        print("Nodos expandidos:",self.nExpandidos)
        print("Tiempo de ejecución:",(self.formatearTiempo(self.tFinal - self.tInicio)),"segundos")
        print("Profundidad:",self.nProfundidad)
        print("Coste de la solución:",self.formatearTiempo(self.nCosteTotal))
        print("Solución:",sol)
    
    def formatearTiempo(self, tiempo):
        horas = int(tiempo // 3600)
        minutos = int((tiempo % 3600) // 60)
        segundos = int(tiempo % 60)
        milisegundos = int((tiempo - int(tiempo)) * 1000000)
        return f"{horas:01d}:{minutos:02d}:{segundos:02d}.{milisegundos:06d}"

    @abstractmethod
    def añadirNodoAFrontera(self, nodo, frontera):
        pass
    @abstractmethod
    def extraerNodoDeFrontera(self, frontera):
        pass
    @abstractmethod
    def esVacia(self, frontera):
        pass

