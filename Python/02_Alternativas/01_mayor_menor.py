'''
Ejercicio 1
Programa que pida dos números e indique si el primero es mayor que el segundo o no.
'''
print("Vamos a ver que número es mayor")

num1 = int(input("Introduce el primer número: "))

num2 = int(input("Introduce el segundo número"))

if (num1 > num2):
    print("El número "+ num1 + " es mayor que el número " + num2)
else:
	print("El número "+ num2 + " es mayor que el número " + num1)
