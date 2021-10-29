"""
Algoritmo: Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene
ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?

La raíz cuadrada la podemos hacer a través de la función sqrt de la librería math cuando la importamos pero la raíz
cúbica no debido a que no podemos elevar nada en esa función por lo que lo haríamos elevando el numero a 1/3.
"""

import math

num = int(input( "Indica el numero para hacer la raíz cuadrada y cúbica: "))

raiz_cuadrada = math.sqrt(num)
raiz_cubica = round(num ** 1/3, 1)

print(f"La raíz cuadrada es: {raiz_cuadrada}")
print(f"La raíz cúbica es: {raiz_cubica}")
