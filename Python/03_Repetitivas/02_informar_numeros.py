"""
@author Kretinoh
1. Pedir el número de numeros a introducir
2. Pedir numero
3. Comprobar si es myor
4. Comprobar si es igual
5. Comprobar si es menor
"""

cantidad_num = int(input("¿Cuántos numeros introducirá en total? "))
mayores, menores, iguales = 0, 0, 0

while cantidad_num >= 1:
    cantidad_num -= 1
    num = int(input("Introduzca un número: "))
    if num > 0:
        mayores += 1
    if num < 0:
        menores += 1
    if num == 0:
        iguales += 1
print(f"Has introducido un total de {mayores} numeros mayores de cero,"
      f" {menores} numeros menores de cero y {iguales} numeros iguales a cero")
