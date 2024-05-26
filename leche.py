
#Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos
#la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
#el costo tiene un descuento del 10%. Si compra más de 24 unidades, el 
#descuento es del 15%. Además posee la promoción a los jubilados.
#La promoción de jubilados es sumarle un 10% de descuento (si posee otros 
#descuentos, se suma los descuentos).
#Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.


##Ingreso de variables y manejo de exepciones
try: precio_leche_litro = float(input("Ingrese el Precio por Litro de la Leche: "))
except ValueError: print("El valor ingresado no es válido. Inténtalo nuevamente.")

try:unidades_vendidas = int(input("Ingrese la Cantidad de Unidades Vendidas: "))
except ValueError: print("El valor ingresado no es válido. Inténtalo nuevamente.")


## Se valida el descuento adicional
jubilado = input("¿Es cliente Jubilado? (Si/No): ")
jubilado = jubilado.lower()

## Se calcula el descuento en base a la cantidad de unidades
if unidades_vendidas > 12 and unidades_vendidas <= 24:
    descuento = 10
elif unidades_vendidas > 24:
    descuento = 15
else:
    descuento = 0

## Se calcula el descuento adicional
if jubilado == "si":
    descuento = descuento + 10

## Se calcula el total a pagar

##print("El cliente debe pagar: ", (unidades_vendidas * precio_leche_litro) * (1 - (descuento / 100))) 

print("Total de Unidades Vendidas: ", unidades_vendidas)
print("El descuento es: ", descuento, "%")
print("El cliente debe pagar: ", (unidades_vendidas * precio_leche_litro) * (1 - (descuento / 100))) 

