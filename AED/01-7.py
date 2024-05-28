#Precio del boleto
#Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia. Para el cálculo
#del mismo se debe considerar el monto base (que se cobra siempre), más un valor extra calculado en
#base a la cantidad de kilómetros a recorrer: Por cada kilómetro a recorrer se cobra $0,30 de adicional.

#Ingreso de datos

print("Calculo del costo de viaje")
print("Ingrese el costo base: ")
costo_base = float(input())
print("Ingrese la distancia en kilómetros: ")
distancia = float(input())
extra_km = 0.30
costo_exra = distancia * extra_km
costo_total = costo_base + costo_exra
print(f"El costo total del viaje es de: {costo_total:.2f}")
