#Intentos de adivinar que v++++ hacen para calcular el coste o tiempo
from math import sqrt

estado = 772970904
latitude = 38.9990718
longitude = -1.8581771
##
destination = 1529724436

distance = 115.461

origin = 772970904

time = 3.8487

coste = 3.8487
##
estado2 = 1529724436
latitude2 = 38.9980868
longitude2 = -1.8584013



vel = 30
a = abs(latitude - latitude2) + abs(longitude - longitude2)
b = sqrt((-latitude + latitude2)**2 + (-longitude + longitude2)**2)
soluciones = []

soluciones.append(a)
soluciones.append(b)
soluciones.append(a/vel)
soluciones.append(b/vel)
soluciones.append(vel/a)
soluciones.append(vel/b)
soluciones.append(a*vel)
soluciones.append(b*vel)
soluciones.append((a/vel)+(b/vel))
soluciones.append((a*vel)+(b*vel))
soluciones.append(((a+b)/2))
soluciones.append(((a+b)/2)/vel)
soluciones.append(a*250/vel)
soluciones.append(a/vel*250)
soluciones.append(b*250/vel)
soluciones.append(b/vel*250)
soluciones.append((a/vel)/250)
soluciones.append((b/vel)/250)

print(soluciones)

for el in soluciones:
    if el == 13.855319999999999 or el == 13.85532:
        print("ENCONTRADO", el, soluciones.index(el))


# 772970904 → 1529724436 (13.855319999999999) 
# Deberia salir 13.855319999999999