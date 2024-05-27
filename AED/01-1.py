#División con resto
#Plantear un script (directamente en el shell de Python) que permita informar,
#para dos valores a y b, el cociente y ab el resultado de la división a/b y el resto de esa división.

a = int(input("Ingrese el primer Valor: "))
b = int(input("Ingrese el segundo Valor: "))

cociente = a // b
resto = a % b

print("El cociente es: ", cociente)
print("El resto es: ", resto)