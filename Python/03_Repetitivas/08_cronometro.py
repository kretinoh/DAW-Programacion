"""
@author kretinoh
    Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

    1. Creamos la hora
    2.ENTRAMOS EN CICLO
        2.2 Creamos la hora
        2.3 Formateamos la hora
        2.4 Imprimimos
        2.5 Esperamos un segundo

https://docs.python.org/3/library/time.html
He usado metodo sleep de este módulo
"""

import time

while True:
    hora_local = time.localtime()
    final = time.strftime("%H:%M:%S", hora_local)
    print("\b"*8 + final, end="")
    time.sleep(1)
