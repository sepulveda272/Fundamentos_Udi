Proceso Ejercicio_7
	Definir ValorHo,valorTotal, diferencia,valorBase , valorExtra  Como Real;
	Definir horasTra Como Entero;
	diferencia = 0;
	Escribir "ingrese el valor de las horas: ";
	Leer ValorHo;
	Escribir  "horas trabajadas: ";
	Leer horasTra;
	
	Si horasTra >= 0 y horasTra <= 40 Entonces
		valorBase =  ValorHo * horasTra;
		valorTotal = valorBase;
		Escribir valorTotal;
	SiNo
		valorBase = ValorHo * 40;
	FinSi
	
	Si horasTra >= 41 y horasTra <= 48 Entonces
		diferencia = horasTra - 40;
		valorExtra = diferencia * (ValorHo*2);
		valorTotal = valorBase + valorExtra;
		Escribir valorTotal;
	FinSi
	
	Si horasTra > 48 Entonces
		diferencia = horasTra - 48;
		valorExtra = 8*ValorHo*2;
		valorExtra = valorExtra + (diferencia * (ValorHo*3));
		valorTotal = valorBase + valorExtra;
		Escribir valorTotal;
	FinSi
	
FinProceso

