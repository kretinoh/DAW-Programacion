"""
@author kretinoh
1. Pedir carácter
3. Si es vocal
    3.2 Imprimir es vocal
4. Si no es vocal
    4.2 Imprimir no es vocal
5. Si es espacio
    5.2 Acabar programa
"""
VOCALES = "aeiou"

while 1 == 1:
    caracter = input("Introduzca un carácter: ")
    if len(caracter) == 1:
        if caracter == " ":
            print("Saliendo del programa.")
            break
        if caracter.lower() in VOCALES:
            print("El carácter es una vocal")
        else:
            print("El carácter no es una vocal")
    else:
        print("Has introducido una longitud errónea vuelva a intentarlo. ")
