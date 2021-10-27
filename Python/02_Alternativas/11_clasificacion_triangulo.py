
datoA = float(input("Introduce el lado A: "))
datoB = float(input("Introduce el lado B: "))
datoC = float(input("Introduce el lado C: "))

pitagoras = datoA + (datoB ** 2)

if pitagoras == datoC ** 2:
    print("Triángulo rectangulo")
elif datoA == datoB or datoA == datoC or datoB == datoC:
    print("El triángulo es isósceles")
elif datoA == datoB and datoB == datoC:
    print("El triángulo es equilátero")
else:
    print("El triángulo es escaleno")
