"""
@author kretinoh
potencia
"""
potencia = 1

base = float(input("Introduce la base: "))
exponente = abs(int(input("Introduce el exponente: ")))

while exponente > 0:
    potencia *= base
    exponente -= 1

print(f"La potencia es: {potencia}")
