Proceso Ejercicio_18
	definir Letra Como Caracter;
	Escribir  "ingrese la su respectiva nota de la A a la F (EN MAYUSCULA LA LETRA) ";
	Leer Letra;
	Si Letra == "A" o Letra == "B" o Letra == "C" o Letra == "D" o Letra == "E" o Letra == "F" Entonces
		Si Letra == "A" Entonces
			Escribir Letra, " = 10";
		SiNo
			Si Letra == "B" Entonces
				Escribir Letra, " = 9";
			SiNo
				Si Letra == "C" Entonces
					Escribir Letra, " = 8";
				SiNo
					Si Letra == "D" Entonces
						Escribir Letra, " = 7";
					SiNo
						Si Letra == "E" Entonces
							Escribir Letra, " = 6";
						SiNo
							Si Letra == "F" Entonces
								Escribir Letra, " = 5";
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	SiNo
		Escribir "aprenda a leer indicaiones ";
	FinSi
FinProceso