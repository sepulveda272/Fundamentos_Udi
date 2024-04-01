Proceso Ejercicio_8
	Definir num1,num2,num3,num4,result Como Entero;
	result = 0;
	Escribir "ingrese 4 numeros";
	Leer num1,num2,num3,num4;
	Si num1 + num2 == num3 o num1 + num2 == num4 Entonces
		result = result + 1;
	FinSi
	si num1 + num3 == num2 o num1 + num3 == num4 Entonces
		result = result + 1;
	FinSi
	si num1 + num4 == num2 o num1 + num4 == num3 Entonces
		result = result + 1;
	FinSi
	si num2 + num4 == num1 o num2 + num4 == num3 Entonces
		result = result + 1;
	FinSi
    si num3 + num2 == num1 o num3 + num2 == num4 Entonces
		result = result + 1;
	FinSi
	si num4 + num3 == num1 o num4 + num3 == num2 Entonces
		result = result + 1;
	FinSi
	Si result > 0 Entonces
		Escribir "SI ", result;
	SiNo
		Escribir "No se encontro";
	FinSi
FinProceso