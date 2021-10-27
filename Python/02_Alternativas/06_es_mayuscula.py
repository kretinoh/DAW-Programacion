"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
Hecho por Rafael Maestre
"""

cadena = input("Introduce la cadena para ver si es mayúscula: ")
if len(cadena) == 1:
    if cadena.isalpha() and cadena.isupper():
        print("La cadena está en mayúsculas")
    elif cadena.isalpha():
        print("La cadena no está en mayúsculas")
    else:
        print("No has introducido una letra válida")
else:
    print("La longitud de la cadena es mayor de la esperada")
