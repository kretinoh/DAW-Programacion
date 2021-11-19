print("Vamos a decir cuantos días tiene un mes")

mes = int(input("Introduce el mes (1-12) "))

if 1 <= mes <= 12:
    if mes == 1:
        print("Enero tiene 31 dias")
    elif mes == 2:
        print("Febrero tiene 28 dias")
    elif mes == 3:
        print("Marzo tiene 31 dias")
    elif mes == 4:
        print("Abril tiene 30 dias")
    elif mes == 5:
        print("Mayo tiene 31 dias")
    elif mes == 6:
        print("Junio tiene 30 dias")
    elif mes == 7:
        print("Julio tiene 31 dias")
    elif mes == 8:
        print("Agosto tiene 31 dias")
    elif mes == 9:
        print("Septiembre tiene 30 dias")
    elif mes == 10:
        print("Octubre tiene 31 dias")
    elif mes == 11:
        print("Noviembre tiene 30 dias")
    elif mes == 12:
        print("Diciembre tiene 31 dias")
else:
    print("No has introducido un mes válido")
