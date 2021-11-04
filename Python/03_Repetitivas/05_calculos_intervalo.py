"""
@author kretinoh

1. Pedir limite inferior
2. Pedir limite superior
3. SI limite_inferior > limite_superior
    3.2 Volver a pedir limites
4.SI num != 0
    4.2
"""
suma = 0
contador = 0
iguales = 0

min_limit = int(input("Introduzca el limite inferior: "))
max_limit = int(input("Introduzca el limite superior: "))

while min_limit > max_limit:
    print("El limite inferior no puede ser mayor que el superior.")
    print("Introduzca de nuevo los límites.\n")
    min_limit = int(input("Introduzca el limite inferior: "))
    max_limit = int(input("Introduzca el limite superior: "))

num = int(input("Introduzca un número (Si introduce cero, saldrá del programa). "))

while num != 0:
    if min_limit < num < max_limit:
        suma += num
    else:
        contador += 1
        if num == min_limit or num == max_limit:
            iguales = True
    num = int(input("Introduzca un número (Cero acabará el programa). "))

print(f"La suma de los números en el intervalo es {suma}\n"
      f"Hay un total de {contador} numeros fuera del intervalo")
if iguales:
    print("Hay números iguales a los limites")
else:
    print("No hay numeros iguales a los límites")

