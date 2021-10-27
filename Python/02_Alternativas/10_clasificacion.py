import math

x1 = float(input("Introduce un valor para x1: "))
y1 = float(input("Introduce un valor para y1: "))
x2 = float(input("Introduce un valor para x2: "))
y2 = float(input("Introduce un valor para y2: "))
r1 = float(input("Introduce un valor para r1: "))
r2 = float(input("Introduce un valor para r2: "))

distancia = math.sqrt(math.pow((x2 - x1), 2) + math.pow((x2 - y1), 2))
suma_radios = r1+r2
diferencia_radios = abs(r1-r2)

if distancia > suma_radios:
    print("Circunferencia exterior")
elif distancia == suma_radios:
    print("Tangente exterior")
elif suma_radios > distancia > diferencia_radios:
    print("Secante")
elif distancia == diferencia_radios:
    print("Tangente interior")
elif distancia < diferencia_radios:
    print("Interior")
elif distancia == 0:
    print("Concentrica")
