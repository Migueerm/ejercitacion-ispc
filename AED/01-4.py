#Últimos dígitos
#¿Cómo usaría el operador resto ( %) para obtener el valor del úlƟmo dígito de un número entero?
#¿Y cómo obtendría los dos ultimos dígitos? Desarrolle un programa que cargue un número entero por
#teclado, y muestre el ultimo dígito del mismo (por un lado) y los dos ultimos dígitos (por otro lado)
#[Ayuda: ¿cuáles son los posibles restos que se obƟenen de dividir un número cualquiera por 10?]


#Ingreso de Datos
print("Programa que calcula los dos ultimos digitos de un numero")
numero = int(input("Ingrese un numero entero: "))

#Calculo de los dos ultimos digitos
Unidad = numero % 10
Decena = numero % 100
print("EL numero correspondiente al ultimo (unidad) es: ", Unidad)
print("Los ultimos 2 digitos son: ", Decena)