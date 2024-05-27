#prestamo banco
#Desarrollar un programa que verifique la edad de una persona
#e indique si es posible otorgarle un prestamo
#condiciones de otorgamiento: 
# sea mayor de edad
# sea menor de 65 años
#caso contrario no se puede otorgar el prestamo

edad = int(input("Ingrese su edad: "))
if edad >= 18 and edad < 65:
    print("Se le Puede otorgar el prestamo")
else:
    print("No se puede otorgar el prestamo")
