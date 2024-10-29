from clasesBasicas import Problema
from BusquedasNoInformadas import Anchura, Profundidad
from BusquedasInformadas import PrimeroMejor,AEstrella
from clasesHeuristica import Heuristica1,Heuristica2,Heuristica3

Huge2 = 'problems/huge/calle_herreros_albacete_2000_2.json' # No va prof
Large1 = 'problems/large/calle_agustina_aroca_albacete_1000_2.json' # No va A*
Large2 = 'problems/large/calle_f_albacete_5000_4.json'
Large3 = 'problems/large/calle_cardenal_tabera_y_araoz_albacete_1000_3.json'
Large4 = 'problems/large/calle_ínsula_barataria_albacete_1000_1.json' # No va A*
Huge1 = 'problems/huge/calle_del_virrey_morcillo_albacete_2000_4.json'
Test1 = 'problems/test/test.json'
Test2 = 'problems/test/test2.json'
Medium1 = 'problems/medium/calle_del_virrey_morcillo_albacete_2000_4.json'
Small1 = 'problems/small/calle_del_virrey_morcillo_albacete_250_3.json'
Small2 = 'problems/small/calle_franciscanos_albacete_250_0.json' # Sin solucion
Small3 = 'problems/small/calle_palmas_de_gran_canaria_albacete_250_4.json' # No va prof

RUTAJSON = Huge2

def hacerAnchura():
    print("\nAnchura:")
    anchura = Anchura(Problema(RUTAJSON))
    anchura.busqueda()

def hacerProfundidad():
    print("\nProfundidad:")
    profundidad = Profundidad(Problema(RUTAJSON))
    profundidad.busqueda()


def hacerPrimeroMejor(h):
    print("\nPrimero Mejor:")
    primeroMejor = PrimeroMejor(Problema(RUTAJSON),h)
    primeroMejor.busqueda()

def hacerAEstrella(h):
    print("\nA Estrella:")

    estrella = AEstrella(Problema(RUTAJSON),h)       
    estrella.busqueda()

h1 = Heuristica1(Problema(RUTAJSON)) # Euclidea
h2 = Heuristica2(Problema(RUTAJSON)) # Geodesica
h3 = Heuristica3(Problema(RUTAJSON)) # Manhattan

hacerAnchura()
hacerProfundidad()
hacerPrimeroMejor(h2)
hacerAEstrella(h2)


