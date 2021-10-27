
"""
si tipo = A + 0.20 si tamaño es 1
si tipo = A + 0.30 si tamaño es 2
si tipo = B - 0.30 si tamaño es 1
si tipo = B - 0.50 si tamaño es 2
"""

kilos = int(input("Introduce los kilos que ha vendido: "))
tipo = input("¿De qué tipo es (A-B)? ")
tamannio = int(input("¿De que tamaño son, 1 o 2? "))
annadido = 0.0
if tipo.upper() == 'A' and tamannio == 1:
    annadido += 0.20
elif tipo.upper() == 'A' and tamannio == 2:
    annadido += 0.30
elif tipo.upper() == 'B' and tamannio == 1:
    annadido -= 0.30
elif tipo.upper() == 'B' and tamannio == 2:
    annadido -= 0.50

print(f"El precio final del producto es de {annadido * kilos} €")
