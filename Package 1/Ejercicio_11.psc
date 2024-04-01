Proceso Ejercicio_11
	Definir corte1, corte2, corte3, Final Como Real;
	Escribir "Ingrese la nota del primer, segundo y tercer corte del estudiante teodoro: ";
	Leer corte1, corte2, corte3;
	Final = (corte1 * 0.30) + (corte2 * 0.30) + (corte3 * 0.40);
	Final = Final * 100;
	Final = trunc(Final);
	Final = Final / 100;
	Escribir "La nota definitiva de Teodoro es ", Final;
FinProceso