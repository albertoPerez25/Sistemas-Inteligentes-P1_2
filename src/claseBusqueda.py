#clase abstracta que tendrá busqueda(), expandir(), estadisticas() e imprimirResultado()
from clasesBasicas import Nodo
from abc import ABC,abstractmethod
import time
from heapq import heappop

class Busqueda(ABC):
    def __init__(self, problema):
        self.frontera = []  # Declaración igual en todos los algoritmos
                            # heapq usa una lista como priority vacia.
                            # heapq es minimamente mas rapido que PriorityQueue al 
                            # no prevenir errores de hilos. Como no usamos concurrencia 
                            # de hilos en esta práctica, heapq es ideal
                            # https://docs.python.org/3/library/queue.html#queue.PriorityQueue
        self.problema = problema
        self.estadoInicial = problema.Inicial
        self.estadoFinal = problema.Final
        self.tInicio = 0
        self.tFinal = 0
        self.cerrados = set()        # Para no volver a expandir nodos ya visitados
        self.nodo = Nodo(problema.Inicial)
        # Estadisticas:
        self.nExpandidos = 0
        self.nProfundidad = 0
        self.nCosteTotal = 0           
        self.nGenerados = 0

    def expandir(self,nodo,problema):
        sucesores = []
        acciones = problema.getAccionesDe(nodo.estado.identifier)
        while acciones:
            accion = heappop(acciones)
            sucesor = Nodo(problema.getEstado(accion.destination))
            sucesor.padre = nodo
            sucesor.accion = accion
            sucesor.coste = nodo.coste + accion.time
            sucesor.profundidad = nodo.profundidad + 1
            self.nGenerados = self.nGenerados + 1
            sucesor.nGenerado = self.nGenerados
            self.añadirNodoAFrontera(sucesor, self.frontera)    # Añadimos los sucesores a frontera.
                                                                # Nos ahorramos un bucle For al añadirlos 
                                                                # desde expandir
                                                            
    def busqueda(self):
        self.tInicio = time.time()
        self.añadirNodoAFrontera(self.nodo,self.frontera)
        while(not self.esVacia(self.frontera)):
            self.nodo = self.extraerNodoDeFrontera(self.frontera)
            if (self.testObjetivo(self.nodo)):
                self.tFinal = time.time()
                return self.listaAcciones(self.nodo)
            if (not self.nodo.estado.identifier in self.cerrados):
                self.expandir(self.nodo, self.problema)     # Obtenemos los sucesores con Expandir()
                self.nExpandidos = self.nExpandidos + 1
                self.cerrados.add(self.nodo.estado.identifier)
        self.tFinal = time.time()
        return self.imprimirResultado([])

    def esVacia(self, frontera): # Igual en todos los algoritmos
        return len(frontera) == 0

    def testObjetivo(self,nodo):
        return nodo.estado.__eq__(self.problema.Final)

    def listaAcciones(self,nodo):
        sol = []                         # Lista de acciones que han llevado desde el final al inicial
        estados = []
        self.nCosteTotal = nodo.coste    # nodo.coste es acumulativo
        self.nProfundidad=nodo.profundidad
        while (nodo.padre):
            sol.append(nodo.accion)
            estados.append(nodo.estado.identifier)
            nodo = nodo.padre
        estados.append(nodo.estado.identifier)
        sol.reverse()                   # Ahora es una lista de acciones desde el inicial al final
        self.imprimirResultado(sol)
        
        return estados

    def imprimirResultado(self,sol):
        if not sol : print("Solución no encontrada")
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

