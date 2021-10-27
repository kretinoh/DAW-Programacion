"""
8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
Programa hecho por Rafael Maestre
"""

print("Calcular comisión y sueldo de un vendedor")

salario = float(input("Introduzca su sueldo base: "))
venta1 = float(input("Introduzca el precio de la venta 1: "))
venta2 = float(input("Introduzca el precio de la venta 2: "))
venta3 = float(input("Introduzca el precio de la venta 3: "))

comision = (venta1 + venta2 + venta3) * 0.1

print("Comisiones de las ventas: ", comision)
print("Su sueldo total es: " + str(salario + comision))

