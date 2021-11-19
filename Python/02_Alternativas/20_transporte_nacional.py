PRECIO_AMERICA_N = 24
PRECIO_AMERICA_C = 20
PRECIO_AMERICA_S = 21
PRECIO_EUROPA = 10
PRECIO_ASIA = 18
precio = 0

gramos = float(input("Cuántos gramos va a transportar: "))

if gramos < 5000:
    zona = int(input("A que ubicación transportará (1-5)\n"
                     "1.America del norte\n"
                     "2.America Central\n"
                     "3.America del Sur\n"
                     "4.Europa\n"
                     "5.Asia"))
    if 1 <= zona <= 5:
        if zona == 1:
            precio = gramos * PRECIO_AMERICA_N
        if zona == 2:
            precio = gramos * PRECIO_AMERICA_C
        if zona == 3:
            precio = gramos * PRECIO_AMERICA_S
        if zona == 4:
            precio = gramos * PRECIO_EUROPA
        if zona == 5:
            precio = gramos * PRECIO_ASIA
    else:
        print("Ha introducido una zona incorrecta.")
    print("El precio total es " + str(precio) + " €")
else:
    print("No trabajamos con tanto peso. Disculpe las molestias")
