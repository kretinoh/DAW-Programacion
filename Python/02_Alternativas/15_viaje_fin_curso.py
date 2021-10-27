total_alumnos = int(input("Cuantos alumnos van en total a la excursión: "))
precio_persona = 0

if total_alumnos >= 100:
    precio_persona += 65
elif 50 <= total_alumnos <= 99:
    precio_persona += 70
elif 30 <= total_alumnos <= 49:
    precio_persona += 95
elif total_alumnos < 30:
    precio_persona = 4000 / total_alumnos

print(f"El precio a pagar por persona es de un total de {precio_persona} €")
