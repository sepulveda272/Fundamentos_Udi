Proceso Ejercicio_14
	Definir num1, num2, num3, num4, num5, num6, num7,num8 ,num9 ,num10, media, rango, mayor, menor Como Real;
	
	Escribir "Ingrese 10 números positivos: ";
	Leer num1, num2, num3, num4, num5, num6, num7,num8 ,num9 ,num10;
	
	Si num1 > 0 y num2 > 0 y num3 > 0 y num4 > 0 y num5 > 0 y num6 > 0 y num7 > 0 y num8 > 0 y num9 > 0 y num10 > 0 Entonces
		Si	num1 >= num2 y num1 >= num3 y num1 >= num4 y num1 >= num5 y num1 >= num6 y num1 >= num7 y num1 >= num8 y num1 >= num9 y num1 >= num10 Entonces
			mayor = num1;
		SiNo
			Si num2 >= num1 y num2 >= num3 y num2>= num4 y num2 >= num5 y num2 >= num6 y num2 >= num7 y num2 >= num8 y num2 >= num9 y num2 >= num10 Entonces
				mayor = num2;
			SiNo
				Si num3 >= num1 y num3 >= num2 y num3 >= num4 y num3 >= num5 y num3 >= num6 y num3 >= num7 y num3 >= num8 y num3 >= num9 y num3 >= num10 Entonces
					mayor = num3;
				SiNo
					Si num4 >= num1 y num4 >= num2 y num4 >= num3 y num4 >= num5 y num4 >= num6 y num4 >= num7 y num4 >= num8 y num4 >= num9 y num4 >= num10 Entonces
						mayor = num4;
					SiNo
						Si num5 >= num1 y num5 >= num2 y num5 >= num3 y num5 >= num4 y num5 >= num6 y num5 >= num7 y num5 >= num8 y num5 >= num9 y num5 >= num10 Entonces
							mayor = num5;
						SiNo
							Si num6 >= num1 y num6 >= num2 y num6 >= num3 y num6 >= num4 y num6 >= num5 y num6 >= num7 y num6 >= num8 y num6 >= num9 y num6 >= num10 Entonces
								mayor = num6;
							SiNo
								Si num7 >= num1 y num7 >= num2 y num7 >= num3 y num7 >= num4 y num7 >= num5 y num7 >= num6 y num7 >= num8 y num7 >= num9 y num7 >= num10 Entonces
									mayor = num7;
								SiNo
									Si num8 >= num1 y num8 >= num2 y num8 >= num3 y num8 >= num4 y num8 >= num5 y num8 >= num6 y num8 >= num7 y num8 >= num9 y num8 >= num10 Entonces
										mayor = num8;
									SiNo
										Si num9 >= num1 y num9 >= num2 y num9 >= num3 y num9 >= num4 y num9 >= num5 y num9 >= num6 y num9 >= num7 y num9 >= num8 y num9 >= num10 Entonces
											mayor = num9;
										SiNo
											mayor = num10;
										FinSi
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
		
		Si	num1 <= num2 y num1 <= num3 y num1 <= num4 y num1 <= num5 y num1 <= num6 y num1 <= num7 y num1 <= num8 y num1 <= num9 y num1 <= num10 Entonces
			menor = num1;
		SiNo
			Si num2 <= num1 y num2 <= num3 y num2<= num4 y num2 <= num5 y num2 <= num6 y num2 <= num7 y num2 <= num8 y num2 <= num9 y num2 <= num10 Entonces
				menor = num2;
			SiNo
				Si num3 <= num1 y num3 <= num2 y num3 <= num4 y num3 <= num5 y num3 <= num6 y num3 <= num7 y num3 <= num8 y num3 <= num9 y num3 <= num10 Entonces
					menor = num3;
				SiNo
					Si num4 <= num1 y num4 <= num2 y num4 <= num3 y num4 <= num5 y num4 <= num6 y num4 <= num7 y num4 <= num8 y num4 <= num9 y num4 <= num10 Entonces
						menor = num4;
					SiNo
						Si num5 <= num1 y num5 <= num2 y num5 <= num3 y num5 <= num4 y num5 <= num6 y num5 <= num7 y num5 <= num8 y num5 <= num9 y num5 <= num10 Entonces
							menor = num5;
						SiNo
							Si num6 <= num1 y num6 <= num2 y num6 <= num3 y num6 <= num4 y num6 <= num5 y num6 <= num7 y num6 <= num8 y num6 <= num9 y num6 <= num10 Entonces
								menor = num6;
							SiNo
								Si num7 <= num1 y num7 <= num2 y num7 <= num3 y num7 <= num4 y num7 <= num5 y num7 <= num6 y num7 <= num8 y num7 <= num9 y num7 <= num10 Entonces
									menor = num7;
								SiNo
									Si num8 <= num1 y num8 <= num2 y num8 <= num3 y num8 <= num4 y num8 <= num5 y num8 <= num6 y num8 <= num7 y num8 <= num9 y num8 <= num10 Entonces
										menor = num8;
									SiNo
										Si num9 <= num1 y num9 <= num2 y num9 <= num3 y num9 <= num4 y num9 <= num5 y num9 <= num6 y num9 <= num7 y num9 <= num8 y num9 <= num10 Entonces
											menor = num9;
										SiNo
											menor = num10;
										FinSi
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
		media = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10) / 10;
		rango = mayor - menor;
		Escribir "La media aritmetica de los 10: ", media;
		Escribir "El rango de los 10 números es: ", rango;
	SiNo
		Escribir "por favor ingrese numeros positivos no negativos";
	FinSi
FinProceso