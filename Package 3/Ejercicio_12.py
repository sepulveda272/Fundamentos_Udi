while True:
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    año = int(input("Ingresa el año: "))
    if dia == 0 and mes == 0 and año == 0:
        break
    else:
        if (año % 4 == 0 and año % 100 != 0 or año % 400 == 0) and año >= 1582 and mes == 2 and dia >= 1 and dia <= 29:
            print(f"{dia} de Febrero de {año}")
        elif dia >= 1 and dia <= 31 and mes % 2 != 0 and mes == 8 and mes == 10 and mes == 12:
            if mes == 1:
                print(f"{dia} de Enero de {año}")
            elif mes == 3:
                print(f"{dia} de Marzo de {año}")
            elif mes == 5:
                print(f"{dia} de Mayo de {año}")
            elif mes == 7:
                print(f"{dia} de Julio de {año}")
            elif mes == 9:
                print(f"{dia} de Septiembre de {año}")
            elif mes == 11:
                print(f"{dia} de Noviembre de {año}")
        elif dia >= 1 and dia <= 30 and mes % 2 == 0 and mes != 2:
            if mes == 4:
                print(f"{dia} de Abril de {año}")
            elif mes == 6:
                print(f"{dia} de Junio de {año}")
            elif mes == 8:
                print(f"{dia} de Agosto de {año}")
            elif mes == 10:
                print(f"{dia} de Octubre de {año}")
            elif mes == 12:
                print(f"{dia} de Diciembre de {año}")
        elif dia >= 1 and dia <= 28 and mes % 2 == 0:
            print(f"{dia} de Febrero de {año}")
        else:
            print("ERROR")