"""
Creado el día 09/10/2021

Algoritmo: Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar
a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

Hay que convertir la hora y los minutos de la salida a segundos y sumárselos a los segundos que ha tardado en llegar a
la otra ciudad
"""

horas_salida = int(input("Hora de la que ha partido de la ciudad: "))
minutos_salida = int(input("Minutos de los que ha partido de la ciudad: "))
segundos_salida = int(input("Segundos a los que ha salido de la ciudad: "))
segundos_llegada = int(input("El tiempo en segundos que ha tardado en llegar a la otra ciudad: "))

print("Lo pasamos todo a segundos para poder sumarle los segundos de la llegada a la otra ciudad: ")
segundos_totales = horas_salida * 3600 + minutos_salida * 60 + segundos_salida
segundos_totales = segundos_totales + segundos_llegada

horas_finales = round(segundos_totales / 3600, 2)
minutos_finales = round((segundos_totales % 3600) / 60, 2)
segundos_finales = round((segundos_totales % 3600) % 60, 2)

print(f"La hora a la que ha llegado a la otra ciudad sería {horas_finales} horas {minutos_finales} minutos y {segundos_finales} segundos")
