"""
Algoritmo: Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de
modo que el resultado sea siempre positivo).
"""

print("Insertar dos números con la finalidad de calcular la distancia de ambos: ")

num_1 = float(input("Inserte el primer número: "))
num_2 = float(input("Inserte el segundo número: "))

distancia = abs(num_1 - num_2)
print("·La distancia entre ambos es: ", distancia)
