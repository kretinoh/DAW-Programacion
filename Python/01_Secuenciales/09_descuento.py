"""
Algoritmo:
Una tienda ofrece un descuento del 15% sobre el total de la compra
y un cliente desea saber cuanto deberá pagar finalmente por su compra.
Hecho por Rafael Maestre
"""
print("Vamos a calcular el precio final de un producto\n------------------------------------------------------")

compra = float(input("Introduzca el precio del producto: "))

descuento_tienda = compra * 0.15
compra_final = compra - descuento_tienda

print("·Está sería la compra sin el descuento: ", compra, "€")
print(f"·Este sería el descuento que le haría a la compra {descuento_tienda:.2} €")
print("·Y esto es lo que pagaría el cliente: ", compra_final, "€")
