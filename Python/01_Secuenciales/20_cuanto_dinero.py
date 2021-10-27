"""
@Autor: Rafael Maestre del Río
@Fecha: 21/10/21
Hecho por Rafael Maestre
---------------------------------------
1.Pedimos monedas que tenemos
2.Calculamos el valor de las monedas que tenemos
    total_e(total de euros) = suma del total de los valores de las monedas de 2 y 1 €
    total_c(total de centimos) = Lo mismo
3. Mostramos la cadena final
"""

print("·A partir de las monedas vamos a calcular cuanto dinero tienes en total")

moneda2 = int(input("-Introduzca cuantas monedas de 2 € tienes: "))
moneda1 = int(input("-Introduzca cuantas monedas de 1 € tienes: "))
moneda50 = int(input("-Introduzca cuantas monedas de 50 cents tienes: "))
moneda20 = int(input("-Introduzca cuantas monedas de 20 cents tienes: "))
moneda10 = int(input("-Introduzca cuantas monedas de 10 cents tienes: "))


total_c = (moneda50 * 50) + (moneda20 * 20) + (moneda10 * 10)
total_e = ((moneda2 * 2) + moneda1) + total_c // 100
print(f"·Tengo un total de {total_e} € con {total_c % 100} céntimos.")
