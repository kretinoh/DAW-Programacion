'''
Crea un programa que pida al usuario dos números
y muestre su división si el segundo no es cero,
o un mensaje de aviso en caso contrario.
Hecho por Rafael Maestre
'''

num1 = float(input("Introduzca un número: "))
num2 = float(input("Introduzca un número: "))

if num2 != 0:
    resultado = num1 / num2
    print(f"La división de {num1} y {num2} da como resultado: {resultado} ")
else:
    print("Fallo al dividir no se puede dividir entre 0 melón")
