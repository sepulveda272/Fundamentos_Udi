cvtos=cvtas=svtos=svtas=edad=0

while edad != 99:
    edad = int(input("Edad: "))
    if edad != 99:
        genero = input("A Vinotinta, O Vinotinto: ").upper()
        if genero == "A":
            cvtas+=1
            svtas+=edad
        elif genero == "O":
            cvtos+=1
            svtos+=edad
        else:
            print("Aprenda a leer, vuela a intentarlo")
if (cvtos + cvtas) > 0:
    ptotal = (svtas + svtos) / ( cvtos + cvtas)
    print ("El promedio total es: ", ptotal)
    if cvtas > 0:
        pvtas = svtas / cvtas
        print (f"El promedio de las vinotinta es: {pvtas:.1f}.")
    else:
        print("No hay vinotintas")
    if cvtos > 0:
        pvtos = svtos / cvtos
        print ("El promedio de las vinotinto es: ",round(pvtos,1))
    else:
        print("No hay vinotintos")
else:
    print ("No hay estudiantes.")