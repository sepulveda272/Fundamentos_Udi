Proceso Ejercicio_13
	Definir a, b Como Entero;
	Definir x Como Real;
	Escribir "Para la formula de primer grado ax+b=0 indicar el valor de a y b";
	Leer a,b;
	Si a <> 0 Entonces
		x = -b / a;
		Escribir -b,"/",a, "=",x;
	SiNo
		Si a==0 y b==0 Entonces
			Escribir "Solucion indeterminada";
		SiNo
			Escribir "Solucion imposible";
		FinSi
	FinSi
FinProceso