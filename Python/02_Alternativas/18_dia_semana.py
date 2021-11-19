print("Vamos a sacar el dia de la semana")

dia = int(input("Introduce un dia de la semana (1-7) "))

if 1 <= dia <= 7:
    if dia == 1:
        print("Es lunes")
    elif dia == 2:
        print("Es martes")
    elif dia == 3:
        print("Es miércoles")
    elif dia == 4:
        print("Es jueves")
    elif dia == 5:
        print("Es viernes")
    elif dia == 6:
        print("Es sábado")
    elif dia == 7:
        print("Es domingo")
else:
    print("Has introducido un día incorrecto")
