import sys

cadena = input("Introduce la cadena: ")
caracter_a_sustituir = input("Introduce un carácter que quiera sustituir: ")
if len(caracter_a_sustituir) != 1:
    print("No ha introducido un caracter", file=sys.stderr)

caracter_sustituto = input("Introduzca el carácter por el cual sustituiremos: ")
if len(caracter_sustituto) != 1:
    print("No ha introducido un carácter", file=sys.stderr)

cadena_final = ""
for caracter in cadena:
    if caracter == caracter_a_sustituir:
        cadena_final += caracter_sustituto
    else:
        cadena_final += caracter

print("La cadena ha quedado así: ", cadena_final)
