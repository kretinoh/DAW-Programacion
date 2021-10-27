"""
Diseña un programa que lea un carácter de teclado y
muestre por pantalla el mensaje «Es signo de puntuación» solo si el carácter leído es un signo de puntuación,
«Es una letra» si es una letra (da igual que sea mayúscula, minúscula o acentuada),
«Es un dígito» si es un dígito,
«Es otro carácter» si no es ninguno de los anteriores y
«No es un carácter» si el usuario ha introducido más de un carácter.
"""
SIGNO_PUNTUACION = ",;:.¿?¡!()<>-_=\"\\"

caracter = input("Introduzca un valor: ")
if len(caracter) == 1:
    if caracter in SIGNO_PUNTUACION:
        print("Es signo de puntuación")
    elif caracter.isalpha():
        print("Es una letra")
    elif caracter.isdigit():
        print("Es un dígito")
    else:
        print("No es un carácter")
else:
    print("La cadena no tiene una longitud válida")
