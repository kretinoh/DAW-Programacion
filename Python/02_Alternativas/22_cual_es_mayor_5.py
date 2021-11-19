num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))
num3 = int(input("Introduce un número: "))
num4 = int(input("Introduce un número: "))
num5 = int(input("Introduce un número: "))

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("El número " + str(num1) + " es el mayor número de los tres")
if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("El número " + str(num2) + " es el mayor número de los tres")
if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print("El número " + str(num3) + " es el mayor número de los tres")
if num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print("El número " + str(num4) + " es el mayor número de los tres")
if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
    print("El número " + str(num5) + " es el mayor número de los tres")
    