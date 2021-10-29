"""
Algoritmo: Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que
intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

No solamente necesitamos tener 2 variables si no necesitamos otra variable que guarde el valor de una (en este caso la a
y que esa misma variable aux (auxiliar) le de el valor guardado de "a" a la variable "b"
"""

a = int(input("Introduce la variable A: "))
b = int(input("Introduce la variable B: "))

aux = a
a = b
b = aux

print(f"Nuevo valor de a: {a}")
print(f"Nuevo valor de b: {b}")
