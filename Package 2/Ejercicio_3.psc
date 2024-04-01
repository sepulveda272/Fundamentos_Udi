Proceso Ejercicio_3
	Definir a,b,c,d Como Real;
	Escribir "ingrese los cuatro numeros";
	Leer a,b,c,d;
	Si a > b y a > c y a > d Entonces
		Escribir "el numero mayor es: ", a;
	SiNo
		Si b > a y b > c y b > d Entonces
			Escribir "el numero mayor es: ", b;
		SiNo
			Si c > a y c > b y c > d Entonces
				Escribir "el numero mayor es: ", c;
			SiNo
				Escribir "el numero mayor es: ", d;
			FinSi
		FinSi
	FinSi
FinProceso
