from clasesBasicas import Problema
from BusquedasNoInformadas import Anchura, Profundidad
from BusquedasInformadas import PrimeroMejor,AEstrella

Huge2 = 'problems/huge/calle_herreros_albacete_2000_2.json'
Large1 = 'problems/large/calle_agustina_aroca_albacete_1000_2.json'
Large2 = 'problems/large/calle_f_albacete_5000_4.json'
Huge1 = 'problems/huge/calle_del_virrey_morcillo_albacete_2000_4.json'
Test1 = 'problems/test/test.json'
Test2 = 'problems/test/test2.json'
Medium1 = 'problems/medium/calle_del_virrey_morcillo_albacete_2000_4.json'
Small1 = 'problems/small/calle_del_virrey_morcillo_albacete_250_3.json'

RUTAJSON = Large2

anchura = Anchura(Problema(RUTAJSON))
profundidad = Profundidad(Problema(RUTAJSON))
primeroMejor = PrimeroMejor(Problema(RUTAJSON))
estrella = AEstrella(Problema(RUTAJSON))

def hacerAnchura():
    print("\nAnchura:")
    anchura.busqueda()

def hacerProfundidad():
    print("\nProfundidad:")
    profundidad.busqueda()

def hacerPrimeroMejor():
    print("\nPrimero Mejor:")
    primeroMejor.busqueda()

def hacerAEstrella():
    print("\nA Estrella:")
    estrella.busqueda()

hacerAnchura()
hacerProfundidad()
hacerPrimeroMejor()
hacerAEstrella()


