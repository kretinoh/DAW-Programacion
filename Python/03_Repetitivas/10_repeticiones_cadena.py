"""
@author: kretinoh
cuenta las ocurrencias de un carácter pedido por teclado de una cadena ingresada por teclado
"""
import sys

cadena = input("Introduce una cadena: ")
letra = input("Introduce la letra a buscar en la cadena: ")

if len(letra) == 1:
    ocurrencias = 0
    for i in cadena:
        if i == letra:
            ocurrencias += 1
    # print("Hay un total de", cadena.count(letra), letra)      ESTA ES LA FORMA SIN BUCLE
    print(f"El carácter {letra} aparece en la cadena {ocurrencias} veces")
else:
    print("Has introducido más de una ", file=sys.stderr)
