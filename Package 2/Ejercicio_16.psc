Proceso Ejercicio_16
	Definir year Como Entero;
	Escribir "ingrese el año";
	Leer year;
	si (year <= 1582) entonces
		Escribir "por la presentacion de la epoca consulte con el calendario gregoriano";
	SiNo
		
		si (year mod 4 == 0 y year mod 100 <> 0 ) Entonces
			Escribir  "es bisisesto";
		SiNo
			si (year mod 400 == 0 ) Entonces
				Escribir "es bisiesto";
			SiNo
				Escribir "no es bisiesto";
			FinSi
		FinSi
	FinSi
FinProceso
