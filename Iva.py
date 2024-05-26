#Desarrollar un programa secuencial que permita ingresar un precio
#calcular el IVA y mostrar el precio final de lista de un producto
#Ejemplo: Si un producto vale $100 y el IVA es 21, el precio de lista es $121

##Ingreso de Precio s/IVA
precio_lista = float(input("Ingrese el precio de lista: "))

##Ingreso de IVA
iva = float(input("Ingrese el porcentaje del IVA: "))

##Calculo de IVA y Precio final
print("El precio final del producto es: ", (precio_lista * (iva / 100) + precio_lista))