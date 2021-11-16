"""
@author kretinoh
1.Pedir num inicio
2.Pedir num fin
3.Si el numero es par
    3.2 for i in range ini fin 2
        3.3 mostrar num
    3.4 for i in range ini + 1 fin 2
        3.5 mostrar num
"""

num_ini = int(input("Introduce el numero de inicio: "))
num_fin = int(input("Introduce el numero de fin: "))

if num_ini < num_fin:
    if num_ini % 2 == 0:
        for i in range(num_ini, num_fin + 1, 2):
            print(i)
    else:
        for i in range(num_ini + 1, num_fin + 1, 2):
            print(i)
else:
    print("Has introducido un número mayor de inicio que el inicio")
