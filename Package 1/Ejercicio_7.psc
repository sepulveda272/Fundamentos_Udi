Proceso Ejercicio_7
	Definir Product1, Product2, Product3, Iva1, Iva2, Iva3, iva Como Real;
	Escribir "Ingrese el porcentaje del IVA: ";
	Leer iva;
	Escribir "Ingrese cuanto vale cada articulo: ";
	leer Product1, Product2, Product3;
	
	Iva1 = Product1*(iva/100);
	Iva2 = Product2*(iva/100);
	Iva3 = Product3*(iva/100);
	
	Escribir " Artículo 1 ";
	Escribir "Valor sin IVA: ", Product1;
	Escribir "Valor del IVA: ", Iva1;
	Escribir "Valor Total: ", Product1 + Iva1;
	
	Escribir " Artículo 2 ";
	Escribir "Valor sin IVA: ", Product2;
	Escribir "Valor del IVA: ", Iva2;
	Escribir "Valor Total: ", Product2 + Iva2;
	
	Escribir " Artículo 3 ";
	Escribir "Valor sin IVA: ", Product3;
	Escribir "Valor del IVA: ", Iva3;
	Escribir "Valor Total: ", Product3 + Iva3;
FinProceso