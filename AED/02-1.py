#Cuadrados y cubos
#Leer dos números y calcular:
#La suma de sus cuadrados.
#El promedio de sus cubos.

print("Cuadrados y cubos")
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

suma = (a**2) + (b**2)
promedio = (a**3 + b**3) / 2

print("La suma de sus cuadrados es: ", suma)
print("El promedio de sus cubos es: ", promedio)