from claseBusqueda import BusquedaNoInformada

class Anchura(BusquedaNoInformada):
    def __init__(self, problema, cerrados = set()):
        super().__init__(problema, cerrados)

    def extraerNodoDeFrontera(self, frontera):
        return frontera.pop(0)