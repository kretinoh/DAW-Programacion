"""
@author: kretinoh
ENUNCIADO: Haz un programa que juegue al piedra/papel/tijera contra el ordenador, que usará
números aleatorios para realizar la tirada. Después de cada jugada pregunta al usuario si quiere
continuar, en caso negativo se muestra el número de partidas jugadas, las ganadas por cada jugador
y las empatadas.
"""
import sys
from random import randint

opcion = "S"
partidas_jugadas = 0
partidas_ganadas = 0
partidas_perdidas = 0
partidas_empatadas = 0

while opcion.upper() == "S":
    eleccion_usuario = int(input("¿Piedra (1), Papel (2) o Tijera (3)? "))
    if eleccion_usuario != 1 and eleccion_usuario != 2 and eleccion_usuario != 3:
        print("No ha introducido un valor correcto", file=sys.stderr)
    else:
        partidas_jugadas += 1                   # Si ha entrado en el else implica que ya ha jugado una partida
        eleccion_ordenador = randint(0, 3)
        if eleccion_ordenador == 0:
            print("Ordenador juega: Piedra")
            if eleccion_usuario == 1:
                print("EMPATE!")
                partidas_empatadas += 1
            elif eleccion_usuario == 2:
                print("GANASTE!")
                partidas_ganadas += 1
            elif eleccion_usuario == 3:
                print("PERDISTE!")
                partidas_perdidas += 1
        elif eleccion_ordenador == 1:
            print("Ordenador juega: Papel")
            if eleccion_usuario == 1:
                print("PERDISTE!")
                partidas_perdidas += 1
            elif eleccion_usuario == 2:
                print("EMPATE!")
                partidas_empatadas += 1
            elif eleccion_usuario == 3:
                print("GANASTE!")
                partidas_ganadas += 1
        elif eleccion_ordenador == 2:
            print("Ordenador juega: Tijera")
            if eleccion_usuario == 1:
                print("GANASTE!")
                partidas_ganadas += 1
            elif eleccion_usuario == 2:
                print("PERDISTE!")
                partidas_perdidas += 1
            elif eleccion_usuario == 3:
                print("EMPATASTE!")
                partidas_empatadas += 1
        opcion = input("Quieres seguir jugando(S/N)?: ")
if opcion.upper() == "N":
    print(f"Partidas jugadas:{partidas_jugadas}\n"
          f"Partidas ganadas:{partidas_ganadas}\n"
          f"Partidas perdidas:{partidas_perdidas}\n"
          f"Partidas empatadas:{partidas_empatadas}")
