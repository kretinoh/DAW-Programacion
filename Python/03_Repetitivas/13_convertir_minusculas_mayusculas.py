cadena = input("Introduce una cadena: ")
cadena_final = ""

for caracter in cadena:
    if caracter.isupper():
        cadena_final += caracter.lower()
    if caracter.islower():
        cadena_final += caracter.upper()
    else:
        cadena_final += caracter
print("La cadena ha quedado tal que así: ", cadena_final)
