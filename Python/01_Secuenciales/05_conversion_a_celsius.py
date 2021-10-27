"""
5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
Programa hecho por Rafael Maestre
"""
print("Vamos a pasar grados Fahrenheit a grados Celsius")

print("Introduzca los grados Fahrenheit")
grados_f = float(input())

grados_c = (grados_f - 32) / 1.8

print(str(grados_f) + "F grados Fahrenheit son " + str(grados_c) + "º grados Celsius")
