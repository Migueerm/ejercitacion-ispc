print ("Programa que calcula el promedio de 5 notas")

#se ingresan las notas

nota1 = float(input("ingrese la primera nota: "))
nota2 = float(input("ingrese la segunda nota: "))
nota3 = float(input("ingrese la tercera nota: "))
nota4 = float(input("ingrese la cuarta nota: "))
nota5 = float(input("ingrese la quinta nota: "))

#se calcula el promedio

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

#se imprime el promedio

print(f"el promedio del estudiante es: {promedio:.2f}")

##  f-string, una característica de Python que permite insertar expresiones dentro de cadenas de texto precediendo la cadena con la letra ‘f’. Las expresiones se indican entre llaves {}