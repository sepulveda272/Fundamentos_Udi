Proceso Ejercicio_2
	Definir a,b,c Como Real;
	Escribir "ingrese los tres numeros";
	Leer a,b,c;
	Si a > b y a > c Entonces
		Escribir "el numero mayor es: ", a;
	SiNo
		Si b > a y b > c Entonces
			Escribir "el numero mayor es: ", b;
		SiNo
			Escribir "el numero mayor es: ", c;
		FinSi
	FinSi
FinProceso
