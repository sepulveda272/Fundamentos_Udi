Algoritmo Ejercicio_19
	Definir Num1 Como Real;
	escribir "escriba el numero entre 1 y 9999 ";
	leer Num1 ;
	si Num1 > 0 y Num1<10 Entonces
		Escribir "el numero ",Num1  ," tiene 1 digito";
	SiNo
		si Num1>=10 y Num1<100 Entonces
			Escribir "el numero ",Num1  ," tiene 2 digitos";
		SiNo
			si Num1>=100 y Num1<1000 Entonces
				Escribir "el numero ",Num1  ," tiene 3 digitos";
			SiNo
				si Num1>=1000 y Num1<=9999 Entonces
					digitos=4;
					Escribir "el numero ",Num1  ," tiene 4 digitos";
				SiNo
					Escribir "el numero no esta en el rango";
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo