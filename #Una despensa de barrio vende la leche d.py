#Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos
#la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
#el costo tiene un descuento del 10%. Si compra más de 24 unidades, el 
#descuento es del 15%. Además posee la promoción a los jubilados.
#La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos).
#Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

def calcular_costo_leche(cantidad_unidades, es_jubilado):
    # Paso 1: Cálculo del Precio sin Descuento
    precio_unitario = 1000
    costo_sin_descuento = cantidad_unidades * precio_unitario

    # Paso 2: Aplicación de Descuentos
    descuento_por_cantidad = 0
    if 12 < cantidad_unidades <= 24:
        descuento_por_cantidad = 0.10
    elif cantidad_unidades > 24:
        descuento_por_cantidad = 0.15

    descuento_adicional_jubilado = 0
    if es_jubilado:
        descuento_adicional_jubilado = 0.10

    # Paso 3: Cálculo del Costo Total con Descuentos
    costo_total = costo_sin_descuento * (1 - descuento_por_cantidad) * (1 - descuento_adicional_jubilado)
    return costo_total

# Entrada de Datos
cantidad_unidades = int(input("Ingrese la cantidad de unidades de leche que desea comprar: "))
es_jubilado = input("¿Es usted jubilado? (Si/No): ").lower() == "si"

# Llamamos a la función y mostramos el resultado
costo_total_leche = calcular_costo_leche(cantidad_unidades, es_jubilado)
print(f"El costo total a pagar es de ${costo_total_leche:.2f}")
