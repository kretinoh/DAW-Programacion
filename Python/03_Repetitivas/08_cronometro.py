"""
@author kretinoh
    CREA UN CRONOMETRO

    1. Creamos la hora
    2.ENTRAMOS EN CICLO
        2.2 Creamos la hora
        2.3 Formateamos la hora
        2.4 Imprimimos
        2.5 Esperamos un segundo

@doc https://docs.python.org/3/library/time.html
"""

import time

while True:
    hora_local = time.localtime()
    final = time.strftime("%H:%M:%S", hora_local)
    print(final)
    time.sleep(1)
