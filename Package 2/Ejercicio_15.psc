Proceso Ejercicio_15
	definir num1, fraccion como real;
	Escribir "Ingrese un n�mero";
	Leer num1;
	fraccion = trunc(num1);
	Si num1 <> fraccion Entonces
		Escribir "Es un n�mero con fraccionario";
	Sino
		Si num1 == fraccion Entonces
			Escribir "No es un n�mero con fraccionario";
		SiNo
			Escribir "ERROR 404";
		FinSi
	FinSi
FinProceso