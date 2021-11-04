"""
@author kretinoh

1. Creamos la hora
2. formateamos la hora
3. imprimimos
4. esperamos 1 sec
"""

import time

while True:
    hora_local = time.localtime()
    final = time.strftime("%H:%M:%S", hora_local)
    print(final)
    time.sleep(1)
