Proceso Ejercicio_5
	Definir Nombre1, Nombre2 Como Caracter;
	Definir nota1,nota2,nota3,nota4,nota5,nota6,pro1,pro2 Como Real;
	Escribir "Ingrese el nombre del primer estudiante";
	Leer Nombre1;
	Escribir "Ingrese el nombre del segundo estudiante";
	Leer Nombre2;
	Escribir "ingrese las 3 notas del estudiante ", Nombre1;
	Leer nota1,nota2,nota3;
	Escribir "ingrese las 3 notas del estudiante ", Nombre2;
	Leer nota4,nota5,nota6;
	pro1 = (nota1+nota2+nota3)/3;
	pro2 = (nota4+nota5+nota6)/3;
	Si pro1 > pro2 Entonces
		Escribir "el estudiante ", Nombre1," tiene el promedio mayor: ",pro1, " y el estudiante ", Nombre2, " tiene el menor promedio: ", pro2;
	SiNo
		Escribir "el estudiante ", Nombre2," tiene el promedio mayor: ",pro2, " y el estudiante ", Nombre1, " tiene el menor promedio: ", pro1;
	FinSi
FinProceso