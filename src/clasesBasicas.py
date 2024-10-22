#GRUPO 9 - 3ºB esiiab
#ALBERTO PEREZ ALVAREZ
#MARCOS LOPEZ GOMEZ

import json
from math import sqrt

Al_Large1 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/large/calle_f_albacete_5000_4.json'
Al_Huge1 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/huge/calle_agustina_aroca_albacete_5000_0.json'
Al_Test1 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/test/test.json'
Al_Medium1 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/medium/calle_maria_marin_500_0.json'
Al_Small1 = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/Sistemas-Inteligentes-P1_2/problems/small/calle_del_virrey_morcillo_albacete_250_3.json'
Ma_Medium1 = '/home/marcos/Documentos/3_Uni/Sistemas_Inteligentes/Programas_python/SInteligentesP1/recursos/problems/medium/calle_maria_marin_500_0.json'
Ma_Test1 = '/home/marcos/Documentos/3_Uni/Sistemas_Inteligentes/Programas_python/SInteligentesP1/recursos/problems/test/test.json'

RUTAJSON = Al_Small1


#Interseccion:
class Estado:
    def __init__(self, id, latitude, longitude):
        self.identifier = id
        self.latitude = latitude
        self.longitude = longitude
    def __str__(self):
        return f"Interseccion: (id={self.identifier}, latitud={self.latitude}, longitud={self.longitude})"
    def __eq__(self, otro):
        if not isinstance(otro, Estado):
            return False
        else:
            return self.identifier == otro.identifier
    def __lt__(self, otro):
        return self.identifier < otro.identifier
    def esId(self, id):
        return self.identifier == id

#Segmento:    
class Accion:
    def __init__(self, origin, destination, distance, speed):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.speed = speed
    def __str__(self):
        return f"Calle: Origen: {self.origin}, Destino: {self.destination}, Distancia: {self.distance}, Velocidad: {self.speed})"
    def __eq__(self, otro):
        if not isinstance(otro, Accion):
            return False
        else:
            return self.origin == otro.origin and self.destination == otro.destination and self.distance == otro.distance and self.speed == otro.speed

class Problema:   
    #Creamos clases para tener objetos que contengan las intersecciones
        #Ahora estas clases son Estado(para intersecciones) y Accion(para segmentos/calles)

    #Constructor de Problema
    def __init__(self,ruta):
        with open(ruta, 'r') as file:
            self.data = json.load(file)
        
        self.dic_estados = {}
        self.dic_acciones = {}
        self.maxSpeed = 0

        #Pasamos las intersecciones del JSON a un nuevo diccionario estados
        for inter in self.data['intersections']:
            self.dic_estados.update({inter['identifier']:Estado(inter['identifier'], inter['latitude'], inter['longitude'])})
            self.dic_acciones.update({inter['identifier']:[]})

        #Cargamos los nodos iniciales y finales del JSON
        self.Inicial = self.dic_estados[self.data["initial"]]
        self.Final = self.dic_estados[self.data["final"]]
        
        #Pasamos los segmentos del JSON a un nuevo diccionario acciones     
        for seg in self.data['segments']:
            if (seg['speed'] > self.maxSpeed):
                self.maxSpeed = seg['speed']
            self.dic_acciones[seg['origin']].append(Accion(seg['origin'], seg['destination'], seg['distance'], seg['speed']))
            
    #Agregar metodos de nodoAux que usen intersection_dic
    def getEstado(self, id):
        return self.dic_estados[id]

    def getDestinoDe(self,segmento):
        return self.dic_estados[segmento.destination]

    #Agregar metodos de nodoAux que usen segments
    def getAccionesDe(self,id):
        return self.dic_acciones[id]

class Nodo:
    def __init__(self, interseccion, padre = None, accionTomada = None, coste = 0, profundidad = 0):
        self.estado = interseccion
        self.padre = padre
        self.accion = accionTomada
        self.coste = coste
        self.profundidad = profundidad
        self.calles = self.getSegmentsOf(self.getIntersectionId(self.estado)) #Lista de calles de la interseccion
        self.it = 0 #Iterador para self.calles
        
    def __str__(self):
        return f"Nodo(estado={self.estado}, padre={self.padre}, accion={self.accion}, coste={self.coste}, profundidad={self.profundidad})"
    
    def __eq__(self,otro):
        if not isinstance(otro, Nodo):
            return False
        return self.estado.__eq__(otro.estado) and self.accion.__eq__(otro.accion) and self.padre.__eq__(otro.padre)
    
    def __lt__(self,otro):
        return self.estado.__lt__(otro.estado)
    
    #METODOS:
    #Devuelve la siguiente calle de la interseccion
    def getSiguienteAccion(self,segmentos = []):
        if (len(segmentos) == 0):
            segmentos = self.calles
            if(segmentos == None):
                return None
        if (self.it >= len(segmentos)):
            return None
        segmento = segmentos[self.it]
        self.it = self.it + 1
        return segmento