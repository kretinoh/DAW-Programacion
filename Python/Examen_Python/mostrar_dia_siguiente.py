"""
@author: kretinoh
ENUNCIADO: Realiza un programa en Python que pida una fecha en formato dd/mm/aaaa del siglo
XXI, compruebe si es correcta, en caso de no serlo, señale el error correspondiente (en el
dispositivo de errores) y acabe el programa de forma anormal, en caso de ser correcta, que muestre
el día siguiente a la misma en el mismo formato.
"""
from datetime import datetime
fecha = input("Introduce una fecha en el formato dd/mm/yyyy: ")
if len(fecha) != 10:
    print("Ha introducido una fecha erronea.")
else:
    fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
    fecha_objeto = fecha_objeto.replace(fecha_objeto.day + 1)
    print(fecha_objeto)

