
annio = int(input("Introduce un año para saber si es bisiesto: "))

if annio % 4 != 0:
    print("No es bisiesto")
elif annio % 4 == 0 and annio % 100 != 0:
    print("Es bisiesto")
elif annio % 4 == 0 and annio % 100 == 0 and annio % 400 != 0:
    print("No es bisiesto")
elif annio % 4 == 0 and annio % 100 == 0 and annio % 400 == 0:
    print("Es bisiesto")
