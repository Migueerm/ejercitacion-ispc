Algoritmo Ejercicio2_2_04_d
	Definir a,b,c,d Como Entero;
	
    Escribir "Ingrese 4 numeros, se determinara cual es el mayor y cual es el menor"
    
    Escribir "Ingrese el primer numero";
    Leer a;
    
    Escribir "Ingrese el segundo numero";
    Leer b;
    
    Escribir "Ingrese el tercer numero";
    Leer c;
    
	Escribir "Ingrese el cuarto numero";
    Leer d;
	
    Si a=b o a=c o b=c O a=d O c=d O a=d Entonces
        Escribir "Existen numeros iguales";
    Fin Si
    
    Si (a>b) Y (a>c) Y (a>d) Entonces
        Escribir "El primer numero es el mayor ",a;
    SiNo
        Si (b>a) Y (b>c) Y (b>d) Entonces
			Escribir "El segundo numero es el mayor ",b;
		SiNo
			Si (c>a) Y (c>b) Y (c>d) Entonces
				Escribir "El tercer numero es el mayor ",c;
			SiNo
				Si (d>a) Y (d>b) Y (d>c) Entonces
					Escribir "El cuarto numero es el mayor ",d;
				Fin Si
			Fin Si
		Fin Si
    Fin Si
	
	Si (a<b) Y (a<c) Y (a<d) Entonces
        Escribir "El primer numero es el menor ",a;
    SiNo
        Si (b<a) Y (b<c) Y (b<d) Entonces
			Escribir "El segundo numero es el menor ",b;
		SiNo
			Si (c<a) Y (c<b) Y (c<d) Entonces
				Escribir "El tercer numero es el menor ",c;
			SiNo
				Si (d<a) Y (d<b) Y (d<c) Entonces
					Escribir "El cuarto numero es el menor ",d;
				Fin Si
			Fin Si
		Fin Si
    Fin Si
    
FinAlgoritmo
