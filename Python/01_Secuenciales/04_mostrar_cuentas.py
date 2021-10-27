"""
4. Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
Programa hecho por Rafael Maestre
"""
print("Vamos a mostrar la suma, resta, división y multiplicación de dos numeros\n")

print("Introduce el primer número: ")
num1 = float(input())

print("Introduce el segundo número: ")
num2 = float(input())

# BANNER PARA MOSTRAR DATOS
print("1.Suma de " + str(num1) + " + " + str(num2) + ": " + str(num1 + num2) + "\n"
      + "2.Resta de " + str(num1) + " - " + str(num2) + ": " + str(num1 - num2) + "\n"
      + "3.División de " + str(num1) + " / " + str(num2) + ": " + str(num1 / num2) + "\n"
      + "4.Multiplicación de " + str(num1) + " x " + str(num2) + ": " + str(num1 * num2))
print(f"La suma entre {num1} y {num2} es {num1+num2:}")
