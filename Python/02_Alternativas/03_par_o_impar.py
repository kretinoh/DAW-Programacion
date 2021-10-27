'''
Escribe un programa que lea un número e indique si es par o impar.
Hecho por Rafael Maestre
'''

num = int(input("Introduce un número para saber si es par o impar: "))

if num % 2 == 0:
    print("El número es par")
elif num % 2 != 0:
    print("El número es impar")
