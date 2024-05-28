#Viaje Córdoba-Rosario
#Un vehículo parte de la ciudad de Córdoba y se dirige a Rosario por autopista. 
#La distancia aproximada entre ambas ciudades es de 400 kilómetros. El vehículo se desplaza con velocidad promedio de 122 km/h.
#Desarrolle un programa que calcule el tempo total en horas que demorará ese vehículo en llegar a
#Rosario. De nuevo, no es necesario converƟr a horas, minutos y segundos: exprese en resultado como
#un número real, tal cual lo haya obtenido del cálculo

#Ingreso de datos
print("Calculo de tiempo de viaje")
print("Ingrese distancia en KM: ")
distancia = float(input())
print("Ingrese la velocidad promedio: ")
velocidad = float(input())

#Calculo de tiempo
tiempo = distancia / velocidad
print(f"El tiempo de viaje en horas es de: {tiempo:.2f}")