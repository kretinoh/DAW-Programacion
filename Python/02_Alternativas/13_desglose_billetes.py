
dato = int(input("Introduce el dinero a desglosar: "))

contador500, contador200, contador100, contador50, contador20, contador10, contador5, contador2, contador1 \
    = 0, 0, 0, 0, 0, 0, 0, 0, 0

while dato != 0:
    if dato >= 500:
        contador500 += 1
        dato %= 500
    elif dato >= 200:
        contador200 += 1
        dato %= 200
    elif dato >= 100:
        contador100 += 1
        dato %= 100
    elif dato >= 50:
        contador50 += 1
        dato %= 50
    elif dato >= 20:
        contador20 += 1
        dato %= 20
    elif dato >= 10:
        contador10 += 1
        dato %= 10
    elif dato >= 5:
        contador5 += 1
        dato %= 5
    elif dato >= 2:
        contador2 += 1
        dato %= 2
    elif dato >= 1:
        contador1 += 1
        dato %= 1

if contador500 != 0:
    print(f"Billetes de 500: {contador500}")
if contador200 != 0:
    print(f"Billetes de 200: {contador200}")
if contador100 != 0:
    print(f"Billetes de 100: {contador100}")
if contador50 != 0:
    print(f"Billetes de 50: {contador50}")
if contador20 != 0:
    print(f"Billetes de 20: {contador20}")
if contador10 != 0:
    print(f"Billetes de 10: {contador10}")
if contador5 != 0:
    print(f"Billetes de 5: {contador5}")
if contador2 != 0:
    print(f"Monedas de 2: {contador2}")
if contador1 != 0:
    print(f"Monedas de 1: {contador1}")
