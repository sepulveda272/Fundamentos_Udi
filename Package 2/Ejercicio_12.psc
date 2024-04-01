Proceso Ejercicio_12
	Definir num1,num2,num3, op Como real;
	Escribir "ingrese los 3 numeros";
	Leer num1,num2,num3;
	Escribir "ingrese (0 ascendente/1 descendente)";
	Leer op;
	Segun op Hacer
		0:
			Si num1 <= num2 y num2 <= num3 Entonces
				Escribir num1 ,",", num2,",", num3 ;
			SiNo
				Si num1 <= num3 y num3 <= num2 Entonces
					Escribir num1 ,",", num3,",", num2 ;
				SiNo
					Si num2 <= num1 y num1 <= num3 Entonces
						Escribir num2 ,",", num1,",", num3 ;
					SiNo
						Si num2 <= num3 y num3 <= num1 Entonces
							Escribir num2 ,",", num3,",", num1 ;
						SiNo
							Si  num3 <= num1 y num1 <= num2 Entonces
								Escribir num3 ,",", num1,",", num2 ;
							SiNo
								Escribir num3 ,",", num2,",", num1 ;
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
			Escribir "asendente";
		1:
			Si num3 >= num2 y num2 >= num1 Entonces
				Escribir num3 ,",", num2,",", num1 ;
			SiNo
				Si num2 >= num3 y num3 >= num1 Entonces
					Escribir num2 ,",", num3,",", num1 ;
				SiNo
					Si num3 >= num1 y num1 >= num2 Entonces
						Escribir num3 ,",", num1,",", num2;
					SiNo
						Si num1 >= num3 y num3 >= num2 Entonces
							Escribir num1 ,",", num3,",", num2 ;
						SiNo
							Si num2 >= num1 y num1 >= num3 Entonces
								Escribir num2 ,",", num1,",", num3 ;
							SiNo
								Escribir num1 ,",", num2,",", num3 ;
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
			Escribir "desendente";
		De Otro Modo:
			Escribir "ingrese una opcion valida por favor";
	FinSegun
FinProceso
	