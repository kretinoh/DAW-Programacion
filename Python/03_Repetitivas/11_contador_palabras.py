cadena = input("Introdce una frase: ")

# palabras = len(cadena.split()) CONTADOR SIN FOR
anterior = " "
contador = 0
for caracter in cadena:
    if caracter != " " and anterior == " ":
        contador += 1
    anterior = caracter
print("Hay un total de " + str(contador) + " palabras")
