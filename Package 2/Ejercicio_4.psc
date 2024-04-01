Proceso Ejercicio_4
	Definir Num1, Num2, result Como Real;
	definir op Como Entero;
	Escribir "ingrese el numero 1 si va a sumar";
	Escribir "ingrese el numero 2 si va a restar";
	Escribir "ingrese el numero 3 si va a multiplicar";
	Escribir "ingrese el numero 4 si va a dividir";
	Leer op;
	Segun op Hacer
		1:
			Escribir "ingrese los dos numeros que va a sumar";
			Leer Num1, Num2;
			result=Num1+Num2;
			Escribir "el resultado de la suma es: ", result;
		2:
			Escribir "ingrese los dos numeros que va a restar";
			Leer Num1, Num2;
			result=Num1-Num2;
			Escribir "el resultado de la resta es: ", result;
		3:
			Escribir "ingrese los dos numeros que va a multiplicar";
			Leer Num1, Num2;
			result=Num1*Num2;
			Escribir "el resultado de la multiplicacion es: ", result;
		4:
			Escribir "ingrese los dos numeros que va a dividir";
			Leer Num1, Num2;
			result=Num1/Num2;
			Escribir "el resultado de la divicion es: ", result;
		De Otro Modo:
			Escribir "No se ecuenta la opcion";
	FinSegun
FinProceso