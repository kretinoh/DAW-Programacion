"""
Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir
tres cosas:

El exponente sea positivo, sólo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
"""
base = float(input("Introduce la base: "))
exponente = float(input("Introduce el exponente: "))
potencia = pow(base, exponente)

if exponente > 0:
    print(f"El resultado de la potencia es {potencia}")
elif exponente == 0:
    print("El resultado de la potencia es 1")
elif exponente < 0:
    potencia = 1 / pow(base, abs(exponente))
    print(f"El resultado es {potencia}")
