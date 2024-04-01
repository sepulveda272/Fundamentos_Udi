Proceso Ejercicio_11
	definir trabCasa, trabCla, acumulativo, actidinal, autoev, final, falta como real;
	Escribir "Ingrese las notas teniendo en cuenta el siguiente orden";
	Escribir "Trabajo en casa / Trabajo en clase / acumulativo / actitudinal / autoevaluacion";
	Leer trabCasa, trabCla, acumulativo, actidinal, autoev;
	final = (trabCasa * 0.2) + (trabCla * 0.35) + (acumulativo * 0.2) + (actidinal * 0.2) + (autoev * 0.05);
	Si (trabCasa > 10 o trabCla > 10 o acumulativo > 10 o actidinal > 10 o autoev > 10) o (trabCasa < 0 o trabCla < 0 o acumulativo < 0 o actidinal < 0 o autoev < 0) entonces
		Escribir "Valores ingresados fuera del rango";
	Sino 
		Si final < 6.5 y acumulativo == 0 Entonces
			falta = 6.5 - final;
			Escribir "Pendiente de una nota minima de: ", falta;
		Sino
			Si final > 6.5 entonces
				Escribir "APROBADO";
			Sino
				Si final < 6.5 y acumulativo <> 0 Entonces
					Escribir "NO APROBADO";
				SiNo
					Escribir "ERROR 404";
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
