Algoritmo Ejercicio1_2_04
	Escribir "introduzca 2 numeros";
	
	Escribir "ingrese el primer numero";
	Leer num1;
	
	Escribir "ingrese el segundo numero";
	Leer num2;
	
	Si num1=num2 Entonces
		Escribir "Ambos numeros son iguales";
	SiNo
		Si num1>num2 Entonces
			Escribir "el primer numero es el mayor ",num1;
		SiNo
			Escribir "el segundo numero es el mayor ",num2;
		Fin Si
	Fin Si
	
	
FinAlgoritmo
