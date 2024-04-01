Proceso Ejercicio_6
    Definir positivo, negativo, neutro Como Entero;
    Definir a, b, c, d, e Como Real;
	Definir cualesPo, cualesNe como caracter;
	cualesPo = "";
	cualesNe = "";
    positivo = 0;
    negativo = 0;
    neutro = 0;
    Escribir "Ingrese el valor de los 5 números:";
    Leer a, b, c, d, e;
    
	Si a > 0 Entonces
		positivo = positivo+1;
		cualesPo = cualesPo  + ConvertirATexto(a) + " ";
	SiNo
		Si a < 0 Entonces
			negativo = negativo +1;
			cualesNe = cualesNe  + ConvertirATexto(a) + " ";
		SiNo
			Si a == 0 Entonces
				neutro = neutro +1;
			SiNo
				Escribir "paila";
			FinSi
		FinSi
	FinSi
	
	Si b > 0 Entonces
		positivo = positivo+1;
		cualesPo = cualesPo  + ConvertirATexto(b) + " ";
	SiNo
		Si b < 0 Entonces
			negativo = negativo +1;
			cualesNe = cualesNe  + ConvertirATexto(b) + " ";
		SiNo
			Si b == 0 Entonces
				neutro = neutro +1;
			SiNo
				Escribir "paila";
			FinSi
		FinSi
	FinSi
	
	Si c > 0 Entonces
		positivo = positivo+1;
		cualesPo = cualesPo  + ConvertirATexto(c) + " ";
	SiNo
		Si c < 0 Entonces
			negativo = negativo +1;
			cualesNe = cualesNe  + ConvertirATexto(c) + " ";
		SiNo
			Si c == 0 Entonces
				neutro = neutro +1;
			SiNo
				Escribir "paila";
			FinSi
		FinSi
	FinSi
	
	Si d > 0 Entonces
		positivo = positivo+1;
		cualesPo = cualesPo  + ConvertirATexto(d) + " ";
	SiNo
		Si d < 0 Entonces
			negativo = negativo +1;
			cualesNe = cualesNe  + ConvertirATexto(d) + " ";
		SiNo
			Si d == 0 Entonces
				neutro = neutro +1;
			SiNo
				Escribir "paila";
			FinSi
		FinSi
	FinSi
	
	Si e > 0 Entonces
		positivo = positivo+1;
		cualesPo = cualesPo  + ConvertirATexto(e) + " ";
	SiNo
		Si e < 0 Entonces
			negativo = negativo +1;
			cualesNe = cualesNe  + ConvertirATexto(e) + " ";
		SiNo
			Si e == 0 Entonces
				neutro = neutro +1;
			SiNo
				Escribir "paila";
			FinSi
		FinSi
	FinSi
	
	Escribir "Cantidad de números positivos:", positivo, "{", cualesPo, "}";
	Escribir "Cantidad de números negativos:", negativo, "{", cualesNe, "}";
	Escribir "Cantidad de números neutros:", neutro;
FinProceso
