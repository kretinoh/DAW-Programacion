"""

Algoritmo: Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que
está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos
vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
alcanzará el vehículo más rápido al otro.

Lo que queremos saber entre esos dos coches es en cuantos segundos va a alcanzar el 2 vehículo al 1 (porque el 2
vehículo es mas rápido que el 1) para calcular eso sabemos que la velocidad es igual al espacio recorrido, es decir, la
distancia entre ambos, entre el tiempo en minutos, despejando esta ecuación tendríamos que el tiempo en minutos sería
igual a la distancia entre la velocidad en km/h de ambos coches.

"""


velocidad_1 = float(input("Ingresa la velocidad 1 del primer coche: "))
velocidad_2 = float(input("Ingresa la velocidad 2 del primer coche"))
distancia = float(input( "A qué distancia están ambos: "))

tiempo = distancia / (velocidad_1 - velocidad_2)
tiempo = -(tiempo * 60)
print(f"Según los datos ingresadosel tiempo que tardaría en coger el segundo coche al primero sería de: {tiempo} minutos")
