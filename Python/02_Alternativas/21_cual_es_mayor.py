num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))
num3 = int(input("Introduce un número: "))

if num1 > num2 and num1 > num3:
    print("El número " + str(num1) + " es el mayor número de los tres")
if num2 > num1 and num2 > num3:
    print("El número " + str(num2) + " es el mayor número de los tres")
if num3 > num1 and num3 > num2:
    print("El número " + str(num3) + " es el mayor número de los tres")
