"""
6. Calcular la media de tres números pedidos por teclado.
Programa hecho por Rafael Maestre
"""
import statistics as stats

print("Vamos a calcular la media de 3 números")
lista = []

for i in range(0, 3):
    num = float(input("Introduce un número: "))
    lista.append(num)

print("La media es : " + str(stats.mean(lista)))
