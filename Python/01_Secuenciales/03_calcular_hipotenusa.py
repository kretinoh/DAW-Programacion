"""
3. Dados los catetos de un triangulo rectangulo, calcular su hipotenusa.
Programa hecho por Rafael Maestre
"""
print("Vamos a calcular la hipotenusa \n")

print("Introduzca un cateto")
cateto1 = float(input()) ** 2

print("Introduzca el otro cateto")
cateto2 = float(input()) ** 2

print("La hipotenusa es " + str((cateto1 + cateto2) ** 2))
