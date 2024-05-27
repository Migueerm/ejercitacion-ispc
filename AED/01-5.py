#Conversión de medidas
#Desarrolle un programa para converƟr una medida dada en pies a sus equivalentes en:
#yardas
#pulgadas
#cenơmetros
#metros
#Sabiendo que:
#1 pie = 12 pulgadas
#1 yarda = 3 pies
#1 pulgada = 2.54 cenơmetros
#1 metro = 100 cenơmetros


#Ingreso de datos
print("Conversión de medidas")
pies = float(input("ingrese la cantidad de pies: "))

#Conversiones
yardas = pies/3
pulgadas = pies*12
centimetros = pulgadas*2.54
metros = centimetros/100

#Impresión de resultados
print(f"la cantidad de yardas es: {yardas:.2f}")
print(f"la cantidad de pulgadas es: {pulgadas:.2f}")
print(f"la cantidad de centimetros es: {centimetros:.2f}")
print(f"la cantidad de metros es: {metros:.2f}")