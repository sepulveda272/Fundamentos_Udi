Proceso Ejercicio_17
	Definir precio, descuento, Final Como Real;
	Escribir "Ingresa el valor del pantalon: ";
	Leer precio;
	Escribir "Ingresa el porcentaje de descuento que tiene el pantalon: ";
	Leer descuento;
	Final = ((precio - (precio * (descuento / 100))) * 0.19) + (precio - (precio * (descuento / 100)));
	Escribir "El valor total del pantalón con descuento de ", descuento, "% es ", Final, " incluyendo IVA";
FinProceso