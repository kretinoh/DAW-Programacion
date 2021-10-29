"""
Creado el día 18/10/2021

Algoritmo: Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
"""

nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu apellido1: ")
apellido2 = input("Dime tu apellido2: ")

inicial_nombre = nombre[0]
inicial_apellido1 = apellido1[0]
inicial_apellido2 = apellido2[0]

print("La inicial del nombre sería" , inicial_nombre, "La inicial del primer apellido sería: ", inicial_apellido1, "La inicial del segundo apellido sería:"
        , inicial_apellido2)
