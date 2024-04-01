Proceso Ejercicio_1
	Definir Num Como Entero;
	//Num = azar(101);
	Escribir "ingrese una numero de 0 al 100";
	Leer Num;
	Si Num > 100 o Num < 0 Entonces
		Escribir "por favor ingrese un numero valido";
	SiNo
		Si Num MOD 2 == 0 Entonces
			Escribir "El numero ",Num," es par";
		SiNo
			Escribir "El numero ",Num," es impar";
		FinSi
	FinSi
FinProceso
