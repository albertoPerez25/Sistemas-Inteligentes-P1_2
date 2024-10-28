from clasesBasicas import Problema
from BusquedasNoInformadas import Anchura, Profundidad
from BusquedasInformadas import PrimeroMejor,AEstrella

Al_Huge2 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/huge/calle_herreros_albacete_2000_2.json'
Al_Large1 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/large/calle_agustina_aroca_albacete_1000_2.json'
Al_Huge1 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/huge/calle_del_virrey_morcillo_albacete_2000_4.json'
Al_Test1 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/test/test.json'
Al_Test2 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/test/test2.json'
Al_Medium1 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/medium/calle_del_virrey_morcillo_albacete_2000_4.json'
Al_Small1 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/small/calle_del_virrey_morcillo_albacete_250_3.json'
Ma_Medium1 = '/home/marcos/Documentos/3_Uni/Sistemas_Inteligentes/Programas_python/SInteligentesP1/recursos/problems/medium/calle_del_virrey_morcillo_albacete_2000_4.json'
Ma_Test1 = '/home/marcos/Documentos/3_Uni/Sistemas_Inteligentes/Programas_python/SInteligentesP1/recursos/problems/test/test.json'

RUTAJSON = Al_Large1

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


