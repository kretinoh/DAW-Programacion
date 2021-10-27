"""
Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda.
Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
Hecho por Rafael Maestre
"""

edad1 = int(input("Introduzca la primera edad: "))
edad2 = int(input("Introduzca la segunda edad: "))

if edad1 > edad2:
    print("La primera persona es mayor que la segunda")
elif edad2 > edad1:
    print("La segunda persona es mayor que la primera")
else:
    print("Tienen la misma edad")
