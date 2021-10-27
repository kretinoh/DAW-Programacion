"""
2. Calcular el perimetro y área de un rectangulo dada su base y su altura.
Programa hecho por Rafael Maestre
"""
print("Introduzca la base")
base = float(input())

print("Introduzca la altura")

altura = float(input())

area = base * altura
perimetro = base * 2 + altura * 2

print("El perímetro es " + str(area) + " y el área es: " + str(perimetro))
