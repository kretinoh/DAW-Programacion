"""
Algoritmo: Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y
muestra la distancia entre ellos.

Para calcular la distancia que hay entre dos puntos de un eje de coordenadas (debido a que un punto tiene un par
de numero hay que hacer el modulo de ambos lo cual seria hacer la raíz cuadrad de la resta de los puntos x al cuadrado
mas la resta de los puntos y al cuadrado
"""

print("Vamos a mostrar la distancia entre dos pares de números ")

x1 = float(input("Dame x1: "))
y1 = float(input("Dame y1: "))

print("Ingrésame el segundopunto: ")

x2 = float(input("Dame x2: "))
y2 = float(input("Dame y2: "))

modulo = round((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5, 0)


print("Esta sería la distancia entre ambos puntos: " + str(modulo))
