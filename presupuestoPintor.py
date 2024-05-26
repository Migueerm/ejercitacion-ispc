print ("Presupuesto de Pintor")

#ingreso de datos

largo = float(input("ingrese el largo: "))
ancho = float(input("ingrese el ancho: "))
precio_metros_cuadrados = float(input("ingrese el precio por metro cuadrado: "))

#calculo del presupuesto

area = largo * ancho
presupuesto = area * precio_metros_cuadrados    

#impresion del presupuesto

print(f"el presupuesto por pintar es: {presupuesto:.2f}")
print(f"Metros cuadrados a pintar: {area:.2f}")