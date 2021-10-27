"""
Enunciado: Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se
compone de los siguientes porcentajes:

* 55% del promedio de sus tres calificaciones parciales.
* 30% de la calificación del examen final.
* 15% de la calificación de un trabajo final
"""
PESO_PARCIALES = 0.55
print("Vamos a calcular su calificación final\n--------------------------------------")

# Pedimos inputs de las notas
parcial1 = float(input("Inserta la nota del primer parcial: "))
parcial2 = float(input("Inserta la nota del segundo parcial: "))
parcial3 = float(input("Inserta la nota del tercer parcial: "))
examen_final = float(input("Inserta la nota del examen final: "))
trabajo_final = float(input("Inserta la nota del trabajo final: "))

# Calculos
media_parciales = ((parcial1 + parcial2 + parcial3) / 3) * PESO_PARCIALES
examen_nota_final = examen_final * 0.30
nota_trabajo_final = trabajo_final * 0.15
nota_total = media_parciales + examen_nota_final + nota_trabajo_final

print("-------------------------------------------\nLa nota final es > ", nota_total)



