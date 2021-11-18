"""
@author = kretinoh
Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras
y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6,
 se mostrará el mensaje: “ERROR: número incorrecto.”.
"""
print("Este programa muestra el lado contrario del dado")
lado = int(input("Introduzca un número del dado "))
if 1 <= lado <= 6:
    if lado == 1:
        lado_str = "seis"
        print("En el lado contrario se encuentra el", lado_str)
    if lado == 1:
        lado_str = "seis"
        print("En el lado contrario se encuentra el", lado_str)
    if lado == 2:
        lado_str = "cinco"
        print("En el lado contrario se encuentra el", lado_str)
    if lado == 3:
        lado_str = "cuatro"
        print("En el lado contrario se encuentra el", lado_str)
    if lado == 4:
        lado_str = "tres"
        print("En el lado contrario se encuentra el", lado_str)
    if lado == 5:
        lado_str = "dos"
        print("En el lado contrario se encuentra el", lado_str)
    if lado == 6:
        lado_str = "uno"
        print("En el lado contrario se encuentra el", lado_str)
else:
    print("ERROR: número incorrecto.")
