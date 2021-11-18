"""
@author = kretinoh

Enunciado:
La política de cobro de una compañía telefónica es: cuando se realiza una llamada,
el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro por minuto,
los siguientes tres, 80 céntimos por minuto, los siguientes dos minutos, 70 céntimos por minuto,
 y a partir del décimo minuto, 50 céntimos por minuto.

Además, se carga un impuesto de 3% cuando es domingo, y si es otro día, en turno de mañana, 15%,
y en turno de tarde, 10%.
Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

Algoritmo:
 Si llamada <= 5min
    precio += 1 * minuto
 Si llamada >5 and <= 8
    precio += 0'80 * minutos
 Si llamada >8 and <= 10
    precio += 0'50 * minutos
 Si dia == domingo
    precio += 3%
 Si dia != domingo
    si tramo == mañana
        precio += 15%
    si tramo == tarde
        precio +=10%

"""
print("Vamos a calcular a que precio le saldrá la llamada")

tramo = input("¿En que tramo del dia llamó (mañana-tarde)? ")
dia = input("Qué dia de la semana llamó? ")
duracion = int(input("Y por último, que duración tuvo la llamada? "))
precio = 0

if duracion <= 5:
    precio = duracion * 1
elif 5 < duracion <= 8:
    precio = duracion * 0.80
elif 8 < duracion <= 10:
    precio = duracion * 0.50
if dia.lower() == "domingo":
    precio += precio * 0.03
elif dia.lower() != "domingo":
    if tramo.lower() == "mañana":
        precio += precio * 0.15
    elif tramo.lower() == "tarde":
        precio += precio * 0.10
    else:
        print("Has introducido un tramo no esperado. El precio final puede no haberse calculado correctamente.")

print("El precio de su llamada ha sido de " + str(precio))
