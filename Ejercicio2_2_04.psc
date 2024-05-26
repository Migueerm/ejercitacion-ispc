Algoritmo Ejercicio2_2_04
	Definir a,b,c Como Entero;
	
    Escribir "Ingrese 3 numeros, se determinara cual es el mayor y cual es el menor"
    
    Escribir "Ingrese el primer numero";
    Leer a;
    
    Escribir "Ingrese el segundo numero";
    Leer b;
    
    Escribir "Ingrese el tercer numero";
    Leer c;
    
    Si a=b o a=c o b=c Entonces
        Escribir "Existen numeros iguales";
    Fin Si
    
    Si (a>b) Y (a>c) Entonces
        Escribir "El primer numero es el mayor ",a;
    SiNo
        Si (b>a) Y (b>c) Entonces
			Escribir "El segundo numero es el mayor ",b;
		SiNo
				Si (c>a) Y (c>b) Entonces
					Escribir "El tercer numero es el mayor ",c;
				Fin Si
		Fin Si
    Fin Si
	
	Si (a<b) Y (a<c) Entonces
        Escribir "El primer numero es el menor ",a;
    SiNo
        Si (b<a) Y (b<c) Entonces
			Escribir "El segundo numero es el menor ",b;
		SiNo
			Si (c<a) Y (c< b) Entonces
				Escribir "El tercer numero es el menor ",c;
			Fin Si
		Fin Si
    Fin Si
    
FinAlgoritmo
