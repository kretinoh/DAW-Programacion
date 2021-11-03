"""
@author Kretinoh
Debes de intentar adivinar un número entre 1 y 100
    1. Generar aleatorio
    2. Pedir número
    3. Si se equivoca restamos intento
        3.2 Y salimos bucle
    4.Si no mostramos que es correco
"""
import random

NUM_ALEATORIO = random.randint(1, 100)
intentos = 10

while intentos >= 1:
    intentos -= 1
    num = int(input("Introduzca un número entre 0 y 100: "))
    if num > NUM_ALEATORIO:
        print(f"El número introducido es mayor. Te quedan {intentos} intentos.")
    if num < NUM_ALEATORIO:
        print("El número introducido es menor. Te quedan {intentos} intentos.")
    if num == NUM_ALEATORIO:
        print("Enhorabuena lo has adivinado")
        break
