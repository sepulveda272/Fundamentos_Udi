while True:
    minutos = int(input("Ingrese tiempo del corredor (minutos): "))
    segundos = int(input("Ingrese tiempo del corredor (segundos): "))
    
    if minutos == 0 and segundos == 0:
        print("Fin de la entrada de datos.")
        break
    
    metros = int(input("Ingrese la distancia de la maratón en metros: "))
    
    tiempoTS = minutos * 60 + segundos
    velocidad = metros / tiempoTS
    
    print("Tiempo del corredor:", minutos, "minutos", segundos, "segundos")
    print("Velocidad media:", velocidad, "metros/segundo")
