Proceso Ejercicio_10
	Definir quiz1, trabajos1, parcial1, quiz2, trabajos2, parcial2, quiz3, trabajos3, parcial3, nota_final como Real;
	
    Escribir "Ingrese la nota del quiz del primer corte (de 0 a 5):";
    Leer quiz1;
    Escribir "Ingrese la nota de los trabajos del primer corte (de 0 a 5):";
    Leer trabajos1;
    Escribir "Ingrese la nota del parcial del primer corte (de 0 a 5):";
    Leer parcial1;
	
    Escribir "Ingrese la nota del quiz del segundo corte (de 0 a 5):";
    Leer quiz2;
    Escribir "Ingrese la nota de los trabajos del segundo corte (de 0 a 5):";
    Leer trabajos2;
    Escribir "Ingrese la nota del parcial del segundo corte (de 0 a 5):";
    Leer parcial2;
	
    Escribir "Ingrese la nota del quiz del tercer corte (de 0 a 5):";
    Leer quiz3;
    Escribir "Ingrese la nota de los trabajos del tercer corte (de 0 a 5):";
    Leer trabajos3;
    Escribir "Ingrese la nota del parcial del tercer corte (de 0 a 5):";
    Leer parcial3;
	
    nota_final <- (quiz1 * 0.05 + trabajos1 * 0.05 + parcial1 * 0.2) + (quiz2 * 0.05 + trabajos2 * 0.05 + parcial2 * 0.2) + (quiz3 * 0.05 + trabajos3 * 0.05 + parcial3 * 0.3);
	
    Si nota_final >= 3 Entonces
        Escribir "La nota final del estudiante es:", nota_final, " y ha aprobado.";
    Sino
        Escribir "La nota final del estudiante es:", nota_final, " y no ha aprobado.";
    FinSi;
FinProceso
