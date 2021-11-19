nota = float(input("Cuál es la calificación obtenida: "))

if nota < 5:
    print("Suspenso")
elif 5 <= nota < 7:
    print("Aprobado")
elif 7 <= nota < 9:
    print("Notable")
elif 9 <= nota < 10:
    print("Sobresaliente")
elif nota == 10:
    print("Matricula de honor")
