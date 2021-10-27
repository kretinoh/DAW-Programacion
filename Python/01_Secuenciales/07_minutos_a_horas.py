"""
7. Realiza un programa que reciba una cantidad de minutos
y muestre por pantalla a cuantas horas y minutos corresponde.
Programa hecho por Rafael Maestre
"""
print("Vamos a pasar minutos a horas y minutos")

minutos_totales = int(input("Introduce los minutos totales: "))

horas = int(minutos_totales / 60)
minutos = int(minutos_totales % 60)

print(str(minutos_totales) + " minutos son " + str(horas) + " horas y " + str(minutos) + " minutos." )
